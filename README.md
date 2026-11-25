# Multi-Country IP Address Internet Blocklist Aggregator

![Workflow Status](https://github.com/dewdmadbro/ip-blocklist-dewd/actions/workflows/ip-aggregation.yml/badge.svg)
![Countries](https://img.shields.io/badge/Countries-50-278EF5)
![Total IPs Blocked](https://img.shields.io/badge/Blocked_IPs-2192572-2D56A8)
          
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

**Last Updated:** 2026-11-25 21:57:23 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 20.8
"China" : 15.6
"Brazil" : 4.6
"India" : 4.5
"Germany" : 3.3
"Netherlands" : 2.9
"Singapore" : 2.8
"Russia" : 2.8
"United Kingdom" : 2.2
"Vietnam" : 2.1
"France" : 1.9
"Indonesia" : 1.8
"Canada" : 1.7
"Pakistan" : 1.6
"Argentina" : 1.5
"Ukraine" : 1.4
"Mexico" : 1.3
"South Korea" : 1.1
"Italy" : 1.1
"Other/Unfiltered" : 25.0
```

## Overall Summary

- **Total Input IPs:** 2,192,572
- **Countries Processed:** 50
- **Combined Unique IPs:** 1,931,461
- **Combined Output File:** `aggregated-multi-50countries-combined.txt`
- **Overall Filter Rate:** 88.09%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 131,096 | 129,226 | 455,326 | 20.77% | `aggregated-us-only.txt` |
| China | CN | 7,927 | 7,926 | 341,867 | 15.59% | `aggregated-cn-only.txt` |
| India | IN | 13,799 | 13,774 | 98,220 | 4.48% | `aggregated-in-only.txt` |
| Germany | DE | 30,809 | 30,705 | 72,105 | 3.29% | `aggregated-de-only.txt` |
| Russia | RU | 13,434 | 13,203 | 60,998 | 2.78% | `aggregated-ru-only.txt` |
| United Kingdom | GB | 36,853 | 36,697 | 49,109 | 2.24% | `aggregated-gb-only.txt` |
| Thailand | TH | 2,112 | 2,112 | 18,783 | 0.86% | `aggregated-th-only.txt` |
| Vietnam | VN | 2,294 | 2,294 | 46,058 | 2.10% | `aggregated-vn-only.txt` |
| South Korea | KR | 4,056 | 4,047 | 24,489 | 1.12% | `aggregated-kr-only.txt` |
| Brazil | BR | 11,637 | 11,590 | 100,777 | 4.60% | `aggregated-br-only.txt` |
| Taiwan | TW | 2,538 | 2,538 | 22,618 | 1.03% | `aggregated-tw-only.txt` |
| Canada | CA | 17,849 | 17,727 | 38,173 | 1.74% | `aggregated-ca-only.txt` |
| Singapore | SG | 9,895 | 9,883 | 61,527 | 2.81% | `aggregated-sg-only.txt` |
| Italy | IT | 10,117 | 10,080 | 24,270 | 1.11% | `aggregated-it-only.txt` |
| Netherlands | NL | 19,221 | 19,122 | 64,313 | 2.93% | `aggregated-nl-only.txt` |
| Indonesia | ID | 6,879 | 6,858 | 40,342 | 1.84% | `aggregated-id-only.txt` |
| France | FR | 33,764 | 33,733 | 41,686 | 1.90% | `aggregated-fr-only.txt` |
| Venezuela | VE | 1,023 | 1,023 | 11,097 | 0.51% | `aggregated-ve-only.txt` |
| Australia | AU | 11,856 | 11,786 | 21,243 | 0.97% | `aggregated-au-only.txt` |
| Turkey | TR | 3,618 | 3,591 | 23,283 | 1.06% | `aggregated-tr-only.txt` |
| Ukraine | UA | 5,421 | 5,379 | 29,927 | 1.36% | `aggregated-ua-only.txt` |
| Iran | IR | 2,080 | 2,079 | 10,737 | 0.49% | `aggregated-ir-only.txt` |
| Poland | PL | 8,541 | 8,513 | 20,717 | 0.94% | `aggregated-pl-only.txt` |
| Mexico | MX | 4,451 | 4,444 | 27,774 | 1.27% | `aggregated-mx-only.txt` |
| Spain | ES | 11,794 | 11,775 | 17,428 | 0.79% | `aggregated-es-only.txt` |
| Argentina | AR | 3,666 | 3,666 | 32,206 | 1.47% | `aggregated-ar-only.txt` |
| Egypt | EG | 800 | 800 | 5,635 | 0.26% | `aggregated-eg-only.txt` |
| Pakistan | PK | 1,462 | 1,460 | 35,981 | 1.64% | `aggregated-pk-only.txt` |
| Malaysia | MY | 2,720 | 2,720 | 10,556 | 0.48% | `aggregated-my-only.txt` |
| Bulgaria | BG | 2,392 | 2,378 | 4,263 | 0.19% | `aggregated-bg-only.txt` |
| Czechia | CZ | 3,807 | 3,805 | 2,988 | 0.14% | `aggregated-cz-only.txt` |
| Colombia | CO | 2,372 | 2,372 | 12,933 | 0.59% | `aggregated-co-only.txt` |
| United Arab Emirates | AE | 4,004 | 4,004 | 7,077 | 0.32% | `aggregated-ae-only.txt` |
| Romania | RO | 4,161 | 4,150 | 4,947 | 0.23% | `aggregated-ro-only.txt` |
| Kazakhstan | KZ | 1,378 | 1,377 | 4,837 | 0.22% | `aggregated-kz-only.txt` |
| Morocco | MA | 531 | 531 | 6,869 | 0.31% | `aggregated-ma-only.txt` |
| Saudi Arabia | SA | 1,825 | 1,825 | 8,206 | 0.37% | `aggregated-sa-only.txt` |
| South Africa | ZA | 4,009 | 3,996 | 13,299 | 0.61% | `aggregated-za-only.txt` |
| Bangladesh | BD | 2,961 | 2,956 | 19,649 | 0.90% | `aggregated-bd-only.txt` |
| Chile | CL | 2,020 | 2,018 | 11,236 | 0.51% | `aggregated-cl-only.txt` |
| Nigeria | NG | 1,195 | 1,195 | 2,709 | 0.12% | `aggregated-ng-only.txt` |
| Kenya | KE | 934 | 934 | 5,289 | 0.24% | `aggregated-ke-only.txt` |
| Algeria | DZ | 233 | 233 | 2,930 | 0.13% | `aggregated-dz-only.txt` |
| Serbia | RS | 1,033 | 1,033 | 1,996 | 0.09% | `aggregated-rs-only.txt` |
| Peru | PE | 1,168 | 1,167 | 3,772 | 0.17% | `aggregated-pe-only.txt` |
| Sri Lanka | LK | 275 | 275 | 1,157 | 0.05% | `aggregated-lk-only.txt` |
| Iraq | IQ | 721 | 721 | 5,594 | 0.26% | `aggregated-iq-only.txt` |
| Ethiopia | ET | 122 | 122 | 1,869 | 0.09% | `aggregated-et-only.txt` |
| Ghana | GH | 373 | 373 | 833 | 0.04% | `aggregated-gh-only.txt` |
| Belarus | BY | 467 | 467 | 1,763 | 0.08% | `aggregated-by-only.txt` |

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

- **`aggregated.txt`** - 2,192,572 total aggregated IPs from all sources
- **`aggregated-ae-only.txt`** - 7,077 IPs from AE
- **`aggregated-ar-only.txt`** - 32,206 IPs from AR
- **`aggregated-au-only.txt`** - 21,243 IPs from AU
- **`aggregated-bd-only.txt`** - 19,649 IPs from BD
- **`aggregated-bg-only.txt`** - 4,263 IPs from BG
- **`aggregated-br-only.txt`** - 100,777 IPs from BR
- **`aggregated-by-only.txt`** - 1,763 IPs from BY
- **`aggregated-ca-only.txt`** - 38,173 IPs from CA
- **`aggregated-cl-only.txt`** - 11,236 IPs from CL
- **`aggregated-cn-only.txt`** - 341,867 IPs from CN
- **`aggregated-co-only.txt`** - 12,933 IPs from CO
- **`aggregated-cz-only.txt`** - 2,988 IPs from CZ
- **`aggregated-de-only.txt`** - 72,105 IPs from DE
- **`aggregated-dz-only.txt`** - 2,930 IPs from DZ
- **`aggregated-eg-only.txt`** - 5,635 IPs from EG
- **`aggregated-es-only.txt`** - 17,428 IPs from ES
- **`aggregated-et-only.txt`** - 1,869 IPs from ET
- **`aggregated-fr-only.txt`** - 41,686 IPs from FR
- **`aggregated-gb-only.txt`** - 49,109 IPs from GB
- **`aggregated-gh-only.txt`** - 833 IPs from GH
- **`aggregated-id-only.txt`** - 40,342 IPs from ID
- **`aggregated-in-only.txt`** - 98,220 IPs from IN
- **`aggregated-iq-only.txt`** - 5,594 IPs from IQ
- **`aggregated-ir-only.txt`** - 10,737 IPs from IR
- **`aggregated-it-only.txt`** - 24,270 IPs from IT
- **`aggregated-ke-only.txt`** - 5,289 IPs from KE
- **`aggregated-kr-only.txt`** - 24,489 IPs from KR
- **`aggregated-kz-only.txt`** - 4,837 IPs from KZ
- **`aggregated-lk-only.txt`** - 1,157 IPs from LK
- **`aggregated-ma-only.txt`** - 6,869 IPs from MA
- **`aggregated-mx-only.txt`** - 27,774 IPs from MX
- **`aggregated-my-only.txt`** - 10,556 IPs from MY
- **`aggregated-ng-only.txt`** - 2,709 IPs from NG
- **`aggregated-nl-only.txt`** - 64,313 IPs from NL
- **`aggregated-pe-only.txt`** - 3,772 IPs from PE
- **`aggregated-pk-only.txt`** - 35,981 IPs from PK
- **`aggregated-pl-only.txt`** - 20,717 IPs from PL
- **`aggregated-ro-only.txt`** - 4,947 IPs from RO
- **`aggregated-rs-only.txt`** - 1,996 IPs from RS
- **`aggregated-ru-only.txt`** - 60,998 IPs from RU
- **`aggregated-sa-only.txt`** - 8,206 IPs from SA
- **`aggregated-sg-only.txt`** - 61,527 IPs from SG
- **`aggregated-th-only.txt`** - 18,783 IPs from TH
- **`aggregated-tr-only.txt`** - 23,283 IPs from TR
- **`aggregated-tw-only.txt`** - 22,618 IPs from TW
- **`aggregated-ua-only.txt`** - 29,927 IPs from UA
- **`aggregated-us-only.txt`** - 455,326 IPs from US
- **`aggregated-ve-only.txt`** - 11,097 IPs from VE
- **`aggregated-vn-only.txt`** - 46,058 IPs from VN
- **`aggregated-za-only.txt`** - 13,299 IPs from ZA
- **`aggregated-multi-50countries-combined.txt`** - 1,931,461 unique IPs (deduplicated across all countries)

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

