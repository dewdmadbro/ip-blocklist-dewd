# Multi-Country IP Aggregation Statistics

**Last Updated:** 2026-05-03 09:41:52 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 16.2
"Netherlands" : 5.3
"Germany" : 3.8
"Singapore" : 3.1
"United Kingdom" : 2.9
"Canada" : 2.3
"France" : 2.0
"Australia" : 1.7
"Australia" : 1.7
"Italy" : 1.5
"South Korea" : 1.4
"Japan" : 1.3
"Mexico" : 1.1
"Spain" : 0.7
"Other/Unfiltered" : 55.1
```

## Overall Summary

- **Total Input IPs:** 900,479
- **Countries Processed:** 14
- **Combined Unique IPs:** 389,500
- **Combined Output File:** `aggregated-multi-14countries-combined.txt`
- **Overall Filter Rate:** 43.25%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| France | FR | 32,393 | 32,367 | 17,600 | 1.95% | `aggregated-fr-only.txt` |
| Netherlands | NL | 18,273 | 18,151 | 47,515 | 5.28% | `aggregated-nl-only.txt` |
| Italy | IT | 9,580 | 9,556 | 13,291 | 1.48% | `aggregated-it-only.txt` |
| Spain | ES | 11,140 | 11,107 | 6,247 | 0.69% | `aggregated-es-only.txt` |
| Mexico | MX | 4,307 | 4,303 | 9,874 | 1.10% | `aggregated-mx-only.txt` |
| Japan | JP | 12,061 | 12,055 | 12,081 | 1.34% | `aggregated-jp-only.txt` |
| Australia | AU | 11,396 | 11,317 | 14,928 | 1.66% | `aggregated-au-only.txt` |
| Singapore | SG | 9,268 | 9,258 | 27,523 | 3.06% | `aggregated-sg-only.txt` |
| United States | US | 169,198 | 167,680 | 145,650 | 16.17% | `aggregated-us-only.txt` |
| Canada | CA | 16,890 | 16,768 | 21,147 | 2.35% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 33,411 | 33,252 | 26,262 | 2.92% | `aggregated-gb-only.txt` |
| Australia | AU | 11,396 | 11,317 | 14,928 | 1.66% | `aggregated-au-only.txt` |
| Germany | DE | 28,972 | 28,867 | 34,565 | 3.84% | `aggregated-de-only.txt` |
| South Korea | KR | 4,006 | 3,996 | 12,817 | 1.42% | `aggregated-kr-only.txt` |

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
- **Source 18:** https://raw.githubusercontent.com/borestad/firehol-mirror/refs/heads/main/firehol_level3.netset
- **Source 19:** https://raw.githubusercontent.com/borestad/firehol-mirror/refs/heads/main/ciarmy.ipset
- **Source 20:** https://raw.githubusercontent.com/borestad/firehol-mirror/refs/heads/main/firehol_level4.netset

## Configuration Details

