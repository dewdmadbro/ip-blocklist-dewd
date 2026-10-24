# Multi-Country IP Address Internet Blocklist Aggregator

![Workflow Status](https://github.com/dewdmadbro/ip-blocklist-dewd/actions/workflows/ip-aggregation.yml/badge.svg)
![Countries](https://img.shields.io/badge/Countries-50-278EF5)
![Total IPs Blocked](https://img.shields.io/badge/Blocked_IPs-2123235-2D56A8)
          
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

**Last Updated:** 2026-10-24 16:08:27 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 19.0
"China" : 14.6
"Brazil" : 5.3
"India" : 4.9
"Germany" : 3.1
"Netherlands" : 2.9
"Singapore" : 2.6
"Russia" : 2.4
"United Kingdom" : 2.3
"Vietnam" : 2.3
"Indonesia" : 2.0
"France" : 1.8
"Argentina" : 1.7
"Canada" : 1.7
"Pakistan" : 1.5
"Ukraine" : 1.4
"Mexico" : 1.4
"Italy" : 1.2
"Turkey" : 1.1
"Other/Unfiltered" : 27.0
```

## Overall Summary

- **Total Input IPs:** 2,123,235
- **Countries Processed:** 50
- **Combined Unique IPs:** 1,851,080
- **Combined Output File:** `aggregated-multi-50countries-combined.txt`
- **Overall Filter Rate:** 87.18%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 128,606 | 126,734 | 403,121 | 18.99% | `aggregated-us-only.txt` |
| China | CN | 8,106 | 8,105 | 309,213 | 14.56% | `aggregated-cn-only.txt` |
| India | IN | 13,526 | 13,501 | 103,100 | 4.86% | `aggregated-in-only.txt` |
| Germany | DE | 30,436 | 30,330 | 65,825 | 3.10% | `aggregated-de-only.txt` |
| Russia | RU | 13,272 | 13,031 | 49,955 | 2.35% | `aggregated-ru-only.txt` |
| United Kingdom | GB | 36,427 | 36,255 | 48,435 | 2.28% | `aggregated-gb-only.txt` |
| Thailand | TH | 2,095 | 2,095 | 19,581 | 0.92% | `aggregated-th-only.txt` |
| Vietnam | VN | 2,270 | 2,270 | 48,146 | 2.27% | `aggregated-vn-only.txt` |
| South Korea | KR | 3,994 | 3,971 | 24,124 | 1.14% | `aggregated-kr-only.txt` |
| Brazil | BR | 11,545 | 11,506 | 112,393 | 5.29% | `aggregated-br-only.txt` |
| Taiwan | TW | 2,460 | 2,460 | 22,071 | 1.04% | `aggregated-tw-only.txt` |
| Canada | CA | 17,658 | 17,529 | 36,283 | 1.71% | `aggregated-ca-only.txt` |
| Singapore | SG | 9,814 | 9,790 | 55,390 | 2.61% | `aggregated-sg-only.txt` |
| Italy | IT | 9,904 | 9,871 | 24,993 | 1.18% | `aggregated-it-only.txt` |
| Netherlands | NL | 18,480 | 18,385 | 61,285 | 2.89% | `aggregated-nl-only.txt` |
| Indonesia | ID | 6,770 | 6,749 | 42,006 | 1.98% | `aggregated-id-only.txt` |
| France | FR | 33,926 | 33,901 | 38,808 | 1.83% | `aggregated-fr-only.txt` |
| Venezuela | VE | 986 | 986 | 12,812 | 0.60% | `aggregated-ve-only.txt` |
| Australia | AU | 12,448 | 12,375 | 20,558 | 0.97% | `aggregated-au-only.txt` |
| Turkey | TR | 3,540 | 3,505 | 24,248 | 1.14% | `aggregated-tr-only.txt` |
| Ukraine | UA | 5,399 | 5,359 | 29,630 | 1.40% | `aggregated-ua-only.txt` |
| Iran | IR | 2,068 | 2,067 | 9,070 | 0.43% | `aggregated-ir-only.txt` |
| Poland | PL | 8,392 | 8,362 | 16,106 | 0.76% | `aggregated-pl-only.txt` |
| Mexico | MX | 4,429 | 4,422 | 29,046 | 1.37% | `aggregated-mx-only.txt` |
| Spain | ES | 11,676 | 11,666 | 17,624 | 0.83% | `aggregated-es-only.txt` |
| Argentina | AR | 3,532 | 3,532 | 36,661 | 1.73% | `aggregated-ar-only.txt` |
| Egypt | EG | 767 | 767 | 6,595 | 0.31% | `aggregated-eg-only.txt` |
| Pakistan | PK | 1,424 | 1,423 | 31,654 | 1.49% | `aggregated-pk-only.txt` |
| Malaysia | MY | 2,624 | 2,624 | 10,397 | 0.49% | `aggregated-my-only.txt` |
| Bulgaria | BG | 2,347 | 2,333 | 4,390 | 0.21% | `aggregated-bg-only.txt` |
| Czechia | CZ | 3,747 | 3,746 | 3,422 | 0.16% | `aggregated-cz-only.txt` |
| Colombia | CO | 2,316 | 2,316 | 14,821 | 0.70% | `aggregated-co-only.txt` |
| United Arab Emirates | AE | 3,959 | 3,959 | 7,821 | 0.37% | `aggregated-ae-only.txt` |
| Romania | RO | 4,120 | 4,110 | 4,348 | 0.20% | `aggregated-ro-only.txt` |
| Kazakhstan | KZ | 1,344 | 1,343 | 6,056 | 0.29% | `aggregated-kz-only.txt` |
| Morocco | MA | 518 | 518 | 9,420 | 0.44% | `aggregated-ma-only.txt` |
| Saudi Arabia | SA | 1,752 | 1,752 | 8,398 | 0.40% | `aggregated-sa-only.txt` |
| South Africa | ZA | 4,131 | 4,118 | 16,092 | 0.76% | `aggregated-za-only.txt` |
| Bangladesh | BD | 2,740 | 2,738 | 20,839 | 0.98% | `aggregated-bd-only.txt` |
| Chile | CL | 1,986 | 1,984 | 12,393 | 0.58% | `aggregated-cl-only.txt` |
| Nigeria | NG | 1,167 | 1,167 | 3,684 | 0.17% | `aggregated-ng-only.txt` |
| Kenya | KE | 910 | 910 | 5,799 | 0.27% | `aggregated-ke-only.txt` |
| Algeria | DZ | 226 | 226 | 4,208 | 0.20% | `aggregated-dz-only.txt` |
| Serbia | RS | 1,024 | 1,022 | 2,348 | 0.11% | `aggregated-rs-only.txt` |
| Peru | PE | 1,135 | 1,134 | 4,251 | 0.20% | `aggregated-pe-only.txt` |
| Sri Lanka | LK | 259 | 259 | 1,323 | 0.06% | `aggregated-lk-only.txt` |
| Iraq | IQ | 695 | 695 | 6,768 | 0.32% | `aggregated-iq-only.txt` |
| Ethiopia | ET | 107 | 107 | 2,477 | 0.12% | `aggregated-et-only.txt` |
| Ghana | GH | 363 | 363 | 934 | 0.04% | `aggregated-gh-only.txt` |
| Belarus | BY | 437 | 437 | 2,158 | 0.10% | `aggregated-by-only.txt` |

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

- **`aggregated.txt`** - 2,123,235 total aggregated IPs from all sources
- **`aggregated-ae-only.txt`** - 7,821 IPs from AE
- **`aggregated-ar-only.txt`** - 36,661 IPs from AR
- **`aggregated-au-only.txt`** - 20,558 IPs from AU
- **`aggregated-bd-only.txt`** - 20,839 IPs from BD
- **`aggregated-bg-only.txt`** - 4,390 IPs from BG
- **`aggregated-br-only.txt`** - 112,393 IPs from BR
- **`aggregated-by-only.txt`** - 2,158 IPs from BY
- **`aggregated-ca-only.txt`** - 36,283 IPs from CA
- **`aggregated-cl-only.txt`** - 12,393 IPs from CL
- **`aggregated-cn-only.txt`** - 309,213 IPs from CN
- **`aggregated-co-only.txt`** - 14,821 IPs from CO
- **`aggregated-cz-only.txt`** - 3,422 IPs from CZ
- **`aggregated-de-only.txt`** - 65,825 IPs from DE
- **`aggregated-dz-only.txt`** - 4,208 IPs from DZ
- **`aggregated-eg-only.txt`** - 6,595 IPs from EG
- **`aggregated-es-only.txt`** - 17,624 IPs from ES
- **`aggregated-et-only.txt`** - 2,477 IPs from ET
- **`aggregated-fr-only.txt`** - 38,808 IPs from FR
- **`aggregated-gb-only.txt`** - 48,435 IPs from GB
- **`aggregated-gh-only.txt`** - 934 IPs from GH
- **`aggregated-id-only.txt`** - 42,006 IPs from ID
- **`aggregated-in-only.txt`** - 103,100 IPs from IN
- **`aggregated-iq-only.txt`** - 6,768 IPs from IQ
- **`aggregated-ir-only.txt`** - 9,070 IPs from IR
- **`aggregated-it-only.txt`** - 24,993 IPs from IT
- **`aggregated-ke-only.txt`** - 5,799 IPs from KE
- **`aggregated-kr-only.txt`** - 24,124 IPs from KR
- **`aggregated-kz-only.txt`** - 6,056 IPs from KZ
- **`aggregated-lk-only.txt`** - 1,323 IPs from LK
- **`aggregated-ma-only.txt`** - 9,420 IPs from MA
- **`aggregated-mx-only.txt`** - 29,046 IPs from MX
- **`aggregated-my-only.txt`** - 10,397 IPs from MY
- **`aggregated-ng-only.txt`** - 3,684 IPs from NG
- **`aggregated-nl-only.txt`** - 61,285 IPs from NL
- **`aggregated-pe-only.txt`** - 4,251 IPs from PE
- **`aggregated-pk-only.txt`** - 31,654 IPs from PK
- **`aggregated-pl-only.txt`** - 16,106 IPs from PL
- **`aggregated-ro-only.txt`** - 4,348 IPs from RO
- **`aggregated-rs-only.txt`** - 2,348 IPs from RS
- **`aggregated-ru-only.txt`** - 49,955 IPs from RU
- **`aggregated-sa-only.txt`** - 8,398 IPs from SA
- **`aggregated-sg-only.txt`** - 55,390 IPs from SG
- **`aggregated-th-only.txt`** - 19,581 IPs from TH
- **`aggregated-tr-only.txt`** - 24,248 IPs from TR
- **`aggregated-tw-only.txt`** - 22,071 IPs from TW
- **`aggregated-ua-only.txt`** - 29,630 IPs from UA
- **`aggregated-us-only.txt`** - 403,121 IPs from US
- **`aggregated-ve-only.txt`** - 12,812 IPs from VE
- **`aggregated-vn-only.txt`** - 48,146 IPs from VN
- **`aggregated-za-only.txt`** - 16,092 IPs from ZA
- **`aggregated-multi-50countries-combined.txt`** - 1,851,080 unique IPs (deduplicated across all countries)

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

