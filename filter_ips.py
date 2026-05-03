#!/usr/bin/env python3
"""
filter_ips.py — Enhanced Multi-Country GeoIP-based IP Address Filtering Tool

This script filters IP addresses by multiple countries using GeoIP data and Zeek's SubnetTree
for efficient network lookups. It processes large IP lists in parallel batches
while preserving original formatting (including CIDR notation).

NEW MULTI-COUNTRY FEATURES:
    - Supports multiple COUNTRY_ISO_CODE_N and COUNTRY_NAME_N variables
    - Generates separate output files for each country
    - Creates combined multi-country output file
    - Enhanced statistics reporting with Mermaid pie charts

REQUIREMENTS:
    pip install pysubnettree pandas python-dotenv requests

MAIN WORKFLOW:
    1. Load configuration from environment variables (.env file)
    2. Download GeoIP CSV data if not present locally
    3. Dynamically detect all COUNTRY_* variables
    4. Filter GeoIP networks by all target countries
    5. Process each country separately with optimized networks
    6. Generate individual country files and combined file
    7. Create comprehensive statistics report with Mermaid pie chart
"""

# =============================================================================
# IMPORTS AND DEPENDENCIES
# =============================================================================

import os                               # Operating system interface
import logging                          # Logging functionality
import ipaddress                        # IP address manipulation and validation
from pathlib import Path                # Modern path handling
from concurrent.futures import ProcessPoolExecutor  # Parallel processing
import multiprocessing as mp            # Multiprocessing utilities
from dotenv import load_dotenv          # Environment variable loading
import shutil                           # High-level file operations
import pandas as pd                     # Data manipulation and analysis
import requests                         # HTTP requests for downloading data
import re                              # Regular expressions for pattern matching

# =============================================================================
# CRITICAL DEPENDENCY CHECK
# =============================================================================

try:
    # SubnetTree is the core component for efficient IP network lookups
    # It provides O(log n) lookup time instead of O(n) for linear searches
    import SubnetTree
except Exception as exc:
    # If SubnetTree is missing, the script cannot function efficiently
    # Provide clear installation instructions and exit gracefully
    raise ImportError(
        "CRITICAL: The Python package 'pysubnettree' (module name 'SubnetTree') is required.\n"
        "This package provides efficient IP network lookups using a tree data structure.\n"
        "Install it with: pip install pysubnettree\n"
        f"Original error: {exc}"
    )

# =============================================================================
# CONFIGURATION AND ENVIRONMENT SETUP
# =============================================================================

# Load environment variables from .env file (if it exists)
# This allows users to configure the script without modifying code
load_dotenv()

# FILE PATH CONFIGURATION
# Define where input and output files are located
GEOIP_CSV_PATH = os.getenv('GEOIP_CSV_PATH', '/data/geoip/geoip2-ipv4.csv')
ALL_IPS_FROM_LISTS = os.getenv('ALL_IPS_FROM_LISTS', '/data/output/aggregated.txt')

# PERFORMANCE TUNING
# Allow override of worker process count via environment variable
# Useful for different hardware configurations or resource constraints
NUM_WORKERS_ENV = os.getenv('NUM_WORKERS')
NUM_WORKERS_OVERRIDE = max(1, int(NUM_WORKERS_ENV)) if NUM_WORKERS_ENV else None

# =============================================================================
# GLOBAL WORKER VARIABLE
# =============================================================================

# This global variable holds the SubnetTree instance in each worker process
# It's initialized once per worker and then used for all IP lookups in that worker
WORKER_TREE = None

# =============================================================================
# COUNTRY CONFIGURATION DETECTION
# =============================================================================

def detect_country_configs():
    """
    Dynamically detect all COUNTRY_ISO_CODE_* and COUNTRY_NAME_* variables from environment.
    
    ENHANCED VERSION: Now properly detects all numbered country configurations
    and handles edge cases that were causing countries to be missed.
    
    RETURNS:
        list: List of tuples (iso_code, country_name, suffix)
        
    EXAMPLE:
        Environment:
            COUNTRY_ISO_CODE_1=US
            COUNTRY_NAME_1=United States
            COUNTRY_ISO_CODE_2=CA
            COUNTRY_NAME_2=Canada
            COUNTRY_ISO_CODE_15=DE
            COUNTRY_NAME_15=Germany
            
        Returns: [('US', 'United States', '1'), ('CA', 'Canada', '2'), ('DE', 'Germany', '15')]
    """
    countries = []
    
    # Get all environment variables
    env_vars = dict(os.environ)
    
    # Debug: Log all COUNTRY_ variables found
    country_vars = {k: v for k, v in env_vars.items() if k.startswith('COUNTRY_')}
    logging.info(f"Found {len(country_vars)} COUNTRY_ variables in environment")
    
    # More flexible regex pattern that catches all numbered variations
    # This will match: COUNTRY_ISO_CODE_1, COUNTRY_ISO_CODE_10, COUNTRY_ISO_CODE_999, etc.
    iso_code_pattern = re.compile(r'^COUNTRY_ISO_CODE(_)?(\d*)$')
    
    # Find all COUNTRY_ISO_CODE variables (including legacy COUNTRY_ISO_CODE without number)
    for var_name, var_value in env_vars.items():
        match = iso_code_pattern.match(var_name)
        if match:
            # Handle both legacy (no number) and numbered formats
            has_underscore = match.group(1) is not None
            number_part = match.group(2)
            
            if has_underscore and number_part:
                # Format: COUNTRY_ISO_CODE_123
                suffix = number_part
                suffix_with_underscore = f"_{suffix}"
            elif not has_underscore and not number_part:
                # Format: COUNTRY_ISO_CODE (legacy)
                suffix = ""
                suffix_with_underscore = ""
            else:
                # Skip malformed patterns like COUNTRY_ISO_CODE_ (underscore but no number)
                logging.debug(f"Skipping malformed country variable: {var_name}")
                continue
            
            iso_code = var_value.strip().upper()  # Normalize to uppercase
            
            # Find corresponding COUNTRY_NAME variable
            name_var = f"COUNTRY_NAME{suffix_with_underscore}"
            country_name = env_vars.get(name_var, f"Unknown-{iso_code}").strip()
            
            if iso_code:  # Only add if ISO code is not empty
                countries.append((iso_code, country_name, suffix))
                logging.info(f"Detected country config: {iso_code} ({country_name}) [suffix: '{suffix or 'legacy'}']")
            else:
                logging.warning(f"Empty ISO code found in {var_name}")
    
    # Sort by suffix for consistent ordering (legacy first, then by number)
    def sort_key(country_tuple):
        _, _, suffix = country_tuple
        if suffix == "":
            return (0, 0)  # Legacy comes first
        else:
            try:
                return (1, int(suffix))  # Then by number
            except ValueError:
                return (2, suffix)  # Non-numeric suffixes last, sorted alphabetically
    
    countries.sort(key=sort_key)
    
    if not countries:
        logging.error("No COUNTRY_ISO_CODE variables found in environment!")
        logging.error("Expected format: COUNTRY_ISO_CODE_1=US, COUNTRY_NAME_1=United States")
        
        # Show what COUNTRY_ variables were found for debugging
        if country_vars:
            logging.error("Found these COUNTRY_ variables:")
            for var_name, var_value in sorted(country_vars.items()):
                logging.error(f"  {var_name}={var_value}")
        else:
            logging.error("No COUNTRY_ variables found at all!")
            
    else:
        logging.info(f"Total countries detected: {len(countries)}")
        
        # Validate that we have both ISO codes and names for each
        missing_names = []
        for iso_code, country_name, suffix in countries:
            if country_name.startswith("Unknown-"):
                missing_names.append(f"COUNTRY_NAME_{suffix}" if suffix else "COUNTRY_NAME")
        
        if missing_names:
            logging.warning(f"Missing country name variables: {', '.join(missing_names)}")
    
    return countries

# =============================================================================
# GEOIP DATA MANAGEMENT FUNCTIONS
# =============================================================================

def download_geoip_file():
    """
    Downloads GeoIP2 IPv4 CSV data if not already present locally.
    
    This function handles the automatic acquisition of GeoIP data, which maps
    IP address ranges to countries. The data is essential for country-based
    IP filtering.
    
    DATA SOURCE:
        - URL: https://datahub.io/core/geoip2-ipv4/r/geoip2-ipv4.csv
        - Contains: network, country_iso_code, country_name columns
        - Format: CIDR networks with country mappings
    
    ERROR HANDLING:
        - Creates parent directories if they don't exist
        - Validates HTTP response status
        - Exits gracefully if download fails
    
    SIDE EFFECTS:
        - Creates directories on filesystem
        - Downloads and writes CSV file
        - May raise SystemExit on failure
    """
    # Check if the GeoIP CSV file already exists on disk
    if not os.path.exists(GEOIP_CSV_PATH):
        logging.info(f"GeoIP file not found at {GEOIP_CSV_PATH}. Initiating download...")
        
        # DataHub provides free, regularly updated GeoIP data
        url = "https://datahub.io/core/geoip2-ipv4/r/geoip2-ipv4.csv"
        
        try:
            # Download the CSV file with a reasonable timeout
            logging.info("Downloading GeoIP2 CSV data from DataHub...")
            response = requests.get(url, timeout=60)
            
            # Check if the download was successful
            if response.status_code == 200:
                # Create parent directories if they don't exist
                # This ensures the full path structure is available
                Path(GEOIP_CSV_PATH).parent.mkdir(parents=True, exist_ok=True)
                
                # Write the downloaded content to disk
                with open(GEOIP_CSV_PATH, 'wb') as file_handle:
                    file_handle.write(response.content)
                
                logging.info("GeoIP2 CSV file downloaded and saved successfully.")
            else:
                # Log the specific HTTP error and exit
                logging.error(f"Download failed with HTTP status: {response.status_code}")
                logging.error("Cannot proceed without GeoIP data. Exiting.")
                raise SystemExit(1)
                
        except requests.exceptions.RequestException as req_exc:
            # Handle network-related errors (timeouts, connection issues, etc.)
            logging.error(f"Network error during download: {req_exc}")
            raise SystemExit(1)
            
    else:
        logging.info(f"GeoIP file already exists at {GEOIP_CSV_PATH}")


def collapse_networks(network_strs):
    """
    Optimizes network lists by collapsing overlapping and adjacent networks.
    
    This function takes a list of CIDR network strings and uses Python's
    ipaddress module to combine overlapping or adjacent networks into larger,
    more efficient blocks. This reduces the number of networks that need to
    be stored in the SubnetTree, improving both memory usage and lookup speed.
    
    ARGS:
        network_strs (list): List of CIDR network strings (e.g., ['1.2.3.0/24'])
    
    RETURNS:
        list: Collapsed network strings with overlaps removed
    
    EXAMPLE:
        Input:  ['192.168.1.0/24', '192.168.2.0/24']
        Output: ['192.168.0.0/23']  # Combined into larger block
    
    OPTIMIZATION BENEFITS:
        - Reduces memory footprint in SubnetTree
        - Improves lookup performance
        - Eliminates redundant network checks
    """
    network_objects = []
    invalid_count = 0
    
    # Convert string representations to ipaddress network objects
    for network_str in network_strs:
        try:
            # Create network object from CIDR string
            # strip() removes any whitespace that might cause parsing errors
            network_obj = ipaddress.ip_network(network_str.strip())
            network_objects.append(network_obj)
        except (ipaddress.AddressValueError, ipaddress.NetmaskValueError, ValueError) as parse_error:
            # Log invalid networks for debugging but continue processing
            invalid_count += 1
            logging.debug(f"Skipping invalid network '{network_str}': {parse_error}")
            continue
    
    # Report parsing results
    if invalid_count > 0:
        logging.warning(f"Skipped {invalid_count} invalid network entries")
    
    # Use ipaddress.collapse_addresses() to merge overlapping/adjacent networks
    # This is a built-in Python optimization that's highly efficient
    collapsed_networks = list(ipaddress.collapse_addresses(network_objects))
    
    # Log the optimization results
    original_count = len(network_objects)
    collapsed_count = len(collapsed_networks)
    reduction_percent = ((original_count - collapsed_count) / original_count * 100) if original_count > 0 else 0
    
    logging.info(f"Network optimization: {original_count} → {collapsed_count} "
                f"({reduction_percent:.1f}% reduction)")
    
    # Convert back to string format for SubnetTree compatibility
    return [str(network) for network in collapsed_networks]


# =============================================================================
# PARALLEL PROCESSING WORKER FUNCTIONS
# =============================================================================

def _init_worker(cidr_list):
    """
    Initializes each worker process with a SubnetTree containing country networks.
    
    This function is called once when each worker process starts up. It builds
    a SubnetTree data structure from the provided CIDR list, which enables
    extremely fast IP lookups (O(log n) instead of O(n) for linear searches).
    
    PROCESS DESIGN:
        - Each worker gets its own copy of the SubnetTree
        - Tree is built once per worker and reused for all lookups
        - Global variable stores the tree for access by batch processing function
    
    ARGS:
        cidr_list (list): List of CIDR strings to add to the SubnetTree
    
    SIDE EFFECTS:
        - Sets global WORKER_TREE variable in the worker process
        - Imports SubnetTree in worker context
        - May log errors for malformed CIDRs but continues processing
    
    PERFORMANCE NOTES:
        - SubnetTree construction is O(n log n)
        - Lookup operations are O(log n)
        - Memory usage scales with number of networks
    """
    global WORKER_TREE
    
    # Import SubnetTree in the worker process context
    # This ensures the module is available in each worker's memory space
    import SubnetTree as WorkerSubnetTree
    
    # Create a new SubnetTree instance for this worker
    subnet_tree = WorkerSubnetTree.SubnetTree()
    
    # Track statistics for logging
    added_count = 0
    error_count = 0
    
    # Add each CIDR network to the tree
    for cidr_string in cidr_list:
        try:
            # Add the network to the tree with value True
            # The value (True) indicates this network matches our country filter
            subnet_tree[cidr_string] = True
            added_count += 1
        except Exception as add_error:
            # Log malformed CIDRs but don't stop processing
            error_count += 1
            logging.debug(f"Failed to add CIDR '{cidr_string}' to SubnetTree: {add_error}")
            continue
    
    # Store the completed tree in the global variable
    WORKER_TREE = subnet_tree
    
    # Log initialization results
    logging.debug(f"Worker initialized: {added_count} networks in SubnetTree "
                 f"({error_count} errors)")


def _process_ip_batch(ip_batch):
    """
    Processes a batch of IP addresses/networks against the country filter.
    
    This is the core worker function that gets executed in parallel across
    multiple processes. Each worker receives a batch of IP addresses and
    checks them against the SubnetTree to determine if they belong to the
    target country.
    
    IP FORMAT HANDLING:
        - Single IPs: 192.168.1.1 → check directly
        - CIDR networks: 192.168.1.0/24 → check network address
        - Preserves original formatting in output
    
    ARGS:
        ip_batch (list): List of IP strings to process (mix of IPs and CIDRs)
    
    RETURNS:
        list: IP strings that match the country filter (preserves original format)
    
    ERROR HANDLING:
        - Skips malformed IPs/CIDRs without stopping
        - Handles SubnetTree lookup exceptions
        - Continues processing even if some IPs fail
    
    PERFORMANCE:
        - Each lookup is O(log n) thanks to SubnetTree
        - Batch processing reduces inter-process communication overhead
        - Memory efficient - processes one IP at a time
    """
    global WORKER_TREE
    
    # Safety check: ensure the worker tree was initialized properly
    if WORKER_TREE is None:
        error_msg = "WORKER_TREE not initialized - worker setup failed"
        logging.error(error_msg)
        raise RuntimeError(error_msg)
    
    # List to collect matching IPs (preserving original format)
    country_matched_ips = []
    
    # Statistics tracking
    processed_count = 0
    matched_count = 0
    error_count = 0
    
    # Process each IP in the batch
    for raw_ip_line in ip_batch:
        # Clean up the input (remove whitespace)
        cleaned_ip = raw_ip_line.strip()
        
        # Skip empty lines
        if not cleaned_ip:
            continue
            
        processed_count += 1
        
        try:
            # Determine what IP address to check against the tree
            if '/' in cleaned_ip:
                # This is a CIDR network (e.g., "192.168.1.0/24")
                # We need to check the network address, not the CIDR string itself
                network_obj = ipaddress.ip_network(cleaned_ip, strict=False)
                ip_to_lookup = str(network_obj.network_address)
                
                logging.debug(f"CIDR '{cleaned_ip}' → checking network address '{ip_to_lookup}'")
            else:
                # This is a single IP address - check it directly
                ip_to_lookup = cleaned_ip
                
        except (ipaddress.AddressValueError, ipaddress.NetmaskValueError, ValueError) as parse_error:
            # Skip malformed IP addresses or CIDR blocks
            error_count += 1
            logging.debug(f"Skipping malformed IP '{cleaned_ip}': {parse_error}")
            continue
        
        try:
            # Perform the SubnetTree lookup
            # This checks if ip_to_lookup falls within any of our country networks
            if ip_to_lookup in WORKER_TREE:
                # IP matches! Add the ORIGINAL format to results
                # This preserves CIDR notation if that's what was input
                country_matched_ips.append(cleaned_ip)
                matched_count += 1
                logging.debug(f"MATCH: '{cleaned_ip}' (checked: '{ip_to_lookup}')")
            else:
                logging.debug(f"No match: '{cleaned_ip}' (checked: '{ip_to_lookup}')")
                
        except Exception as lookup_error:
            # Handle any SubnetTree lookup errors (shouldn't happen with valid IPs)
            error_count += 1
            logging.debug(f"SubnetTree lookup failed for '{ip_to_lookup}': {lookup_error}")
            continue
    
    # Log batch processing results
    logging.debug(f"Batch complete: {processed_count} processed, {matched_count} matched, "
                 f"{error_count} errors")
    
    return country_matched_ips


# =============================================================================
# MERMAID PIE CHART GENERATION
# =============================================================================
def generate_mermaid_pie_chart(country_statistics, total_input_ips, top_n=19):
    """
    Generate a Mermaid pie chart to visualize the distribution of IPs 
    based on the top countries with the highest filter rates.
    The rest of the countries will be grouped under "Other/Unfiltered".
    
    Parameters:
        country_statistics (list of dict): List of dictionaries containing country stats.
            Each dictionary should include 'country_name', 'iso_code', and 'ips_matched'.
        total_input_ips (int): The total number of input IPs.
        top_n (int): The number of top countries to include in the chart. Defaults to 19.

    Returns:
        str: Mermaid formatted pie chart or an empty chart if no significant data exists.
    """
    # If no IPs were processed, return an empty pie chart with a message
    if total_input_ips == 0:
        return "```mermaid\npie title No IPs processed\n\"No Data\" : 100\n```"

    # Create a list of countries with their corresponding filter rate (percentage of matched IPs)
    country_stats_with_rate = []
    for stats in country_statistics:
        rate = (stats['ips_matched'] / total_input_ips * 100) if total_input_ips > 0 else 0
        country_stats_with_rate.append({**stats, 'filter_rate': rate})

    # Sort countries by filter rate in descending order
    sorted_stats = sorted(country_stats_with_rate, key=lambda x: x['filter_rate'], reverse=True)

    # Get the top N countries and the rest (other countries)
    top_countries = sorted_stats[:top_n]
    other_countries = sorted_stats[top_n:]

    # Initialize a list to hold pie chart entries and a variable to track total top IPs
    pie_entries = []
    total_top_ips = 0
    total_top_filter_rate = 0  # To calculate the sum of filter rates for the top countries

    # Process the top N countries and add them to the pie chart
    for stats in top_countries:
        if stats['ips_matched'] > 0:
            percentage = stats['filter_rate']
            if percentage >= 0.1:  # Only include countries with a filter rate above 0.1%
                country_label = f"{stats['country_name']}"
                pie_entries.append(f'"{country_label}" : {percentage:.1f}')
                total_top_ips += stats['ips_matched']
                total_top_filter_rate += percentage  # Sum of the filter rates for top countries

    # Calculate the "Other/Unfiltered" category
    other_percentage = 100 - total_top_filter_rate  # The remainder goes to "Other/Unfiltered"

    # Always include "Other/Unfiltered" as the last entry if it's >= 0.1%
    if other_percentage >= 0.1:
        pie_entries.append(f'"Other/Unfiltered" : {other_percentage:.1f}')

    # If no pie entries, return an empty pie chart
    if not pie_entries:
        return (
            "```mermaid\n"
            "pie showData title IP Blocklist Distribution by Country\n"
            "\"No significant data\" : 100\n"
            "```"
        )

    # Generate the final Mermaid pie chart content
    chart_content = (
        "```mermaid\n"
        "pie showData title IP Blocklist Distribution by Country\n"
        + "\n".join(pie_entries) +
        "\n```"
    )
    
    # Return the generated chart content
    return chart_content


# =============================================================================
# MULTI-COUNTRY FILTERING FUNCTIONS
# =============================================================================

def process_single_country(iso_code, country_name, suffix, geoip_dataframe, input_ip_list, optimal_workers):
    """
    Process IPs for a single country and return filtered results.
    
    ARGS:
        iso_code (str): Country ISO code (e.g., 'US')
        country_name (str): Full country name (e.g., 'United States')
        suffix (str): Variable suffix (e.g., '1', '2', or '' for legacy)
        geoip_dataframe (pd.DataFrame): GeoIP data
        input_ip_list (list): List of IPs to filter
        optimal_workers (int): Number of worker processes to use
        
    RETURNS:
        tuple: (filtered_ips_list, stats_dict)
    """
    logging.info(f"=== Processing {country_name} ({iso_code}) ===")
    
    # Filter networks for this country
    country_mask = (
        (geoip_dataframe.get('country_iso_code') == iso_code) | 
        (geoip_dataframe.get('country_name') == country_name)
    )
    
    country_networks = (geoip_dataframe[country_mask]['network']
                       .dropna()
                       .astype(str)
                       .tolist())
    
    logging.info(f"Found {len(country_networks)} networks for {country_name}")
    
    if len(country_networks) == 0:
        logging.warning(f"No networks found for {country_name} ({iso_code})")
        return [], {
            'iso_code': iso_code,
            'country_name': country_name,
            'suffix': suffix,
            'networks_found': 0,
            'networks_optimized': 0,
            'ips_matched': 0,
            'output_file': None
        }
    
    # Optimize networks
    optimized_cidrs = collapse_networks(country_networks)
    
    if len(optimized_cidrs) == 0:
        logging.warning(f"Network optimization resulted in empty list for {country_name}")
        return [], {
            'iso_code': iso_code,
            'country_name': country_name,
            'suffix': suffix,
            'networks_found': len(country_networks),
            'networks_optimized': 0,
            'ips_matched': 0,
            'output_file': None
        }
    
    # Calculate batches for this country
    total_input_ips = len(input_ip_list)
    batches_per_worker = 4
    total_desired_batches = optimal_workers * batches_per_worker
    batch_size = max(1, total_input_ips // total_desired_batches)
    
    # Split input IPs into batches
    ip_batches = []
    for start_idx in range(0, total_input_ips, batch_size):
        end_idx = min(start_idx + batch_size, total_input_ips)
        batch = input_ip_list[start_idx:end_idx]
        ip_batches.append(batch)
    
    # Process batches in parallel
    filtered_ips = []
    
    try:
        with ProcessPoolExecutor(
            max_workers=optimal_workers,
            initializer=_init_worker,
            initargs=(optimized_cidrs,)
        ) as process_executor:
            
            batch_results = process_executor.map(_process_ip_batch, ip_batches)
            
            for batch_result in batch_results:
                filtered_ips.extend(batch_result)
                
    except Exception as parallel_error:
        logging.error(f"Parallel processing failed for {country_name}: {parallel_error}")
        logging.info("Falling back to single-threaded processing...")
        
        # Single-threaded fallback
        fallback_tree = SubnetTree.SubnetTree()
        for cidr in optimized_cidrs:
            try:
                fallback_tree[cidr] = True
            except Exception:
                continue
        
        for raw_ip in input_ip_list:
            cleaned_ip = raw_ip.strip()
            if not cleaned_ip:
                continue
                
            try:
                if '/' in cleaned_ip:
                    network_obj = ipaddress.ip_network(cleaned_ip, strict=False)
                    ip_to_check = str(network_obj.network_address)
                else:
                    ip_to_check = cleaned_ip
                    
            except Exception:
                continue
            
            try:
                if ip_to_check in fallback_tree:
                    filtered_ips.append(cleaned_ip)
            except Exception:
                continue
    
    # Generate output filename
    output_filename = f"aggregated-{iso_code.lower()}-only.txt"
    output_path = f"/data/output/{output_filename}"
    
    # Write results to file
    try:
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w') as output_file:
            for ip_address in filtered_ips:
                output_file.write(f"{ip_address}\n")
        logging.info(f"Written {len(filtered_ips)} IPs to {output_path}")
    except IOError as write_error:
        logging.error(f"Failed to write {output_path}: {write_error}")
        output_filename = None
    
    # Return results and statistics
    stats = {
        'iso_code': iso_code,
        'country_name': country_name,
        'suffix': suffix,
        'networks_found': len(country_networks),
        'networks_optimized': len(optimized_cidrs),
        'ips_matched': len(filtered_ips),
        'output_file': output_filename
    }
    
    return filtered_ips, stats


# =============================================================================
# MAIN FILTERING LOGIC
# =============================================================================

def filter_multi_country_ips():
    """
    Main orchestration function for multi-country IP filtering.
    
    This enhanced version processes multiple countries in sequence,
    generates individual output files for each country, creates a
    combined multi-country file, and produces comprehensive statistics
    with Mermaid pie chart visualization.
    """
    
    logging.info("=== MULTI-COUNTRY IP FILTERING PROCESS STARTED ===")
    
    # =========================================================================
    # STAGE 1: ENVIRONMENT SETUP AND VALIDATION
    # =========================================================================
    
    # Detect all country configurations
    country_configs = detect_country_configs()
    
    if not country_configs:
        logging.error("No country configurations found. Please set COUNTRY_ISO_CODE_* variables.")
        raise SystemExit(1)
    
    logging.info(f"Processing {len(country_configs)} countries")
    for iso_code, country_name, suffix in country_configs:
        logging.info(f"  - {country_name} ({iso_code}) [suffix: {suffix or 'legacy'}]")
    
    # =========================================================================
    # STAGE 2: GEOIP DATA ACQUISITION
    # =========================================================================
    
    logging.info("Stage 1: Acquiring GeoIP database...")
    download_geoip_file()
    
    # =========================================================================
    # STAGE 3: GEOIP DATA LOADING AND VALIDATION
    # =========================================================================
    
    logging.info("Stage 2: Loading and validating GeoIP database...")
    
    try:
        geoip_dataframe = pd.read_csv(GEOIP_CSV_PATH)
        logging.info(f"GeoIP database loaded: {len(geoip_dataframe)} total entries")
        
    except (FileNotFoundError, pd.errors.EmptyDataError, pd.errors.ParserError) as csv_error:
        logging.error(f"Failed to load GeoIP CSV file: {csv_error}")
        raise SystemExit(1)
    
    if 'network' not in geoip_dataframe.columns:
        logging.error("GeoIP CSV missing required 'network' column")
        logging.error(f"Available columns: {list(geoip_dataframe.columns)}")
        raise SystemExit(1)
    
    # =========================================================================
    # STAGE 4: INPUT DATA LOADING
    # =========================================================================
    
    logging.info("Stage 3: Loading input IP list...")
    
    try:
        with open(ALL_IPS_FROM_LISTS, 'r') as input_file:
            input_ip_list = [line.rstrip('\n') for line in input_file if line.strip()]
            
    except FileNotFoundError:
        logging.error(f"Input IP file not found: {ALL_IPS_FROM_LISTS}")
        raise SystemExit(1)
    except IOError as io_error:
        logging.error(f"Failed to read input file: {io_error}")
        raise SystemExit(1)
    
    total_input_ips = len(input_ip_list)
    logging.info(f"Loaded {total_input_ips} IP entries for processing")
    
    if total_input_ips == 0:
        logging.info("No IPs to process. Exiting.")
        return
    
    # =========================================================================
    # STAGE 5: PARALLEL PROCESSING SETUP
    # =========================================================================
    
    logging.info("Stage 4: Setting up parallel processing...")
    
    system_cpu_count = mp.cpu_count()
    optimal_workers = min(NUM_WORKERS_OVERRIDE or system_cpu_count, 4)
    
    logging.info(f"Using {optimal_workers} worker processes")
    
    # =========================================================================
    # STAGE 6: PROCESS EACH COUNTRY
    # =========================================================================
    
    logging.info("Stage 5: Processing countries...")
    
    all_country_results = []
    country_statistics = []
    all_filtered_ips = set()  # Use set to avoid duplicates in combined file
    
    for iso_code, country_name, suffix in country_configs:
        filtered_ips, stats = process_single_country(
            iso_code, country_name, suffix, geoip_dataframe, 
            input_ip_list, optimal_workers
        )
        
        all_country_results.append((iso_code, country_name, filtered_ips))
        country_statistics.append(stats)
        
        # Add to combined set (automatically deduplicates)
        all_filtered_ips.update(filtered_ips)
        
        logging.info(f"Completed {country_name}: {len(filtered_ips)} IPs")
    
    # =========================================================================
    # STAGE 7: CREATE COMBINED MULTI-COUNTRY FILE
    # =========================================================================
    
    logging.info("Stage 6: Creating combined multi-country file...")
    
    # Create combined filename
    country_codes = [iso.lower() for iso, _, _ in country_configs]
    if len(country_codes) <= 3:
        combined_suffix = "-".join(country_codes)
    else:
        combined_suffix = f"multi-{len(country_codes)}countries"
    
    combined_filename = f"aggregated-{combined_suffix}-combined.txt"
    combined_path = f"/data/output/{combined_filename}"
    
    # Write combined file
    try:
        Path(combined_path).parent.mkdir(parents=True, exist_ok=True)
        with open(combined_path, 'w') as combined_file:
            for ip_address in sorted(all_filtered_ips):  # Sort for consistency
                combined_file.write(f"{ip_address}\n")
        logging.info(f"Written {len(all_filtered_ips)} unique IPs to {combined_path}")
    except IOError as write_error:
        logging.error(f"Failed to write combined file: {write_error}")
        combined_filename = None
    
    # =========================================================================
    # STAGE 8: GENERATE COMPREHENSIVE STATISTICS WITH MERMAID PIE CHART
    # =========================================================================
    
    logging.info("Stage 7: Generating statistics with Mermaid pie chart...")
    
    # Generate Mermaid pie chart
    pie_chart = generate_mermaid_pie_chart(country_statistics, total_input_ips)
    
    # Create detailed statistics file
    stats_path = "/data/output/stats.md"
    
    try:
        with open(stats_path, 'w') as stats_file:
            stats_file.write("# Multi-Country IP Aggregation Statistics\n\n")
            stats_file.write(f"**Last Updated:** {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S UTC')}\n\n")
            
            # Add Mermaid pie chart
            stats_file.write("## 📈 Country Distribution\n\n")
            stats_file.write(pie_chart)
            stats_file.write("\n\n")
            
            # Overall summary
            stats_file.write("## Overall Summary\n\n")
            stats_file.write(f"- **Total Input IPs:** {total_input_ips:,}\n")
            stats_file.write(f"- **Countries Processed:** {len(country_configs)}\n")
            stats_file.write(f"- **Combined Unique IPs:** {len(all_filtered_ips):,}\n")
            if combined_filename:
                stats_file.write(f"- **Combined Output File:** `{combined_filename}`\n")
            
            combined_percentage = (len(all_filtered_ips) / total_input_ips * 100) if total_input_ips > 0 else 0
            stats_file.write(f"- **Overall Filter Rate:** {combined_percentage:.2f}%\n\n")
            
            # Per-country breakdown
            stats_file.write("## Per-Country Results\n\n")
            stats_file.write("| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |\n")
            stats_file.write("|---------|------|----------------|--------------------|-----------|-----------|-----------|\n")
            
            for stats in country_statistics:
                filter_rate = (stats['ips_matched'] / total_input_ips * 100) if total_input_ips > 0 else 0
                output_file = stats['output_file'] if stats['output_file'] else "❌ Failed"
                stats_file.write(f"| {stats['country_name']} | {stats['iso_code']} | "
                               f"{stats['networks_found']:,} | {stats['networks_optimized']:,} | "
                               f"{stats['ips_matched']:,} | {filter_rate:.2f}% | `{output_file}` |\n")
            
            stats_file.write("\n")
            
            # IP Sources
            stats_file.write("## IP Sources\n\n")
            env_vars = dict(os.environ)
            list_vars = [(k, v) for k, v in env_vars.items() if k.startswith('LIST_')]
            list_vars.sort(key=lambda x: int(x[0].split('_')[1]) if x[0].split('_')[1].isdigit() else 999)
            
            for var_name, url in list_vars:
                list_num = var_name.replace('LIST_', '')
                stats_file.write(f"- **Source {list_num}:** {url}\n")
            
            stats_file.write("\n")
            
            # Configuration details
            stats_file.write("## Configuration Details\n\n")

        logging.info(f"Statistics with Mermaid pie chart written to {stats_path}")
        
    except IOError as stats_error:
        logging.error(f"Failed to write statistics file: {stats_error}")
    
    # =========================================================================
    # STAGE 9: CLEANUP AND FINAL REPORTING
    # =========================================================================
    
    logging.info("Stage 8: Final reporting and cleanup...")
    
    # Console summary
    logging.info("=== MULTI-COUNTRY FILTERING RESULTS ===")
    logging.info(f"Input IPs: {total_input_ips:,}")
    logging.info(f"Countries: {len(country_configs)}")
    logging.info(f"Combined Unique IPs: {len(all_filtered_ips):,}")
    logging.info(f"Overall Filter Rate: {combined_percentage:.2f}%")
    
    logging.info("\nPer-Country Summary:")
    for stats in country_statistics:
        filter_rate = (stats['ips_matched'] / total_input_ips * 100) if total_input_ips > 0 else 0
        logging.info(f"  {stats['country_name']} ({stats['iso_code']}): {stats['ips_matched']:,} IPs ({filter_rate:.2f}%)")
    
    # Clean up GeoIP directory
    geoip_directory = Path(GEOIP_CSV_PATH).parent
    if geoip_directory.exists() and geoip_directory.is_dir():
        try:
            logging.info(f"Cleaning up GeoIP directory: {geoip_directory}")
            shutil.rmtree(geoip_directory)
            logging.info("GeoIP directory removed successfully")
        except Exception as cleanup_error:
            logging.warning(f"Failed to remove GeoIP directory: {cleanup_error}")
    
    logging.info("=== MULTI-COUNTRY IP FILTERING PROCESS COMPLETED ===")


# =============================================================================
# SCRIPT ENTRY POINT
# =============================================================================

if __name__ == "__main__":
    """
    Script entry point - sets up logging and starts the multi-country filtering process.
    """
    
    # Configure logging for informative output
    logging.basicConfig(
        level=logging.INFO,
        format='[%(levelname)s] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Start the multi-country IP filtering process
    try:
        filter_multi_country_ips()
    except KeyboardInterrupt:
        logging.info("Process interrupted by user")
        raise SystemExit(130)  # Standard exit code for Ctrl+C
    except Exception as unexpected_error:
        logging.error(f"Unexpected error: {unexpected_error}")
        raise SystemExit(1)
