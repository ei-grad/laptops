# Linux Laptop Research: Sustained CPU Performance

**Date:** 2026-01-22
**Use Case:** Kernel compilation, PySpark data processing (sustained multi-core loads)

## Requirements Summary

| Requirement | Target | Maximum |
|-------------|--------|---------|
| Size | ≤14" | 15" |
| Weight | ≤1.7 kg | 2.0 kg |
| RAM | 32 GB | - |
| Sustained clocks | ≥3.0 GHz multi-core | - |
| Noise | Quiet/moderate | <45 dB(A) |
| Throttling | Stable after heat-soak | - |

## Top Recommendations

### 1. Lenovo ThinkPad T14 Gen 5/6 AMD ⭐ BEST OVERALL

**Why:** Best balance of sustained performance, thermals, noise, and Linux support.

| Spec | Value |
|------|-------|
| Weight | ~1.46 kg |
| Sustained Power | 22.5W PL1 |
| Noise (load) | ~40 dB(A) |
| Linux | Excellent (kernel 6.5+) |

- Better cooling than T14s (thicker chassis, ~300g heavier)
- Sustains TDP 2× longer than T14s before dropping
- Cinebench loop: "Performance remains relatively stable"
- Profile: **Balanced** or **Performance**

### 2. HP EliteBook 845 G11 — HIGHEST SUSTAINED POWER

| Spec | Value |
|------|-------|
| Weight | ~1.5 kg |
| Sustained Power | **41W PL1** |
| Noise (load) | Quiet (single fan busy under load) |
| Linux | Good AMD support |

- Impressive 41W sustained (highest in class)
- "Stable under sustained workloads and on battery"
- Gets warm but maintains performance
- Profile: **HP Smart Sense** (auto-switches, 35-41W range)

### 3. Lenovo ThinkPad T14s Gen 6 AMD — LIGHTEST OPTION

| Spec | Value |
|------|-------|
| Weight | **1.3 kg** |
| Sustained Power | 25W PL1 (Best Performance) |
| Noise (load) | "Neither extremely hot nor loud" |
| Linux | Fedora 41 / Ubuntu 24.04+ |

Power profiles:
- Best Battery: 11W / 14W burst
- Balanced: 15W / 26W burst
- **Best Performance: 25W / 32W burst** ← Use this

Trade-off: Thinner = less thermal headroom than T14.

### 4. Framework 13 AMD — BEST LINUX ECOSYSTEM

| Spec | Value |
|------|-------|
| Weight | ~1.3 kg |
| Sustained Power | 35W PL1, 25W avg |
| Noise (load) | ~41 dB(A) |
| Linux | Excellent, open-source EC |

- Open firmware allows fan curve tuning
- LVFS/Fwupd support
- 15% performance drop in extended Cinebench loops
- Can hit 100°C (tunable via firmware)

### 5. ASUS ProArt PX13 (HN7306) — FASTEST 13" CONVERTIBLE

| Spec | Value |
|------|-------|
| Weight | 1.39 kg |
| Sustained Power | **65W PL1** (80W burst) |
| Noise (load) | ~40-53 dB(A) |
| Linux | Works (xanmod/OEM kernel) |

- 12-core HX 370 at 65W sustained — exceptional for 13.3"
- Cinebench R23: 23,020 multi — fastest sub-14" laptop
- "Manages to avoid thermal throttling"
- RTX 4050/4060/4070 dGPU options
- Profile: **Standard** (Whisper mode too slow)
- **2026 variant:** Ryzen AI Max+ 395 (Strix Halo), no dGPU, up to 128GB RAM

Trade-off: Gets loud (~53 dB) at full load. 2-in-1 form factor.
**Linux note:** Stock Ubuntu 24.04 has WiFi/backlight/fan issues. Use xanmod kernel.

### 6. Lenovo Yoga Pro 7 14 AMD — HIGHEST RAW POWER

| Spec | Value |
|------|-------|
| Weight | ~1.55 kg |
| Sustained Power | **70W PL1** |
| Noise (load) | 36 dB (Balanced) / **47 dB** (High Perf) |
| Linux | Good AMD support |

- 70W sustained is impressive for 14"
- Avoid High Performance mode unless noise-tolerant
- 100W adapter insufficient under full load
- Profile: **Balanced/Adaptive** (~45-50W, quieter)

## Comparison Table

| Model | Weight | Sustained W | Noise | Risk |
|-------|--------|-------------|-------|------|
| **ThinkPad T14 AMD** | 1.46 kg | 22.5W | ~40 dB | Low ✓ |
| **ThinkPad T14s G6 AMD** | 1.3 kg | 25W | ~38-40 dB | Low ✓ |
| **HP EliteBook 845 G11** | 1.5 kg | 41W | Quiet | Low ✓ |
| **ASUS ProArt PX13** | 1.39 kg | 65W | 40-53 dB | Medium |
| **Yoga Pro 7 14 AMD** | 1.55 kg | 70W | 36-47 dB | Medium |
| **Framework 13 AMD** | 1.3 kg | 35W | ~41 dB | Medium |
| System76 Darter Pro | 1.6 kg | ~35W | DIY tuning | Medium |
| ROG Flow Z13 | 1.2 kg | 60-85W | 42-50 dB | **High ⚠** |

## Excluded Models

| Model | Reason |
|-------|--------|
| ASUS Zenbook 14 AMD | Throttles from 50W → 28W under sustained load |
| LG Gram 14 | "Worst thermal throttling for P-series" |
| Framework 16 | Too heavy (2+ kg), CPU hits 100°C |
| Xiaomi/Huawei | Intel DPTF broken on Linux (up to 50% perf loss) |
| ThinkPad P14s AMD | "Unacceptable noise" - even silent mode at 24W |
| ROG Flow Z13 | Overheating investigation, inconsistent thermals |

## CPU Comparison: 8840HS vs HX 370

| Spec | Ryzen 7 8840HS | Ryzen AI 9 HX 370 |
|------|----------------|-------------------|
| Architecture | Zen 4 | Zen 5 |
| Cores/Threads | 8C/16T | 12C/24T |
| L3 Cache | 16 MB | 24 MB |
| Multi-core gain | baseline | **+30-40%** |
| cTDP Range | 20-30W | 15-54W |

**Recommendation:** HX 370 is faster, but laptop implementation matters more. A well-cooled 8840HS at 41W (EliteBook) may outperform a throttled HX 370 at 28W.

## Decision Matrix

| Priority | Best Choice |
|----------|-------------|
| Balanced (performance + quiet + weight) | ThinkPad T14 AMD |
| Lightest | ThinkPad T14s G6 AMD (1.3 kg) |
| Maximum sustained power (14") | Yoga Pro 7 14 (70W) |
| Best perf/weight ratio | **ASUS ProArt PX13** (65W @ 1.39kg) |
| Highest multi-core (sub-14") | **ASUS ProArt PX13** (CB R23: 23,020) |
| Proven/stable thermals | HP EliteBook 845 G11 (41W) |
| Linux ecosystem / repairability | Framework 13 AMD |
| Open firmware / DIY | System76 Darter Pro |
