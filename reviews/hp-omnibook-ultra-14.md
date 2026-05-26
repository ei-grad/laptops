---
model: HP OmniBook Ultra 14
slug: hp-omnibook-ultra-14
manufacturer: HP
status: available
form_factor: clamshell
weight_kg: 1.53
battery_wh: 64
price_usd: 1050
display:
  aspect_ratio: '16:10'
  panel: OLED
  refresh_hz: 120
  resolution: 2880x1800
  size_in: 14.0
variants:
- benchmarks:
    cinebench_r23_multi: 21812
    cinebench_r23_single: 1988
    geekbench6_multi: 15220
  cpu:
    arch: Strix Point
    boost_ghz: 5.1
    cores: 12
    name: AMD Ryzen AI 9 HX 375
    threads: 24
  gpu:
    compute_units: 16
    name: Radeon 890M
    type: integrated
  power:
    pl1_w: 47
    pl2_w: 57
  ram_gb: 32
  ram_type: LPDDR5X
  ram_upgradeable: false
  year: 2025
noise:
  idle_dba: 40
  max_dba: 50
linux:
  issues:
  - Not tested on Linux
  - Strix Point generally works with kernel 6.12+
  status: unknown
sources:
- https://www.notebookcheck.net/Ryzen-AI-9-HX-375-performance-debut-HP-OmniBook-Ultra-14-laptop-review.893965.0.html
---
# HP OmniBook Ultra 14

## Overview

Best value HX 370-class laptop at $1,050. 47W sustained with strong multi-core scores.

## Sustained Performance

- **47W PL1 sustained** — strong for a consumer ultrabook
- CB R23 multi 21,812 — performance dips "just a few percentage points" in sustained loops
- Peak noise at 50 dB is loud but not extreme

## Limitations

- 32 GB LPDDR5X soldered — not upgradeable
- ~40 dB at idle is higher than competitors
- Linux not tested but Strix Point generally works with kernel 6.12+

## Sources

- [NotebookCheck review](https://www.notebookcheck.net/Ryzen-AI-9-HX-375-performance-debut-HP-OmniBook-Ultra-14-laptop-review.893965.0.html)