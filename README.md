# Multi-Country IP Address Internet Blocklist Aggregator

![Workflow Status](https://github.com/dewdmadbro/ip-blocklist-dewd/actions/workflows/ip-aggregation.yml/badge.svg)
![Countries](https://img.shields.io/badge/Countries-50-278EF5)
![Total IPs Blocked](https://img.shields.io/badge/Blocked_IPs-1062996-2D56A8)
          
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

**Last Updated:** 2026-05-18 16:03:18 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 19.1
"China" : 12.8
"India" : 6.2
"Netherlands" : 4.8
"Brazil" : 4.2
"Germany" : 3.8
"Vietnam" : 3.3
"Singapore" : 3.0
"United Kingdom" : 2.8
"Indonesia" : 2.4
"Russia" : 2.4
"Canada" : 2.1
"France" : 1.9
"Australia" : 1.5
"South Korea" : 1.3
"Italy" : 1.3
"Thailand" : 1.3
"Pakistan" : 1.3
"Taiwan" : 1.2
"Other/Unfiltered" : 23.1
```

## Overall Summary

- **Total Input IPs:** 1,062,996
- **Countries Processed:** 50
- **Combined Unique IPs:** 941,249
- **Combined Output File:** `aggregated-multi-50countries-combined.txt`
- **Overall Filter Rate:** 88.55%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 167,217 | 165,713 | 203,480 | 19.14% | `aggregated-us-only.txt` |
| China | CN | 7,572 | 7,571 | 136,520 | 12.84% | `aggregated-cn-only.txt` |
| India | IN | 12,832 | 12,801 | 66,049 | 6.21% | `aggregated-in-only.txt` |
| Germany | DE | 28,842 | 28,762 | 39,940 | 3.76% | `aggregated-de-only.txt` |
| Russia | RU | 13,087 | 12,857 | 25,123 | 2.36% | `aggregated-ru-only.txt` |
| United Kingdom | GB | 33,930 | 33,764 | 30,284 | 2.85% | `aggregated-gb-only.txt` |
| Thailand | TH | 1,936 | 1,935 | 13,615 | 1.28% | `aggregated-th-only.txt` |
| Vietnam | VN | 2,142 | 2,142 | 35,530 | 3.34% | `aggregated-vn-only.txt` |
| South Korea | KR | 3,976 | 3,966 | 14,331 | 1.35% | `aggregated-kr-only.txt` |
| Brazil | BR | 13,022 | 12,952 | 44,214 | 4.16% | `aggregated-br-only.txt` |
| Taiwan | TW | 2,417 | 2,417 | 13,024 | 1.23% | `aggregated-tw-only.txt` |
| Canada | CA | 17,079 | 16,951 | 22,815 | 2.15% | `aggregated-ca-only.txt` |
| Singapore | SG | 9,249 | 9,239 | 32,335 | 3.04% | `aggregated-sg-only.txt` |
| Italy | IT | 9,537 | 9,513 | 13,889 | 1.31% | `aggregated-it-only.txt` |
| Netherlands | NL | 18,516 | 18,392 | 50,981 | 4.80% | `aggregated-nl-only.txt` |
| Indonesia | ID | 6,418 | 6,397 | 25,340 | 2.38% | `aggregated-id-only.txt` |
| France | FR | 32,086 | 32,060 | 20,161 | 1.90% | `aggregated-fr-only.txt` |
| Venezuela | VE | 924 | 924 | 6,494 | 0.61% | `aggregated-ve-only.txt` |
| Australia | AU | 12,099 | 12,029 | 15,873 | 1.49% | `aggregated-au-only.txt` |
| Turkey | TR | 3,406 | 3,380 | 12,377 | 1.16% | `aggregated-tr-only.txt` |
| Ukraine | UA | 5,551 | 5,496 | 8,085 | 0.76% | `aggregated-ua-only.txt` |
| Iran | IR | 2,016 | 2,015 | 3,941 | 0.37% | `aggregated-ir-only.txt` |
| Poland | PL | 8,036 | 8,005 | 7,465 | 0.70% | `aggregated-pl-only.txt` |
| Mexico | MX | 4,410 | 4,406 | 10,593 | 1.00% | `aggregated-mx-only.txt` |
| Spain | ES | 11,163 | 11,132 | 7,626 | 0.72% | `aggregated-es-only.txt` |
| Argentina | AR | 3,467 | 3,465 | 8,993 | 0.85% | `aggregated-ar-only.txt` |
| Egypt | EG | 716 | 716 | 2,731 | 0.26% | `aggregated-eg-only.txt` |
| Pakistan | PK | 1,319 | 1,319 | 13,447 | 1.27% | `aggregated-pk-only.txt` |
| Malaysia | MY | 2,492 | 2,492 | 5,232 | 0.49% | `aggregated-my-only.txt` |
| Bulgaria | BG | 2,275 | 2,265 | 2,750 | 0.26% | `aggregated-bg-only.txt` |
| Czechia | CZ | 3,605 | 3,604 | 1,684 | 0.16% | `aggregated-cz-only.txt` |
| Colombia | CO | 2,207 | 2,207 | 4,501 | 0.42% | `aggregated-co-only.txt` |
| United Arab Emirates | AE | 3,233 | 3,233 | 3,407 | 0.32% | `aggregated-ae-only.txt` |
| Romania | RO | 3,924 | 3,915 | 2,092 | 0.20% | `aggregated-ro-only.txt` |
| Kazakhstan | KZ | 1,259 | 1,258 | 2,332 | 0.22% | `aggregated-kz-only.txt` |
| Morocco | MA | 475 | 475 | 3,444 | 0.32% | `aggregated-ma-only.txt` |
| Saudi Arabia | SA | 1,623 | 1,623 | 3,771 | 0.35% | `aggregated-sa-only.txt` |
| South Africa | ZA | 3,965 | 3,952 | 6,902 | 0.65% | `aggregated-za-only.txt` |
| Bangladesh | BD | 2,614 | 2,609 | 5,233 | 0.49% | `aggregated-bd-only.txt` |
| Chile | CL | 1,886 | 1,886 | 2,390 | 0.22% | `aggregated-cl-only.txt` |
| Nigeria | NG | 1,072 | 1,072 | 1,125 | 0.11% | `aggregated-ng-only.txt` |
| Kenya | KE | 855 | 855 | 2,425 | 0.23% | `aggregated-ke-only.txt` |
| Algeria | DZ | 217 | 217 | 1,575 | 0.15% | `aggregated-dz-only.txt` |
| Serbia | RS | 945 | 943 | 1,011 | 0.10% | `aggregated-rs-only.txt` |
| Peru | PE | 1,093 | 1,092 | 1,507 | 0.14% | `aggregated-pe-only.txt` |
| Sri Lanka | LK | 247 | 247 | 631 | 0.06% | `aggregated-lk-only.txt` |
| Iraq | IQ | 682 | 682 | 1,899 | 0.18% | `aggregated-iq-only.txt` |
| Ethiopia | ET | 98 | 98 | 900 | 0.08% | `aggregated-et-only.txt` |
| Ghana | GH | 341 | 341 | 499 | 0.05% | `aggregated-gh-only.txt` |
| Belarus | BY | 418 | 418 | 683 | 0.06% | `aggregated-by-only.txt` |

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

- **`aggregated.txt`** - 1,062,996 total aggregated IPs from all sources
- **`aggregated-ae-only.txt`** - 3,407 IPs from AE
- **`aggregated-ar-only.txt`** - 8,993 IPs from AR
- **`aggregated-au-only.txt`** - 15,873 IPs from AU
- **`aggregated-bd-only.txt`** - 5,233 IPs from BD
- **`aggregated-bg-only.txt`** - 2,750 IPs from BG
- **`aggregated-br-only.txt`** - 44,214 IPs from BR
- **`aggregated-by-only.txt`** - 683 IPs from BY
- **`aggregated-ca-only.txt`** - 22,815 IPs from CA
- **`aggregated-cl-only.txt`** - 2,390 IPs from CL
- **`aggregated-cn-only.txt`** - 136,520 IPs from CN
- **`aggregated-co-only.txt`** - 4,501 IPs from CO
- **`aggregated-cz-only.txt`** - 1,684 IPs from CZ
- **`aggregated-de-only.txt`** - 39,940 IPs from DE
- **`aggregated-dz-only.txt`** - 1,575 IPs from DZ
- **`aggregated-eg-only.txt`** - 2,731 IPs from EG
- **`aggregated-es-only.txt`** - 7,626 IPs from ES
- **`aggregated-et-only.txt`** - 900 IPs from ET
- **`aggregated-fr-only.txt`** - 20,161 IPs from FR
- **`aggregated-gb-only.txt`** - 30,284 IPs from GB
- **`aggregated-gh-only.txt`** - 499 IPs from GH
- **`aggregated-id-only.txt`** - 25,340 IPs from ID
- **`aggregated-in-only.txt`** - 66,049 IPs from IN
- **`aggregated-iq-only.txt`** - 1,899 IPs from IQ
- **`aggregated-ir-only.txt`** - 3,941 IPs from IR
- **`aggregated-it-only.txt`** - 13,889 IPs from IT
- **`aggregated-ke-only.txt`** - 2,425 IPs from KE
- **`aggregated-kr-only.txt`** - 14,331 IPs from KR
- **`aggregated-kz-only.txt`** - 2,332 IPs from KZ
- **`aggregated-lk-only.txt`** - 631 IPs from LK
- **`aggregated-ma-only.txt`** - 3,444 IPs from MA
- **`aggregated-mx-only.txt`** - 10,593 IPs from MX
- **`aggregated-my-only.txt`** - 5,232 IPs from MY
- **`aggregated-ng-only.txt`** - 1,125 IPs from NG
- **`aggregated-nl-only.txt`** - 50,981 IPs from NL
- **`aggregated-pe-only.txt`** - 1,507 IPs from PE
- **`aggregated-pk-only.txt`** - 13,447 IPs from PK
- **`aggregated-pl-only.txt`** - 7,465 IPs from PL
- **`aggregated-ro-only.txt`** - 2,092 IPs from RO
- **`aggregated-rs-only.txt`** - 1,011 IPs from RS
- **`aggregated-ru-only.txt`** - 25,123 IPs from RU
- **`aggregated-sa-only.txt`** - 3,771 IPs from SA
- **`aggregated-sg-only.txt`** - 32,335 IPs from SG
- **`aggregated-th-only.txt`** - 13,615 IPs from TH
- **`aggregated-tr-only.txt`** - 12,377 IPs from TR
- **`aggregated-tw-only.txt`** - 13,024 IPs from TW
- **`aggregated-ua-only.txt`** - 8,085 IPs from UA
- **`aggregated-us-only.txt`** - 203,480 IPs from US
- **`aggregated-ve-only.txt`** - 6,494 IPs from VE
- **`aggregated-vn-only.txt`** - 35,530 IPs from VN
- **`aggregated-za-only.txt`** - 6,902 IPs from ZA
- **`aggregated-multi-50countries-combined.txt`** - 941,249 unique IPs (deduplicated across all countries)

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

