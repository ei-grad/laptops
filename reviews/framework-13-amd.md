---
model: Framework 13 AMD
slug: framework-13-amd
manufacturer: Framework
status: recommended
form_factor: clamshell
weight_kg: 1.3
battery_wh: 61
display:
  aspect_ratio: '3:2'
  panel: IPS
  refresh_hz: 60
  resolution: 2256x1504
  size_in: 13.5
variants:
- cpu:
    arch: Phoenix
    cores: 8
    name: AMD Ryzen 7 7840U
    threads: 16
  gpu:
    compute_units: 12
    name: Radeon 780M
    type: integrated
  power:
    pl1_w: 35
    pl2_w: 51
  ram_gb: 64
  ram_type: DDR5 SO-DIMM
  ram_upgradeable: true
  year: 2024
- cpu:
    arch: Strix Point
    cores: 12
    name: AMD Ryzen AI 9 HX 370
    threads: 24
  gpu:
    compute_units: 16
    name: Radeon 890M
    type: integrated
  power:
    pl1_w: 33
    pl2_w: 46
  ram_gb: 64
  ram_type: DDR5 SO-DIMM
  ram_upgradeable: true
  year: 2025
noise:
  performance_dba: 41
linux:
  issues:
  - Can hit 100C under load
  status: excellent
sources:
- https://www.phoronix.com/review/framework-13-amd/6
- https://www.notebookcheck.net/Framework-Laptop-13-5-Ryzen-7-7840U-review-So-much-better-than-the-Intel-version.756613.0.html
- https://boilingsteam.com/framework-13-amd-review-on-linux/
- https://community.frame.work/t/ai-9-hx-370-thermals/73778
---
# Framework 13 AMD

### Specifications
- **Display:** 13.5"
- **Weight:** ~1.3 kg
- **CPU Options:** Ryzen 7 7840U / Ryzen AI 9 HX 370

### Power Configuration (7840U)
- **PL2 (Burst):** 51W
- **PL1 (Sustained):** 35W
- Average under load: 25W
- Idle: 1.6W

### Thermal & Noise Data
- **~41 dB(A)** during encoding/stress tests
- Quieter at idle vs Intel version
- Can hit 100°C under load
- 15% performance drop in extended CineBench R15 loops
- Framework prioritizes performance over noise

### Ryzen AI 9 HX 370 Variant
- Boosts to 3.2 GHz / 46W, drops to 2.6 GHz / 33W after 1 min
- Some users report 80-85°C just during downloads

### Linux Compatibility
- Ubuntu 24.10: Everything works out of box
- LVFS/Fwupd firmware updates
- Open-source EC (fan curve tuning possible)
- Fedora 41, Bazzite, Bluefin supported