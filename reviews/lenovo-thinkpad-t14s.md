---
model: Lenovo ThinkPad T14s
slug: lenovo-thinkpad-t14s
manufacturer: Lenovo
status: announced
form_factor: clamshell
weight_kg: 1.09
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
  status: available
  weight_kg: 1.3
  year: 2025
- cpu:
    arch: Gorgon Point
    boost_ghz: 5.1
    cores: 8
    name: AMD Ryzen AI 7 PRO 450
    threads: 16
  gpu:
    compute_units: 8
    name: Radeon 860M
    type: integrated
  power:
    pl1_w: 25
    pl2_w: 35
  ram_gb: 64
  ram_type: LPDDR5X-8533
  sku: Gen 7 AMD
  status: announced
  weight_kg: 1.09
  year: 2026
noise:
  performance_dba: 38
linux:
  issues:
  - Gen 7 AMD variant not yet shipping (Intel-only so far)
  - Gen 7 at 1.09 kg may compromise sustained thermals vs Gen 6 (1.3 kg)
  - Gen 7 top AMD CPU is Ryzen AI 7 PRO 450, not HX PRO 470
  status: good
sources:
- https://www.notebookcheck.net/Lenovo-ThinkPad-T14s-Gen-6-laptop-review-The-AMD-version-returns-with-the-Ryzen-AI-7-Pro-360.923414.0.html
- https://www.phoronix.com/review/amd-ryzen-ai-7-360-thinkpad-t14s-gen6
- https://www.notebookcheck.net/Lenovo-releases-ThinkPad-T14s-Gen-7-internationally-with-Intel-Panther-Lake-processors.1280901.0.html
- https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_T14s_Gen_7_AMD/ThinkPad_T14s_Gen_7_AMD_Spec.pdf
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

- **Weight:** **1.09 kg** (lightest T-series ever, down from 1.3 kg)
- **CPU:** Up to Ryzen AI 7 PRO 450 (8C/16T), not HX-class
- **Battery:** 58 Wh
- **Display:** up to 1800p OLED (VRR 30-120Hz, 500 nits)
- **RAM:** Up to 64 GB LPDDR5X-8533, soldered (not upgradeable)
- AMD variant not yet available — Intel Panther Lake shipping first

### Assessment

Gen 6: proven lightest option with decent sustained power.
Gen 7: impressive 1.09 kg, larger RAM ceiling, and official Linux preload options in PSREF, but it drops to an 8-core top AMD CPU. Wait for AMD variant and sustained power reviews.
