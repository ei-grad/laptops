# Intel & Qualcomm Thin-and-Light Laptops for Sustained Linux Performance (2025-2026)

**Date:** 2026-05-26
**Use Case:** Kernel compilation, PySpark (sustained multi-core loads under Linux)
**Scope:** Under 2 kg, Intel and Qualcomm platforms only

---

## Intel DPTF / DTT Status on Linux (2026)

### Background

Intel's Dynamic Platform and Thermal Framework (DPTF) / Dynamic Tuning Technology (DTT) is a closed-source thermal management system that determines whether a laptop is on a desk or on a lap, adjusting power limits accordingly. Under Linux, without a working DPTF implementation, many Intel laptops assume perpetual "on-lap" mode and throttle the CPU via BDPROCHOT, keeping temps at ~70C and preventing fans from spinning up properly. This caused **up to 50% performance loss** on affected models (Lenovo, Xiaomi, Huawei).

### Current State (2026)

**Partial fix, vendor-dependent. No longer a blanket "avoid Intel" situation.**

1. **Lenovo firmware fix:** Lenovo rolled out OS-agnostic firmware via LVFS for newer ThinkPads (X1 Carbon 2019 generation onwards) that uses smarter thermal sensor monitoring instead of relying on DPTF. Older models (T480, T580, X1C6, P1G1, X1E1) will NOT get this fix.

2. **Kernel int340x/DPTF drivers:** Continuously improved since kernel 5.12. Linux 6.14 added Panther Lake DPTF support including DLVR (Digital Linear Voltage Regulator) and workload-aware power floor hints. Panther Lake processors provide hardware-level workload residency analysis.

3. **thermald --adaptive:** Since kernel 5.12, `thermald` can read DPTF adaptive performance tables. Effectiveness is hit-or-miss: helps on some platforms, marginal on others. Still no full DPTF policy engine on Linux.

4. **Lunar Lake 400MHz bug:** On some laptops (ThinkPad X1 Carbon Gen 13, Framework 13), the Core Ultra 200V gets stuck at 400MHz under the default "balanced" ACPI platform profile. **Workaround:** switch to "performance" profile. This is a separate issue from classic DPTF throttling but equally crippling.

5. **Panther Lake:** Intel's 18A-based chips have the most complete DPTF driver support to date. thermald has been tested on Dell XPS 2026 Panther Lake laptops. The workload classification hints are new and promising.

### Vendor Risk Assessment

| Vendor | DPTF Risk | Notes |
|--------|-----------|-------|
| Lenovo ThinkPad (2019+) | **Low** | OS-agnostic firmware via LVFS |
| Dell XPS Developer Edition | **Low** | Ships with Ubuntu, tuned for Linux |
| Framework | **Low** | Open firmware, community-driven |
| System76 | **Low** | Coreboot, no DPTF dependency |
| HP EliteBook (Intel) | **Medium** | Less Linux-specific firmware work |
| Xiaomi / Huawei | **High** | No DPTF fix, avoid for Linux |
| Generic OEMs | **Medium-High** | Test before buying |

**Bottom line:** DPTF is no longer a universal Intel dealbreaker, but you must pick the right vendor. Lenovo ThinkPads, Dell XPS Developer Edition, and Framework are safe. Generic Intel ultrabooks remain risky.

---

## Intel Arrow Lake-H (Core Ultra 200H)

### Specifications

| Spec | Core Ultra 9 285H | Core Ultra 7 255H |
|------|-------------------|-------------------|
| Architecture | Arrow Lake (Intel 20A + TSMC N3B) |
| Cores/Threads | 16 (6P+8E+2LP) / 16T | 16 (6P+8E+2LP) / 16T |
| Max Boost | 5.4 GHz | 4.8 GHz |
| L3 Cache | 24 MB | 24 MB |
| Base TDP | 45W | 45W |
| Max Turbo Power | 115W | 80W |
| Hyperthreading | **No** | **No** |

**Key limitation:** No hyperthreading. 16 cores = 16 threads (vs AMD HX 370: 12C/24T).

### Sustained Multi-Core Performance

Performance varies dramatically by laptop thermal design:

| Laptop | CPU | Sustained Power | CB 2024 Multi | CB R23 Multi |
|--------|-----|----------------|---------------|--------------|
| MSI Prestige 16 AI Evo | 285H | **45-55W** | 991 | 20,442 |
| ASUS Zenbook Duo | 285H | **24W** | 740 | 16,632 |

At sustained power, the 285H matches AMD Ryzen AI 9 365 (~996 CB2024) but falls behind the HX 370 (1,213 CB2024).

### Key Finding

Arrow Lake-H performs well at lower power limits but shows diminishing returns above 80W. Good efficiency, mediocre sustained multi-core vs AMD.

### Arrow Lake-H vs AMD Strix Point

| Metric | Core Ultra 9 285H | Ryzen AI 9 HX 370 | Difference |
|--------|-------------------|-------------------|------------|
| CB R23 Single | 2,110 | 2,010 | Intel +5% |
| CB R23 Multi | 20,191 | 23,302 | **AMD +15%** |
| CB 2024 Single | 127 | 116 | Intel +9% |
| CB 2024 Multi | 1,068 | 1,213 | **AMD +14%** |
| Threads | 16 | 24 | AMD +50% |
| Sustained TDP | 45-55W typ | 25-65W typ | Varies |

**For kernel compilation:** AMD wins on multi-core by ~15%. Intel's lack of HT hurts in thread-heavy workloads.

### Arrow Lake-H Ultrabooks (Under 2 kg)

- **ASUS Zenbook 14** — ~1.25 kg, but sustains only 24W (bad for compilation)
- **Acer Swift Go 14** — ~1.3 kg, budget option
- **MSI Prestige 16** — ~1.6 kg, better sustained power (45-55W)
- **Lenovo Yoga Pro 7 14** — Intel variant, ~1.5 kg

Most Arrow Lake-H laptops are 15-16" gaming/performance machines exceeding 2 kg.

---

## Intel Lunar Lake (Core Ultra 200V)

### Specifications

| Spec | Core Ultra 9 288V | Core Ultra 7 258V |
|------|-------------------|-------------------|
| Architecture | Lunar Lake |
| Cores/Threads | 8 (4P+4E) / 8T | 8 (4P+4E) / 8T |
| Max Boost | 5.1 GHz | 4.8 GHz |
| L3 Cache | 12 MB | 12 MB |
| Base TDP | 17W | 17W |
| Max Turbo Power | 37W | 37W |
| RAM | On-package LPDDR5X (32GB max) | On-package |

### Assessment for Sustained Workloads

**Not suitable for kernel compilation or heavy multi-core work.**

- Only 8 cores / 8 threads at max 37W
- Designed for efficiency and battery life, not sustained performance
- 22.5W PL1 sustained on ThinkPad T14 Gen 6 Intel

### Linux Issues

1. **400MHz frequency bug:** CPU gets stuck at 400MHz under "balanced" ACPI profile on multiple laptops (ThinkPad X1 Carbon Gen 13, Framework 13). Workaround: set "performance" profile.
2. **Xe2 GPU issues:** Early testing showed GPU performance far behind Windows. Graphics were "a fraction of Windows performance." Improved with newer kernels.
3. **Conflicting reports:** Some Phoronix testing showed Lunar Lake 14% faster on Linux than Windows (averaging across benchmarks), while others showed severe frequency scaling problems.

### Lunar Lake vs AMD for Sustained Workloads

AMD Strix Point (HX 370) is **up to 1.6x faster** than Lunar Lake in multi-threaded Linux workloads (Tom's Hardware). This is expected given the core count difference (12C/24T vs 8C/8T).

**Verdict:** Lunar Lake is an efficiency platform. Use it for battery life, not compilation. Comparable to AMD's PRO 360 tier, not HX 370.

---

## Intel Panther Lake (Core Ultra Series 3) — NEW (2026)

### Specifications

| Spec | Core Ultra X9 388H | Core Ultra X7 358H | Core Ultra 9 386H |
|------|--------------------|--------------------|-------------------|
| Architecture | Panther Lake (Intel 18A) |
| Cores/Threads | 4P+8E+4LPe / 16T | 4P+8E+4LPe / 16T | 4P+4LPe / 8T |
| Max Boost | 5.1 GHz | 4.8 GHz | 4.9 GHz |
| TDP Range | 15-80W | 15-80W | 12-55W |
| iGPU | Arc B390 (12 Xe3) | Arc B390 (12 Xe3) | 4 Xe3 cores |
| Process | Intel 18A (RibbonFET + PowerVia) |

Intel claims: +24% multi-thread vs Arrow Lake, +50% power efficiency vs AMD Ryzen AI 300.

### Linux Performance (Phoronix, Feb 2026)

Tested on MSI Prestige 14 Flip AI+ Evo with Ubuntu 26.04, Linux 6.19:

- **CPU performance exceeded expectations** for both performance and power efficiency
- Faster than Meteor Lake and competitive with Arrow Lake-H
- **But still behind AMD HX 370 in Linux kernel compilation** — AMD Ryzen AI 9 365 and HX 370 were both faster at their defaults
- OpenBenchmarking geometric mean: HX 370 was **1.31x faster** than X7 358H across all benchmarks

### Linux Support Status

- Kernel 6.14+: DPTF/int340x thermal drivers, RAPL support
- Kernel 6.19+: Good general support
- Linux 7.1: Idle driver C-states optimization, FRED enabled by default
- thermald tested on Dell XPS 2026 Panther Lake
- Arch-based distros (Omarchy 3.5) report full compatibility with kernel 6.19.10

### Panther Lake Laptops (Under 2 kg)

| Laptop | Weight | CPU Options | Notes |
|--------|--------|-------------|-------|
| **Framework 13 Pro** | **1.4 kg** | X7 358H, Ultra 5 325 | LPCAMM2, 74Wh, vapor chamber, 10-15h Linux battery |
| Dell XPS 14/16 | ~1.4-1.8 kg | X9 388H, X7 358H | Developer Edition available |
| Lenovo ThinkPad X1 Carbon | ~1.1 kg | 386H, 365 | 8-core only (LPe variant) |
| ASUS Zenbook Duo | TBD | X7 358H | Dual-screen |
| Samsung Galaxy Book6 Pro | ~1.2-1.5 kg | Various | Consumer-grade |

### Verdict

Panther Lake is Intel's most competitive laptop platform in years. Excellent power efficiency on 18A, strong Linux driver support. But for raw sustained multi-core throughput, AMD HX 370/470 still wins by ~30%. The best reason to choose Panther Lake: vendor-specific Linux advantages (Framework, Dell XPS Dev Edition) and the Arc B390 iGPU.

---

## Best Intel Laptops for Sustained Linux Workloads (2026)

### 1. Framework 13 Pro (Panther Lake) — BEST INTEL OPTION

| Spec | Value |
|------|-------|
| Weight | 1.4 kg |
| CPU | Core Ultra X7 358H (16C/16T) |
| Sustained TDP | 15-28W (efficiency) to 80W (burst) |
| Battery | 74Wh, 10-15h mixed Linux use |
| Linux | Excellent (open EC, LVFS, Ubuntu certified) |
| Price | ~$1,300 |

- Vapor chamber + dual fans
- LPCAMM2 RAM (upgradeable!)
- Under sustained 30min Cinebench R24 load: 78C, ~48 dB
- No DPTF concerns (open firmware)

### 2. ThinkPad T14 Gen 6 Intel (Lunar Lake)

| Spec | Value |
|------|-------|
| Weight | ~1.4 kg |
| CPU | Core Ultra 7 258V (8C/8T) |
| Sustained TDP | 22.5W PL1 |
| Linux | ArchWiki: everything works (kernel 6.18+) |

**Caution:** Only 8 cores/8 threads. Not competitive with AMD variant for compilation. Must use "performance" profile to avoid 400MHz bug.

### 3. Dell XPS 13/14 Developer Edition (Panther Lake)

| Spec | Value |
|------|-------|
| Weight | ~1.2-1.4 kg |
| CPU | Core Ultra X7 358H or similar |
| Linux | Ships with Ubuntu, native support |

Note: XPS 16 with X7 358H showed throttling (100C, clock reduction under stress). The 13/14" models may have similar thermal constraints.

### 4. System76 Darter Pro

| Spec | Value |
|------|-------|
| Weight | ~1.6 kg |
| CPU | Intel Core Ultra H-series |
| Linux | Coreboot, open firmware, full control |

No DPTF dependency. Open fan curves. But runs hot at the bottom and gets loud during compilation.

---

## Qualcomm Snapdragon X Elite Linux Status (2026)

### Hardware Support (Linux 6.15+ / 6.18+)

| Component | Status | Notes |
|-----------|--------|-------|
| Boot/Install | Works | Ubuntu 25.04+, Fedora WIP |
| CPU | Works | But performance regressions |
| GPU (Adreno X1) | Partial | Basic accel, behind Intel/AMD iGPU |
| WiFi | Works | Kernel 6.15+ |
| Bluetooth | Works | |
| Suspend/Resume | Works | But power drain reported |
| Audio | Works | |
| Webcam | Partial | Software camera support |
| USB-C DP | Works | |
| Speakers | Varies | Some laptops missing (Dell XPS 9345) |
| Fingerprint | Not working | |
| Battery reporting | Varies | Missing on some models |
| NPU | **Not functional** | |
| KVM/Virtualization | **Not working** | No hardware-accelerated VMs |
| Hardware video decode | **Not working** | Most apps |
| USB4 full speed | **Not working** | |

### Performance Under Linux

**Phoronix end-of-2025 assessment: "Disappointing"**

Testing on Ubuntu 25.10 with Linux 6.18 kernel:

- Performance regressed to the level of **5-year-old Intel Tiger Lake** chips
- Worse than September 2025 testing — went backwards
- Laptop (Acer Swift 14 AI) was frequently shutting off due to power/thermal thresholds
- Far behind AMD Ryzen AI 300 and Intel Core Ultra in all benchmarks

**Snapdragon X Elite benchmark scores (Windows, for reference):**

| Metric | X Elite (X1E-84-100) | AMD HX 370 | Intel 285H |
|--------|---------------------|------------|------------|
| CB 2024 Single | 130 | 116 | 127 |
| CB 2024 Multi | 1,034 | 1,213 | 1,068 |
| CB R23 Multi | ~15,000 | 23,302 | 20,191 |

On Linux, actual performance is **far below** these Windows numbers.

### Snapdragon X2 Elite (2026)

The X2 Elite Extreme (X2E-96-100) is a significant hardware upgrade:

| Spec | X Elite (X1E-84-100) | X2 Elite Extreme (X2E-96-100) |
|------|---------------------|-------------------------------|
| Cores | 12 (8P+4E) | 18 (12 Prime + 6 Performance) |
| Process | 4nm | 3nm |
| Max Boost | 3.8 GHz | 5.0 GHz |
| CB 2024 Multi | 1,034 | **1,761** (Performance mode) |
| CB 2024 Single | 130 | **151** |
| GPU | Adreno X1-85 | Adreno X2-90 |
| NPU | 45 TOPS | 80 TOPS |

**Linux kernel 6.19:** Initial GPU/display support for Adreno X2-85 being upstreamed. GNOME Shell and Chrome functional. deqp-gles31 >99.9% pass rate. Vulkan driver (Turnip) still pending.

**Linux status:** X2 Elite is too new for reliable Linux benchmarks. Qualcomm is upstreaming drivers, but given X1 Elite's trajectory, expect 12-18 months before Linux is usable for daily driving.

### Snapdragon X Laptops and Linux

| Laptop | Chip | Linux Status |
|--------|------|-------------|
| ThinkPad T14s Gen 6 Snapdragon | X Elite | Kernel 6.15+ basic support; battery life amazing on Windows (21h), untested on Linux |
| Dell XPS 13 9345 | X1 | Patches posted; speakers/mic/fingerprint/battery not working |
| Samsung Galaxy Book | X Elite | Not tested for Linux |
| Lenovo Yoga Slim 7x | X Elite | Kernel 6.15+ basic support |
| **TUXEDO X1E laptop** | X Elite | **CANCELED** (Nov 2025) |

### Software Compatibility

| Tool | Status |
|------|--------|
| x86 emulation (FEX-EMU) | Works for games/apps, performance penalty |
| Docker (native ARM64) | No KVM means no hardware-accelerated VMs; containers work via QEMU user-mode |
| GCC/LLVM native ARM64 | Works |
| Python/Node.js native | Works |
| Rust native | Works |
| Java native | Works |
| x86 Docker images | Via QEMU, significant performance penalty |

### Battery Life: Linux vs Windows

No direct Linux vs Windows battery comparisons exist for Snapdragon X laptops. On Windows, the ThinkPad T14s Gen 6 Snapdragon achieves **21 hours** (light use). On Linux, TUXEDO reported battery life was a major shortfall, and the Acer Swift 14 AI was shutting off under load due to power/thermal issues.

**Verdict:** The efficiency advantage is likely real at the hardware level but unrealized on Linux due to immature power management drivers.

---

## Intel vs AMD vs Qualcomm: Direct Comparison for Sustained Linux Workloads

### Multi-Core Performance Ranking (Sustained, Linux)

| Rank | CPU | CB R23 Multi | CB 2024 Multi | Linux Status |
|------|-----|-------------|---------------|-------------|
| 1 | AMD Ryzen AI 9 HX 370 | 23,302 | 1,213 | Excellent |
| 2 | Intel Core Ultra 9 285H | 20,191 | 1,068 | Good (vendor-dependent) |
| 3 | Intel Core Ultra X7 358H | ~20,000 est. | ~1,000 est. | Good (early, improving) |
| 4 | AMD Ryzen AI 9 365 | ~20,000 | 996 | Excellent |
| 5 | Snapdragon X Elite (Windows) | ~15,000 | 1,034 | **Bad (avoid)** |
| 6 | Intel Core Ultra 7 258V | N/A | N/A | OK (8C only, 400MHz bug) |
| 7 | Snapdragon X Elite (Linux) | **~5,000-8,000** | **~400-600** | **Broken** |

### Power Efficiency

| Platform | Efficiency Tier | Battery Life (Linux, typical) |
|----------|----------------|------------------------------|
| Lunar Lake (200V) | Best | 10-15h |
| Panther Lake (Ultra 300) | Very Good | 10-15h (Framework 13 Pro) |
| AMD Strix Point | Good | 8-12h |
| Arrow Lake-H (200H) | Average | 6-10h |
| Snapdragon X Elite | Unknown on Linux | 21h on Windows, untested Linux |

### Recommendation Matrix

| Priority | Best Intel | Best Overall |
|----------|-----------|-------------|
| Maximum sustained multi-core (thin) | Intel N/A — AMD wins | AMD HX 370/470 in well-cooled chassis |
| Best Intel Linux laptop | Framework 13 Pro (Panther Lake) | Framework 13 AMD (Strix Point) |
| Battery life + decent perf | ThinkPad X1 Carbon (Lunar Lake) | ThinkPad T14s Gen 6 AMD |
| Open firmware / DIY | Framework 13 Pro or System76 | Framework 13 AMD |
| Avoid | Snapdragon anything (Linux) | Snapdragon anything (Linux) |

---

## Key Conclusions

### Intel

1. **DPTF is no longer a blanket dealbreaker.** Lenovo's OS-agnostic firmware and improved kernel drivers have largely fixed the issue for major vendors. Pick Lenovo ThinkPad, Dell XPS Dev Edition, or Framework and you're fine.

2. **Arrow Lake-H:** Decent sustained performance but ~15% behind AMD HX 370 in multi-core. No hyperthreading hurts.

3. **Lunar Lake:** Efficiency platform only. 8C/8T at 37W max. Not for compilation. Has a nasty 400MHz frequency bug on Linux.

4. **Panther Lake (NEW):** Intel's most promising laptop chip. Good Linux support (kernel 6.19+, thermald tested). But still ~30% behind AMD HX 370 in sustained multi-core Linux benchmarks. Best for: Framework 13 Pro users who want Intel ecosystem advantages.

5. **Intel's advantage:** Better iGPU (Arc B390 on Panther Lake), better power efficiency per watt, better Thunderbolt/USB4 support. **AMD's advantage:** Raw sustained multi-core throughput, no DPTF complications.

### Qualcomm

1. **Snapdragon X Elite on Linux: Avoid.** Performance at Tiger Lake levels, frequent thermal shutdowns, no KVM, missing features. TUXEDO canceled their X1E laptop.

2. **Snapdragon X2 Elite:** Hardware is impressive (18 cores, 3nm, competitive with AMD). Linux kernel upstreaming in progress (GPU in 6.19). But realistically 12-18 months from being a viable Linux daily driver.

3. **Software compatibility:** No KVM means Docker is crippled (user-mode QEMU only). Native ARM64 toolchains work, but x86 emulation via FEX-EMU has overhead.

4. **Battery life advantage:** Likely real in hardware but completely unrealized on Linux due to immature power management.

5. **Check back in late 2026/2027** for X2 Elite Linux viability.

---

## Sources

### Intel DPTF/Thermal
- [Intel DPTF Kernel Documentation](https://docs.kernel.org/driver-api/thermal/intel_dptf.html)
- [mjg59 — DPTF Adaptive Policy Reverse Engineering](https://mjg59.dreamwidth.org/54923.html)
- [Lenovo Linux Thermal Throttling Fix (Phoronix)](https://www.phoronix.com/news/Lenovo-Linux-Thermal-Throttling)
- [erpalma/throttled Workaround](https://github.com/erpalma/throttled)
- [Linux 6.14 Thermal Drivers for Panther Lake (Phoronix)](https://www.phoronix.com/news/Linux-6.14-Thermal)

### Arrow Lake-H
- [NotebookCheck Arrow Lake-H CPU Analysis](https://www.notebookcheck.net/Intel-Arrow-Lake-H-CPU-analysis-Core-Ultra-200H-makes-Lunar-Lake-almost-redundant.959328.0.html)
- [Phoronix Arrow Lake Linux Redux (2025)](https://www.phoronix.com/review/core-ultra-9-285k-2025)
- [Phoronix AMD Ryzen 9000 vs Arrow Lake Linux Q1 2025](https://www.phoronix.com/review/ryzen9000-core-ultra-linux613)

### Lunar Lake
- [Phoronix Lunar Lake Xe2 Graphics Linux (Disappointing)](https://www.phoronix.com/review/lunar-lake-xe2)
- [Phoronix Lunar Lake Linux vs Windows (400MHz Bug)](https://www.phoronix.com/review/lunarlake-xe2-windows-linux-2025)
- [Arch Linux Lunar Lake Issues Thread](https://bbs.archlinux.org/viewtopic.php?id=300155)
- [Tom's Hardware AMD vs Intel Lunar Lake Linux Showdown](https://www.tomshardware.com/pc-components/cpus/amd-ryzen-ai-300-cpu-beats-intel-core-ultra-200v-cpu-in-linux-showdown-strix-point-was-up-to-1-6x-faster-than-lunar-lake)

### Panther Lake
- [Intel CES 2026 Panther Lake Announcement](https://newsroom.intel.com/client-computing/ces-2026-intel-core-ultra-series-3-debut-first-built-on-intel-18a)
- [Phoronix Core Ultra X7 358H Linux Benchmarks](https://www.phoronix.com/review/intel-core-ultra-x7-358h-linux)
- [OpenBenchmarking X7 358H vs HX 370](https://openbenchmarking.org/vs/Processor/Intel+Core+Ultra+X7+358H,AMD+Ryzen+AI+9+HX+370)
- [Omarchy 3.5 Full Panther Lake Support](https://linuxiac.com/arch-based-omarchy-3-5-brings-full-intel-panther-lake-support/)
- [Phoronix Panther Lake C-States Linux 7.1](https://www.phoronix.com/news/Intel-Panther-Lake-C-States)

### Framework 13 Pro
- [Framework Laptop 13 Pro Official](https://frame.work/laptop13pro)
- [Framework 13 Pro Linux Review (linuxano)](https://linuxano.com/framework-laptop-13-pro-for-linux-users/)
- [Engadget Framework 13 Pro Launch](https://www.engadget.com/computing/laptops/framework-launches-the-laptop-13-pro-with-intels-new-panther-lake-chips-181503934.html)

### Snapdragon X Elite / X2 Elite
- [Phoronix Snapdragon X Elite Linux EOY 2025 (Disappointing)](https://www.phoronix.com/review/snapdragon-x-elite-linux-eoy2025)
- [Tom's Hardware Snapdragon X Elite Linux Regressions](https://www.tomshardware.com/laptops/ultrabooks-ultraportables/qualcomm-snapdragon-x-elites-latest-linux-benchmarks-show-significant-regressions-promising-chip-continues-to-be-plagued-by-software-support-issues)
- [TUXEDO Cancels Snapdragon X Elite Laptop](https://xthe.com/news/snapdragon-x-elite-notebook-dead-in-water-what-this-means-for-arm-on-linux/)
- [Linaro — Linux on Snapdragon X Elite](https://www.linaro.org/blog/linux-on-snapdragon-x-elite/)
- [Qualcomm X2 Elite GPU Upstreaming in Linux 6.19 (Phoronix)](https://www.phoronix.com/news/Qualcomm-X2-Elite-GPU-Linux-619)
- [NotebookCheck Snapdragon X2 Elite Extreme Benchmarks](https://www.notebookcheck.net/Qualcomm-Snapdragon-X2-Elite-Extreme-Analysis-Benchmarks-Efficiency-Serious-rival-for-Apple-and-a-problem-for-AMD-Intel.1266974.0.html)
- [Dell XPS 9345 Linux Patches (Phoronix)](https://www.phoronix.com/news/Dell-XPS-9345-Linux-Patches)
- [Phoronix Snapdragon X Elite Ubuntu Benchmarks](https://www.phoronix.com/review/snapdragon-x-elite-linux-benchmarks/6)

### ThinkPad Intel
- [NotebookCheck ThinkPad T14 Gen 6 Intel Review](https://www.notebookcheck.net/This-is-how-Intel-beats-AMD-Lenovo-ThinkPad-T14-Gen-6-laptop-review.1144489.0.html)
- [ArchWiki ThinkPad T14/T14s Intel Gen 6](https://wiki.archlinux.org/title/Lenovo_ThinkPad_T14/T14s_(Intel)_Gen_6)
