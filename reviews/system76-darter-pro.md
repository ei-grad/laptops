---
model: System76 Darter Pro
slug: system76-darter-pro
manufacturer: System76
status: available
form_factor: clamshell
weight_kg: 1.6

display:
  size_in: 14
  aspect_ratio: "16:10"

variants:
  - year: 2024
    cpu:
      name: Intel Core Ultra H-series
      cores: 14
      threads: 18
      arch: Meteor Lake
    gpu:
      name: Intel Arc
      type: integrated
    ram_gb: 64
    ram_type: DDR5 SO-DIMM
    ram_upgradeable: true
    power:
      pl1_w: 35
      pl2_w: 65

linux:
  status: excellent
  issues:
    - Bottom of chassis can become uncomfortably hot
    - Fan noise during compiles described as irritating
---

# System76 Darter Pro

### Specifications
- **Display:** 14" / 16"
- **Weight:** ~1.6 kg (14") / ~1.9 kg (16")
- **CPU:** Intel Core Ultra H-series
- **Firmware:** Coreboot (open-source)

### Thermal Behavior
- Fan ramps at 65-70°C, max at 90°C
- Safe operating range: 70-100°C
- "Bottom of chassis can become uncomfortably hot"
- One reviewer had RMA due to thermal issues
- "Compiling TypeScript causes fan to ramp to irritating levels"

### Strengths
- Open-source firmware (full fan curve control)
- Intel ME mostly disabled
- 30-40% faster than Lemur Pro in sustained loads
- Excellent Linux integration

### Noise
- No dB measurements in reviews
- Subjective: "Not that bad" / "Irritating during compiles"
- Tunable via open firmware

### Lemur Pro (Not Recommended for Heavy Workloads)
- U-series CPU (efficiency-focused)
- Not suitable for sustained compilation workloads

### Sources
- [Gear Report Darter Pro 10](https://gear-report.com/system76-darter-pro-10-darp10-review/)
- [Boiling Steam Darter Pro](https://boilingsteam.com/the-darter-pro-lightweight-linux-laptop-full-review/)
- [System76 Fan Noise Support](https://support.system76.com/articles/fan-noise/)

---

