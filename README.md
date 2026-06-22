# Multi-Country IP Address Internet Blocklist Aggregator

![Workflow Status](https://github.com/dewdmadbro/ip-blocklist-dewd/actions/workflows/ip-aggregation.yml/badge.svg)
![Countries](https://img.shields.io/badge/Countries-50-278EF5)
![Total IPs Blocked](https://img.shields.io/badge/Blocked_IPs-1133209-2D56A8)
          
![Issues](https://img.shields.io/github/issues/dewdmadbro/ip-blocklist-dewd)
![Last Commit](https://img.shields.io/github/last-commit/dewdmadbro/ip-blocklist-dewd)
![Forks](https://img.shields.io/github/forks/dewdmadbro/ip-blocklist-dewd)

* * *

Automated IP blocklist aggregation with multi-country geographical filtering

* * *

## 🚀 Features

- **Multi-Country Support**: Filter IPs from multiple countries - aggregate or individual lists
- **Automated Aggregation**: Combines multiple IP blocklists into a single deduplicated list
- **Geographical Filtering**: Filters IPs by country with support for multiple countries
- **Individual & Combined Files**: Generates both per-country files and combined multi-country files
- **Docker Support**: Runs in containerized environment for consistency
- **GitHub Actions**: Automated daily updates with manual trigger support
- **Multi-source**: Supports multiple URL sources via environment configuration
- **Enhanced Statistics**: Comprehensive reporting with per-country breakdowns

## 📊 Latest Statistics

**Last Updated:** 2026-06-22 05:39:39 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 19.4
"China" : 12.8
"India" : 6.3
"Netherlands" : 4.5
"Brazil" : 4.3
"Germany" : 3.9
"Vietnam" : 3.1
"Singapore" : 3.1
"United Kingdom" : 2.8
"Indonesia" : 2.4
"Russia" : 2.3
"Canada" : 2.2
"France" : 1.8
"Australia" : 1.5
"South Korea" : 1.3
"Pakistan" : 1.3
"Italy" : 1.3
"Thailand" : 1.2
"Taiwan" : 1.2
"Other/Unfiltered" : 23.4
```

## Overall Summary

- **Total Input IPs:** 1,133,209
- **Countries Processed:** 50
- **Combined Unique IPs:** 1,000,539
- **Combined Output File:** `aggregated-multi-50countries-combined.txt`
- **Overall Filter Rate:** 88.29%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 157,756 | 155,950 | 219,705 | 19.39% | `aggregated-us-only.txt` |
| China | CN | 7,904 | 7,903 | 144,748 | 12.77% | `aggregated-cn-only.txt` |
| India | IN | 12,970 | 12,938 | 71,599 | 6.32% | `aggregated-in-only.txt` |
| Germany | DE | 28,842 | 28,762 | 43,724 | 3.86% | `aggregated-de-only.txt` |
| Russia | RU | 13,176 | 12,937 | 25,861 | 2.28% | `aggregated-ru-only.txt` |
| United Kingdom | GB | 35,639 | 35,460 | 31,319 | 2.76% | `aggregated-gb-only.txt` |
| Thailand | TH | 1,954 | 1,954 | 13,872 | 1.22% | `aggregated-th-only.txt` |
| Vietnam | VN | 2,164 | 2,164 | 35,592 | 3.14% | `aggregated-vn-only.txt` |
| South Korea | KR | 3,964 | 3,954 | 14,864 | 1.31% | `aggregated-kr-only.txt` |
| Brazil | BR | 13,475 | 13,440 | 48,435 | 4.27% | `aggregated-br-only.txt` |
| Taiwan | TW | 2,417 | 2,417 | 13,527 | 1.19% | `aggregated-tw-only.txt` |
| Canada | CA | 17,019 | 16,891 | 24,505 | 2.16% | `aggregated-ca-only.txt` |
| Singapore | SG | 9,303 | 9,293 | 35,406 | 3.12% | `aggregated-sg-only.txt` |
| Italy | IT | 9,635 | 9,611 | 14,677 | 1.30% | `aggregated-it-only.txt` |
| Netherlands | NL | 18,841 | 18,711 | 50,959 | 4.50% | `aggregated-nl-only.txt` |
| Indonesia | ID | 6,422 | 6,401 | 26,705 | 2.36% | `aggregated-id-only.txt` |
| France | FR | 32,646 | 32,619 | 20,944 | 1.85% | `aggregated-fr-only.txt` |
| Venezuela | VE | 941 | 941 | 6,761 | 0.60% | `aggregated-ve-only.txt` |
| Australia | AU | 12,040 | 11,957 | 16,748 | 1.48% | `aggregated-au-only.txt` |
| Turkey | TR | 3,403 | 3,379 | 13,059 | 1.15% | `aggregated-tr-only.txt` |
| Ukraine | UA | 5,552 | 5,497 | 8,288 | 0.73% | `aggregated-ua-only.txt` |
| Iran | IR | 2,046 | 2,045 | 4,521 | 0.40% | `aggregated-ir-only.txt` |
| Poland | PL | 8,097 | 8,063 | 7,626 | 0.67% | `aggregated-pl-only.txt` |
| Mexico | MX | 4,379 | 4,375 | 11,824 | 1.04% | `aggregated-mx-only.txt` |
| Spain | ES | 11,030 | 11,008 | 8,229 | 0.73% | `aggregated-es-only.txt` |
| Argentina | AR | 3,459 | 3,457 | 9,516 | 0.84% | `aggregated-ar-only.txt` |
| Egypt | EG | 737 | 737 | 3,048 | 0.27% | `aggregated-eg-only.txt` |
| Pakistan | PK | 1,364 | 1,362 | 14,838 | 1.31% | `aggregated-pk-only.txt` |
| Malaysia | MY | 2,530 | 2,530 | 5,481 | 0.48% | `aggregated-my-only.txt` |
| Bulgaria | BG | 2,335 | 2,324 | 2,867 | 0.25% | `aggregated-bg-only.txt` |
| Czechia | CZ | 3,623 | 3,622 | 1,731 | 0.15% | `aggregated-cz-only.txt` |
| Colombia | CO | 2,199 | 2,199 | 4,839 | 0.43% | `aggregated-co-only.txt` |
| United Arab Emirates | AE | 3,314 | 3,314 | 3,730 | 0.33% | `aggregated-ae-only.txt` |
| Romania | RO | 4,016 | 4,006 | 2,215 | 0.20% | `aggregated-ro-only.txt` |
| Kazakhstan | KZ | 1,307 | 1,306 | 2,452 | 0.22% | `aggregated-kz-only.txt` |
| Morocco | MA | 478 | 478 | 3,683 | 0.33% | `aggregated-ma-only.txt` |
| Saudi Arabia | SA | 1,634 | 1,634 | 4,064 | 0.36% | `aggregated-sa-only.txt` |
| South Africa | ZA | 3,972 | 3,958 | 6,793 | 0.60% | `aggregated-za-only.txt` |
| Bangladesh | BD | 2,623 | 2,621 | 5,655 | 0.50% | `aggregated-bd-only.txt` |
| Chile | CL | 1,898 | 1,897 | 2,668 | 0.24% | `aggregated-cl-only.txt` |
| Nigeria | NG | 1,080 | 1,080 | 1,230 | 0.11% | `aggregated-ng-only.txt` |
| Kenya | KE | 866 | 866 | 2,667 | 0.24% | `aggregated-ke-only.txt` |
| Algeria | DZ | 220 | 220 | 1,772 | 0.16% | `aggregated-dz-only.txt` |
| Serbia | RS | 960 | 958 | 1,102 | 0.10% | `aggregated-rs-only.txt` |
| Peru | PE | 1,105 | 1,104 | 1,649 | 0.15% | `aggregated-pe-only.txt` |
| Sri Lanka | LK | 250 | 250 | 799 | 0.07% | `aggregated-lk-only.txt` |
| Iraq | IQ | 683 | 683 | 2,099 | 0.19% | `aggregated-iq-only.txt` |
| Ethiopia | ET | 99 | 99 | 949 | 0.08% | `aggregated-et-only.txt` |
| Ghana | GH | 340 | 340 | 527 | 0.05% | `aggregated-gh-only.txt` |
| Belarus | BY | 421 | 421 | 667 | 0.06% | `aggregated-by-only.txt` |

## IP Sources

- **Source 1:** https://raw.githubusercontent.com/borestad/firehol-mirror/refs/heads/main/firehol_level1.netset
- **Source 2:** https://raw.githubusercontent.com/borestad/firehol-mirror/refs/heads/main/firehol_level2.netset
- **Source 3:** https://rules.emergingthreats.net/fwrules/emerging-Block-IPs.txt
- **Source 4:** https://feodotracker.abuse.ch/downloads/ipblocklist_recommended.txt
- **Source 5:** https://raw.githubusercontent.com/stamparm/ipsum/master/levels/2.txt
- **Source 6:** https://raw.githubusercontent.com/borestad/iplists/refs/heads/main/spamhaus/spamhaus-drop.ipv4
- **Source 7:** https://raw.githubusercontent.com/borestad/iplists/refs/heads/main/spamhaus/spamhaus-asndrop.ipv4
- **Source 8:** https://raw.githubusercontent.com/romainmarcoux/malicious-ip/refs/heads/main/full-300k-aa.txt
- **Source 9:** https://raw.githubusercontent.com/romainmarcoux/malicious-ip/refs/heads/main/full-300k-ab.txt
- **Source 10:** https://raw.githubusercontent.com/romainmarcoux/malicious-ip/refs/heads/main/full-300k-ac.txt
- **Source 11:** https://raw.githubusercontent.com/romainmarcoux/malicious-ip/refs/heads/main/full-300k-ad.txt
- **Source 12:** http://cinsscore.com/list/ci-badguys.txt
- **Source 13:** https://cdn.jsdelivr.net/gh/LittleJake/ip-blacklist/all_blacklist.txt
- **Source 14:** https://raw.githubusercontent.com/MagicTeaMC/bad-ips/refs/heads/main/bad-ips.txt
- **Source 15:** https://raw.githubusercontent.com/MagicTeaMC/MCSTORM-IP/main/mcstorm-ip.txt
- **Source 16:** https://opendbl.net/lists/blocklistde-all.list
- **Source 17:** https://raw.githubusercontent.com/bitwire-it/ipblocklist/refs/heads/main/ip-list.txt
- **Source 18:** https://raw.githubusercontent.com/sefinek/Malicious-IP-Addresses/refs/heads/main/lists/main.txt
- **Source 19:** https://raw.githubusercontent.com/borestad/firehol-mirror/refs/heads/main/firehol_level3.netset
- **Source 20:** https://raw.githubusercontent.com/borestad/firehol-mirror/refs/heads/main/firehol_level4.netset
- **Source 21:** https://raw.githubusercontent.com/borestad/firehol-mirror/refs/heads/main/firehol_webserver.netset

## Configuration Details


### 📁 Generated Files

- **`aggregated.txt`** - 1,133,209 total aggregated IPs from all sources
- **`aggregated-ae-only.txt`** - 3,730 IPs from AE
- **`aggregated-ar-only.txt`** - 9,516 IPs from AR
- **`aggregated-au-only.txt`** - 16,748 IPs from AU
- **`aggregated-bd-only.txt`** - 5,655 IPs from BD
- **`aggregated-bg-only.txt`** - 2,867 IPs from BG
- **`aggregated-br-only.txt`** - 48,435 IPs from BR
- **`aggregated-by-only.txt`** - 667 IPs from BY
- **`aggregated-ca-only.txt`** - 24,505 IPs from CA
- **`aggregated-cl-only.txt`** - 2,668 IPs from CL
- **`aggregated-cn-only.txt`** - 144,748 IPs from CN
- **`aggregated-co-only.txt`** - 4,839 IPs from CO
- **`aggregated-cz-only.txt`** - 1,731 IPs from CZ
- **`aggregated-de-only.txt`** - 43,724 IPs from DE
- **`aggregated-dz-only.txt`** - 1,772 IPs from DZ
- **`aggregated-eg-only.txt`** - 3,048 IPs from EG
- **`aggregated-es-only.txt`** - 8,229 IPs from ES
- **`aggregated-et-only.txt`** - 949 IPs from ET
- **`aggregated-fr-only.txt`** - 20,944 IPs from FR
- **`aggregated-gb-only.txt`** - 31,319 IPs from GB
- **`aggregated-gh-only.txt`** - 527 IPs from GH
- **`aggregated-id-only.txt`** - 26,705 IPs from ID
- **`aggregated-in-only.txt`** - 71,599 IPs from IN
- **`aggregated-iq-only.txt`** - 2,099 IPs from IQ
- **`aggregated-ir-only.txt`** - 4,521 IPs from IR
- **`aggregated-it-only.txt`** - 14,677 IPs from IT
- **`aggregated-ke-only.txt`** - 2,667 IPs from KE
- **`aggregated-kr-only.txt`** - 14,864 IPs from KR
- **`aggregated-kz-only.txt`** - 2,452 IPs from KZ
- **`aggregated-lk-only.txt`** - 799 IPs from LK
- **`aggregated-ma-only.txt`** - 3,683 IPs from MA
- **`aggregated-mx-only.txt`** - 11,824 IPs from MX
- **`aggregated-my-only.txt`** - 5,481 IPs from MY
- **`aggregated-ng-only.txt`** - 1,230 IPs from NG
- **`aggregated-nl-only.txt`** - 50,959 IPs from NL
- **`aggregated-pe-only.txt`** - 1,649 IPs from PE
- **`aggregated-pk-only.txt`** - 14,838 IPs from PK
- **`aggregated-pl-only.txt`** - 7,626 IPs from PL
- **`aggregated-ro-only.txt`** - 2,215 IPs from RO
- **`aggregated-rs-only.txt`** - 1,102 IPs from RS
- **`aggregated-ru-only.txt`** - 25,861 IPs from RU
- **`aggregated-sa-only.txt`** - 4,064 IPs from SA
- **`aggregated-sg-only.txt`** - 35,406 IPs from SG
- **`aggregated-th-only.txt`** - 13,872 IPs from TH
- **`aggregated-tr-only.txt`** - 13,059 IPs from TR
- **`aggregated-tw-only.txt`** - 13,527 IPs from TW
- **`aggregated-ua-only.txt`** - 8,288 IPs from UA
- **`aggregated-us-only.txt`** - 219,705 IPs from US
- **`aggregated-ve-only.txt`** - 6,761 IPs from VE
- **`aggregated-vn-only.txt`** - 35,592 IPs from VN
- **`aggregated-za-only.txt`** - 6,793 IPs from ZA
- **`aggregated-multi-50countries-combined.txt`** - 1,000,539 unique IPs (deduplicated across all countries)

---

## 🛴 Install

Set up your own copy of this repository to aggregate and filter your IP blocklists for multiple countries.

* * *

### 👆 Click the green "Use this template" button in the upper right corner

         
1. **Sign in** to GitHub and navigate to [this repository](https://github.com/dewdmadbro/ip-blocklist-dewd).
2. Click the **"Use this template"** button (in the upper right corner).
3. Select **Create a new repository**. Enter a name (e.g., `my-eu-badip-blocklist`), and confirm.
4. Your new repository is now independent — it will not share commit history with the original.
5. You can immediately begin editing or configuring it for your own multi-country IP aggregation project.

> The **"Use this template"** button on GitHub allows you to quickly create a new, independent repository pre-populated with the project's files and structure. Your new repository won't inherit commit history from the template. This is perfect for your personal blocklist repo.

*Usage is below for steps on running this repository with Github Actions in your new IP aggregation project.*


## 🛠 Usage

### GitHub Actions (Recommended)

#### First Step - Enable Write Permissions

1. **Enable Actions**: Go to Settings > Actions > General > Workflow permissions
2. **Set Permissions**: Select "Read and write permissions", click "Save".


#### Second Step - Configure The Repo

3. **Configure Environment**: Edit `.env` file with your desired sources and countries
4. **Your Favorite Blocklists**: Load as many blocklists as you like, just make sure the line starts with `LIST1_`, `LIST2_`, `LIST3_`, etc.
5. **Multiple Countries**: Countries can be modified the same way, `COUNTRY_ISO_CODE_1`, `COUNTRY_NAME_1`, `COUNTRY_ISO_CODE_2`, `COUNTRY_NAME_2`, etc.
6. **Find Country Codes**: You can find your country codes in the [geoip2-ipv4 spreadsheet](https://datahub.io/core/geoip2-ipv4)
7. **Automatic Runs**: The workflow runs twice daily. At both **02:17 AM/PM UTC** or it will run anytime if you [modified the cron file](https://github.com/dewdmadbro/ip-blocklist-dewd/edit/main/.github/workflows/ip-aggregation.yml)


#### Third Step - Running This Action

8. **Run This Now**: You can run this Github Action by using the "Action" tab up top
9. **Generate Multi-Country Blocklists**: Under "All workflows" you can find this action
10. **Run workflow**: On this page, off to the right is a button with a dropdown to "Run workflow"
11. **Off to the races**: Each run will consume some of your free monthly Github Actions 2000 min (33.3 hours)

> Please adjust cron, it is how often your aggregator runs in [.github/workflows/ip-aggregation.yml](https://github.com/dewdmadbro/ip-blocklist-dewd/edit/main/.github/workflows/ip-aggregation.yml), also modify your blacklists and countries in the [.env](https://github.com/dewdmadbro/ip-blocklist-dewd/edit/main/.env) file.

## ⚙ Configuration

### 🌍 Multi-Country Setup

The `.env` file supports multiple countries:

```bash
# European Union Example
COUNTRY_ISO_CODE_1=DE
COUNTRY_NAME_1=Germany

COUNTRY_ISO_CODE_2=FR
COUNTRY_NAME_2=France

COUNTRY_ISO_CODE_3=NL
COUNTRY_NAME_3=Netherlands

COUNTRY_ISO_CODE_4=IT
COUNTRY_NAME_4=Italy

COUNTRY_ISO_CODE_5=ES
COUNTRY_NAME_5=Spain
```

This will generate:
- `aggregated-de-only.txt` (Germany IPs)
- `aggregated-fr-only.txt` (France IPs) 
- `aggregated-nl-only.txt` (Netherlands IPs)
- `aggregated-it-only.txt` (Italy IPs)
- `aggregated-es-only.txt` (Spain IPs)
- `aggregated-multi-5countries-combined.txt` (All countries combined, deduplicated)

### Sample .env file

```bash
# Add your IP list sources
LIST_1=https://example.com/blocklist1.txt
LIST_2=https://example.com/blocklist2.txt

# Set multiple countries (NEW FEATURE!)
COUNTRY_ISO_CODE_1=DE
COUNTRY_NAME_1=Germany

COUNTRY_ISO_CODE_2=FR  
COUNTRY_NAME_2=France

# Configure paths (usually don't need to change)
GEOIP_CSV_PATH=/data/geoip/geoip2-ipv4.csv
ALL_IPS_FROM_LISTS=/data/output/aggregated.txt
```

## 🏠 Local Deployment (Alternative)

If you'd rather download this repo and run this project offline, the instructions are below:

### 1. Clone the repository

The first step is to download the files from the internet, and get them locally on your machine.

```bash
git clone https://github.com/dewdmadbro/ip-blocklist-dewd.git
```

### 2. Configure your sources and countries in .env

The next step is to configure the project to your liking. Edit your `.env` file. You can enter as many IP based block lists as you need and configure multiple countries.

```bash
nano .env
```

### 3. Run with Docker Compose

You can now run the project and see what happens.

```bash
docker compose up --build
```

### 4. Check results

Let's see what happened!

```bash
ls -la data/output/
```

## 📁 Output Files

### Per-Country Files
- `data/output/aggregated-{country-code}-only.txt` - Country-specific IPs (e.g., `aggregated-de-only.txt` for Germany)

### Combined Multi-Country Files  
- `data/output/aggregated-multi-{number-of-countries-total}countries-combined.txt` - Combined IPs from all countries (deduplicated)
- Example: `aggregated-multi-3countries-combined.txt` for Germany + France + Netherlands

### Core Files
- `data/output/aggregated.txt` - All deduplicated IPs from all sources (before country filtering)
- `data/output/stats.md` - Comprehensive processing statistics with per-country breakdowns

## 🔄 Workflow Triggers

The GitHub Action runs automatically when:

- **Daily Schedule**: Every day, twice. Once at at 02:17 AM UTC and then again at 02:17 PM UTC
- **File Changes**: When `.env`, `Dockerfile`, or key scripts are modified
- **Manual Trigger**: Via GitHub Actions interface


## 🧹 Starting With Clean Output

If you're going to customize the list: 

- You should remove the [./data/output](https://github.com/dewdmadbro/ip-blocklist-dewd/edit/main/data/output) folder, as it will only contain data pertinent to the last run.

- Always remove the [./data/output](https://github.com/dewdmadbro/ip-blocklist-dewd/edit/main/data/output) folder when you customize the countries. 

> This will ensure you dont include older, unused countries in your new aggreagtion lists.



## ⚡ Performance

- **Multi-Country Processing**: Parallel processing of multiple countries
- **Processing Speed**: ~10,000 IPs per second for filtering per country
- **Parallel Processing**: Multi-core optimization for large datasets  
- **Memory Efficient**: Streaming processing for large files
- **Optimized Lookup**: Integer-based IP range matching with SubnetTree
- **Network Optimization**: Automatic collapsing of overlapping CIDR blocks

## 🌼 Features and Optimizations

- **🌍 Multi-country IP blocklist aggregation** for comprehensive regional security  
- **📊 Per-country statistical analysis** with detailed filtering metrics
- **🔄 Automated multi-country updates** via GitHub Actions
- **🚀 Parallel country processing** for improved performance
- **📁 Individual and combined output files** for flexible deployment
- **🛡️ Regional threat mitigation** with configurable multi-country rules
- **💾 Memory-efficient processing** even with multiple large country datasets
- **🔗 Network optimization** with automatic CIDR block collapsing

## 👍 Acknowledgements

This project would not have been possible without the amazing work of the following other projects:

* * *

### 🎩 Datopian

Thank you to [Datopian](https://github.com/datasets/geoip2-ipv4) for maintaining the [GeoIP2 IPv4 dataset](https://datahub.io/core/geoip2-ipv4). This dataset provides otherwise impossible information for IP geolocation, allowing this project to filter IPs based on multiple countries simultaneously.

- [GeoIP2 IPv4 Dataset](https://datahub.io/core/geoip2-ipv4) by Datopian is essential for filtering and identifying IP addresses across various countries, enabling the dynamic multi-country functionality of this project.


* * *

### 🦘 Andrew Twin

Special thanks to [Andrew Twin](https://github.com/andrewtwin) for creating and sharing the [IP Aggregator](https://github.com/andrewtwin/ip-aggregator) project. Andrew's work on efficiently aggregating IP blocklists was a fundamental inspiration and foundation for this enhanced multi-country version.

- The [IP Aggregator](https://github.com/andrewtwin/ip-aggregator) allows easy downloading, parsing, and filtering of multiple IP blocklists, which this project leverages and extends for multi-country IP management tasks.


* * *

### 📗 Blocklist maintainers

I would like to additionally acknowledge the maintainers and contributors of various [IP blocklists](https://github.com/topics/ip-blocklist) and [IP blacklists](https://github.com/topics/ip-blacklist). Thank you for maintaining up-to-date, community-driven threat intelligence that forms the foundation of generating these multi-country filtered files. While the specific lists in this repo may vary, the collective dedication to improving online security and privacy of all contributors is deeply appreciated.


* * *

