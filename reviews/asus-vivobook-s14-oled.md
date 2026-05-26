---
model: ASUS VivoBook S 14 OLED
slug: asus-vivobook-s14-oled
manufacturer: ASUS
status: available
form_factor: clamshell
weight_kg: 1.31
battery_wh: 75
price_usd: 1200
display:
  aspect_ratio: '16:10'
  panel: OLED
  size_in: 14.0
variants:
- benchmarks:
    cinebench_r23_multi: 21058
    cinebench_r23_single: 2001
    geekbench6_multi: 15059
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
    pl1_w: 54
    pl2_w: 65
  ram_gb: 32
  ram_type: LPDDR5X
  ram_upgradeable: false
  sku: M5406WA
  year: 2025
noise:
  balanced_dba: 39
  low_power_dba: 34
  max_dba: 53
  performance_dba: 49
linux:
  issues:
  - Not tested on Linux
  - WiFi chip may overheat under sustained 45W+ load with WiFi active
  - Strix Point generally works with kernel 6.12+
  status: unknown
sources:
- https://www.notebookcheck.net/Asus-VivoBook-S-14-OLED-laptop-review-Successful-performance-of-the-Ryzen-AI-9-HX-370.880476.0.html
---
# ASUS VivoBook S 14 OLED (M5406WA)

## Overview

Lightest HX 370 laptop at 1.31 kg with impressive 54W sustained power.

## Sustained Performance

- **54W PL1 sustained** — remarkable for 1.31 kg
- CB R23 multi 21,058 — strong
- R15 loop showed some variance (2,603-3,345 range) — "not completely constant"
- Standard profile at 39 dB is a good daily driver
- Performance mode at 49 dB gets loud

## Concerns

- WiFi chip overheating reported under sustained 45W+ load with WiFi active
- 32 GB LPDDR5X soldered — not upgradeable
- Linux untested

## Sources

- [NotebookCheck review](https://www.notebookcheck.net/Asus-VivoBook-S-14-OLED-laptop-review-Successful-performance-of-the-Ryzen-AI-9-HX-370.880476.0.html)