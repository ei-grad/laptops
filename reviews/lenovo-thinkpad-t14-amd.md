---
model: Lenovo ThinkPad T14 AMD
slug: lenovo-thinkpad-t14-amd
manufacturer: Lenovo
status: available
form_factor: clamshell
weight_kg: 1.28
battery_wh: 75
price_usd: 1500
display:
  aspect_ratio: '16:10'
  size_in: 14
variants:
- cpu:
    arch: Hawk Point
    cores: 8
    name: AMD Ryzen 7 PRO 8840U
    threads: 16
  gpu:
    compute_units: 12
    name: Radeon 780M
    type: integrated
  power:
    pl1_w: 22.5
    pl2_w: 30
  ram_gb: 32
  ram_type: DDR5
  ram_upgradeable: true
  sku: Gen 5
  year: 2024
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
    pl1_w: 22.5
    pl2_w: 30
  ram_gb: 32
  ram_type: DDR5
  ram_upgradeable: true
  sku: Gen 6
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
  battery_wh: 75
  power:
    pl1_w: 30
    pl2_w: 45
  ram_gb: 64
  ram_type: DDR5 SO-DIMM
  ram_upgradeable: true
  sku: Gen 7
  year: 2026
noise:
  balanced_dba: 40
  max_dba: 43.9
linux:
  boot_params:
  - acpi.ec_no_wakeup=1
  issues:
  - Wi-Fi suspend issue resolved in kernel 6.16
  - Gen 7 not yet reviewed on Linux
  kernel_min: '6.5'
  status: good
sources:
- https://www.notebookcheck.net/Lenovo-ThinkPad-T14-G3-review-Business-laptop-is-worse-with-Intel-and-Nvidia.702431.0.html
- https://www.cruisetech.co.uk/blogs/news/lenovo-thinkpad-t14s-vs-t14
- https://wiki.archlinux.org/title/Lenovo_ThinkPad_P14s_(AMD)_Gen_5
- https://www.notebookcheck.net/New-Lenovo-ThinkPad-T14-Gen-7-and-T16-Gen-5-come-with-75-Wh-battery-Intel-Panther-Lake-or-AMD-Gorgon-Point.1239024.0.html
- https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_T14_Gen_7_AMD/ThinkPad_T14_Gen_7_AMD_Spec.pdf
- https://www.ubergizmo.com/2026/03/lenovo-thinkpad-t14-t16-gen-5/
---

# Lenovo ThinkPad T14 AMD

## Gen 5 (2024) / Gen 6 (2025)

- **Weight:** ~1.46 kg
- **CPU:** Ryzen 7 PRO 8840U (Gen 5) / Ryzen AI 7 PRO 360 (Gen 6)
- **Sustained Power:** 22.5W PL1
- Cinebench loop: "Performance remains relatively stable"
- Better cooling than T14s (thicker chassis, ~300g heavier)
- Sustains TDP 2x longer than T14s before dropping
- Gen 5: 43.9 dB(A) max; Gen 6: 38.5 dB(A) max under stress

### Linux (Gen 5/6)

- ArchWiki: "Same hardware as P14s"
- AMD P-State EPP driver default since kernel 6.5
- Wi-Fi suspend issue resolved in kernel 6.16
- Workaround for sleep: `acpi.ec_no_wakeup=1`

## Gen 7 (2026, Gorgon Point)

- **Weight:** 1.28 kg (60 Wh) / 1.32 kg (75 Wh)
- **CPU:** Up to Ryzen AI 9 HX PRO 470 (12C/24T)
- **Battery:** 60 Wh or **75 Wh** (up from 57 Wh — 31% larger)
- **RAM:** Up to 64 GB DDR5 SO-DIMM (user-upgradeable)
- **Ports:** 2x Thunderbolt 4, 2x USB-A, HDMI 2.1, RJ45

### Key Improvements (Gen 7)

- 75 Wh battery option
- Modular USB-C charging ports
- Tool-less battery removal
- User-replaceable SSD, 5G card, keyboard

### Sustained Power (Gen 7)

Not yet reviewed. Expect 25-35W based on chassis design.

### Assessment

Gen 5/6: proven, stable, best balance of performance/noise/weight.
Gen 7: most practical business ultrabook (SO-DIMM + 75 Wh + RJ45). Wait for sustained power reviews.
