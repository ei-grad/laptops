---
model: Lenovo ThinkPad P14s AMD
slug: lenovo-thinkpad-p14s-amd
manufacturer: Lenovo
status: available
form_factor: clamshell
weight_kg: 1.29
battery_wh: 75
price_usd: 1579
display:
  aspect_ratio: '16:10'
  size_in: 14
variants:
- benchmarks:
    cinebench_r23_multi: 18520
    cinebench_r23_single: 1939
    geekbench6_multi: 14739
  cpu:
    arch: Strix Point
    boost_ghz: 5.1
    cores: 12
    name: AMD Ryzen AI 9 HX PRO 370
    threads: 24
  gpu:
    compute_units: 16
    name: Radeon 890M
    type: integrated
  power:
    pl1_w: 36
    pl2_w: 51
  ram_gb: 64
  ram_type: LPDDR5X
  sku: Gen 6
  year: 2025
- battery_wh: 75
  cpu:
    arch: Gorgon Point
    cores: 12
    name: AMD Ryzen AI 9 HX PRO 470
    threads: 24
  gpu:
    compute_units: 16
    name: Radeon 890M
    type: integrated
  power:
    pl1_w: 30
    pl2_w: 45
  ram_gb: 96
  ram_type: DDR5-5600 SO-DIMM
  ram_upgradeable: true
  sku: Gen 7
  year: 2026
noise: {}
linux:
  issues:
  - Gen 5 and earlier excluded for noise; Gen 6 improved
  - Gen 7 not yet reviewed on Linux
  status: good
sources:
- https://www.notebookcheck.net/Most-powerful-AMD-14-inch-ThinkPad-with-Ryzen-AI-9-HX-Lenovo-ThinkPad-P14s-Gen-6-AMD-laptop-review.1030845.0.html
- https://www.notebookcheck.net/Lenovo-launches-new-14-inch-ThinkPad-with-AMD-Gorgon-Point-and-up-to-96-GB-RAM.1251719.0.html
---

# Lenovo ThinkPad P14s AMD

## Gen 6 (2025, HX PRO 370)

- **Weight:** 1.44 kg
- **CPU:** Ryzen AI 9 HX PRO 370 (12C/24T)
- **RAM:** Up to 64 GB LPDDR5X (soldered)
- **Sustained Power:** 36W PL1 (Best Performance mode)
- CB R23 multi: 18,520
- R15 loop stable: 2,647-3,082 range
- No throttling on battery
- ISV-certified workstation

### Reassessment

Previous research excluded P14s for "unacceptable noise even silent mode at 24W" (Gen 5). The Gen 6 review contradicts this — NotebookCheck says "performance does not come at the cost of fan noise or extreme case temperatures."

## Gen 7 (2026, HX PRO 470)

- **Weight:** 1.29 kg
- **CPU:** Up to Ryzen AI 9 HX PRO 470
- **Battery:** 60 Wh or 75 Wh
- **RAM:** Up to **96 GB DDR5-5600 SO-DIMM** (upgradeable!)
- **Storage:** PCIe 4.0 or 5.0, up to 2 TB
- **Display:** 14" 1200p IPS or 2.8K OLED (120Hz, DCI-P3)
- **Ports:** USB-A, Thunderbolt 4, HDMI, RJ45, nano-SIM, smart card

### Key Difference from T14

Higher RAM ceiling (96 GB vs 64 GB), PCIe 5.0 SSD option, ISV-certified workstation. If you need >64 GB RAM, this is the one.
