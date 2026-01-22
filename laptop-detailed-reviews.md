# Detailed Laptop Reviews and Data

## Lenovo ThinkPad T14 Gen 5/6 AMD

### Specifications
- **Display:** 14"
- **Weight:** ~1.46 kg
- **CPU:** Ryzen 7 PRO 8840U (Gen 5) / Ryzen AI 7 PRO 360 (Gen 6)
- **Sustained Power:** 22.5W PL1

### Thermal & Noise Data
- Gen 6 Intel (same chassis): **38.5 dB(A)** max under stress
- Gen 5: **43.9 dB(A)** with identical cooling
- "Performance remains relatively stable in the Cinebench loop"
- During stress test: ~40 dB(A), GPU stable at 30W

### T14 vs T14s Comparison
- T14 achieves ~10% higher performance than T14s (R20 multi-threaded)
- T14 sustains 22.5W vs T14s at ~19W
- T14 takes ~2× longer for TDP to drop
- T14 is ~300g heavier with better cooling

### Linux Compatibility
- ArchWiki: "Same hardware as P14s"
- AMD P-State EPP driver default since kernel 6.5
- Wi-Fi suspend issue resolved in kernel 6.16
- Workaround for sleep: `acpi.ec_no_wakeup=1`

### Sources
- [NotebookCheck T14 G3 Review](https://www.notebookcheck.net/Lenovo-ThinkPad-T14-G3-review-Business-laptop-is-worse-with-Intel-and-Nvidia.702431.0.html)
- [CruiseTech T14 vs T14s](https://www.cruisetech.co.uk/blogs/news/lenovo-thinkpad-t14s-vs-t14)
- [Arch Wiki P14s Gen 5](https://wiki.archlinux.org/title/Lenovo_ThinkPad_P14s_(AMD)_Gen_5)

---

## Lenovo ThinkPad T14s Gen 6 AMD

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

## HP EliteBook 845 G11

### Specifications
- **Display:** 14"
- **Weight:** ~1.5 kg
- **CPU:** AMD Ryzen 7 PRO 8840HS (Hawk Point-HS, Zen 4)
- **Cooling:** Single fan

### Power Limits
- **PL2 (Burst):** 51W
- **PL1 (Sustained):** 41W
- Profiles are close together (35-41W)

### Thermal & Noise Data
- "Performance stable under sustained workloads and on battery"
- "Breezed through typical business tasks in almost total silence"
- Cinebench 2024 30-min test: ambient ~23.5 dB(A)
- Gets warm under sustained load (single fan design)
- HP Smart Sense auto-switches modes

### Sources
- [NotebookCheck EliteBook 845 G11](https://www.notebookcheck.net/HP-EliteBook-845-G11-Laptop-Review-No-major-changes-but-still-one-of-the-best-business-notebooks.941399.0.html)
- [TechRadar EliteBook 845 G11](https://www.techradar.com/pro/hp-elitebook-845-g11-14in-business-laptop-review)

---

## Framework 13 AMD

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

## ASUS ProArt PX13 (HN7306)

### Model Variants
- **2024-2025 (Strix Point):** HX 370 + RTX 4050/4060/4070, up to 32GB RAM
- **2026 (Strix Halo):** Ryzen AI Max+ 395, Radeon 8060S iGPU (no dGPU), up to 128GB unified memory

### Specifications (2024-2025)
- **Display:** 13.3" 3K OLED (2880×1800), 60Hz, touch, convertible
- **Weight:** 1.39 kg (1.84 kg with charger)
- **CPU:** AMD Ryzen AI 9 HX 370 (Strix Point, 12C/24T)
- **GPU:** NVIDIA RTX 4050/4060/4070 Laptop
- **RAM:** 32GB LPDDR5X (soldered)
- **WiFi:** MediaTek MT7925 (Wi-Fi 7)

### Power Configuration
- **PL2 (Burst):** 80W
- **PL1 (Sustained):** **65W**
- Battery mode: 55W max (~10% performance drop)

### Benchmark Scores
- **Cinebench R15:** 3,489 (multi)
- **Cinebench R23:** 23,020 (multi) — fastest 13.3" laptop
- **Cinebench 2024:** 769 (CPU multi), 114 (single)

### Thermal & Noise Data

| Mode | Noise | Notes |
|------|-------|-------|
| Idle/Light | Silent | Fans off |
| Medium load | Low-40s dB(A) | Acceptable |
| Full load | **~53 dB(A)** | Gaming/stress |
| Whisper mode | Quiet | Reduced performance |

- "Manages to avoid thermal throttling, maintaining consistent performance"
- "Didn't get nearly as hot and loud during demanding tasks as expected"
- Fans can be "slightly high pitched" — more noticeable than similar volume
- After BIOS updates, fan behavior improved significantly
- Surface stays thermally controlled

### Stress Test Behavior
- Processor briefly uses 80W, settles to **65W sustained**
- "Drop in performance remains low but results fluctuate slightly"
- Performance fluctuation due to short Cinebench R15 test catching different power phases
- "Even in 'worst' case, HX 370 is the fastest chip"
- 14% faster than Ryzen 9 8945HS on average

### Linux Compatibility

| Component | Status | Fix |
|-----------|--------|-----|
| WiFi (MT7925) | ⚠️ | Kernel 6.7+ required |
| Keyboard backlight | ⚠️ | linux-oem-24.04c or xanmod |
| Fan control | ⚠️ | linux-oem-24.04c or xanmod |
| HDMI output | ⚠️ | xanmod kernel |
| NVIDIA dGPU | ⚠️ | nvidia 530.41.03+ |
| CPU/RAM/NVMe | ✓ | Works |

**Recommended:** Use xanmod kernel on Ubuntu 24.04 for full hardware support.
User reports confirm working setup with xanmod (HDMI, WiFi, backlight all functional).
See [LinuxQuestions thread](https://www.linuxquestions.org/questions/linux-laptop-and-netbook-25/ubuntu-24-04-on-asus-proart-px13-hn7306wi_hn7306wi-4175751777-new/) for details.

### Caveats
- 13.3" 2-in-1 form factor — compact but less cooling headroom than 14" clamshells
- RTX GPU adds heat/power complexity
- OLED 60Hz (no high refresh option)
- Whisper mode reduces performance significantly

### Best Use Case
Excellent for sustained workloads if you accept ~53 dB noise under full load. The 65W sustained power and 12-core HX 370 make it the most powerful sub-14" convertible. Good for compilation if noise isn't critical.

### Sources
- [NotebookCheck ProArt PX13 Review](https://www.notebookcheck.net/Asus-ProArt-PX13-review-The-world-s-fastest-13-3-inch-2-in-1-thanks-to-AMD-Zen-5-and-RTX-4070-laptop.868429.0.html)
- [PCWorld ProArt PX13 Review](https://www.pcworld.com/article/2418049/asus-proart-px13-review.html)
- [UltrabookReview 12-Month Review](https://www.ultrabookreview.com/72323-asus-proart-px13-review/)
- [Windows Central ProArt PX13](https://www.windowscentral.com/laptops/asus-proart-px13-review)
- [Linux Hardware Database - PX13](https://linux-hardware.org/?probe=c0107457aa)

---

## Lenovo Yoga Pro 7 14 AMD

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

## System76 Darter Pro

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

## ASUS ROG Flow Z13 (2025) ⚠️ NOT RECOMMENDED

### Specifications
- **Display:** 13.4" (tablet/2-in-1)
- **Weight:** ~1.2 kg (tablet only)
- **CPU:** AMD Ryzen AI Max+ 395 (Strix Halo)
- **TDP:** 120W max, ~60W typical

### Power & Thermal Data

| Mode | Noise | Power |
|------|-------|-------|
| Silent | Inaudible | Reduced |
| Performance | ~42 dB | Good |
| Turbo | ~50 dB | Maximum |
| Manual (maxed) | ~50 dB | 85W sustained |

### Mixed Reviews on Throttling
- HotHardware: "Never observed thermal throttling"
- Windows Central: "You WILL experience thermal throttling"
- Tom's Guide: 91.6% stability over 25 Time Spy runs
- Reports of 96-100°C temps, sudden shutdowns

### Known Issues
- **Law firm investigating overheating reports**
- Random FPS drops requiring reboot
- Software/driver instability
- Compact form factor = thermal compromises

### Sources
- [Tom's Guide ROG Flow Z13](https://www.tomsguide.com/computing/laptops/gaming-laptops/asus-rog-flow-z13-2025-review)
- [HotHardware ROG Flow Z13](https://hothardware.com/reviews/rog-flow-z13-review?page=4)
- [Windows Central ROG Flow Z13](https://www.windowscentral.com/hardware/asus/asus-rog-flow-z13-2025-review)
- [RTINGS ROG Flow Z13](https://www.rtings.com/laptop/reviews/asus/rog-flow-z13-gz302-2025)

---

## Excluded Models (Details)

### ASUS Zenbook 14 AMD
- Cinebench R23: Started at 13,843, dropped to high 8,000s
- Power drops from 50W → 28W over 5-6 minutes
- "Throttles hard on looped Cinebench test"
- Source: [Tom's Hardware](https://www.tomshardware.com/laptops/ultrabooks-ultraportables/asus-zenbook-14-oled-ux3405m-review)

### LG Gram 14
- "Thermal throttling is the worst case I've seen for P-series"
- Frame rate drops from 15 to 10 FPS under load
- Source: [NotebookCheck LG Gram Style 14](https://www.notebookcheck.net/LG-Gram-Style-14-laptop-review-Elegant-fast-and-too-hot.744925.0.html)

### Xiaomi / Huawei Laptops
- Intel DPTF not supported on Linux
- Up to 50% performance loss vs Windows
- Limited sustained-load review data
- Source: [Phoronix Lenovo Thermal Throttling](https://www.phoronix.com/news/Lenovo-Linux-Thermal-Throttling)

### ThinkPad P14s AMD
- Even silent mode runs at 24W ("windmill")
- "Unacceptable noise" per user reports
- Profiles unbalanced vs T14
- Source: [Fedora Linux on P14s Gen 5](https://www.bovender.de/posts/2024/08/experience-with-running-fedora-linux-on-a-thinkpad-p14s-gen-5/)
