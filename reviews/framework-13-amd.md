---
model: Framework 13 AMD
slug: framework-13-amd
manufacturer: Framework
status: recommended
form_factor: clamshell
weight_kg: 1.3
battery_wh: 61

display:
  size_in: 13.5
  resolution: 2256x1504
  panel: IPS
  refresh_hz: 60
  aspect_ratio: "3:2"

variants:
  - year: 2024
    cpu:
      name: AMD Ryzen 7 7840U
      cores: 8
      threads: 16
      arch: Phoenix
    gpu:
      name: Radeon 780M
      type: integrated
      compute_units: 12
    ram_gb: 64
    ram_type: DDR5 SO-DIMM
    ram_upgradeable: true
    power:
      pl1_w: 35
      pl2_w: 51

  - year: 2025
    cpu:
      name: AMD Ryzen AI 9 HX 370
      cores: 12
      threads: 24
      arch: Strix Point
    gpu:
      name: Radeon 890M
      type: integrated
      compute_units: 16
    ram_gb: 64
    ram_type: DDR5 SO-DIMM
    ram_upgradeable: true
    power:
      pl1_w: 33
      pl2_w: 46

noise:
  performance_dba: 41

linux:
  status: excellent
  issues:
    - Can hit 100C under load
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

### Sources
- [Phoronix Framework 13 AMD](https://www.phoronix.com/review/framework-13-amd/6)
- [NotebookCheck Framework 13 7840U](https://www.notebookcheck.net/Framework-Laptop-13-5-Ryzen-7-7840U-review-So-much-better-than-the-Intel-version.756613.0.html)
- [Boiling Steam Framework 13](https://boilingsteam.com/framework-13-amd-review-on-linux/)
- [Framework HX 370 Thermals Discussion](https://community.frame.work/t/ai-9-hx-370-thermals/73778)

---

