# Multi-Country IP Address Internet Blocklist Aggregator

![Workflow Status](https://github.com/dewdmadbro/ip-blocklist-dewd/actions/workflows/ip-aggregation.yml/badge.svg)
![Countries](https://img.shields.io/badge/Countries-50-278EF5)
![Total IPs Blocked](https://img.shields.io/badge/Blocked_IPs-1981535-2D56A8)
          
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

**Last Updated:** 2026-09-20 21:02:59 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 19.0
"China" : 13.1
"Brazil" : 6.1
"India" : 5.0
"Netherlands" : 2.9
"Germany" : 2.8
"Vietnam" : 2.5
"Singapore" : 2.4
"Russia" : 2.3
"United Kingdom" : 2.3
"Indonesia" : 2.1
"Canada" : 1.8
"France" : 1.8
"Argentina" : 1.7
"Pakistan" : 1.5
"Mexico" : 1.4
"Ukraine" : 1.3
"Turkey" : 1.2
"Italy" : 1.1
"Other/Unfiltered" : 27.7
```

## Overall Summary

- **Total Input IPs:** 1,981,535
- **Countries Processed:** 50
- **Combined Unique IPs:** 1,718,272
- **Combined Output File:** `aggregated-multi-50countries-combined.txt`
- **Overall Filter Rate:** 86.71%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 128,919 | 127,081 | 377,415 | 19.05% | `aggregated-us-only.txt` |
| China | CN | 8,091 | 8,090 | 260,024 | 13.12% | `aggregated-cn-only.txt` |
| India | IN | 13,284 | 13,257 | 99,056 | 5.00% | `aggregated-in-only.txt` |
| Germany | DE | 29,692 | 29,583 | 55,858 | 2.82% | `aggregated-de-only.txt` |
| Russia | RU | 13,208 | 12,972 | 45,815 | 2.31% | `aggregated-ru-only.txt` |
| United Kingdom | GB | 36,037 | 35,862 | 45,098 | 2.28% | `aggregated-gb-only.txt` |
| Thailand | TH | 2,087 | 2,087 | 19,775 | 1.00% | `aggregated-th-only.txt` |
| Vietnam | VN | 2,231 | 2,231 | 48,976 | 2.47% | `aggregated-vn-only.txt` |
| South Korea | KR | 3,953 | 3,919 | 21,927 | 1.11% | `aggregated-kr-only.txt` |
| Brazil | BR | 12,549 | 12,508 | 121,714 | 6.14% | `aggregated-br-only.txt` |
| Taiwan | TW | 2,432 | 2,432 | 20,814 | 1.05% | `aggregated-tw-only.txt` |
| Canada | CA | 17,281 | 17,163 | 36,037 | 1.82% | `aggregated-ca-only.txt` |
| Singapore | SG | 9,652 | 9,642 | 48,389 | 2.44% | `aggregated-sg-only.txt` |
| Italy | IT | 9,775 | 9,761 | 22,344 | 1.13% | `aggregated-it-only.txt` |
| Netherlands | NL | 18,262 | 18,151 | 57,474 | 2.90% | `aggregated-nl-only.txt` |
| Indonesia | ID | 6,635 | 6,614 | 41,183 | 2.08% | `aggregated-id-only.txt` |
| France | FR | 33,431 | 33,402 | 35,234 | 1.78% | `aggregated-fr-only.txt` |
| Venezuela | VE | 966 | 966 | 12,994 | 0.66% | `aggregated-ve-only.txt` |
| Australia | AU | 12,686 | 12,614 | 20,387 | 1.03% | `aggregated-au-only.txt` |
| Turkey | TR | 3,535 | 3,510 | 23,311 | 1.18% | `aggregated-tr-only.txt` |
| Ukraine | UA | 5,533 | 5,492 | 25,252 | 1.27% | `aggregated-ua-only.txt` |
| Iran | IR | 2,075 | 2,074 | 7,234 | 0.37% | `aggregated-ir-only.txt` |
| Poland | PL | 8,261 | 8,231 | 11,919 | 0.60% | `aggregated-pl-only.txt` |
| Mexico | MX | 4,267 | 4,263 | 27,957 | 1.41% | `aggregated-mx-only.txt` |
| Spain | ES | 11,567 | 11,531 | 17,291 | 0.87% | `aggregated-es-only.txt` |
| Argentina | AR | 3,494 | 3,492 | 33,501 | 1.69% | `aggregated-ar-only.txt` |
| Egypt | EG | 743 | 743 | 6,656 | 0.34% | `aggregated-eg-only.txt` |
| Pakistan | PK | 1,373 | 1,372 | 28,900 | 1.46% | `aggregated-pk-only.txt` |
| Malaysia | MY | 2,600 | 2,600 | 9,114 | 0.46% | `aggregated-my-only.txt` |
| Bulgaria | BG | 2,371 | 2,361 | 4,246 | 0.21% | `aggregated-bg-only.txt` |
| Czechia | CZ | 3,722 | 3,721 | 3,014 | 0.15% | `aggregated-cz-only.txt` |
| Colombia | CO | 2,254 | 2,254 | 14,004 | 0.71% | `aggregated-co-only.txt` |
| United Arab Emirates | AE | 3,804 | 3,804 | 7,937 | 0.40% | `aggregated-ae-only.txt` |
| Romania | RO | 4,081 | 4,072 | 4,047 | 0.20% | `aggregated-ro-only.txt` |
| Kazakhstan | KZ | 1,313 | 1,310 | 6,440 | 0.33% | `aggregated-kz-only.txt` |
| Morocco | MA | 491 | 491 | 10,181 | 0.51% | `aggregated-ma-only.txt` |
| Saudi Arabia | SA | 1,720 | 1,720 | 9,473 | 0.48% | `aggregated-sa-only.txt` |
| South Africa | ZA | 4,109 | 4,095 | 15,075 | 0.76% | `aggregated-za-only.txt` |
| Bangladesh | BD | 2,721 | 2,719 | 16,917 | 0.85% | `aggregated-bd-only.txt` |
| Chile | CL | 1,957 | 1,955 | 11,522 | 0.58% | `aggregated-cl-only.txt` |
| Nigeria | NG | 1,126 | 1,126 | 3,201 | 0.16% | `aggregated-ng-only.txt` |
| Kenya | KE | 891 | 891 | 5,436 | 0.27% | `aggregated-ke-only.txt` |
| Algeria | DZ | 220 | 220 | 4,599 | 0.23% | `aggregated-dz-only.txt` |
| Serbia | RS | 1,007 | 1,005 | 2,331 | 0.12% | `aggregated-rs-only.txt` |
| Peru | PE | 1,121 | 1,120 | 3,863 | 0.19% | `aggregated-pe-only.txt` |
| Sri Lanka | LK | 253 | 253 | 1,297 | 0.07% | `aggregated-lk-only.txt` |
| Iraq | IQ | 666 | 666 | 7,447 | 0.38% | `aggregated-iq-only.txt` |
| Ethiopia | ET | 100 | 100 | 2,533 | 0.13% | `aggregated-et-only.txt` |
| Ghana | GH | 352 | 352 | 926 | 0.05% | `aggregated-gh-only.txt` |
| Belarus | BY | 427 | 427 | 2,134 | 0.11% | `aggregated-by-only.txt` |

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

- **`aggregated.txt`** - 1,981,535 total aggregated IPs from all sources
- **`aggregated-ae-only.txt`** - 7,937 IPs from AE
- **`aggregated-ar-only.txt`** - 33,501 IPs from AR
- **`aggregated-au-only.txt`** - 20,387 IPs from AU
- **`aggregated-bd-only.txt`** - 16,917 IPs from BD
- **`aggregated-bg-only.txt`** - 4,246 IPs from BG
- **`aggregated-br-only.txt`** - 121,714 IPs from BR
- **`aggregated-by-only.txt`** - 2,134 IPs from BY
- **`aggregated-ca-only.txt`** - 36,037 IPs from CA
- **`aggregated-cl-only.txt`** - 11,522 IPs from CL
- **`aggregated-cn-only.txt`** - 260,024 IPs from CN
- **`aggregated-co-only.txt`** - 14,004 IPs from CO
- **`aggregated-cz-only.txt`** - 3,014 IPs from CZ
- **`aggregated-de-only.txt`** - 55,858 IPs from DE
- **`aggregated-dz-only.txt`** - 4,599 IPs from DZ
- **`aggregated-eg-only.txt`** - 6,656 IPs from EG
- **`aggregated-es-only.txt`** - 17,291 IPs from ES
- **`aggregated-et-only.txt`** - 2,533 IPs from ET
- **`aggregated-fr-only.txt`** - 35,234 IPs from FR
- **`aggregated-gb-only.txt`** - 45,098 IPs from GB
- **`aggregated-gh-only.txt`** - 926 IPs from GH
- **`aggregated-id-only.txt`** - 41,183 IPs from ID
- **`aggregated-in-only.txt`** - 99,056 IPs from IN
- **`aggregated-iq-only.txt`** - 7,447 IPs from IQ
- **`aggregated-ir-only.txt`** - 7,234 IPs from IR
- **`aggregated-it-only.txt`** - 22,344 IPs from IT
- **`aggregated-ke-only.txt`** - 5,436 IPs from KE
- **`aggregated-kr-only.txt`** - 21,927 IPs from KR
- **`aggregated-kz-only.txt`** - 6,440 IPs from KZ
- **`aggregated-lk-only.txt`** - 1,297 IPs from LK
- **`aggregated-ma-only.txt`** - 10,181 IPs from MA
- **`aggregated-mx-only.txt`** - 27,957 IPs from MX
- **`aggregated-my-only.txt`** - 9,114 IPs from MY
- **`aggregated-ng-only.txt`** - 3,201 IPs from NG
- **`aggregated-nl-only.txt`** - 57,474 IPs from NL
- **`aggregated-pe-only.txt`** - 3,863 IPs from PE
- **`aggregated-pk-only.txt`** - 28,900 IPs from PK
- **`aggregated-pl-only.txt`** - 11,919 IPs from PL
- **`aggregated-ro-only.txt`** - 4,047 IPs from RO
- **`aggregated-rs-only.txt`** - 2,331 IPs from RS
- **`aggregated-ru-only.txt`** - 45,815 IPs from RU
- **`aggregated-sa-only.txt`** - 9,473 IPs from SA
- **`aggregated-sg-only.txt`** - 48,389 IPs from SG
- **`aggregated-th-only.txt`** - 19,775 IPs from TH
- **`aggregated-tr-only.txt`** - 23,311 IPs from TR
- **`aggregated-tw-only.txt`** - 20,814 IPs from TW
- **`aggregated-ua-only.txt`** - 25,252 IPs from UA
- **`aggregated-us-only.txt`** - 377,415 IPs from US
- **`aggregated-ve-only.txt`** - 12,994 IPs from VE
- **`aggregated-vn-only.txt`** - 48,976 IPs from VN
- **`aggregated-za-only.txt`** - 15,075 IPs from ZA
- **`aggregated-multi-50countries-combined.txt`** - 1,718,272 unique IPs (deduplicated across all countries)

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

