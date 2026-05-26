# Linux Laptop Research: Sustained CPU Performance

**Date:** 2026-05-26
**Use Case:** Kernel compilation, PySpark data processing (sustained multi-core loads)

## Requirements Summary

| Requirement | Target |
|-------------|--------|
| Weight | ≤1.6 kg |
| RAM | 32 GB minimum |
| Sustained clocks | ≥2.8 GHz multi-core, no throttling after heat-soak |
| Noise | <45 dB(A) under load |
| Linux | Working out of box or with minor workarounds |

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

### Reviewed, Linux confirmed

| Model | Weight | Sustained W | CB R23 Multi | Noise (balanced) | RAM | Linux |
|-------|--------|-------------|-------------|-----------------|-----|-------|
| **TUXEDO InfinityBook Pro 14** | 1.49 kg | **65W** | **22,784** | 34 dB | 128 GB DDR5 SO-DIMM | **Excellent** |
| **ASUS ProArt PX13** | 1.39 kg | **65W** | 23,020 | 43 dB | 32 GB LPDDR5X | Fair ¹ |
| **ASUS Zenbook S 16 (2026)** | 1.5 kg | 35W | 17,580 | 36 dB | 32 GB LPDDR5x-8533 | Good |
| **ThinkPad P14s Gen 6 AMD** | 1.44 kg | 36W | 18,520 | Quiet | 64 GB LPDDR5X | Good |
| **Framework 13 AMD** | 1.3 kg | ~33W | — | ~41 dB | 64 GB DDR5 SO-DIMM | **Excellent** |
| **HP EliteBook 845 G11** | 1.5 kg | 41W | — | Quiet | 32 GB LPDDR5X | Good |
| **ThinkPad T14 Gen 5/6 AMD** | 1.46 kg | 22.5W | — | ~40 dB | 32 GB DDR5 SO-DIMM | Good |
| **ThinkPad T14s G6 AMD** | 1.3 kg | 25W | — | ~38 dB | 32 GB LPDDR5X-7500 | Good |
| **Yoga Pro 7 14 AMD** | 1.55 kg | **70W** | — | 36 dB | 32 GB LPDDR5X | Unknown |

¹ ProArt PX13 needs xanmod kernel; stock Ubuntu has WiFi/backlight/fan issues.

### Promising (strong specs, Linux not yet verified)

| Model | Weight | Sustained W | CB R23 Multi | RAM | Price |
|-------|--------|-------------|-------------|-----|-------|
| **ASUS VivoBook S 14 OLED** | **1.31 kg** | 54W | 21,058 | 32 GB LPDDR5X | $1,200 |
| **HP OmniBook Ultra 14** | 1.53 kg | 47W | 21,812 | 32 GB LPDDR5X | $1,050 |

### Announced / Awaiting Reviews

| Model | Weight | Sustained W (est.) | RAM | Key Feature | Status |
|-------|--------|-------------------|-----|-------------|--------|
| **Framework 13 Pro AMD** | 1.4 kg | ~33W | 64 GB DDR5 SO-DIMM | Ubuntu certified, open firmware | Announced |
| **Framework 13 Pro Intel** | 1.4 kg | 28W | 64 GB LPCAMM2 | Best Intel efficiency, ~16 hrs battery | Announced |
| **ASUS ExpertBook P5 G2** | 1.27 kg | **45W** (claimed) | 96 GB DDR5 SO-DIMM | Best perf/weight if claim holds | Announced |
| **ThinkPad T14 Gen 7 AMD** | 1.28 kg | 25-35W | 64 GB DDR5 SO-DIMM | 75 Wh battery + RJ45 | Gen 7 not reviewed |
| **HP EliteBook X G2a** | **<1 kg** | TBD | 64 GB DDR5-8533 | Lightest AMD business | Thermal concerns |

### Not Recommended

| Model | Weight | Reason |
|-------|--------|--------|
| ROG Flow Z13 | 1.2 kg | Overheating investigation, inconsistent thermals |
| Dell Pro 14 Plus | 1.58 kg | Throttles HX 370 to 25W — CB R23 only 12,684 |
| System76 Darter Pro | 1.6 kg | Hot, noisy during compiles |

## Intel Options (May 2026 Update)

See [overviews/intel-qualcomm-linux-2026.md](overviews/intel-qualcomm-linux-2026.md) for full analysis.

### 7. Framework 13 Pro Intel (Panther Lake) — BEST INTEL OPTION

| Spec | Value |
|------|-------|
| Weight | 1.4 kg |
| CPU | Core Ultra X7 358H (16C/16T, no HT) |
| Sustained TDP | 15-80W range |
| Battery | 74Wh, 10-15h Linux |
| Linux | Excellent (open EC, LVFS, Ubuntu certified) |

- Intel 18A process, vapor chamber cooling
- LPCAMM2 RAM (upgradeable)
- Under 30min Cinebench R24: 78C, ~48 dB
- No DPTF concerns (open firmware)
- **But ~30% slower than AMD HX 370 in sustained multi-core (Linux kernel compilation)**

### Intel DPTF Status (2026)

**No longer a blanket dealbreaker.** Lenovo OS-agnostic firmware fix via LVFS for ThinkPads (2019+), improved kernel int340x drivers, thermald --adaptive. Safe vendors: Lenovo ThinkPad, Dell XPS Dev Edition, Framework, System76. Still risky: Xiaomi, Huawei, generic OEMs.

### Excluded Intel Models

| Model | Reason |
|-------|--------|
| ThinkPad T14 Gen 6 Intel (Lunar Lake) | Only 8C/8T, 37W max TDP, 400MHz frequency bug on "balanced" profile |
| Arrow Lake-H ultrabooks | Most are >2 kg; thin ones (Zenbook 14) sustain only 24W |
| Any Lunar Lake for compilation | Efficiency platform, not for sustained workloads |

## Qualcomm Status (May 2026)

**Not recommended for Linux.** See [overviews/intel-qualcomm-linux-2026.md](overviews/intel-qualcomm-linux-2026.md).

- Snapdragon X Elite Linux: Tiger Lake-level performance, thermal shutdowns, no KVM, TUXEDO canceled their laptop
- Snapdragon X2 Elite: Impressive hardware (18C, 3nm, CB2024 multi 1,761) but Linux support 12-18 months away
- No working KVM = Docker is crippled (QEMU user-mode only)
- Battery advantage unrealized on Linux (immature power management)

## Excluded Models

| Model | Reason |
|-------|--------|
| ASUS Zenbook 14 AMD | Throttles from 50W to 28W under sustained load |
| LG Gram 14 | "Worst thermal throttling for P-series" |
| Framework 16 | Too heavy (2+ kg), CPU hits 100C |
| Xiaomi/Huawei | Intel DPTF broken on Linux (up to 50% perf loss) |
| ThinkPad P14s AMD (Gen 5 and earlier) | "Unacceptable noise" — Gen 6 reconsidered, see comparison table |
| ROG Flow Z13 | Overheating investigation, inconsistent thermals |
| **All Snapdragon X laptops** | **Linux support immature, Tiger Lake-level perf, no KVM** |
| **Intel Lunar Lake (for compilation)** | **8C/8T max, 37W TDP, 400MHz bug** |

## CPU Comparison: 8840HS vs HX 370

| Spec | Ryzen 7 8840HS | Ryzen AI 9 HX 370 |
|------|----------------|-------------------|
| Architecture | Zen 4 | Zen 5 |
| Cores/Threads | 8C/16T | 12C/24T |
| L3 Cache | 16 MB | 24 MB |
| Multi-core gain | baseline | **+30-40%** |
| cTDP Range | 20-30W | 15-54W |

**Recommendation:** HX 370 is faster, but laptop implementation matters more. A well-cooled 8840HS at 41W (EliteBook) may outperform a throttled HX 370 at 28W.

## Cross-Platform Comparison (Sustained Multi-Core, Linux)

| CPU | CB R23 Multi | CB 2024 Multi | Linux Status | Notes |
|-----|-------------|---------------|-------------|-------|
| AMD Ryzen AI 9 HX 370 | 23,302 | 1,213 | Excellent | Best for compilation |
| Intel Core Ultra 9 285H | 20,191 | 1,068 | Good (vendor-dep) | No HT, ~15% behind AMD |
| Intel Core Ultra X7 358H | ~20,000 | ~1,000 est. | Good (improving) | 18A, best Intel efficiency |
| AMD Ryzen AI 9 365 | ~20,000 | 996 | Excellent | Good value |
| Snapdragon X Elite (Windows) | ~15,000 | 1,034 | **Bad** | Tiger Lake perf on Linux |
| Intel Core Ultra 7 258V | N/A | N/A | OK (8C only) | Efficiency only |

**AMD remains the clear winner for sustained multi-core Linux workloads.** Intel Panther Lake is the best Intel option but still ~30% behind. Qualcomm is not viable.

## Decision Matrix

| Priority | Best Choice |
|----------|-------------|
| **Best overall (perf + Linux + RAM)** | **TUXEDO InfinityBook Pro 14** (65W, 128 GB DDR5 SO-DIMM, native Linux) |
| Best perf/weight ratio | ASUS ProArt PX13 (65W @ 1.39 kg) — Linux needs xanmod kernel |
| Best value (Linux unverified) | HP OmniBook Ultra 14 (47W, CB R23 21,812, $1,050) |
| Lightest | ThinkPad T14s G6 AMD (1.1 kg, 25W) |
| Maximum sustained power (14") | Yoga Pro 7 14 (70W) — but loud (47 dB) |
| Proven business + benchmarks | ThinkPad P14s Gen 6 (36W, CB R23 18,520, Linux good) |
| Proven/stable thermals | HP EliteBook 845 G11 (41W, Linux good) |
| Linux ecosystem / repairability | Framework 13 AMD (open EC, LVFS, excellent Linux) |
| Most RAM (SO-DIMM) | TUXEDO IB Pro 14 (128 GB DDR5 SO-DIMM) |
| Best 16" all-rounder | ASUS Zenbook S 16 2026 (35W, 83 Wh, quiet) |
| Best Intel option (announced) | Framework 13 Pro Intel (Panther Lake, LPCAMM2) — ~30% behind AMD |
| Business + RJ45 + battery (needs review) | ThinkPad T14 Gen 7 AMD (75 Wh, DDR5 SO-DIMM, RJ45) |
