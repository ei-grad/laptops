---
model: Lenovo ThinkPad T14s
slug: lenovo-thinkpad-t14s
manufacturer: Lenovo
status: available
form_factor: clamshell
weight_kg: 1.1
battery_wh: 58
display:
  aspect_ratio: '16:10'
  size_in: 14
variants:
- cpu:
    arch: Strix Point
    cores: 8
    name: AMD Ryzen AI 7 PRO 360
    threads: 16
  gpu:
    compute_units: 8
    name: Radeon 860M
    type: integrated
  power:
    pl1_w: 25
    pl2_w: 32
  ram_gb: 32
  ram_type: LPDDR5X-7500
  sku: Gen 6 AMD
  year: 2025
- cpu:
    arch: Gorgon Point
    cores: 12
    name: AMD Ryzen AI 9 HX PRO 470
    threads: 24
  gpu:
    compute_units: 16
    name: Radeon 890M
    type: integrated
  power:
    pl1_w: 25
    pl2_w: 35
  ram_gb: 32
  ram_type: LPDDR5X
  sku: Gen 7 AMD
  year: 2026
noise:
  performance_dba: 38
linux:
  issues:
  - Gen 7 AMD variant not yet shipping (Intel-only so far)
  - Gen 7 at 1.1 kg may compromise sustained thermals vs Gen 6 (1.3 kg)
  status: good
sources:
- https://www.notebookcheck.net/Lenovo-ThinkPad-T14s-Gen-6-laptop-review-The-AMD-version-returns-with-the-Ryzen-AI-7-Pro-360.923414.0.html
- https://www.phoronix.com/review/amd-ryzen-ai-7-360-thinkpad-t14s-gen6
- https://www.notebookcheck.net/Lenovo-releases-ThinkPad-T14s-Gen-7-internationally-with-Intel-Panther-Lake-processors.1280901.0.html
- https://www.engadget.com/computing/laptops/lenovos-thinkpads-get-a-spec-bump-at-mwc-2026-230100419.html
---

# Lenovo ThinkPad T14s

## Gen 6 AMD (2025)

- **Weight:** 1.3 kg
- **CPU:** Ryzen AI 7 PRO 360 (8C/16T, Strix Point)
- **RAM:** 32 GB LPDDR5X-7500 (soldered)

### Power Profiles (Gen 6)

| Mode | PL1 (Sustained) | PL2 (Burst) |
|------|-----------------|-------------|
| Best Battery | 11W | 14W |
| Balanced | 15W | 26W |
| Best Performance | **25W** | 32W |

- "Delivers stable performance on a high level"
- "Neither extremely hot nor loud"
- Battery: ~30% throttle

### Linux (Gen 6)

- Phoronix: 200+ benchmarks on Ubuntu 25.04
- Fedora 41 / Ubuntu 24.04 LTS (HWE) work out of box

## Gen 7 (2026)

- **Weight:** **1.1 kg** (lightest T-series ever, down from 1.3 kg)
- **Battery:** 58 Wh
- **Display:** up to 1800p OLED (VRR 30-120Hz, 500 nits)
- **RAM:** Soldered (not upgradeable)
- AMD variant not yet available — Intel Panther Lake shipping first

### Assessment

Gen 6: proven lightest option with decent sustained power.
Gen 7: impressive 1.1 kg but may compromise thermals. Wait for AMD variant and sustained power reviews.
