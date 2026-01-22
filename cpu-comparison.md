# AMD Mobile CPU Comparison: Complete Guide

## Quick Reference: CPU Hierarchy (2024-2025)

### Performance Tiers

| Tier | Series | Codename | Architecture | Use Case |
|------|--------|----------|--------------|----------|
| **Flagship** | Ryzen AI Max+ 395/398 | Strix Halo | Zen 5 (16C) | Workstation replacement |
| **High-End** | Ryzen AI 9 HX 370/375 | Strix Point | Zen 5 + Zen 5c (12C) | Premium performance |
| **Mid-High** | Ryzen AI 9 365 | Strix Point | Zen 5 + Zen 5c (10C) | Balanced performance |
| **Mainstream** | Ryzen AI 7 350/PRO 360 | Strix/Krackan | Zen 5 + Zen 5c (8C) | Everyday + light workloads |
| **Mature** | Ryzen 7 8840HS/8845HS | Hawk Point | Zen 4 (8C) | Proven, stable |

---

## Cinebench R23 Benchmark Comparison

| Processor | Architecture | Cores | Single | Multi | Notes |
|-----------|--------------|-------|--------|-------|-------|
| Ryzen AI Max+ 395 | Strix Halo | 16C/32T | ~2100 | ~30000 | 45-120W TDP |
| Ryzen AI 9 HX 370 | Strix Point | 12C/24T | 2010 | 23302 | 15-54W cTDP |
| Ryzen AI 9 HX 375 | Strix Point | 12C/24T | ~2010 | ~23300 | ≈HX 370 |
| Ryzen 7 8845HS | Hawk Point | 8C/16T | 1766 | 16161 | Pure Zen 4 |
| Ryzen AI 9 365 | Strix Point | 10C/20T | ~1960 | ~20000 | Mid-range Zen 5 |
| Ryzen AI 7 PRO 360 | Strix Point | 8C/16T | 1958 | 13794 | Business |
| Ryzen AI 7 350 | Krackan Point | 8C/16T | 1943 | 14607 | 28W TDP |
| Ryzen 7 8840HS | Hawk Point | 8C/16T | ~1750 | ~15500 | 20-30W |

---

## Detailed Comparisons

### Strix Point Family (Zen 5 + Zen 5c)

#### HX 370 vs HX 375

| Spec | HX 370 | HX 375 |
|------|--------|--------|
| Cores | 12 (4 Zen 5 + 8 Zen 5c) | 12 (4 Zen 5 + 8 Zen 5c) |
| Max Boost | 5.1 GHz | 5.1 GHz |
| L3 Cache | 24 MB | 24 MB |
| iGPU | Radeon 890M | Radeon 890M |
| **Difference** | **~1%** | Essentially identical |

**Verdict:** No meaningful difference. Choose based on laptop, not CPU SKU.

#### HX 370 vs AI 9 365

| Metric | HX 370 | AI 9 365 | Difference |
|--------|--------|----------|------------|
| Cores | 12C/24T | 10C/20T | +20% |
| L3 Cache | 24 MB | 24 MB | Same |
| iGPU | Radeon 890M | Radeon 880M | +6% GPU |
| Multi-core | baseline | -13 to -16% | |
| Single-core | baseline | ~same | |

**Verdict:** HX 370 is ~16% faster multi-core. AI 9 365 offers better value for most users.

#### HX 370 vs AI 7 PRO 360

| Metric | HX 370 | AI 7 PRO 360 | Difference |
|--------|--------|--------------|------------|
| Cores | 12C/24T | 8C/16T | +50% |
| L3 Cache | 24 MB | 16 MB | +50% |
| iGPU | Radeon 890M | Radeon 880M | +6% GPU |
| Multi-core | baseline | **-40 to -59%** | |
| Single-core | baseline | ~same | |

**Verdict:** HX 370 significantly faster in multi-threaded. PRO 360 better for efficiency/battery.

#### AI 9 365 vs AI 7 350

| Metric | AI 9 365 | AI 7 350 | Difference |
|--------|----------|----------|------------|
| Cores | 10C/20T | 8C/16T | +25% |
| L3 Cache | 24 MB | 16 MB | +50% |
| iGPU | Radeon 880M | Radeon 860M | Better |
| Multi-core | baseline | -17 to -34% | |
| Single-core | baseline | -2% | |

**Verdict:** AI 9 365 is the better choice for multi-threaded workloads. AI 7 350 for budget builds.

---

### Hawk Point Family (Zen 4)

#### 8845HS vs 8840HS vs 8840U

| Spec | 8845HS | 8840HS | 8840U |
|------|--------|--------|-------|
| Base/Boost | 3.8/5.1 GHz | 3.3/5.1 GHz | 3.3/5.1 GHz |
| TDP | 35-54W | 20-30W | 15-28W |
| Target | Performance | Balanced | Ultrabook |
| Multi-core diff | baseline | ~same | **-18%** |
| Power usage | baseline | -10% | **-47%** |

**Key insight:** All are rebadged Ryzen 7 7840 variants with improved NPU.
- **8845HS:** Maximum performance, gaming laptops
- **8840HS:** Balanced (EliteBook 845 G11 sustains 41W!)
- **8840U:** Efficiency-first, thin ultrabooks

---

### Strix Halo Family (Zen 5, High-Power)

#### Max+ 395 vs Max PRO 390 vs Max 390

| Spec | Max+ 395 | Max PRO 390 | Max 390 |
|------|----------|-------------|---------|
| Cores | 16C/32T | 12C/24T | 12C/24T |
| L2/L3 Cache | 16/64 MB | 12/64 MB | 12/64 MB |
| iGPU | Radeon 8060S (40 CU) | Radeon 8050S (32 CU) | Radeon 8050S |
| Memory BW | 256 GB/s | 256 GB/s | 256 GB/s |
| TDP | 45-120W | 45-120W | 45-120W |
| Multi-core diff | baseline | **-24%** | ~same as PRO |

**Verdict:** Max+ 395 for maximum performance. Max 390 variants for better value.

#### Max+ 395 vs HX 370

| Metric | Max+ 395 | HX 370 | Notes |
|--------|----------|--------|-------|
| Cores | 16C/32T | 12C/24T | +33% |
| L3 Cache | 64 MB | 24 MB | +167% |
| Memory BW | 256 GB/s | 90 GB/s | +184% |
| iGPU | 40 CU | 16 CU | +150% |
| Multi-core | **+40%** | baseline | At same power |
| TDP range | 45-120W | 15-54W | Higher ceiling |

**Power scaling:**
- Below 25W: Nearly identical performance
- 40W+: Max+ 395 pulls ahead significantly
- 70W+: Max+ 395 shows full advantage (~2× in some games)

---

## Sustained Power by Laptop Implementation

### Strix Point (HX 370/365/PRO 360) — cTDP 15-54W

| Laptop | CPU | Sustained Power | Notes |
|--------|-----|-----------------|-------|
| **ASUS ProArt PX13** | HX 370 | **65W** | Best 13" implementation |
| Framework 13 | HX 370 | ~33W | Runs hot (100°C) |
| ASUS Zenbook S16 | HX 370 | ~35W | Well-cooled |
| Larger gaming | HX 370 | Up to 80W | Best case |
| ThinkPad T14s G6 | PRO 360 | 25W | Best Performance mode |
| Yoga Pro 7 14 | AI 7 350 | 70W | Aggressive cooling |

### Hawk Point (8840HS/8845HS) — cTDP 20-54W

| Laptop | CPU | Sustained Power | Notes |
|--------|-----|-----------------|-------|
| HP EliteBook 845 G11 | 8840HS | **41W** | Excellent sustained |
| Framework 13 (older) | 7840U | ~25W | Comparable to 8840U |
| General ultrabooks | 8840U | 15-28W | Efficiency mode |

### Strix Halo (Max+ 395) — cTDP 45-120W

| Laptop | CPU | Sustained Power | Notes |
|--------|-----|-----------------|-------|
| ROG Flow Z13 | Max+ 395 | ~80W | Tablet form factor |
| ASUS ProArt P16 | Max+ 395 | ~100W | Workstation |
| Full-size gaming | Max+ 395 | 100-120W | Maximum performance |

---

## Key Insights for Sustained Workloads

### 1. Laptop Thermal Design > CPU SKU

A well-cooled Hawk Point (8840HS at 41W) can match a thermally-limited Strix Point (HX 370 at 28W).

### 2. Zen 5c Cores: Trade-off

Strix Point uses 4 full Zen 5 + 8 efficiency Zen 5c cores.
- **Advantage:** Better multi-threaded at same power
- **Disadvantage:** Zen 5c runs at lower clocks than full Zen 4

Pure Zen 4 (8845HS with 8 full cores) can match Strix Point in some sustained scenarios.

### 3. Power Scaling Behavior

| Power Level | Best Architecture |
|-------------|-------------------|
| <25W | Strix Point (efficiency) |
| 25-45W | Either (depends on cooling) |
| 45W+ | Strix Halo (if available) |

### 4. For Kernel Compilation / PySpark

| Priority | Recommendation |
|----------|----------------|
| Predictable, proven | Ryzen 7 8840HS (EliteBook 845 G11, 41W) |
| Maximum cores/threads | HX 370 in well-cooled chassis |
| Light + efficient | AI 7 PRO 360 (ThinkPad T14s G6, 25W) |
| Highest raw power | AI 9 365+ in Yoga Pro 7 (70W) |

---

## Upcoming: Gorgon Point (2025-2026)

| SKU | Cores | Replaces |
|-----|-------|----------|
| Ryzen AI 9 HX 475 | 12C/24T | HX 370/375 |
| Ryzen AI 9 HX 470 | 12C/24T | HX 370/375 |
| Ryzen AI 9 465 | 10C/20T | AI 9 365 |

Same architecture (Zen 5 + Zen 5c), likely minor clock improvements.

---

## Sources

### Benchmark Data
- [NanoReview Cinebench Scores](https://nanoreview.net/en/cpu-list/cinebench-scores)
- [PassMark CPU Benchmarks](https://www.cpubenchmark.net/compare/)
- [CPU-Monkey Comparisons](https://www.cpu-monkey.com/)
- [Technical.city Benchmark Showdowns](https://technical.city/)

### Reviews & Analysis
- [Phoronix HX 370 Review](https://www.phoronix.com/review/amd-ryzen-ai-9-hx-370/13)
- [Phoronix Ryzen AI Max 390](https://www.phoronix.com/review/amd-ryzen-ai-max-390/9)
- [NotebookCheck HX 370 Specs](https://www.notebookcheck.net/AMD-Ryzen-AI-9-HX-370-Processor-Benchmarks-and-Specs.836729.0.html)
- [AnandTech Ryzen AI 300 Announcement](https://www.anandtech.com/show/21419/amd-announces-the-ryzen-ai-300-series-for-mobile-zen-5-with-rdna-35-and-xdna2-npu-with-50-tops)
- [UltrabookReview Strix Point Laptops](https://www.ultrabookreview.com/69393-ryzen-ai-9-laptops/)
- [UltrabookReview Strix Halo Laptops](https://www.ultrabookreview.com/70442-amd-strix-halo-laptops/)

### Cinebench Leaks/Reports
- [VideoCardz HX 370 Cinebench](https://videocardz.com/newz/amd-ryzen-ai-9-hx-370-strix-point-apu-breaks-2k-points-cinebench-r23-single-core-test)
- [TechNetBooks Ryzen AI 7 350 Benchmarks](https://www.technetbooks.com/2025/02/ryzen-ai-7-350-krackan-point-benchmarks.html)
