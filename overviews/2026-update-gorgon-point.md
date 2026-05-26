# 2026 AMD Laptop Update: Gorgon Point & New Models

**Date:** 2026-05-26
**Focus:** Thin-and-light (<2kg) AMD laptops with sustained multi-core performance under Linux

---

## AMD Gorgon Point Platform Overview

Gorgon Point (Ryzen AI 400 series) launched Q1 2026 as a mid-cycle refresh of Strix Point / Krackan Point.

### What Changed vs Strix Point

| Spec | Strix Point (Ryzen AI 300) | Gorgon Point (Ryzen AI 400) | Delta |
|------|---------------------------|----------------------------|-------|
| Architecture | Zen 5 + Zen 5c | Zen 5 + Zen 5c (same) | None |
| Max Boost | 5.1 GHz (HX 370) | 5.2 GHz (HX 470) | +2% |
| Memory | LPDDR5X-7500 | LPDDR5X-8533 | +14% BW |
| NPU | 50 TOPS (XDNA 2) | 55 TOPS (XDNA 2) | +10% |
| iGPU | Radeon 890M (16 CU) | Radeon 890M (16 CU) | Same |
| Base TDP | 28W | 28W | Same |
| cTDP max | 54W | 54W | Same |

**Bottom line:** 3-5% CPU performance improvement from clocks alone, ~12% multi-core improvement in best-case scenarios (per Notebookcheck). NOT worth upgrading from Strix Point.

### Key Gorgon Point SKUs

| SKU | Cores | Threads | Boost | NPU TOPS | Replaces |
|-----|-------|---------|-------|----------|----------|
| Ryzen AI 9 HX 475 | 12C (4 Zen5 + 8 Zen5c) | 24T | 5.2 GHz | 60 | HX 370/375 |
| Ryzen AI 9 HX 470 | 12C (4 Zen5 + 8 Zen5c) | 24T | 5.25 GHz | 55 | HX 370/375 |
| Ryzen AI 9 465 | 10C (4 Zen5 + 6 Zen5c) | 20T | 5.0 GHz | 50 | AI 9 365 |
| Ryzen AI 7 450 | 8C (4 Zen5 + 4 Zen5c) | 16T | 5.1 GHz | 50 | AI 7 350 |
| Ryzen AI 7 445 | 6C (2 Zen5 + 4 Zen5c) | 12T | ~4.9 GHz | 50 | Krackan |
| Ryzen AI 5 435 | 6C | 12T | ~4.6 GHz | 45 | Krackan |

### Benchmark Data (Gorgon Point)

#### Ryzen AI 9 HX 470 (12C/24T, 28W default, up to 54W)

| Benchmark | Score | Notes |
|-----------|-------|-------|
| Cinebench 2024 SC | 119-122 (avg 120) | +3% vs HX 370 |
| Cinebench 2024 MC | 1,087-1,247 (avg 1,173) | At 35-45W |
| Cinebench R23 SC | 2,061-2,072 (avg 2,066) | |
| Cinebench R23 MC | 22,589-23,946 (avg 23,380) | +12% vs HX 370 (~20,658) |

#### Ryzen AI 9 465 (10C/20T, tested in ASUS ZenBook S16)

| Benchmark | Score | Notes |
|-----------|-------|-------|
| Cinebench 2024 SC | 115 | |
| Cinebench 2024 MC | 953 | At 45W PL2 / 35W PL1 |
| Cinebench R23 SC | 1,997 | |
| Cinebench R23 MC | 17,580 | |
| Geekbench 6.6 SC | 2,834 | |
| Geekbench 6.6 MC | 14,562 | |

#### Power Scaling (Ryzen AI 9 465)

| Power Limit | CB 2024 MC Score | Notes |
|-------------|------------------|-------|
| 20W | 768 | Efficiency mode |
| 28W (default) | 842 | Standard TDP |
| 35W (PL1) | 930 | Sustained |
| 45W (PL2) | 953 | Short burst |

---

## Model-by-Model Updates

---

### 1. Lenovo ThinkPad T14 Gen 7 AMD (Gorgon Point)

**Status:** Announced MWC 2026 (March), available April 2026
**Price:** From EUR 1,400

| Spec | Value |
|------|-------|
| CPU | AMD Ryzen AI 5/7/9 PRO 400 (Gorgon Point) |
| Weight | 1.28 kg (60Wh) / 1.32 kg (75Wh) WLAN |
| Weight (WWAN) | 1.37 kg (60Wh) / 1.40 kg (75Wh) |
| Battery | 60 Wh or **75 Wh** (up from 57 Wh max) |
| RAM | Up to 64 GB DDR5 SO-DIMM (user-upgradeable!) |
| Display | 14" options incl. OLED |
| Ports | 2x Thunderbolt 4 (USB PD/DP 2.1), 2x USB-A, HDMI 2.1, RJ45 |
| Charging | 65W USB-C |

**Key improvements over Gen 5/6:**
- 75 Wh battery option (31% larger than previous 57 Wh)
- Modular USB-C charging ports
- Tool-less battery removal (two release buttons)
- User-replaceable SSD, 5G card, keyboard
- Easier bottom cover removal

**Sustained power:** Not yet reviewed. Expect 25-35W range based on chassis design (similar to Gen 5/6).

**Linux:** Not yet reviewed. Gorgon Point uses same Zen 5 / RDNA 3.5 as Strix Point, so kernel 6.12+ should work. The PRO SKUs often get better vPro/firmware support.

**Verdict:** Strong candidate. The SO-DIMM RAM upgradability + 75 Wh battery + RJ45 Ethernet make this the most practical business ultrabook. Wait for sustained power reviews.

---

### 1b. Lenovo ThinkPad T14s Gen 7

**Status:** Announced MWC 2026, Intel Panther Lake variant shipping. AMD Gorgon Point variant **later in 2026**.

| Spec | Value |
|------|-------|
| Weight | **1.1 kg** (lightest T-series ever) |
| Battery | 58 Wh |
| Display | 14" up to 1800p OLED (VRR 30-120Hz, 500 nits) |
| RAM | Soldered (not upgradeable) |

**Note:** AMD variant not yet available. Intel variant already shipping. Weight reduction from 1.3 kg (Gen 6) to 1.1 kg is impressive but may compromise sustained thermals.

---

### 1c. Lenovo ThinkPad P14s Gen 7 AMD (Workstation)

**Status:** Available from April 2026
**Price:** From EUR 1,990

| Spec | Value |
|------|-------|
| CPU | Up to Ryzen AI 9 HX PRO 470 |
| Weight | From 1.29 kg |
| Battery | 60 Wh or 75 Wh |
| RAM | Up to **96 GB DDR5-5600** (SO-DIMM) |
| Storage | PCIe 4.0 or 5.0, up to 2 TB |
| Display | 14" 1200p IPS or 2.8K OLED (120Hz, DCI-P3) |
| Ports | USB-A, Thunderbolt 4, HDMI, RJ45, nano-SIM, smart card |

**Key difference from T14:** Higher RAM ceiling (96 GB vs 64 GB), PCIe 5.0 SSD option, ISV-certified workstation. Same chassis dimensions. If you need >64 GB RAM, this is the one.

---

### 2. Framework Laptop 13 Pro (2026)

**Status:** Announced April 21, 2026. Ships June 2026 (Intel). AMD later (July+).

| Spec | Value |
|------|-------|
| CPU (AMD) | Ryzen AI 9 HX 370 (Strix Point, NOT Gorgon Point) |
| CPU (Intel) | Core Ultra 5/X7/X9 Series 3 |
| Weight | 1.4 kg |
| Battery | **74 Wh** (21% up from prior gen) |
| RAM (Intel) | LPCAMM2, up to 64 GB LPDDR5X-7467 (user-replaceable) |
| RAM (AMD) | DDR5-5600 SO-DIMM, up to 64 GB (user-replaceable) |
| Display | 13.5" 2880x1920 (3:2), 700 nits, 1800:1 |
| Thickness | <16 mm |
| Price | From $1,199 (DIY) / $1,499 (pre-built) |

**Major changes:**
- Full CNC aluminum chassis (ground-up redesign)
- Haptic touchpad
- Touch display option
- LPCAMM2 memory on Intel variant (AMD uses SO-DIMM DDR5)
- Wi-Fi 7 (Intel BE211)
- **First Framework laptop Ubuntu Certified by Canonical**
- Ubuntu pre-built configs outselling Windows

**AMD variant note:** Still uses Strix Point (HX 370), NOT Gorgon Point. Framework has not announced a Gorgon Point mainboard. The AMD mainboard is priced at $449 standalone (upgrade path for existing owners).

**Linux status:** Excellent. Ubuntu 25.04 with kernel 6.14 works perfectly per Phoronix. Arch Wiki has a dedicated page. CachyOS, Clear Linux, and Debian 13 all tested and working well.

**Sustained performance (Strix Point HX 370):** ~33W sustained (from earlier Framework 13 testing). Runs hot (up to 100C) but maintains performance. Open-source EC firmware allows fan curve customization.

**Verdict:** Best Linux laptop ecosystem. The redesigned chassis with 74 Wh battery is a significant upgrade. However, the AMD variant still uses Strix Point (not Gorgon Point), and at $1,199+ it commands a premium. LPCAMM2 is a standout feature.

---

### 3. HP EliteBook X G2a (AMD)

**Status:** Announced CES 2026 (January). Available Spring 2026.
**Price:** TBD

The EliteBook 845/865 naming is retired. The new lineup is EliteBook X G2a (AMD) / G2i (Intel) / G2q (Qualcomm).

| Spec | Value |
|------|-------|
| CPU | Up to Ryzen AI 9 HX PRO 470 |
| Weight | **Under 1 kg** (~0.99 kg) |
| Battery | 56 Wh (standard) or 68 Wh |
| RAM | Up to 64 GB DDR5-8533 |
| Storage | Up to 2 TB PCIe Gen4/Gen5 NVMe |
| Display | 14" options: WUXGA OLED, WUXGA LCD, 3K 120Hz VRR OLED |
| Ports | 2x Thunderbolt 4, Bluetooth 5.4, Wi-Fi 7 |
| Camera | 5 MP |
| NPU | Up to 55 TOPS |
| Charging | 65W (upgradeable to 100W) |

**CPU options:** Ryzen AI 9 HX Pro 470, AI 7 Pro 450, AI 5 Pro 440, AI 5 435

**Key points:**
- Sub-1 kg with AMD CPU is remarkable (was ~1.5 kg on EliteBook 845 G11)
- Same physical chassis for AMD/Intel/Qualcomm variants
- CES 2026 Innovation Award
- Previous EliteBook 845 G11 sustained 41W -- unclear if this sub-1kg chassis can match that
- The extreme weight reduction raises thermal concerns for sustained loads

**Linux status:** Unknown for G2a specifically. Previous EliteBook 845 G11 had good AMD Linux support.

**Verdict:** Potentially the lightest AMD business ultrabook at under 1 kg. But sub-1kg + 56 Wh battery + high-power CPU = likely thermal compromise under sustained loads. Wait for sustained power reviews before buying for CPU-intensive work. The 845 G11's 41W sustained was partly due to its thicker chassis.

---

### 4. Lenovo Yoga Product Line (2026)

#### Yoga 7a 2-in-1 (14" / 16", Gorgon Point)

| Spec | Value |
|------|-------|
| CPU | Up to Ryzen AI 7 445 (6C/12T only!) |
| Display | 14" 2880x1800 OLED 120Hz or 16" variant |
| Battery | 70 Wh |
| RAM | Up to 32 GB LPDDR5X-7500 |
| Price | From $849 (14") |

**Warning:** The Ryzen AI 7 445 is a downgrade from the previous gen's 8-core chip. Only 6 cores/12 threads. Reviews note it is "significantly slower than its predecessor in both multi-core and single-core workloads." Not recommended for sustained multi-core work.

#### Yoga Pro 7a (15", Strix Halo)

| Spec | Value |
|------|-------|
| CPU | AMD Ryzen AI Max+ Series (Strix Halo) |
| Display | 15.3" 2.5K OLED |
| RAM | Up to 128 GB unified memory |
| TDP | Up to 95W |
| Price | From EUR 2,499 / $2,099 |
| Availability | June 2026 (EU), August 2026 (US) |

**Note:** Strix Halo, not Gorgon Point. This is a workstation-class machine. Weight not confirmed but likely >1.8 kg given 15.3" + 95W TDP.

**No direct successor to the Yoga Pro 7 14 AMD (Gen 9) with Gorgon Point has been announced.** The 14" Yoga Pro 7 was one of the best sustained performers at 70W. Its absence from the 2026 lineup is a gap.

---

### 5. ASUS ZenBook S16 (UM5606GA, Gorgon Point)

**Status:** Available, reviewed
**Price:** ~$1,300-1,500 (estimated)

| Spec | Value |
|------|-------|
| CPU | AMD Ryzen AI 9 465 (10C/20T) |
| Weight | **1.5 kg** |
| Thickness | 12.9 mm |
| Battery | 83 Wh |
| Display | 16" OLED, 3K 120Hz, 1000 nits |
| Sustained Power | **35W PL1 / 45W PL2** |
| Noise (idle/light) | Under 25 dB(A) |
| Noise (Performance mode) | Significantly louder (not specified) |
| Cooling | Dual fans, 37% enlarged vapor chamber vs prior gen |

**Benchmarks (Ryzen AI 9 465):**

| Test | Score |
|------|-------|
| Cinebench 2024 MC | 953 |
| Cinebench R23 MC | 17,580 |
| Geekbench 6.6 MC | 14,562 |

**Key findings:**
- 35W sustained is good for a 1.5 kg 16" ultrabook
- Outperforms Intel Core Ultra 7 by ~40% in multi-core
- Quiet under 25 dB during light use
- Performance mode gets loud
- 83 Wh battery is excellent
- Previous gen (HX 370) throttled from 50W to 28W -- this gen improves to 35W sustained

**Linux status:** Not specifically tested in available reviews.

**Verdict:** Good general-purpose thin-and-light. 35W sustained is adequate but not exceptional. The 83 Wh battery is a strong point. Note: this has the 10-core AI 9 465, NOT the 12-core HX 470. The HX 470 variant would be more interesting for sustained multi-core.

---

### 5b. ASUS ZenBook 14 OLED (UM3406, Gorgon Point)

| Spec | Value |
|------|-------|
| CPU | Up to Ryzen AI 7 445 |
| Weight | **1.2 kg** |
| Battery | 75 Wh |
| Display | 14" OLED, up to 2K 120Hz |
| Thickness | 14.9 mm |
| RAM | 32 GB LPDDR5X |
| Charging | 68W USB-C |

**Note:** Only available with up to AI 7 445 (6C/12T). Not suitable for heavy multi-core work. Lightweight and good battery, but limited CPU tier.

---

### 5c. ASUS ProArt PX13 (2026, HN7306)

**Status:** Available from February 2026

| Spec | Value |
|------|-------|
| CPU | AMD Ryzen AI Max 385 or Max+ 395 (Strix Halo) |
| Weight | 1.38 kg |
| Battery | 73 Wh |
| Display | 13.3" 2.8K OLED, 60 Hz |
| RAM | Up to 128 GB unified memory |
| Charging | 130W USB-C |

**Note:** This uses Strix Halo (not Gorgon Point). The Max+ 395 with 16 cores could be a multi-core beast, but the 60 Hz display is a disappointment. The 2025 variant with HX 370 + dGPU sustained 65W. The Strix Halo variant trades the dGPU for massive unified memory.

---

### 5d. ASUS ExpertBook P5 G2 (14" AMD)

| Spec | Value |
|------|-------|
| CPU | Up to Ryzen AI 9 HX (Gorgon Point) |
| Weight | **1.27 kg** (14") / 1.57 kg (16") |
| Battery | 70 Wh |
| RAM | Up to 96 GB DDR5 (upgradeable) |
| Storage | Up to 3 TB dual SSD |
| Display | 14" up to 2.5K 144Hz (16:10) |
| Sustained TDP | Up to 45W |
| MIL-STD | 810H |

**Interesting:** 45W sustained TDP claimed by ASUS, in a 1.27 kg chassis. If true, this would be among the best performance-per-kg ratios. DDR5 SO-DIMM upgradeable to 96 GB. This is a direct competitor to the ThinkPad P14s Gen 7.

---

### 6. Other Notable AMD Thin-and-Lights (2026)

#### LG Gram Pro 16 (AMD)

| Spec | Value |
|------|-------|
| CPU | Ryzen AI 7 450 (8C/16T) |
| Weight | **1.18 kg** (16"!) |
| Battery | 77 Wh |
| RAM | 32 GB LPDDR5X |

Absurdly light for 16". But only 8-core AI 7 450, and LG Gram has historically had terrible thermal throttling. Not recommended for sustained loads.

#### LG Gram Pro 14 (AMD)

| Spec | Value |
|------|-------|
| CPU | Up to Ryzen AI 5 435 |
| Weight | **1.12 kg** |
| Battery | 72 Wh |

Even lighter, but only 6-core budget CPU. Not for our use case.

#### Acer Aspire 14 AI

| Spec | Value |
|------|-------|
| CPU | Up to Ryzen AI 7 445 |
| Weight | 1.27 kg |
| Battery | 65 Wh |

Budget option. Limited CPU tier.

#### Dell XPS 13/14 (2026)

Intel-only (Panther Lake). No AMD option. Not relevant.

#### Samsung Galaxy Book6 Series (2026)

Intel-only (Panther Lake). No AMD option. Not relevant.

---

## AMD Fire Range (Zen 5 HX, 2025-2026)

| SKU | Cores | TDP | 3D V-Cache |
|-----|-------|-----|------------|
| Ryzen 9 9955HX3D | 16C/32T | 55W | Yes (96 MB L3) |
| Ryzen 9 9955HX | 16C/32T | 55W | No |
| Ryzen 9 9850HX | 12C/24T | 55W | No |

Fire Range uses desktop Zen 5 chiplets in BGA package. 55W default TDP (down from 75W+ on Dragon Range).

**Ultrabook implementations: None.** Fire Range is strictly for thick gaming laptops with discrete GPUs. No manufacturer has put Fire Range into a thin-and-light. The chiplet design requires more cooling headroom than monolithic APUs.

Community frustration exists -- AMD can do 16 full Zen 5 cores in the AI Max+ 395 (monolithic) at 45-120W, but Fire Range's chiplet approach needs different cooling. No ultrabook Fire Range is expected.

---

## Linux Compatibility Status (2026)

### Gorgon Point / Strix Point GPU (Radeon 890M, RDNA 3.5)

| Component | Kernel Version | Status |
|-----------|---------------|--------|
| Display/GPU (amdgpu) | 6.11+ | Working (DCN, GFX 11.5.0) |
| Wi-Fi | varies by module | Generally working |
| NPU (XDNA 2) | 7.0+ or DKMS | Working, needed for AI workloads |
| Sensors (lm-sensors) | 6.10+ | AMD sensors work well out of box |

**Known issue:** amdgpu bugs in kernel 6.18.x and 6.19.x cause instability after heavy GPU workloads on Radeon 890M (Strix Point / Gorgon Point). Framework community has documented this. Use 6.14 (Ubuntu 25.04) or wait for fixes.

**ROCm:** ROCm 7.2.2 announced at CES 2026 with Ryzen AI 400 support, unified Linux+Windows release.

**Best tested distros (per Phoronix on Framework 13 Strix Point):**
- Ubuntu 25.04 (kernel 6.14, Mesa 25.0) -- no issues
- CachyOS -- best performance
- Clear Linux -- best performance
- Fedora Workstation 42 -- working
- Arch (rolling) -- working, watch for kernel 6.18/6.19 amdgpu bugs

---

## Updated Comparison Table (2026 Models)

| Model | Weight | CPU | Sustained W | Battery | RAM | Price | Linux |
|-------|--------|-----|-------------|---------|-----|-------|-------|
| **ThinkPad T14 Gen 7 AMD** | 1.28 kg | HX Pro 470 | ~25-35W (est) | 75 Wh | 64 GB SO-DIMM | EUR 1,400+ | Expected good |
| **ThinkPad P14s Gen 7 AMD** | 1.29 kg | HX Pro 470 | ~25-35W (est) | 75 Wh | **96 GB SO-DIMM** | EUR 1,990+ | Expected good |
| **ThinkPad T14s Gen 7 AMD** | **1.1 kg** | Gorgon Point | TBD | 58 Wh | Soldered | TBD | Not yet avail |
| **HP EliteBook X G2a** | **<1 kg** | HX Pro 470 | TBD (concern) | 56/68 Wh | 64 GB | TBD | Unknown |
| **Framework 13 Pro (AMD)** | 1.4 kg | HX 370 (Strix) | ~33W | **74 Wh** | 64 GB SO-DIMM | $1,199+ | Excellent |
| **ASUS ZenBook S16** | 1.5 kg | AI 9 465 | **35W** | **83 Wh** | 32 GB | ~$1,300 | Likely good |
| **ASUS ExpertBook P5 G2** | **1.27 kg** | HX 470 | **45W** (claimed) | 70 Wh | **96 GB SO-DIMM** | TBD | Unknown |
| **ASUS ProArt PX13 (2026)** | 1.38 kg | Max+ 395 (Halo) | ~65W+ | 73 Wh | 128 GB | ~$2,000+ | Needs testing |

---

## Preliminary Recommendations (2026)

### For Sustained Multi-Core (Kernel Compilation, PySpark)

**Wait-and-see (need reviews):**
1. **ASUS ExpertBook P5 G2 (14")** -- If 45W sustained claim holds true at 1.27 kg, this is the new champion. 96 GB upgradeable RAM is a bonus.
2. **ThinkPad T14 Gen 7 AMD** -- The 75 Wh battery + SO-DIMM RAM + RJ45 make it the most complete package. Need sustained power data.
3. **HP EliteBook X G2a** -- Sub-1 kg is tempting but may not sustain high power.

**Available now, proven:**
4. **Framework 13 Pro (AMD)** -- Best Linux ecosystem, 74 Wh, SO-DIMM RAM. HX 370 at ~33W sustained. Ubuntu certified.
5. **ASUS ZenBook S16** -- 35W sustained, 83 Wh, quiet. Good all-rounder but only 10-core AI 9 465.

**High performance (heavier):**
6. **ASUS ProArt PX13 (2026, Strix Halo)** -- Max+ 395 with 16 cores is raw power at 1.38 kg. But 60 Hz display is a drawback.

### Decision Matrix Update

| Priority | 2026 Best Choice | Status |
|----------|------------------|--------|
| Balanced (perf + quiet + weight) | ThinkPad T14 Gen 7 AMD | Needs review |
| Lightest AMD | HP EliteBook X G2a (<1 kg) | Needs review |
| Lightest proven Linux | ThinkPad T14s Gen 7 AMD (1.1 kg) | AMD not yet shipping |
| Best Linux ecosystem | Framework 13 Pro AMD | Available July 2026 |
| Maximum sustained (ultrabook) | ASUS ExpertBook P5 G2 (45W claimed) | Needs review |
| Maximum raw cores | ASUS ProArt PX13 Strix Halo (16C) | Available |
| Most upgradeable RAM | ThinkPad P14s Gen 7 AMD (96 GB) | Available |
| Best battery | ASUS ZenBook S16 (83 Wh) | Available |

---

## Sources

### AMD Gorgon Point
- [Notebookcheck: Gorgon Point Performance Analysis](https://www.notebookcheck.net/AMD-Ryzen-AI-400-Performance-Analysis-Gorgon-Point-debuts-with-only-minor-improvements.1211982.0.html)
- [Notebookcheck: HX 470 Benchmarks and Specs](https://www.notebookcheck.net/AMD-Ryzen-AI-9-HX-470-Processor-Benchmarks-and-Specs.1197753.0.html)
- [UltrabookReview: Complete List of Gorgon Point Laptops](https://www.ultrabookreview.com/74602-amd-gorgon-point-laptops/)
- [WCCFTech: Ryzen AI 400 Launch](https://wccftech.com/amd-ryzen-ai-400-gorgon-point-launch-up-to-12-zen-5-cores-60-tops-70-percent-faster-vs-intel-at-same-tdp/)
- [VideoCardz: HX 470 Gorgon Point Spotted](https://videocardz.com/newz/amd-ryzen-ai-hx-470-gorgon-point-mobile-processor-spotted-with-5-25-ghz-turbo-clock)
- [Igor's Lab: Gorgon Point Analysis](https://www.igorslab.de/en/amd-ryzen-ai-400-also-known-as-gorgon-point-lots-of-new-models-but-based-on-current-information-its-more-of-a-refresh-of-strix-and-krakan/)

### ThinkPad T14 / T14s / P14s Gen 7
- [Notebookcheck: ThinkPad T14 Gen 7 + T16 Gen 5](https://www.notebookcheck.net/New-Lenovo-ThinkPad-T14-Gen-7-and-T16-Gen-5-come-with-75-Wh-battery-Intel-Panther-Lake-or-AMD-Gorgon-Point.1239024.0.html)
- [Notebookcheck: ThinkPad T14s Gen 7 Intel](https://www.notebookcheck.net/Lenovo-releases-ThinkPad-T14s-Gen-7-internationally-with-Intel-Panther-Lake-processors.1280901.0.html)
- [Lenovo PSREF: ThinkPad T14 Gen 7 AMD](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_T14_Gen_7_AMD/ThinkPad_T14_Gen_7_AMD_Spec.pdf)
- [Notebookcheck: P14s Gen 7 with 96GB RAM](https://www.notebookcheck.net/Lenovo-launches-new-14-inch-ThinkPad-with-AMD-Gorgon-Point-and-up-to-96-GB-RAM.1251719.0.html)
- [Ubergizmo: ThinkPad T14 Gen 7 Repairability](https://www.ubergizmo.com/2026/03/lenovo-thinkpad-t14-t16-gen-5/)
- [Engadget: ThinkPad MWC 2026](https://www.engadget.com/computing/laptops/lenovos-thinkpads-get-a-spec-bump-at-mwc-2026-230100419.html)

### Framework 13 Pro
- [Framework Official: Laptop 13 Pro](https://frame.work/blog/introducing-framework-laptop-13-pro)
- [Tom's Hardware: Framework 13 Pro Redesign](https://www.tomshardware.com/laptops/frameworks-overhauled-laptop-13-pro-brings-a-redesigned-chassis-intel-core-ultra-series-3-system-aims-to-be-a-macbook-pro-for-linux-users)
- [Phoronix: Framework 13 AMD Strix Point Linux](https://www.phoronix.com/review/framework-13-amd-strix-point)
- [Phoronix: Framework 13 Power & Performance Tuning](https://www.phoronix.com/review/framework-13-ryzen-ai-power)
- [Arch Wiki: Framework 13 AMD Ryzen AI 300](https://wiki.archlinux.org/title/Framework_Laptop_13_(AMD_Ryzen_AI_300_Series))

### HP EliteBook X G2a
- [Notebookcheck: EliteBook X G2 Announcement](https://www.notebookcheck.net/HP-unveils-EliteBook-X-G2q-and-EliteBook-X-G2x-enterprise-laptops-with-new-Qualcomm-and-AMD-CPUs.1196602.0.html)
- [Windows Central: EliteBook X G2 CES](https://www.windowscentral.com/hardware/hp/hp-elitebook-x-14-g2-announcements-ces-2026)
- [gHacks: EliteBook X G2 Light Designs](https://www.ghacks.net/2026/01/07/hps-elitebook-x-g2-laptops-put-serious-ai-power-in-shockingly-light-designs/)
- [HP Official: Next Chapter of Intelligent Work](https://www.hp.com/us-en/newsroom/press-releases/2026/hp-drives-the-next-chapter-of-intelligent-work.html)

### ASUS Models
- [Notebookcheck: ZenBook S16 OLED Review](https://www.notebookcheck.net/The-perfect-everyday-laptop-with-AMD-Ryzen-400-Asus-Zenbook-S16-OLED-review.1221965.0.html)
- [Trusted Reviews: ZenBook S16 2026](https://www.trustedreviews.com/reviews/asus-zenbook-s-16-2026)
- [UltrabookReview: ZenBook S16 and S14 2026](https://www.ultrabookreview.com/74512-asus-zenbook-s16-s14/)
- [ASUS Press: CES 2026 AI PC Lineup](https://press.asus.com/news/press-releases/asus-ces-2026-ai-pc-lineup/)
- [WCCFTech: ASUS 2026 AMD Laptops](https://wccftech.com/asus-2026-amd-laptops-ryzen-ai-400-ryzen-ai-max-zenbook-expertbook-proart-vivobook/)
- [ASUS: ExpertBook P5 G2 14 AMD](https://www.asus.com/laptops/for-work/expertbook/asus-expertbook-p5-g2-14-amd/)

### Lenovo Yoga
- [Notebookcheck: Yoga 7a 2-in-1 Gorgon Point](https://www.notebookcheck.net/Lenovo-Yoga-7a-2-in-1-premium-convertible-laptop-refreshed-with-AMD-Gorgon-Point-APUs.1198632.0.html)
- [Liliputing: Yoga Pro 7a Strix Halo](https://liliputing.com/lenovo-yoga-pro-7a-is-a-amd-strix-halo-laptop-with-a-15-3-inch-oled-display-up-to-128gb-ram-and-pen-support/)

### AMD Fire Range
- [Tom's Hardware: Fire Range HX3D Launch](https://www.tomshardware.com/pc-components/cpus/amd-launches-fire-range-hx3d-mobile-processor-with-game-boosting-3d-v-cache-other-hx-series-skus-built-on-zen-5-desktop-cpu-silicon)
- [VideoCardz: Ryzen 9000HX Fire Range](https://videocardz.com/newz/amd-launches-ryzen-9000hx-fire-range-mobile-cpu-series-up-to-16-zen5-cores-and-140mb-cache)
- [UltrabookReview: Fire Range Laptops List](https://www.ultrabookreview.com/70461-amd-fire-range-laptops/)

### Linux Support
- [Phoronix: AMD Ryzen AI NPUs Linux LLMs](https://www.phoronix.com/news/AMD-Ryzen-AI-NPUs-Linux-LLMs)
- [TechPowerUp: Linux 7.1 NPU Support](https://www.techpowerup.com/347409/linux-7-1-kernel-will-enhance-support-for-amd-ryzen-ai-npus)
- [Framework Community: amdgpu kernel 6.18/6.19 bugs](https://community.frame.work/t/attn-critical-bugs-in-amdgpu-driver-included-with-kernel-6-18-x-6-19-x/79221)
- [VideoCardz: ROCm 7.2.2 at CES 2026](https://videocardz.com/newz/amd-highlights-rocm-7-2-2-at-ces-2026-with-ryzen-ai-400-support-and-a-single-windows-plus-linux-release)
