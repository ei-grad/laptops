---
model: TUXEDO InfinityBook Pro 14
slug: tuxedo-infinitybook-pro-14
manufacturer: TUXEDO
status: recommended
form_factor: clamshell
weight_kg: 1.49
battery_wh: 80
price_usd: 1300
display:
  aspect_ratio: '16:10'
  panel: IPS
  refresh_hz: 120
  resolution: 2880x1800
  size_in: 14.0
variants:
- benchmarks:
    cinebench_r23_multi: 22784
    cinebench_r23_single: 2036
    geekbench6_multi: 15735
  cpu:
    arch: Strix Point
    boost_ghz: 5.1
    cores: 12
    name: AMD Ryzen AI 9 HX 370
    threads: 24
  gpu:
    compute_units: 16
    name: Radeon 890M
    type: integrated
  power:
    pl1_w: 65
    pl2_w: 70
  ram_gb: 128
  ram_type: DDR5 SO-DIMM
  ram_upgradeable: true
  year: 2025
noise:
  balanced_dba: 34.1
  max_dba: 46.6
  performance_dba: 42
linux:
  issues: []
  kernel_min: '6.10'
  status: excellent
sources:
- https://www.notebookcheck.net/Tuxedo-Infinity-Book-Pro-14-Gen10-Review-Linux-ultrabook-with-AMD-Zen-5-128-GB-RAM.1095463.0.html
- https://www.tuxedocomputers.com/en/TUXEDO-InfinityBook-Pro-14-Gen10.tuxedo
---
# TUXEDO InfinityBook Pro 14 Gen10

## Overview

Same barebone as XMG Evo 14 (E25) / Schenker Vision 14 — Tongfang **GX4** (`X4SP4NAL`). Ships with TUXEDO OS (Ubuntu-based) or Ubuntu. Native Linux support with everything working out of the box. See [ODM barebones overview](../overviews/odm-barebones-linux.md) for the full brand↔chassis mapping.

## Sustained Performance

- **65W PL1 sustained** — matches ProArt PX13, exceptional for 1.49 kg
- Cinebench R15 loop: stable 3,390-3,457 range — minimal variance
- No throttling reported in extended stress tests
- Balanced profile at 34 dB is quiet for daily use
- Enthusiast profile at 42 dB is a good performance/noise compromise

## Key Specs

- 2x SO-DIMM DDR5 — upgradeable to **128 GB**
- 80 Wh battery
- Dual 47mm fans, Honeywell PTM7958 thermal pads
- 14" 2.8K IPS display, 500 nits
- Wi-Fi 7, Bluetooth 5.4

## Comparison vs ProArt PX13

| | TUXEDO IB Pro 14 | ProArt PX13 (2024) |
|--|--|--|
| Sustained power | 65W | 65W |
| CB R23 multi | 22,784 | 23,020 |
| Weight | 1.49 kg | 1.39 kg |
| RAM | 128 GB upgradeable | 32 GB soldered |
| Linux | Excellent (native) | Fair (xanmod needed) |
| dGPU | No | RTX 4050/4060/4070 |
| Price | ~1,200 EUR | ~2,000 USD |

ProArt PX13 is lighter and has dGPU option, but TUXEDO wins on RAM upgradeability, Linux support, and price.

## Sources

- [NotebookCheck review](https://www.notebookcheck.net/Tuxedo-Infinity-Book-Pro-14-Gen10-Review-Linux-ultrabook-with-AMD-Zen-5-128-GB-RAM.1095463.0.html)
- [TUXEDO product page](https://www.tuxedocomputers.com/en/TUXEDO-InfinityBook-Pro-14-Gen10.tuxedo)