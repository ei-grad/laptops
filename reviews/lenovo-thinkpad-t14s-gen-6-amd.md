---
model: Lenovo ThinkPad T14s Gen 6 AMD
slug: lenovo-thinkpad-t14s-gen-6-amd
manufacturer: Lenovo
status: available
form_factor: clamshell
weight_kg: 1.3

display:
  size_in: 14
  aspect_ratio: "16:10"

variants:
  - year: 2025
    cpu:
      name: AMD Ryzen AI 7 PRO 360
      cores: 8
      threads: 16
      arch: Strix Point
    gpu:
      name: Radeon 860M
      type: integrated
      compute_units: 8
    ram_gb: 32
    ram_type: LPDDR5X-7500
    power:
      pl1_w: 25
      pl2_w: 32

noise:
  performance_dba: 38

linux:
  status: good
---

# Lenovo ThinkPad T14s Gen 6 AMD

### Specifications
- **Display:** 14"
- **Weight:** 1.3 kg
- **CPU:** Ryzen AI 7 PRO 360 (Strix Point, Zen 5)
- **RAM:** 32GB LPDDR5X-7500 (soldered)

### Power Profiles
| Mode | PL1 (Sustained) | PL2 (Burst) |
|------|-----------------|-------------|
| Best Battery | 11W | 14W |
| Balanced | 15W | 26W |
| Best Performance | **25W** | 32W |

### Thermal & Noise Data
- "Delivers stable performance on a high level"
- "Neither extremely hot nor loud"
- "Manages to keep performance up even under sustained load"
- Battery: ~30% throttle

### Linux Compatibility
- Phoronix: 200+ benchmarks on Ubuntu 25.04
- Fedora 41 / Ubuntu 24.04 LTS (HWE) work out of box
- Modern kernel recommended for best support

### Sources
- [NotebookCheck T14s G6 AMD](https://www.notebookcheck.net/Lenovo-ThinkPad-T14s-Gen-6-laptop-review-The-AMD-version-returns-with-the-Ryzen-AI-7-Pro-360.923414.0.html)
- [Phoronix T14s G6 Linux Review](https://www.phoronix.com/review/amd-ryzen-ai-7-360-thinkpad-t14s-gen6)

---

