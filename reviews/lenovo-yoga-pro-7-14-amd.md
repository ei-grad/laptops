---
model: Lenovo Yoga Pro 7 14 AMD
slug: lenovo-yoga-pro-7-14-amd
manufacturer: Lenovo
status: available
form_factor: clamshell
weight_kg: 1.55

display:
  size_in: 14
  panel: OLED
  refresh_hz: 120
  aspect_ratio: "16:10"

variants:
  - year: 2025
    cpu:
      name: AMD Ryzen AI 9 365
      cores: 10
      threads: 20
      arch: Strix Point
    gpu:
      name: Radeon 880M
      type: integrated
      compute_units: 12
    ram_gb: 32
    ram_type: LPDDR5X
    power:
      pl1_w: 70
      pl2_w: 85

noise:
  idle_dba: 25
  balanced_dba: 36
  performance_dba: 47

linux:
  status: unknown
---

# Lenovo Yoga Pro 7 14 AMD

### Specifications
- **Display:** 14" OLED (90-120Hz)
- **Weight:** ~1.55 kg
- **CPU:** Ryzen AI 7 350 / Ryzen AI 9 365

### Power Configuration (Gen 10)
- **PL2 (Burst):** 85W
- **PL1 (Sustained):** 70W
- 100W adapter (insufficient under full load!)

### Thermal & Noise Data

| Mode | Noise | Notes |
|------|-------|-------|
| Idle/Light | Silent | Fans off |
| Balanced | ~36 dB(A) | 45-50W sustained |
| High Performance | **47 dB(A)** | 70W sustained |

- "70W for the processor could be kept stable"
- Surface temps ~40°C hotspots (aggressive fans)
- "Performance remained stable under continuous load"

### Caveats
- High Performance mode is LOUD (47 dB)
- 100W PSU drains battery under full load
- Previous gen complaints about noise/heat

### Sources
- [NotebookCheck Yoga Pro 7 G10](https://www.notebookcheck.net/90-Hz-OLED-with-AdobeRGB-Lenovo-Yoga-Pro-7-14-G10-laptop-review.1002232.0.html)
- [UltrabookReview Yoga Pro 7 Gen 9](https://www.ultrabookreview.com/69904-lenovo-yoga-pro7-review/)

---

