#!/bin/bash
set -e  # Exit immediately if a command exits with a non-zero status

# Safely load environment variables from .env while ignoring comments and empty lines
while IFS='=' read -r key value; do
  # Ignore lines that are comments or empty
  if [[ ! "$key" =~ ^# && -n "$key" ]]; then
    export "$key=$value"
  fi
done < .env

# Where to save raw files
INPUT_DIR="/data/input"
COMBINED_INPUT="/tmp/all_input.txt"
OUTPUT_DIR="/data/output"

# Create the input and output directories if they don't exist
mkdir -p "$INPUT_DIR"
mkdir -p "$OUTPUT_DIR"

# Clear the OUTPUT_DIR before generating new output files
echo "[INFO] Clearing output directory $OUTPUT_DIR before generating new files..."
rm -rf "$OUTPUT_DIR"/*

# Load LIST variables dynamically into an array (supports LIST_#, LIST_VPS#, LIST_DATA#, etc.)
LISTS=()
for var in $(env | grep '^LIST_' | cut -d= -f1); do
  LISTS+=("${!var}")  # Append value of each LIST_ variable to the LISTS array
done

# Ensure the LISTS array is populated
if [ ${#LISTS[@]} -eq 0 ]; then
  echo "[ERROR] No LIST URLs found in the environment variables!"
  exit 1
fi

# Download files
echo "[INFO] Downloading ${#LISTS[@]} files..."
for url in "${LISTS[@]}"; do
  fname="$(basename "$url")"  # Extract the file name from the URL
  echo "[INFO] → $url → $INPUT_DIR/$fname"
  
  # Download and save file
  if ! wget -q -O "$INPUT_DIR/$fname" "$url"; then
    echo "[WARNING] Failed to download file from $url, skipping..."
    continue
  fi
done

# Check if any files were downloaded
if [ ! "$(ls -A $INPUT_DIR 2>/dev/null)" ]; then
  echo "[ERROR] No files were successfully downloaded!"
  exit 1
fi

# Combine all downloaded files into one input file
echo "[INFO] Combining all downloaded files..."
> "$COMBINED_INPUT"  # Create/clear the combined input file

for file in "$INPUT_DIR"/*; do
  if [ -f "$file" ]; then
    echo "[INFO] Adding $(basename "$file")..."
    # Add file content and ensure it ends with a newline
    cat "$file" >> "$COMBINED_INPUT"
    echo "" >> "$COMBINED_INPUT"
  fi
done

# Check if combined file has content
if [[ ! -s "$COMBINED_INPUT" ]]; then
  echo "[ERROR] Combined input file is empty!"
  exit 1
fi

echo "[INFO] Combined $(wc -l < "$COMBINED_INPUT") lines from all sources"

# Run the aggregation script with stdin input
echo "[INFO] Running IP aggregation..."
if ! python /app/__main__.py -s < "$COMBINED_INPUT" > "$OUTPUT_DIR/aggregated.txt" 2>/dev/null; then
  echo "[ERROR] IP aggregation failed!"
  exit 1
fi

echo "[INFO] Aggregation complete: $(wc -l < "$OUTPUT_DIR/aggregated.txt") unique networks/IPs"

# Check for multi-country configuration (NEW FORMAT) or legacy single country
COUNTRY_VARS_FOUND=false

# Check for numbered country variables (COUNTRY_ISO_CODE_1, COUNTRY_ISO_CODE_2, etc.)
for var in $(env | grep '^COUNTRY_ISO_CODE_[0-9]' | cut -d= -f1); do
  if [ -n "${!var}" ]; then
    COUNTRY_VARS_FOUND=true
    break
  fi
done

# Check for legacy single country variable if no numbered ones found
if [ "$COUNTRY_VARS_FOUND" = false ] && [ -n "$COUNTRY_ISO_CODE" ]; then
  COUNTRY_VARS_FOUND=true
fi

# Run country filtering if any country configuration is found
if [ "$COUNTRY_VARS_FOUND" = true ]; then
  echo "[INFO] Country configuration detected, running multi-country filtering..."
  if ! python /app/filter_ips.py; then
    echo "[WARNING] Country filtering failed, but continuing..."
  fi
else
  echo "[INFO] No country filtering configuration found - skipping geographic filtering"
  echo "[INFO] To enable country filtering, set COUNTRY_ISO_CODE_1, COUNTRY_NAME_1, etc. in .env"
fi

# Clean up downloaded input files and temporary files
echo "[INFO] Cleaning up temporary files..."
rm -rf "$INPUT_DIR"
rm -f "$COMBINED_INPUT"

echo "[INFO] Processing complete!"
echo "[INFO] Results saved to $OUTPUT_DIR/"

# Show final results
if [ -f "$OUTPUT_DIR/aggregated.txt" ]; then
  echo "[INFO] Aggregated IPs: $(wc -l < "$OUTPUT_DIR/aggregated.txt")"
fi

# Show country-specific results if they exist
echo "[INFO] Checking for country-specific output files..."
for country_file in "$OUTPUT_DIR"/aggregated-*-only.txt; do
  if [ -f "$country_file" ]; then
    filename=$(basename "$country_file")
    count=$(wc -l < "$country_file")
    echo "[INFO] $filename: $count IPs"
  fi
done

# Show combined multi-country files if they exist
for combined_file in "$OUTPUT_DIR"/aggregated-*-combined.txt; do
  if [ -f "$combined_file" ]; then
    filename=$(basename "$combined_file")
    count=$(wc -l < "$combined_file")
    echo "[INFO] Combined file $filename: $count IPs"
  fi
done
