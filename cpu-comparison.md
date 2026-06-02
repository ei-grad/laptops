# AMD Mobile CPU Comparison: Complete Guide

## Quick Reference: CPU Hierarchy (2024-2026)

### Performance Tiers

| Tier | Series | Codename | Architecture | Use Case |
|------|--------|----------|--------------|----------|
| **Ultra-High** | Ryzen 9 9955HX3D / 9955HX | Fire Range | Zen 5 (16C, desktop-class) | Desktop replacement, gaming |
| **Flagship** | Ryzen AI Max+ 395/392/388 | Strix Halo | Zen 5 (8-16C) + 40 CU iGPU | Workstation replacement |
| **Flagship (refresh)** | Ryzen AI Max+ PRO 495 | Gorgon Halo | Zen 5 (16C), 192GB RAM | AI/LLM workstation (Q3 2026) |
| **High-End (new)** | Ryzen AI 9 HX 475/470 | Gorgon Point | Zen 5 + Zen 5c (12C) | Premium performance |
| **High-End** | Ryzen AI 9 HX 370/375 | Strix Point | Zen 5 + Zen 5c (12C) | Premium performance |
| **Mid-High (new)** | Ryzen AI 9 465 | Gorgon Point | Zen 5 + Zen 5c (10C) | Balanced performance |
| **Mid-High** | Ryzen AI 9 365 | Strix Point | Zen 5 + Zen 5c (10C) | Balanced performance |
| **Mainstream (new)** | Ryzen AI 7 450 | Gorgon Point | Zen 5 + Zen 5c (8C) | Everyday + light workloads |
| **Mainstream** | Ryzen AI 7 350/PRO 360 | Strix/Krackan | Zen 5 + Zen 5c (8C) | Everyday + light workloads |
| **Mature** | Ryzen 7 8840HS/8845HS | Hawk Point | Zen 4 (8C) | Proven, stable |

---

## Cinebench R23 Benchmark Comparison

### AMD Mobile CPUs

| Processor | Codename | Cores | Single | Multi | TDP | Notes |
|-----------|----------|-------|--------|-------|-----|-------|
| **Ryzen 9 9955HX3D** | Fire Range | 16C/32T | 2172 | 39065 | 55-75W | 128MB L3 (3D V-Cache) |
| **Ryzen 9 9955HX** | Fire Range | 16C/32T | 2138 | 37800 | 55-75W | Desktop Zen 5 cores |
| Ryzen AI Max+ 395 | Strix Halo | 16C/32T | 2043 | 34474 | 45-120W | Avg; range 29k-37k |
| **Ryzen 9 9850HX** | Fire Range | 12C/24T | ~2100 | 26711 | 55-75W | 64MB L3 |
| **Ryzen AI 9 HX 470** | Gorgon Point | 12C/24T | 2066 | 23380 | 28-54W | Refresh of HX 370 |
| Ryzen AI 9 HX 370 | Strix Point | 12C/24T | 2010 | 23302 | 15-54W | |
| Ryzen AI 9 HX 375 | Strix Point | 12C/24T | ~2010 | ~23300 | 15-54W | ≈HX 370 |
| **Ryzen AI 9 HX 475** | Gorgon Point | 12C/24T | ~2070 | ~23500 | 28-54W | Early data, ≈HX 470 |
| Ryzen AI 9 365 | Strix Point | 10C/20T | ~1960 | ~20000 | 15-54W | |
| **Ryzen AI 9 465** | Gorgon Point | 10C/20T | 1997 | 17580 | 28-54W | Slightly below AI 9 365 |
| **Ryzen AI 7 450** | Gorgon Point | 8C/16T | 2038 | 18316 | 28-54W | Single-laptop data |
| Ryzen 7 8845HS | Hawk Point | 8C/16T | 1766 | 16161 | 35-54W | Pure Zen 4 |
| Ryzen AI 7 PRO 360 | Strix Point | 8C/16T | 1958 | 13794 | 15-54W | Business |
| Ryzen AI 7 350 | Krackan Point | 8C/16T | 1943 | 14607 | 28W | |
| Ryzen 7 8840HS | Hawk Point | 8C/16T | ~1750 | ~15500 | 20-30W | |

### Intel Competition (for reference)

| Processor | Codename | Cores | CB R23 Single | CB R23 Multi | TDP | Notes |
|-----------|----------|-------|---------------|--------------|-----|-------|
| Core Ultra 9 285H | Arrow Lake H | 16C/16T | 2110 | 20191 | 45-115W | No HT, 6P+8E+2LP |
| Core Ultra X9 388H | Panther Lake | 16C/16T | TBD | ~20000 est. | 15-80W | 18A process, Q2 2026 |
| Core Ultra X7 358H | Panther Lake | 16C/16T | TBD | ~20000 | 15-80W | Early leaks only |

### Cinebench 2024 Benchmark Comparison

| Processor | Codename | Single | Multi | Notes |
|-----------|----------|--------|-------|-------|
| Ryzen 9 9955HX3D | Fire Range | 130 | 2117 | |
| Ryzen 9 9955HX | Fire Range | 129 | 1962 | |
| Ryzen AI Max+ 395 | Strix Halo | 115 | 1791 | Avg; range 1648-1912 |
| Ryzen AI Max+ 392 | Strix Halo | 109 | 1380 | 12C, early data |
| Intel Core Ultra 9 285H | Arrow Lake H | 127 | 1068 | |
| Ryzen AI 9 HX 470 | Gorgon Point | 120 | 1173 | Avg; range 1087-1247 |
| Ryzen AI 9 465 | Gorgon Point | 115 | 873-953 | 28-45W range |
| Ryzen AI 7 450 | Gorgon Point | 118 | 972 | |

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

### Strix Halo Family (Zen 5, High-Power) — Updated May 2026

#### Full Strix Halo Lineup (including CES 2026 additions)

| SKU | Cores | Boost | iGPU | L3 Cache | TDP | Status |
|-----|-------|-------|------|----------|-----|--------|
| Max+ 395 | 16C/32T | 5.1 GHz | Radeon 8060S (40 CU) | 64 MB | 45-120W | Shipping |
| **Max+ 392** | 12C/24T | 5.0 GHz | Radeon 8060S (40 CU) | 64 MB | 45-120W | **New Jan 2026** |
| Max 390 / PRO 390 | 12C/24T | 5.0 GHz | Radeon 8050S (32 CU) | 64 MB | 45-120W | Shipping |
| **Max+ 388** | 8C/16T | 5.0 GHz | Radeon 8060S (40 CU) | 64 MB | 45-120W | **New Jan 2026** |
| Max 385 / PRO 385 | 8C/16T | 5.0 GHz | Radeon 8050S (32 CU) | 64 MB | 45-120W | Shipping |

**Max+ 392 and Max+ 388:** Same 40 CU Radeon 8060S GPU as the flagship Max+ 395, but with fewer CPU cores. Key differentiator: full GPU at lower price points. The 40 CU iGPU delivers ~60 TFLOPS vs 48 TFLOPS from the 32 CU variants.

**Max+ 392 benchmarks (ASUS TUF Gaming A14):**
- Geekbench 6: 2,917 single / 18,071 multi
- Cinebench 2024: 109 single / 1,380 multi
- 3DMark Time Spy CPU: 9,820

#### Max+ 395 vs Max PRO 390 vs Max 390

| Spec | Max+ 395 | Max PRO 390 | Max 390 |
|------|----------|-------------|---------|
| Cores | 16C/32T | 12C/24T | 12C/24T |
| L2/L3 Cache | 16/64 MB | 12/64 MB | 12/64 MB |
| iGPU | Radeon 8060S (40 CU) | Radeon 8050S (32 CU) | Radeon 8050S |
| Memory BW | 256 GB/s | 256 GB/s | 256 GB/s |
| TDP | 45-120W | 45-120W | 45-120W |
| Multi-core diff | baseline | **-24%** | ~same as PRO |

**Verdict:** Max+ 395 for maximum performance. Max 390 variants for better value. New Max+ 392/388 offer full GPU with fewer CPU cores.

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

#### Gorgon Halo (Ryzen AI Max+ PRO 495) — Q3 2026

Strix Halo refresh with one major upgrade: **up to 192GB unified memory** (160GB usable as VRAM).

| Spec | Max+ PRO 495 | Max+ 395 | Difference |
|------|--------------|----------|------------|
| Cores | 16C/32T | 16C/32T | Same |
| Boost | 5.2 GHz | 5.1 GHz | +100 MHz |
| iGPU | Radeon 8065S (40 CU) | Radeon 8060S (40 CU) | ~3% faster |
| Max RAM | **192 GB** | 128 GB | **+50%** |
| NPU | 50 TOPS | 50 TOPS | Same |
| Multi-core | ~+4% | baseline | Minimal CPU gain |

AMD claims this is the first x86 client processor capable of running 300B+ parameter LLMs locally. Systems from ASUS, HP, and Lenovo expected Q3 2026.

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
| Yoga Pro 7 14 | AI 9 365 | 70W | Aggressive cooling |

### Hawk Point (8840HS/8845HS) — cTDP 20-54W

| Laptop | CPU | Sustained Power | Notes |
|--------|-----|-----------------|-------|
| HP EliteBook 845 G11 | 8840HS | **41W** | Excellent sustained |
| Framework 13 (older) | 7840U | ~25W | Comparable to 8840U |
| General ultrabooks | 8840U | 15-28W | Efficiency mode |

### Strix Halo (Max+ 395) — cTDP 45-120W

| Laptop | CPU | Sustained Power | Notes |
|--------|-----|-----------------|-------|
| **HP ZBook Ultra G1a 14** | Max+ PRO 395 | **66W** | 14" workstation; CB R23 ~29,200 sustained, Ubuntu-certified |
| **ASUS ProArt PX13 GoPro** | Max+ 395 | **70W** (Performance) | 13.3" convertible; CB R23 30,403 (10-min), 1.39 kg; Manual mode 95W/115W |
| ROG Flow Z13 | Max+ 395 | ~80W | Tablet form factor |
| Full-size gaming | Max+ 395 | 100-120W | Maximum performance |

See [Strix Halo on Linux overview](overviews/strix-halo-linux.md) for the full laptop catalog and Linux support status.

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
| **Maximum raw throughput** | **Ryzen 9 9955HX/9955HX3D** (Fire Range, 37-39k multi) |
| Maximum APU performance | Ryzen AI Max+ 395 (Strix Halo, 34k multi) |
| Thin + high performance | HX 370/470 in well-cooled chassis (23k multi) |
| Predictable, proven | Ryzen 7 8840HS (EliteBook 845 G11, 41W) |
| Light + efficient | AI 7 PRO 360 (ThinkPad T14s G6, 25W) |
| Highest raw power, thin | AI 9 365+ in Yoga Pro 7 (70W) |

---

## Gorgon Point (Ryzen AI 400 Series) — Shipping 2026

Mid-cycle refresh of Strix Point and Krackan Point. Same Zen 5/Zen 5c architecture, same RDNA 3.5 iGPU. Gains are marginal: slightly higher clocks, faster memory support (LPDDR5x-8533), and bumped NPU TOPS.

### Full Gorgon Point Lineup

| SKU | Cores | Boost | iGPU | L3 | TDP | NPU TOPS | Replaces |
|-----|-------|-------|------|----|-----|----------|----------|
| AI 9 HX 475 | 12C/24T (4+8) | 5.2 GHz | Radeon 890M (16 CU) | 24 MB | 28-54W | 60 | HX 375 |
| AI 9 HX 470 | 12C/24T (4+8) | 5.2 GHz | Radeon 890M (16 CU) | 24 MB | 28-54W | 55 | HX 370 |
| AI 9 465 | 10C/20T (4+6) | 5.0 GHz | Radeon 880M (12 CU) | 24 MB | 28-54W | 50 | AI 9 365 |
| AI 7 450 | 8C/16T (4+4) | 5.1 GHz | Radeon 860M (8 CU) | 16 MB | 28-54W | 50 | AI 7 350 |
| AI 7 445 | 6C/12T | TBD | Radeon 840M (4 CU) | TBD | TBD | TBD | AI 5 340 |
| AI 5 435 | 6C/12T | TBD | Radeon 840M (4 CU) | TBD | TBD | TBD | Budget |

### Gorgon Point Performance vs Predecessors

| SKU Pair | CB R23 Single | CB R23 Multi | Difference |
|----------|---------------|--------------|------------|
| HX 470 vs HX 370 | 2066 vs 2010 | 23380 vs 23302 | +3% single, ~0% multi |
| AI 9 465 vs AI 9 365 | 1997 vs ~1960 | 17580 vs ~20000 | +2% single, **-12% multi** |
| AI 7 450 vs AI 7 350 | 2038 vs 1943 | 18316 vs 14607 | +5% single, **+25% multi** |

The AI 7 450's unusually high multi-core score (18316) may reflect a single generous laptop implementation rather than typical performance. The AI 9 465's lower-than-expected multi-core may reflect a 28W test config. Take these early numbers with caution.

### Gorgon Point Laptops (confirmed as of May 2026)

Acer Aspire 14/16 AI, Acer Swift Go 16 AI, Acer Nitro V 16 AI, ASUS ROG Zephyrus G14, ASUS TUF Gaming A14, ASUS ExpertBook B3/P5 G2, ASUS Vivobook S14/S16, ASUS Zenbook 14/S16, HP EliteBook X G2a 14, HP OmniBook X Flip, Lenovo Legion 5a/7a, Lenovo ThinkPad T14/T16, Lenovo IdeaPad 5a Slim, Lenovo Yoga 7a/Yoga Slim 7a, LG Gram 16, LG Gram Pro 14.

**Bottom line:** Gorgon Point is a rebrand with clock bumps. If you already have Strix Point or Krackan Point, there is no reason to upgrade. For new purchases, these will simply replace the 300-series at the same price points.

---

## Fire Range (Ryzen 9 9000HX) — Desktop-Class Mobile

Fire Range brings full Zen 5 desktop cores (not Zen 5c) to thick gaming/workstation laptops. These pair with discrete GPUs (no integrated gaming-class GPU).

### Fire Range Lineup

| SKU | Cores | Boost | L3 Cache | TDP | iGPU | Key Feature |
|-----|-------|-------|----------|-----|------|-------------|
| Ryzen 9 9955HX3D | 16C/32T | 5.4 GHz | **128 MB** | 55-75W | Radeon 610M | 3D V-Cache |
| Ryzen 9 9955HX | 16C/32T | 5.4 GHz | 64 MB | 55-75W | Radeon 610M | |
| Ryzen 9 9850HX | 12C/24T | 5.2 GHz | 64 MB | 55-75W | Radeon 610M | |

All cores are full Zen 5 (no Zen 5c). This means higher per-core performance than Strix Point/Gorgon Point at equivalent clocks, but substantially higher power draw.

### Fire Range Performance

| SKU | CB R23 Single | CB R23 Multi | CB 2024 Single | CB 2024 Multi | GB6 SC | GB6 MC |
|-----|---------------|--------------|----------------|---------------|--------|--------|
| 9955HX3D | 2172 | 39065 | 130 | 2117 | — | — |
| 9955HX | 2138 | 37800 | 129 | 1962 | — | — |
| 9850HX | ~2100 | 26711 | — | — | 3147 | 18113 |

### Fire Range vs Strix Halo vs Strix Point

| Metric | 9955HX3D | Max+ 395 | HX 370 |
|--------|----------|----------|--------|
| CB R23 Multi | 39065 | 34474 | 23302 |
| CB R23 Single | 2172 | 2043 | 2010 |
| All-core arch | Pure Zen 5 | Pure Zen 5 | Zen 5 + Zen 5c |
| L3 Cache | 128 MB | 64 MB | 24 MB |
| iGPU | Minimal | 40 CU (60 TFLOPS) | 16 CU |
| TDP range | 55-75W | 45-120W | 15-54W |
| Use case | Gaming + dGPU | Workstation / no dGPU | Thin performance |

Fire Range wins raw CPU throughput. Strix Halo wins on integrated GPU and memory bandwidth. Strix Point/Gorgon Point wins on power efficiency.

**For sustained CPU workloads (compilation, data processing):** Fire Range in a well-cooled chassis is the fastest option by a significant margin. The 9955HX3D's 3D V-Cache helps with gaming but not compilation workloads (where the non-3D 9955HX performs similarly).

---

## Competition: Intel and Qualcomm (May 2026)

Full analysis: [overviews/intel-qualcomm-linux-2026.md](overviews/intel-qualcomm-linux-2026.md)

### Intel DPTF Status Update (2026)

**No longer a blanket dealbreaker.** Key changes since initial research:
- Lenovo OS-agnostic firmware via LVFS for ThinkPads (2019+)
- Kernel int340x/DPTF drivers improved continuously since 5.12; Panther Lake has the most complete support
- thermald --adaptive works on some platforms (not all)
- Lunar Lake has a separate 400MHz frequency bug (workaround: use "performance" profile)
- **Safe vendors:** Lenovo ThinkPad, Dell XPS Dev Edition, Framework, System76
- **Still risky:** Xiaomi, Huawei, generic OEMs

### Intel Arrow Lake H (Core Ultra 200H) — Shipping

| Spec | Core Ultra 9 285H |
|------|-------------------|
| Architecture | Arrow Lake (Intel 20A + TSMC N3B) |
| Cores | 16 (6P + 8E + 2LP), **no HT** = 16 threads |
| Boost | 5.4 GHz |
| TDP | 45W base, 115W turbo |
| CB R23 Single | 2,110 |
| CB R23 Multi | 20,191 |
| CB 2024 Single | 127 |
| CB 2024 Multi | 1,068 |

Competitive with AMD Strix Point in single-thread, but falls behind in multi-thread due to no hyperthreading. AMD HX 370 (23302 multi) beats it by ~15%.

Sustained power varies wildly by laptop: MSI Prestige 16 sustains 45-55W (CB2024: 991), ASUS Zenbook Duo sustains only 24W (CB2024: 740). Performance shows diminishing returns above 80W.

Phoronix 2025 retesting showed Arrow Lake-S (desktop) gained ~9% performance and 15% less power after a year of kernel/compiler optimizations.

### Intel Lunar Lake (Core Ultra 200V) — Efficiency Only

| Spec | Core Ultra 7 258V |
|------|-------------------|
| Architecture | Lunar Lake |
| Cores | 8 (4P + 4E), **no HT** = 8 threads |
| Boost | 4.8 GHz |
| TDP | 17W base, 37W max turbo |

**Not suitable for sustained multi-core workloads.** Only 8C/8T at max 37W.

AMD Strix Point (HX 370) is up to **1.6x faster** in multi-threaded Linux workloads (Tom's Hardware).

**Linux issues:**
- 400MHz frequency bug on "balanced" ACPI profile (ThinkPad X1C Gen 13, Framework 13). Workaround: switch to "performance" profile.
- Xe2 GPU performance initially far behind Windows. Improved with newer kernels.
- Some Phoronix tests showed 14% faster on Linux vs Windows; others showed severe frequency scaling issues. Inconsistent.

### Intel Panther Lake (Core Ultra 300) — Shipping Q2 2026

Intel's 18A process node (RibbonFET + PowerVia). 200+ system designs confirmed.

| SKU | Cores/Threads | P-Core Boost | TDP | iGPU | Notes |
|-----|---------------|-------------|-----|------|-------|
| Core Ultra X9 388H | 4P+8E+4LPe / 16T | 5.1 GHz | 15-80W | Arc B390 (12 Xe3, 122 GPU TOPS) | Flagship |
| Core Ultra 9 386H | 4P+4LPe / 8T | 4.9 GHz | 12-55W | 4 Xe3 cores | Thin premium |
| Core Ultra X7 358H | 4P+8E+4LPe / 16T | 4.8 GHz | 15-80W | Arc B390 (12 Xe3) | High-perf |
| Core Ultra 7 365 | 4P+4LPe / 8T | 4.8 GHz | 12-55W | 4 Xe3 cores | Mainstream |

**Intel claims:** +24% multi-thread vs Arrow Lake, +50% efficiency vs AMD Ryzen AI 300, +60% multi-thread vs own predecessor (flagship). Up to 27h battery life.

**Phoronix Linux benchmarks (Feb 2026, Ubuntu 26.04, Linux 6.19):**
- X7 358H "exceeded expectations in both performance and power efficiency"
- Faster than Meteor Lake and competitive with Arrow Lake-H
- **But still behind AMD HX 370 in Linux kernel compilation**
- OpenBenchmarking geometric mean: **HX 370 was 1.31x faster** than X7 358H across all benchmarks
- Still no hyperthreading (16C/16T)

**Linux support:**
- Kernel 6.14+: DPTF/int340x thermal drivers, RAPL support
- Kernel 6.19+: Good general support, thermald tested on Dell XPS 2026
- Linux 7.1: Idle driver C-states, FRED enabled by default
- Arch-based distros (Omarchy 3.5) report full compatibility

**Key Panther Lake laptops (under 2 kg):**
- Framework 13 Pro: 1.4 kg, X7 358H, LPCAMM2, 74Wh, open firmware
- Dell XPS 14: ~1.4 kg, Developer Edition with Ubuntu
- ThinkPad X1 Carbon: ~1.1 kg (8-core 386H only)

**Verdict:** Intel's most competitive mobile chip in years. Best power efficiency, strong Linux support. But raw sustained multi-core still ~30% behind AMD HX 370/470.

### Qualcomm Snapdragon X Elite — Not Recommended for Linux (May 2026)

**Status: Avoid for Linux workloads.**

- **TUXEDO canceled** their Snapdragon X Elite Linux laptop after 18+ months of development
- Performance regressions on Linux: Phoronix end-of-2025 testing shows performance comparable to **5-year-old Intel Tiger Lake** chips
- Frequent thermal shutdowns under sustained load
- Missing under Linux: KVM virtualization, USB4 full speeds, hardware video decode, reliable battery life, NPU
- Qualcomm refused to open-source DSP headers, dimming future Linux support prospects
- Kernel support: Linux 6.15+ has basic boot support; Ubuntu 25.04+ installable
- Working: WiFi, Bluetooth, suspend/resume, basic GPU, USB-C DP
- Not working: KVM, NPU, fingerprint, hardware video decode, USB4 full speed

**Windows benchmarks (for reference only):**

| Metric | X Elite (X1E-84-100) | X Elite (X1E-78-100) |
|--------|---------------------|---------------------|
| CB 2024 Single | 130 | 108 |
| CB 2024 Multi | 1,034 | 974 |
| CB R23 Multi | ~15,000 | ~14,000 |
| Geekbench 6 SC | ~2,400 | ~2,400 |

On Linux, actual performance is **far below** these Windows numbers due to driver/scheduler issues.

### Qualcomm Snapdragon X2 Elite — Future Potential (H1 2026)

Hardware is a major upgrade. Linux not yet viable.

| Spec | X Elite (X1E-84-100) | X2 Elite Extreme (X2E-96-100) |
|------|---------------------|-------------------------------|
| Cores | 12 (8P+4E) | 18 (12 Prime + 6 Performance) |
| Process | 4nm | 3nm |
| Max Boost | 3.8 GHz | 5.0 GHz |
| CB 2024 Multi | 1,034 | **1,761** (Performance mode) |
| CB 2024 Single | 130 | **151** |
| GPU | Adreno X1-85 | Adreno X2-90 |
| NPU | 45 TOPS | 80 TOPS |

NotebookCheck calls it "a serious rival for Apple and a problem for AMD & Intel" — on Windows.

**Linux status:**
- Kernel 6.19: Initial GPU/display support for Adreno X2 being upstreamed
- GNOME Shell and Chrome functional, deqp-gles31 >99.9% pass
- Vulkan driver (Turnip) pending
- No KVM virtualization = Docker crippled (QEMU user-mode only)
- Realistically 12-18 months from viable Linux daily driver

**Software compatibility (ARM64 Linux):**
- Native: GCC, LLVM, Python, Node.js, Rust, Java all work
- x86 emulation: FEX-EMU for games/legacy apps (performance penalty)
- Docker: ARM64 containers work; x86 images via QEMU (slow)
- KVM: Not working = no hardware-accelerated VMs

### Cross-Platform Summary for Sustained Linux Workloads

| CPU | CB R23 Multi | CB 2024 Multi | Linux Quality | Best For |
|-----|-------------|---------------|---------------|----------|
| AMD HX 370 | **23,302** | **1,213** | Excellent | Sustained compilation |
| Intel 285H (Arrow Lake) | 20,191 | 1,068 | Good (vendor-dep) | If AMD unavailable |
| Intel X7 358H (Panther Lake) | ~20,000 | ~1,000 | Good | Best Intel efficiency |
| AMD AI 9 365 | ~20,000 | 996 | Excellent | Value multi-core |
| Snapdragon X2 Elite (Windows) | est. ~25,000 | 1,761 | **Not viable** | Wait 12-18 months |
| Snapdragon X Elite (Windows) | ~15,000 | 1,034 | **Broken** | Avoid |
| Intel 258V (Lunar Lake) | N/A | N/A | OK (8C only) | Battery life only |

**AMD remains the clear winner for sustained multi-core Linux workloads.** Intel Panther Lake is the best Intel choice (efficiency + Linux support) but ~30% behind in throughput. Qualcomm X Elite is not viable; X2 Elite has potential but needs 12-18 months of kernel/driver maturation.

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

### New Sources (May 2026 Update)

#### Gorgon Point
- [NotebookCheck HX 470 Benchmarks](https://www.notebookcheck.net/AMD-Ryzen-AI-9-HX-470-Processor-Benchmarks-and-Specs.1197753.0.html)
- [NotebookCheck HX 475 Specs](https://www.notebookcheck.net/AMD-Ryzen-AI-9-HX-475-Processor-Benchmarks-and-Specs.1197731.0.html)
- [NotebookCheck AI 9 465 Benchmarks](https://www.notebookcheck.net/AMD-Ryzen-AI-9-465-Processor-Benchmarks-and-Specs.1197759.0.html)
- [NotebookCheck AI 7 450 Benchmarks](https://www.notebookcheck.net/AMD-Ryzen-AI-7-450-Processor-Benchmarks-and-Specs.1197762.0.html)
- [UltrabookReview Gorgon Point Laptops](https://www.ultrabookreview.com/74602-amd-gorgon-point-laptops/)
- [UltrabookReview 2026 AMD Hardware Explained](https://www.ultrabookreview.com/70408-amd-hardware-explained/)
- [TechPowerUp HX 470 Announcement](https://www.techpowerup.com/343070/amd-ryzen-ai-9-hx-470-gorgon-point-apu-12c-24t-and-5-25-ghz-boost)

#### Fire Range
- [NotebookCheck 9955HX3D Benchmarks](https://www.notebookcheck.net/AMD-Ryzen-9-9955HX3D-Processor-Benchmarks-and-Specs.941514.0.html)
- [NotebookCheck 9955HX Benchmarks](https://www.notebookcheck.net/AMD-Ryzen-9-9955HX-Processor-Benchmarks-and-Specs.941515.0.html)
- [NotebookCheck 9850HX Benchmarks](https://www.notebookcheck.net/AMD-Ryzen-9-9850HX-Processor-Benchmarks-and-Specs.941946.0.html)
- [Tom's Hardware Fire Range Launch](https://www.tomshardware.com/pc-components/cpus/amd-launches-fire-range-hx3d-mobile-processor-with-game-boosting-3d-v-cache-other-hx-series-skus-built-on-zen-5-desktop-cpu-silicon)
- [UltrabookReview Fire Range Laptops](https://www.ultrabookreview.com/70461-amd-fire-range-laptops/)

#### Strix Halo Updates
- [TechPowerUp Max+ 392/388 Expansion](https://www.techpowerup.com/344786/amd-expands-ryzen-ai-max-strix-halo-processor-lineup)
- [NotebookCheck Max+ 392 Benchmarks](https://www.notebookcheck.net/New-AMD-Strix-Halo-Ryzen-AI-Max-392-stars-in-early-benchmark-after-CES-2026-debut.1204390.0.html)
- [NotebookCheck Max+ 395 Benchmarks](https://www.notebookcheck.net/AMD-Ryzen-AI-Max-395-Processor-Benchmarks-and-Specs.942323.0.html)
- [Tom's Hardware Max+ 392 Benchmarks](https://www.tomshardware.com/pc-components/cpus/amds-upcoming-ryzen-ai-max-392-hot-on-the-heels-of-9800x3d-in-early-benchmarks-new-strix-halo-apu-almost-matches-ryzen-7-beast-in-multi-core-performance)

#### Gorgon Halo
- [TechPowerUp Ryzen AI Max+ PRO 495](https://www.techpowerup.com/348739/amd-ryzen-ai-max-pro-495-gorgon-halo-apu-appears-with-radeon-8065s)
- [Tom's Hardware Gorgon Halo 192GB](https://www.tomshardware.com/pc-components/cpus/amd-ryzen-ai-max-400-gorgon-halo-packs-up-to-192gb-of-unified-memory-refreshed-apu-uses-zen-5-and-rdna-3-5-and-can-clock-up-to-5-2-ghz)
- [NotebookCheck Ryzen AI Max 400 Official](https://www.notebookcheck.net/AMD-Ryzen-AI-Max-400-lineup-now-official-with-up-to-192-GB-RAM.1301777.0.html)
- [TechPowerUp Ryzen AI Max 400 Launch](https://www.techpowerup.com/349218/amd-launches-the-ryzen-ai-max-400-series-processors-strix-halo-gets-a-memory-upgrade)

#### Intel Competition
- [NotebookCheck Core Ultra 9 285H Benchmarks](https://www.notebookcheck.net/Intel-Core-Ultra-9-285H-Processor-Benchmarks-and-Specs.944114.0.html)
- [NotebookCheck Arrow Lake-H CPU Analysis](https://www.notebookcheck.net/Intel-Arrow-Lake-H-CPU-analysis-Core-Ultra-200H-makes-Lunar-Lake-almost-redundant.959328.0.html)
- [Laptop Mag Arrow Lake H Tests](https://www.laptopmag.com/laptops/windows-laptops/intel-arrow-lake-h-crushes-apple-m4-ryzen-ai-9-and-snapdragon-x-elite-in-our-lab-tests)
- [NotebookCheck Arrow Lake H vs Strix Point](https://www.notebookcheck.net/Intel-s-new-sweet-spot-CPU-Arrow-Lake-H-goes-head-to-head-with-AMD-Strix-Point.941968.0.html)
- [Phoronix Arrow Lake Redux 2025 (+9% perf, -15% power)](https://www.phoronix.com/review/core-ultra-9-285k-2025)
- [UltrabookReview Panther Lake Laptops](https://www.ultrabookreview.com/74624-intel-panther-lake-laptops/)
- [Tom's Hardware Panther Lake Unveil](https://www.tomshardware.com/pc-components/cpus/intel-takes-the-wraps-off-panther-lake-first-18a-client-processor-brings-the-best-of-lunar-lake-and-arrow-lake-together-in-one-package)
- [HotHardware Panther Lake CES Performance](https://hothardware.com/news/intel-ces-2026-panther-lake-is-a-go)
- [TechPowerUp Panther Lake CB R23 Leaks](https://www.techpowerup.com/342443/leaked-intel-core-ultra-x7-358h-and-ultra-5-338h-cinebench-r23-scores-reveal-concerning-cpu-performance)
- [Phoronix Panther Lake X7 358H Linux Benchmarks](https://www.phoronix.com/review/intel-core-ultra-x7-358h-linux)
- [OpenBenchmarking X7 358H vs HX 370](https://openbenchmarking.org/vs/Processor/Intel+Core+Ultra+X7+358H,AMD+Ryzen+AI+9+HX+370)
- [Intel CES 2026 Panther Lake Newsroom](https://newsroom.intel.com/client-computing/ces-2026-intel-core-ultra-series-3-debut-first-built-on-intel-18a)

#### Intel Lunar Lake Linux
- [Phoronix Lunar Lake Xe2 Graphics (Disappointing)](https://www.phoronix.com/review/lunar-lake-xe2)
- [Phoronix Lunar Lake Linux vs Windows (400MHz Bug)](https://www.phoronix.com/review/lunarlake-xe2-windows-linux-2025)
- [Arch Linux Lunar Lake Issues Thread](https://bbs.archlinux.org/viewtopic.php?id=300155)
- [Tom's Hardware AMD vs Intel Lunar Lake Linux](https://www.tomshardware.com/pc-components/cpus/amd-ryzen-ai-300-cpu-beats-intel-core-ultra-200v-cpu-in-linux-showdown-strix-point-was-up-to-1-6x-faster-than-lunar-lake)
- [Framework 13 400MHz Bug](https://community.frame.work/t/cpu-not-scaling-and-stuck-at-400mhz/63913)

#### Intel DPTF / Thermal
- [Lenovo Linux Thermal Throttling Fix (Phoronix)](https://www.phoronix.com/news/Lenovo-Linux-Thermal-Throttling)
- [NotebookCheck Lenovo DPTF Acknowledgment](https://www.notebookcheck.net/Lenovo-admits-ThinkPad-CPU-throttling-problem-when-running-Linux-fix-in-development.435549.0.html)
- [mjg59 DPTF Adaptive Policy](https://mjg59.dreamwidth.org/54923.html)
- [erpalma/throttled Workaround](https://github.com/erpalma/throttled)
- [Linux 6.14 Thermal Drivers for Panther Lake](https://www.phoronix.com/news/Linux-6.14-Thermal)
- [Omarchy 3.5 Panther Lake Support](https://linuxiac.com/arch-based-omarchy-3-5-brings-full-intel-panther-lake-support/)
- [Phoronix Panther Lake C-States Linux 7.1](https://www.phoronix.com/news/Intel-Panther-Lake-C-States)

#### Intel Laptop Reviews
- [NotebookCheck ThinkPad T14 Gen 6 Intel](https://www.notebookcheck.net/This-is-how-Intel-beats-AMD-Lenovo-ThinkPad-T14-Gen-6-laptop-review.1144489.0.html)
- [ArchWiki ThinkPad T14/T14s Intel Gen 6](https://wiki.archlinux.org/title/Lenovo_ThinkPad_T14/T14s_(Intel)_Gen_6)
- [Framework 13 Pro Official](https://frame.work/laptop13pro)
- [Framework 13 Pro Linux Review](https://linuxano.com/framework-laptop-13-pro-for-linux-users/)
- [Dell XPS 13 Developer Edition Linux Review](https://linuxsystemcomputers.com/hardware-laptops/linux-laptops/dell-xps-13-developer-edition/)
- [NotebookCheck Dell XPS 16 Panther Lake Review](https://www.notebookcheck.net/Dell-XPS-16-Core-Ultra-X7-358H-review-Out-with-Nvidia-in-with-Intel-Arc-B390.1264689.0.html)

#### Qualcomm Snapdragon X Elite / X2 Elite Linux
- [Phoronix Snapdragon X Elite Linux EOY 2025 (Disappointing)](https://www.phoronix.com/review/snapdragon-x-elite-linux-eoy2025)
- [Tom's Hardware Snapdragon Linux Regressions](https://www.tomshardware.com/laptops/ultrabooks-ultraportables/qualcomm-snapdragon-x-elites-latest-linux-benchmarks-show-significant-regressions-promising-chip-continues-to-be-plagued-by-software-support-issues)
- [VideoCardz Qualcomm DSP Headers Refused](https://videocardz.com/newz/qualcomm-shuts-door-on-snapdragon-x-dsp-headers-open-sourcing-linux-support-hopes-fade)
- [Linaro Linux on Snapdragon X Elite](https://www.linaro.org/blog/linux-on-snapdragon-x-elite/)
- [TUXEDO Cancels X1E Laptop](https://xthe.com/news/snapdragon-x-elite-notebook-dead-in-water-what-this-means-for-arm-on-linux/)
- [Phoronix X2 Elite GPU Upstreaming Linux 6.19](https://www.phoronix.com/news/Qualcomm-X2-Elite-GPU-Linux-619)
- [NotebookCheck X2 Elite Extreme Benchmarks](https://www.notebookcheck.net/Qualcomm-Snapdragon-X2-Elite-Extreme-Analysis-Benchmarks-Efficiency-Serious-rival-for-Apple-and-a-problem-for-AMD-Intel.1266974.0.html)
- [Dell XPS 9345 Linux Patches (Phoronix)](https://www.phoronix.com/news/Dell-XPS-9345-Linux-Patches)
- [Phoronix Snapdragon X Elite Ubuntu Benchmarks](https://www.phoronix.com/review/snapdragon-x-elite-linux-benchmarks/6)
