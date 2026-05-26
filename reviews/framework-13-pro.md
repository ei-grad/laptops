---
model: Framework 13 Pro
slug: framework-13-pro
manufacturer: Framework
status: announced
form_factor: clamshell
weight_kg: 1.4
battery_wh: 74.5
price_usd: 1199
display:
  aspect_ratio: '3:2'
  brightness_nits: 700
  contrast: 1800
  panel: IPS LTPS
  refresh_hz: 120
  resolution: 2880x1920
  size_in: 13.5
  touch: true
variants:
- cpu:
    arch: Panther Lake (Intel 18A)
    cores: 16
    name: Intel Core Ultra X7 358H
    threads: 16
  gpu:
    name: Intel Arc (integrated)
    type: integrated
  power:
    pl1_w: 28
    pl2_w: 80
  ram_gb: 64
  ram_type: LPCAMM2 LPDDR5X-7467
  ram_upgradeable: true
  sku: Intel Panther Lake
  status: announced
  weight_kg: 1.4
  year: 2026
- cpu:
    arch: Strix Point (Zen 5 + Zen 5C)
    cores: 12
    name: AMD Ryzen AI 9 HX 370
    threads: 24
  gpu:
    compute_units: 16
    name: Radeon 890M
    type: integrated
  power:
    pl1_w: 33
    pl2_w: 46
  ram_gb: 64
  ram_type: DDR5-5600 SO-DIMM
  ram_upgradeable: true
  sku: AMD Strix Point
  status: announced
  weight_kg: 1.4
  year: 2026
linux:
  notes:
  - First Framework laptop Ubuntu Certified by Canonical
  issues:
  - Requires Mesa 25.0+ for Intel Arc / Radeon 890M
  kernel_min: '6.14'
  status: excellent
sources:
- https://www.phoronix.com/review/framework-13-amd-strix-point
- https://www.phoronix.com/review/framework-13-ryzen-ai-power
- https://www.phoronix.com/news/Framework-Laptop-13-Pro
- https://www.notebookcheck.net/We-go-hands-on-with-the-Framework-Laptop-13-Pro-and-the-improvements-are-night-and-day.1281339.0.html
- https://www.notebookcheck.net/Framework-Laptop-13-5-Ryzen-AI-9-review-Skip-the-Intel-version-for-better-performance.997363.0.html
- https://www.notebookcheck.net/Framework-Laptop-13-Pro-promises-more-battery-life-performance-and-metal.1280024.0.html
- https://www.notebookcheck.net/Leaving-Apple-MacBook-Pro-for-Framework-Laptop-13-Pro-Over-1-3rd-of-Laptop-13-Pro-buyers-are-reportedly-ex-MacBook-Pro.1283484.0.html
- https://www.tomshardware.com/laptops/frameworks-overhauled-laptop-13-pro-brings-a-redesigned-chassis-intel-core-ultra-series-3-system-aims-to-be-a-macbook-pro-for-linux-users
- https://www.pcworld.com/article/3120596/hands-on-with-the-framework-laptop-13-pro-a-killer-upgrade.html
- https://www.heise.de/en/news/Framework-Laptop-13-Pro-AMD-more-expensive-than-Intel-Ubuntu-pre-installed-11268489.html
- https://hardware.slashdot.org/story/26/04/21/2019256/framework-laptop-13-pro-is-a-major-overhaul-for-the-modular-upgradeable-laptop
- https://9to5mac.com/2026/04/22/the-macbook-pro-for-linux-users-both-copies-and-contrasts-with-apple/
- https://www.notebookcheck.net/Framework-claims-Dell-is-trying-to-derail-Framework-s-marketing-by-sending-influencers-Dell-XPS-laptops.1283482.0.html
- https://world.hey.com/dhh/the-new-framework-13-hx370-68675e0e
- https://world.hey.com/dhh/panther-lake-is-the-real-deal-4bd731f1
- https://news.ycombinator.com/item?id=47852177
- https://news.ycombinator.com/item?id=47852401
- https://news.ycombinator.com/item?id=47902816
- https://community.frame.work/t/introducing-framework-laptop-13-pro/81951
- https://community.frame.work/t/2026-linux-distro-survey-framework-laptop-13-pro/82459
- https://www.techrxiv.org/doi/10.36227/techrxiv.176591390.00588709
- https://frame.work/blog/introducing-framework-laptop-13-pro
- https://frame.work/laptop13pro
- https://www.phoronix.com/review/framework-13-amd-linux-2025
- https://www.phoronix.com/review/amd-ryzen-ai-9-hx-370/3
---
# Framework 13 Pro (2026)

**Status:** Announced April 21, 2026. Intel Pro configurations ship June 2026; AMD Strix Point availability is region/config dependent and should be treated as pre-review.
**Price:** From $1,199 (DIY) / $1,499 (pre-built)
**Last updated:** 2026-05-26

## Specifications

| Spec | Intel Variant | AMD Variant |
|------|---------------|-------------|
| CPU | Core Ultra 5 325 / X7 358H / X9 388H | Ryzen AI 7 350 / AI 9 HX 370 |
| Architecture | Panther Lake (Intel 18A) | Strix Point (Zen 5 + Zen 5C) |
| RAM Type | **LPCAMM2** LPDDR5X-7467 | DDR5-5600 **SO-DIMM** |
| RAM Max | 64 GB | 64 GB |
| Battery | 74.5 Wh (850 Wh/L density) | 74.5 Wh |
| Display | 13.5" 2880x1920 3:2, 700 nit, 1800:1, 30-120 Hz VRR, touch, matte | Same |
| Weight | 1.4 kg | 1.4 kg |
| Thickness | 15.85 mm | 15.85 mm |
| Storage | M.2 2280 PCIe 5.0 (up to 8 TB, 14,000 MB/s) | Same |
| Wi-Fi | Intel BE211 (Wi-Fi 7) | Same |
| Ports | 4x Thunderbolt 4 via expansion cards | Same |
| Battery Longevity | 80% capacity after 1,000 cycles | Same |
| Charger | 100W GaN | Same |

**IMPORTANT: AMD uses SO-DIMM DDR5-5600, NOT LPCAMM2.** Only the Intel Panther Lake Pro configuration gets LPCAMM2.

## Major Changes from Framework 13 (old)

- Full CNC 6063 aluminum chassis (ground-up redesign, not aluminum-plastic hybrid)
- Haptic touchpad (4 piezo elements, MacBook-like, no mechanical click switch)
- Touch display (in-cell, first on a Framework 13")
- LPCAMM2 memory on Intel variant (replaceable, unlike soldered LPDDR5X in competing ultrabooks)
- 74.5 Wh battery (22% increase from 61 Wh prior gen)
- Honeywell phase-change thermal interface material
- Redesigned heatsink and fan system
- Side-mounted speakers with Dolby Atmos (ported out of chassis)
- Per-unit factory color calibration on display
- Wi-Fi 7 (Intel BE211)
- Fingerprint reader with Linux support
- 1.5 mm key travel keyboard (two colorway options)
- **First Framework laptop Ubuntu Certified by Canonical**
- Ubuntu pre-built configs outselling Windows
- Open-source surface CAD released for accessories
- 3-year warranty option (US)
- Backward-compatible: new parts can be installed into older Framework 13 chassis and vice versa

---

## 1. Phoronix Linux Review (AMD Strix Point, April 2025)

**Source:** [Phoronix: Framework 13 AMD Strix Point](https://www.phoronix.com/review/framework-13-amd-strix-point) (reviewed the pre-Pro chassis with same HX 370 SoC)

Phoronix tested the Framework 13 with AMD Ryzen AI 9 HX 370 (12 Zen 5 cores: 4 Zen 5 + 8 Zen 5C, 24 threads, Radeon 890M RDNA 3.5 iGPU).

### Sustained Benchmarks
- **Kernel compilation power draw:** Average 24W, peak 33W -- significantly better than Intel Core Ultra 7 155H (Meteor Lake) which drew 34W average while being much slower
- **Cinebench R23 Multi-Core:** 17,963 points (on Framework 13.5 with same SoC per NotebookCheck)
- **Sustained power (Prime95):** 33W sustained after initial 46W boost
- **Performance exceeded** the ASUS Zenbook S16 with the same SoC

### Thermal Behavior
- **CPU temp under Prime95:** ~80C average, 82C with combined CPU+GPU stress
- **Gaming temp (Cyberpunk 2077):** ~75C
- **Idle temp:** ~52C
- Up to 15% throttling observed over extended multi-core loops in the old chassis

### Linux Distribution Performance
- **Best performers:** CachyOS, Clear Linux, Debian 13
- **Minimum recommended:** Linux 6.14 + Mesa 25.0 for full support
- **Tested distros:** CachyOS, Clear Linux, Debian 13, Fedora 42, Manjaro 25.0, openSUSE Tumbleweed, Ubuntu 25.04
- Open-source AMD driver stack works out of the box

### Power Tuning
- [Phoronix: Power & Performance Tuning](https://www.phoronix.com/review/framework-13-ryzen-ai-power) covers additional power profile optimization

**Note:** Phoronix has announced the Framework Laptop 13 Pro ([Phoronix announcement](https://www.phoronix.com/news/Framework-Laptop-13-Pro)) but has not yet published a full review of the Pro chassis. The benchmark data above is from the pre-Pro Framework 13 with the same HX 370 SoC. The Pro's redesigned thermal system (new heatsink, phase-change TIM) should improve these numbers.

---

## 2. NotebookCheck Review

### Hands-On (April 2026)
**Source:** [NotebookCheck hands-on](https://www.notebookcheck.net/We-go-hands-on-with-the-Framework-Laptop-13-Pro-and-the-improvements-are-night-and-day.1281339.0.html)

- Chassis rigidity described as "night and day" improvement over the old model
- 5052 aluminum alloy frame is "much more substantial" -- old model "would flex and creak much more readily"
- Display: 2880x1920, 120 Hz, 700 nit, touchscreen, but OLED not available (likely battery concerns)
- Keyboard: "crisper feedback" with 1.5 mm key travel
- Trackpad: "MacBook-like haptics"
- **Panther Lake X7 can allegedly run Cyberpunk 2077 at 1080p/60fps** on integrated graphics
- Noted the laptop is heavier (1.4 kg) and thicker (15.9 mm) than some 14" competitors (Lenovo Yoga 7 Ultra 14 is under 1 kg)

### Full review: Not yet published as of May 2026.

### Prior Model Data (Framework 13.5 Ryzen AI 9 HX 370)
**Source:** [NotebookCheck: Framework Laptop 13.5 Ryzen AI 9](https://www.notebookcheck.net/Framework-Laptop-13-5-Ryzen-AI-9-review-Skip-the-Intel-version-for-better-performance.997363.0.html)

| Metric | Value |
|--------|-------|
| Cinebench R23 MC | 17,963 |
| Cinebench R15 MC | 2,823 |
| PCMark 10 | 7,530 |
| Prime95 sustained power | 33W (after 46W initial boost) |
| Prime95 temp | 80C avg |
| Combined stress temp | 82C |
| Gaming temp | 75C |
| Idle temp | 52C |
| Display brightness | 530 nit (max), 506 nit (avg) |
| Contrast | 1766:1 |
| sRGB coverage | 95.9% |
| Display P3 | 71.9% |
| Adobe RGB | 70.8% |
| Throttling under sustained load | up to 15% |
| vs Intel variant | 30-35% faster than Core Ultra 7 |

NotebookCheck verdict on AMD variant of old model: "Skip the Intel version for better performance."

### Announcement Coverage
**Source:** [NotebookCheck: Framework 13 Pro announcement](https://www.notebookcheck.net/Framework-Laptop-13-Pro-promises-more-battery-life-performance-and-metal.1280024.0.html)

- Available with Intel Core Ultra X7 358H or AMD Ryzen AI 9 HX 370
- 74.5 Wh battery, up to 20 hours claimed
- Starts at $1,200 (barebones Core Ultra 5) up to $1,600+ (Core Ultra X7)

### Buyer Demographics
**Source:** [NotebookCheck: ex-MacBook Pro buyers](https://www.notebookcheck.net/Leaving-Apple-MacBook-Pro-for-Framework-Laptop-13-Pro-Over-1-3rd-of-Laptop-13-Pro-buyers-are-reportedly-ex-MacBook-Pro.1283484.0.html)

- **Over 1/3 of pre-orders** came from ex-MacBook Pro users (Framework post-purchase survey)
- MacBook switchers chose **Linux over Windows** as their destination OS
- Intel base ($1,499 with 16 GB/512 GB) undercuts MacBook Pro 14 M5 ($1,699) by $200

---

## 3. Other Major Reviews

### Tom's Hardware (April 21, 2026)
**Source:** [Tom's Hardware](https://www.tomshardware.com/laptops/frameworks-overhauled-laptop-13-pro-brings-a-redesigned-chassis-intel-core-ultra-series-3-system-aims-to-be-a-macbook-pro-for-linux-users)

- Positioned as "MacBook Pro for Linux users"
- Ground-up redesign, not an iteration on the old Laptop 13
- Intel Core Ultra Series 3 (Panther Lake) with up to 16 cores on Intel 18A process
- Full hands-on review pending (announcement coverage only)

### PCWorld Hands-On (April 2026)
**Source:** [PCWorld hands-on](https://www.pcworld.com/article/3120596/hands-on-with-the-framework-laptop-13-pro-a-killer-upgrade.html)

- Chassis feels "pleasingly solid in the hand" -- addresses older model's wiggliness
- Keyboard earns "roughly B+ or higher"
- 700 nit display described as "ideal for working outside"
- Framework claims 20+ hours Netflix 4K streaming (12 hours more than old gen)
- LPCAMM2 replacement requires just three screws
- Dolby Atmos speakers stuttered during demo (suspected driver issue, not hardware)
- "Hyper-detailed assembly guides" with QR codes for each component
- Verdict: "an across-the-board upgrade"

### Heise Online (April 2026)
**Source:** [Heise: AMD more expensive than Intel](https://www.heise.de/en/news/Framework-Laptop-13-Pro-AMD-more-expensive-than-Intel-Ubuntu-pre-installed-11268489.html)

Key finding: **AMD variant uses SO-DIMM DDR5-5600, NOT LPCAMM2 LPDDR5X-7467.**

| Config | Intel | AMD |
|--------|-------|-----|
| Entry | €1,349 (Core Ultra 5 325) | €1,579 (Ryzen AI 7 350) |
| Mid-range | €1,799 (Core Ultra X7 358H) | €1,859 (Ryzen AI 9 HX 370) |
| RAM type | LPCAMM2 LPDDR5X-7467 | DDR5-5600 SO-DIMM |

AMD variant pre-orders open, delivery starting July 2026.

### Slashdot, Hackster.io, 9to5Mac
- [Slashdot discussion](https://hardware.slashdot.org/story/26/04/21/2019256/framework-laptop-13-pro-is-a-major-overhaul-for-the-modular-upgradeable-laptop) -- "major overhaul for the modular, upgradeable laptop"
- [9to5Mac](https://9to5mac.com/2026/04/22/the-macbook-pro-for-linux-users-both-copies-and-contrasts-with-apple/) -- "'The MacBook Pro for Linux users' both copies and contrasts with Apple"
- Dell reportedly tried to counter-program the launch by sending XPS laptops to influencers ([NotebookCheck](https://www.notebookcheck.net/Framework-claims-Dell-is-trying-to-derail-Framework-s-marketing-by-sending-influencers-Dell-XPS-laptops.1283482.0.html))

### The Verge, Ars Technica, AnandTech
- No dedicated full reviews found as of May 2026. The Verge and Ars Technica domains blocked from web search crawlers.
- Ars Technica coverage referenced in Slashdot discussions but no direct review link found.
- AnandTech remains defunct (shut down 2024).

---

## 4. DHH (David Heinemeier Hansson) Reviews

### Framework 13 HX370 Review (April 2025)
**Source:** [DHH: The new Framework 13 HX370](https://world.hey.com/dhh/the-new-framework-13-hx370-68675e0e)

- **HEY test suite:** 2m07s (vs 2m43s on 7840U, 2m49s on M4 Pro) -- ~20% faster in single-core than 7840U
- **Price:** $1,992 with 32 GB/1 TB (comparable to M4 Pro MBP14 at $2,199)
- **Battery:** ~6 hours mixed use, 8-10 hours writing-only -- trailing Qualcomm and Apple
- **Linux:** "the best Linux laptop you can buy today, which by extension makes it the best web developer laptop too"
- **Display:** 3:2 matte screen -- "this is the best looking laptop screen I've ever used for programming"
- **Keyboard:** "a big step up over the MacBook Pro, primarily because of the 50% longer key travel"
- Suggested Ryzen AI 7 350 at ~$1,600 as the "sweet spot"
- Verdict: "Hard to go wrong"

### Panther Lake Review (2026)
**Source:** [DHH: Panther Lake is the real deal](https://world.hey.com/dhh/panther-lake-is-the-real-deal-4bd731f1)

- **Geekbench 6:** 17,500 on Panther Lake 358H -- "about 10% faster than the already excellent AMD HX370, and a match for Apple's M5"
- **Idle power:** Dell XPS 14 with Panther Lake achieves 1.4W idle on Omarchy (Linux)
- **Battery life:** "around 16 hours" on a 74 Wh machine (mixed real-world use on Omarchy Linux)
- **Massive improvement** from AMD's ~6 hours to Intel Panther Lake's ~16 hours
- Credits Dell/Intel collaboration on Linux power optimization
- "Finally resolving the key barrier preventing Omarchy adoption: battery life disadvantage versus Apple"

**Implication for Framework 13 Pro:** The Intel Panther Lake variant may deliver dramatically better battery life (~16 hrs) than the AMD variant (~6 hrs), based on DHH's testing of both architectures. However, DHH's Panther Lake testing was on a Dell XPS 14, not the Framework 13 Pro specifically.

---

## 5. Community Feedback

### Hacker News (April 2026)
**Sources:**
- [HN: Framework Laptop 13 Pro](https://news.ycombinator.com/item?id=47852177)
- [HN: Framework 13 Pro Announced](https://news.ycombinator.com/item?id=47852401)
- [HN: Major Upgrades and Linux Front and Center](https://news.ycombinator.com/item?id=47902816)

Key discussion points:
- **Linux battery life:** Community expects 20+ hours on Intel but wants Linux-specific benchmarks (Framework only published Windows numbers). Framework CEO promised Linux benchmarks and sent pre-release units to distro developers for suspend/resume testing.
- **Thermals concern:** Existing Framework 13 owners report throttling and fan noise during video calls (11th gen Intel). CEO responded that Core Ultra Series 3 should keep fan off during calls due to hardware encode/decode.
- **LPCAMM2 pricing concern:** 64 GB LPCAMM2 module is ~$900 CAD vs ~$160 CAD for equivalent DDR4 SO-DIMM capacity. Consensus: impressive tech but expensive.
- **Pricing vs upgradability trade-off:** Tension between Framework's premium costs and long-term upgrade value. One owner: "If this would change, it would become just an over-priced laptop... might as well buy another ThinkPad or Dell XPS."
- **Haptic trackpad:** Mixed reactions. Some want MacBook-quality haptics, others prefer physical buttons for fewer misclicks.
- **Backward compatibility praised:** "one can buy individually any or all of the new parts and make any original FW13 into a 13 Pro without having to spend thousands"
- **Palm rejection issues:** Some Linux users disabled tap-to-click entirely due to unintended palm detection
- **Soft surface ventilation:** Bottom intake holes get blocked on laps/sofas, causing overheating
- **CEO transparency:** Community appreciates Framework's honest marketing language

### Framework Community Forums
**Source:** [Framework Community: Introducing Laptop 13 Pro](https://community.frame.work/t/introducing-framework-laptop-13-pro/81951)

- Active [2026 Linux Distro Survey](https://community.frame.work/t/2026-linux-distro-survey-framework-laptop-13-pro/82459) for Laptop 13 Pro
- Thermal question asked ("Does the new chassis improve thermals/acoustics with existing mainboards?") but no direct answer from Framework yet
- Upgrade path enthusiasm: all new parts individually purchasable
- LPCAMM2 pricing concern echoed
- AMD HX 370 "388H DIY" reported out of stock in some regions quickly
- No real-world Linux usage reports yet (units haven't shipped as of May 2026)

### Reddit (r/framework)
No indexed results found for Laptop 13 Pro discussions as of May 2026.

---

## 6. Comparison: 2026 Pro vs 2025 Framework 13 AMD

| Feature | Framework 13 (2025, Strix Point) | Framework 13 Pro (2026) |
|---------|----------------------------------|-------------------------|
| Chassis | Aluminum-plastic hybrid, flex/creak | Full CNC 6063 aluminum, rigid |
| Battery | 61 Wh | 74.5 Wh (+22%) |
| Battery life (AMD, DHH) | ~6 hrs mixed | TBD (same SoC, bigger battery should help) |
| Battery life (Intel, DHH) | N/A | ~16 hrs mixed (Panther Lake, Dell test) |
| Display | 2880x1920, non-touch | 2880x1920, 700 nit, touch, VRR 30-120 Hz |
| RAM (Intel) | DDR5 SO-DIMM | LPCAMM2 LPDDR5X-7467 |
| RAM (AMD) | DDR5-5600 SO-DIMM | DDR5-5600 SO-DIMM (unchanged) |
| Trackpad | Mechanical click | Haptic (4 piezo elements) |
| Thermal interface | Standard paste | Honeywell phase-change TIM |
| Speakers | Bottom-firing | Side-mounted, Dolby Atmos |
| Ubuntu Certified | No | Yes |
| Keyboard | 1.5 mm travel | 1.5 mm travel, new colorways |
| Weight | ~1.3 kg | 1.4 kg |
| Thickness | ~15.8 mm | 15.85 mm |
| Price (DIY base) | ~$1,049 | $1,199 |

### Thermal Improvements
The Pro chassis uses:
- Redesigned heatsink and fan system
- Honeywell phase-change thermal interface material
- Full CNC aluminum chassis (better heat spreading than old mixed-material design)

Expected thermal impact: reduced throttling under sustained load (old model showed up to 15% throttling in extended Cinebench loops). No independent thermal comparison data yet -- units haven't shipped.

---

## 7. LPCAMM2 Details

### Intel Variant Only
- **Type:** LPCAMM2 with LPDDR5X chips
- **Speed:** 7,467 MT/s
- **Capacities:** 16 GB, 32 GB, 64 GB (higher coming later)
- **User-replaceable:** Yes, 3 screws to swap
- **Voltage:** 1.05V (LPDDR5X)

### AMD Variant Uses SO-DIMM
- **Type:** DDR5-5600 SO-DIMM (standard)
- **Dual-channel capable** via two SO-DIMM slots

### LPCAMM2 vs Soldered LPDDR5X
LPCAMM2 delivers the **same bandwidth and power efficiency** as soldered LPDDR5X because it uses the same LPDDR5X chips on a compression connector with minimal trace length. The key advantage is modularity -- you get soldered-equivalent performance with user-replaceability.

### LPCAMM2 vs DDR5 SO-DIMM
| Metric | LPCAMM2 (LPDDR5X-7467) | DDR5-5600 SO-DIMM |
|--------|-------------------------|-------------------|
| Bandwidth | ~120 GB/s | ~89.6 GB/s |
| Bandwidth advantage | +33.9% | baseline |
| Active power | -58% vs SO-DIMM | baseline |
| Standby power | -80% vs SO-DIMM | baseline |
| Data rate | 7,467 MT/s | 5,600 MT/s |
| Voltage | 1.05V | 1.1V |
| Form factor | Smaller, flat | Larger, DIMM slot |
| Upgradeable | Yes (3 screws) | Yes (slot) |
| Pricing (32 GB) | ~€490 | ~€452-524 (1-2 sticks) |

**Source:** [TechRxiv: LPCAMM2 vs DDR5 SO-DIMM Benchmarking](https://www.techrxiv.org/doi/10.36227/techrxiv.176591390.00588709)

---

## 8. Price and Availability

### Intel Variants (Ship June 2026)
| Configuration | Price (USD) | Price (EUR) |
|---------------|-------------|-------------|
| DIY, Core Ultra 5 325 (no RAM/SSD) | $1,199 | €1,349 |
| Pre-built, Core Ultra X7 358H, 32 GB, 1 TB, Linux | $2,099 | ~€1,799 |
| Pre-built, Core Ultra X7 358H, 32 GB, 1 TB, Windows | $2,299 | -- |
| Ultra X9 | Sold out | -- |

### AMD Variants (Ship July 2026)
| Configuration | Price (USD) | Price (EUR) |
|---------------|-------------|-------------|
| DIY, Ryzen AI 7 350 | -- | €1,579 |
| Mid-range, Ryzen AI 9 HX 370 | -- | €1,859 |
| Pre-built, HX 370, 64 GB, 2 TB | $3,099 | -- |

### Mainboard Upgrade Kit
- $449 for standalone Pro mainboard (works in older Framework 13 chassis)

### Demand
- Six batches of Intel variant sold out within days of April 2026 announcement
- Ultra X9 already out of stock
- AMD HX 370 DIY reported out of stock in some regions
- Later orders pushed to August 2026 delivery
- **Over 1/3 of buyers are ex-MacBook Pro users** (Framework survey)
- **Ubuntu configs outselling Windows**

---

## Assessment

The Framework 13 Pro is a genuine generational leap over the old Framework 13. The CNC aluminum chassis, 74.5 Wh battery, improved thermals (phase-change TIM), haptic trackpad, and Ubuntu certification make it the most polished Linux laptop Framework has produced.

**Critical caveat for the AMD variant:** It uses DDR5-5600 SO-DIMM, NOT LPCAMM2. The LPCAMM2 advantage (33% more bandwidth, 58% less power) is Intel-only. AMD buyers also pay more (€1,859 vs €1,799 for comparable tier) and ship later (July vs June). The AMD variant's main advantage is raw multi-threaded CPU performance (HX 370 is 30-35% faster than Intel's previous gen per NotebookCheck).

**Battery life gap:** Based on DHH's testing of both architectures, Intel Panther Lake delivers ~16 hours vs AMD's ~6 hours of mixed use. Even with the 22% larger battery, the AMD variant will likely trail significantly in battery life.

**For sustained CPU workloads:** The HX 370 delivers 33W sustained at 80C with ~24W during kernel compilation -- excellent efficiency. The new Pro chassis thermal design should reduce the 15% throttling seen in the old chassis.

**No full independent reviews yet** -- Intel units ship June 2026. Current AMD performance data comes from testing the same HX 370 SoC in the prior-generation Framework 13 chassis.
