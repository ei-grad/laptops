---
model: Lenovo ThinkPad T14 Gen 5/6 AMD
slug: lenovo-thinkpad-t14-gen-56-amd
manufacturer: Lenovo
status: available
form_factor: clamshell
weight_kg: 1.46
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
  year: 2025
noise:
  balanced_dba: 40
  max_dba: 43.9
linux:
  boot_params:
  - acpi.ec_no_wakeup=1
  issues:
  - Wi-Fi suspend issue resolved in kernel 6.16
  kernel_min: '6.5'
  status: good
sources:
- https://www.notebookcheck.net/Lenovo-ThinkPad-T14-G3-review-Business-laptop-is-worse-with-Intel-and-Nvidia.702431.0.html
- https://www.cruisetech.co.uk/blogs/news/lenovo-thinkpad-t14s-vs-t14
- https://wiki.archlinux.org/title/Lenovo_ThinkPad_P14s_(AMD)_Gen_5
---
# Lenovo ThinkPad T14 Gen 5/6 AMD

### Specifications
- **Display:** 14"
- **Weight:** ~1.46 kg
- **CPU:** Ryzen 7 PRO 8840U (Gen 5) / Ryzen AI 7 PRO 360 (Gen 6)
- **Sustained Power:** 22.5W PL1

### Thermal & Noise Data
- Gen 6 Intel (same chassis): **38.5 dB(A)** max under stress
- Gen 5: **43.9 dB(A)** with identical cooling
- "Performance remains relatively stable in the Cinebench loop"
- During stress test: ~40 dB(A), GPU stable at 30W

### T14 vs T14s Comparison
- T14 achieves ~10% higher performance than T14s (R20 multi-threaded)
- T14 sustains 22.5W vs T14s at ~19W
- T14 takes ~2× longer for TDP to drop
- T14 is ~300g heavier with better cooling

### Linux Compatibility
- ArchWiki: "Same hardware as P14s"
- AMD P-State EPP driver default since kernel 6.5
- Wi-Fi suspend issue resolved in kernel 6.16
- Workaround for sleep: `acpi.ec_no_wakeup=1`