---
model: TUXEDO InfinityBook Pro 15
slug: tuxedo-infinitybook-pro-15
manufacturer: TUXEDO
status: excluded
form_factor: clamshell
weight_kg: 1.77
battery_wh: 99.0
price_usd: 1850
display:
  aspect_ratio: '16:10'
  panel: IPS
  refresh_hz: 300
  resolution: 2560x1600
  size_in: 15.3
  brightness_nits: 545
variants:
- benchmarks: {}
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
    pl1_w: 65.0
    pl2_w: 90.0
  ram_gb: 128
  ram_type: DDR5 SO-DIMM
  ram_upgradeable: true
  year: 2025
noise:
  balanced_dba: 32.9
  max_dba: 47.9
  performance_dba: 36.3
linux:
  issues: []
  kernel_min: '6.10'
  notes:
  - Ships with Ubuntu 24.04 or TUXEDO OS
  - TUXEDO Control Center for fan profiles
  status: excellent
sources:
- https://www.tuxedocomputers.com/en/TUXEDO-InfinityBook-Pro-15-Gen10-AMD.tuxedo
- https://www.notebookcheck.net/Tuxedo-InfinityBook-Pro-15-Gen-10-Premium-Linux-laptop-with-Ryzen-AI-9-240-Hz-display-and-99-Wh-battery.1071854.0.html
- https://www.notebookcheck.net/XMG-Evo-15-M25-laptop-review-A-good-Windows-alternative-to-the-MacBook-Air-15.1211981.0.html
---
# TUXEDO InfinityBook Pro 15 Gen10

**Excluded: weight (1.77 kg) exceeds the ≤1.6 kg criterion.**

## Overview

Same Tongfang GX5 barebone as XMG EVO 15 (E25) / Schenker Vision 15. Ships with TUXEDO OS (Ubuntu-based) or Ubuntu 24.04. 15.3" sibling of the [InfinityBook Pro 14](./tuxedo-infinitybook-pro-14.md).

## Sustained Performance

Chassis cooling rated for **90W** at full fan speed (confirmed on Intel variant in XMG EVO 15 M25 NotebookCheck review). The AMD variant at 90W sustained has not been independently benchmarked — the 65W PL1 in frontmatter is a conservative estimate matching the reviewed 14" sibling with the same CPU.

The 15" chassis should score higher than the 14" at 90W — estimated CB R23 multi ~24,000-25,000 based on the 14" result of 22,784 at 65W. Frontmatter benchmarks left empty pending independent review.

## Key Specs

- 2x SO-DIMM DDR5-5600 — upgradeable to **128 GB**
- 99 Wh battery — largest in the lineup
- 15.3" 2.5K IPS display, 545 nits peak, 300 Hz (AMD) / 240 Hz (Intel)
- Wi-Fi 6E (AMD RZ616), Bluetooth 5.2
- 1x USB4 (rear) — DP 2.1, PD-in up to 150W
- 1x USB-C 3.2 Gen2 (left) — DP 1.4a, PD up to 100W
- From ~€1,714 (base HX 370 config); fully configured (64 GB Crucial, 2 TB Samsung 990 PRO, custom branding): €2,717 per unit

## Docking and Power Delivery

**PD sensitivity is a known issue.** The InfinityBook Pro series is very sensitive to voltage drops from dock PD — disconnects under CPU load with most 60-100W docks. See [USB4 Docking on Linux](../overviews/usb4-docking-linux.md) for tested docks and recommendations.

The 150W charger exceeds the 100W PD ceiling of most docks. A ThinkPad Thunderbolt 5 Smart Dock (~$550) or similar 140W+ PD dock is required for stable single-cable operation, adding significant cost.

## Why Excluded (and Why Bought Anyway)

Exceeds the 1.6 kg weight criterion (1.77 kg). Chosen as a work laptop due to:
- 99 Wh battery (vs 80 Wh on the 14")
- 90W cooling headroom (vs 65W on the 14")
- 15.3" screen for daily work
- Native Linux support, Russian keyboard layout, B2B ordering with custom branding

## Sources

- [TUXEDO product page](https://www.tuxedocomputers.com/en/TUXEDO-InfinityBook-Pro-15-Gen10-AMD.tuxedo)
- [NotebookCheck announcement](https://www.notebookcheck.net/Tuxedo-InfinityBook-Pro-15-Gen-10-Premium-Linux-laptop-with-Ryzen-AI-9-240-Hz-display-and-99-Wh-battery.1071854.0.html)
- [NotebookCheck XMG EVO 15 M25 review](https://www.notebookcheck.net/XMG-Evo-15-M25-laptop-review-A-good-Windows-alternative-to-the-MacBook-Air-15.1211981.0.html) (same Tongfang GX5 chassis)
