# Changelog

## 2026-06-25

### Updated
- TUXEDO InfinityBook Pro 15 — corrected the docking/PD analysis: the 150W charging is a **proprietary 20V/7.5A profile** (outside USB-PD; verified on the TUXEDO product page), not PD 3.1. No dock can supply it, so any dock caps the laptop at **100W**; a 140W/180W PD 3.1 dock only adds voltage stability, not wattage. The rear USB4 port is the sole Thunderbolt port **and** the sole 150W port, while the left USB-C is 100W and not USB4 — so **Thunderbolt docking and 150W charging are mutually exclusive even with two cables.** Removed the earlier "needs a ~$550 140W+ dock for full-power single-cable operation" framing across review, docking overview, excluded-models, summary, and README.
- TUXEDO InfinityBook Pro 15 docking — added primary-source community reports (r/tuxedocomputers): PD-sensitivity dock resets under load confirmed across multiple docks (Kensington SD5700T, Dell WD22TB4, Belkin/i-tec, TUXEDO Triple Dock; fix = 2nd charger or TDP cap). TUXEDO support confirms 100W ≠ full performance on the **15** (90W), while the **14** (65W) reaches full performance on 100W and runs stable single-cable on a Lenovo TB5 7500. Restored the Lenovo 7500 single-cable stability note with correct attribution (IBP 14, not 15).

### Recommendations
- Added a selection criterion (README "Key Criteria" + `CLAUDE.md`): require full-power charging over **standard USB-C PD** (SPR ≤100W, or PD 3.1 EPR up to 240W — though most docks cap at 140W) and prefer the charging port to also be USB4/Thunderbolt — avoid proprietary >100W profiles that force a Thunderbolt-vs-full-power trade-off.

## 2026-06-02

### Added
- Strix Halo overview: `overviews/strix-halo-linux.md` — full catalog of AMD Ryzen AI Max / Max+ laptops (June 2026): HP ZBook Ultra G1a, ROG Flow Z13, ProArt PX13, ASUS TUF A14, Lenovo Yoga Pro 7a / Legion 7a, MetaMech 16; mini-PC/handheld exclusions; platform Linux status (kernel 6.14+/Mesa 25, IR webcam needs ISP4 ~6.18, NPU/ROCm caveats on gfx1151); why Strix Halo is overkill for CPU-bound compilation (iGPU/256 GB/s bandwidth wasted)
- HP ZBook Ultra G1a 14: `reviews/hp-zbook-ultra-g1a.md` — Ryzen AI Max+ PRO 395, 66W sustained, CB R23 30,706 (highest in set), 128 GB LPDDR5X, 1.586 kg, Ubuntu 24.04 certified (Linux good). Status available; held back from recommended by ~48 dB load noise, soldered RAM, ~$4,000, 140W charger needing a dock
- ODM barebones overview: `overviews/odm-barebones-linux.md` — maps Linux laptop brands to their underlying Tongfang/Uniwill and Clevo chassis (2024-2026). Clarifies Uniwill = Tongfang (one ODM), Clevo = separate; GX4 = 14" / GX5 = 15.3"; confirmed twins (IB Pro 14 ≡ XMG EVO 14 ≡ Tongfang GX4; Darter Pro darp11 ≡ Clevo V560TU); brand→ODM table (TUXEDO, System76, NovaCustom, XMG/Schenker, Eluktronics, Sager, etc.); per-chassis Linux/PD notes

### Updated
- ASUS ProArt PX13 — 2026 GoPro Edition (Strix Halo Max+ 395) now independently reviewed: 70W sustained (Performance), CB R23 30,403 (10-min), GB6 18,956 multi, 1.39 kg (**lightest reviewed Strix Halo**), 128 GB LPDDR5X-8000. Linux fair — needs kernel 7.0 mainline (ACP70 audio quirks landed 2026-03-16), boot params, and manual TAS2783 speaker-firmware extraction. Frontmatter 2026 variant updated with real benchmarks/power
- Strix Halo overview — refreshed review statuses: PX13 GoPro and ASUS TUF A14 (Max+ 392, 1.48 kg) moved from announced to reviewed; clarified the reviewed Legion 7a **16"** is Gorgon Point HX 470 (not Strix Halo) while the 15.3" Strix Halo Legion 7a is still forthcoming; confirmed **no Chinese laptop barebones** on Max+ 395 (China activity is mini-PCs / AI Halo Box / Mini AI Workstations, plus the finished MetaMech 16 laptop)

## 2026-05-28

### Added
- TUXEDO InfinityBook Pro 15 Gen10: `reviews/tuxedo-infinitybook-pro-15.md` — Tongfang GX5 chassis, 90W cooling capacity, 99 Wh battery, 128 GB DDR5 SO-DIMM, same HX 370 CPU as 14". Excluded (1.77 kg exceeds ≤1.6 kg criterion)
- Comprehensive TB4/TB5 and eGPU dock overview: `overviews/usb4-docking-linux.md` — 20+ TB5 docks compared, TB4 docks still relevant, eGPU docks with PD (AORUS AI BOX, GPD G1, ROG XG Mobile, Minisforum DEG2), AMD USB4 compatibility (MST issues, kernel regressions), PD requirements, USB-C monitor compatibility, Linux eGPU state

### Updated
- `CLAUDE.md` — added PD/docking cost rule: laptops with >100W chargers require expensive docks (~$550), note as hidden cost in reviews
- `README.md` — added docking cost key insight, dock overview link
- `laptop-research-summary.md` — added InfinityBook Pro 15 to Not Recommended table

## 2026-05-26

### Added
- ASUS Zenbook S 16 (UM5606): `reviews/asus-zenbook-s-16.md` — 28W/35W sustained, 3K OLED, ceraluminum, Linux works with kernel 6.14+ and amdgpu boot param
- Gorgon Point overview: `overviews/2026-update-gorgon-point.md` — Ryzen AI 400 is a minor Strix Point refresh (+3-5% clocks), not worth upgrading
- TUXEDO InfinityBook Pro 14 Gen10: `reviews/tuxedo-infinitybook-pro-14.md` — **65W sustained**, 128 GB upgradeable RAM, native Linux, 1.49 kg, CB R23 22,784
- HP OmniBook Ultra 14: `reviews/hp-omnibook-ultra-14.md` — 47W sustained, CB R23 21,812, best value at $1,050
- ASUS VivoBook S 14 OLED: `reviews/asus-vivobook-s14-oled.md` — lightest HX 370 at 1.31 kg, 54W sustained
- Lenovo ThinkPad P14s AMD: `reviews/lenovo-thinkpad-p14s-amd.md` — Gen 6 HX PRO 370 at 36W sustained plus Gen 7 HX PRO 470 / 96 GB SO-DIMM watchlist
- Lenovo ThinkPad T14 AMD: `reviews/lenovo-thinkpad-t14-amd.md` — Gen 7 Gorgon Point, 75 Wh battery, up to 96 GB SO-DIMM, RJ45
- HP EliteBook X G2a: `reviews/hp-elitebook-x-g2a.md` — sub-1 kg with Gorgon Point, thermal concerns
- ASUS ExpertBook P5 G2: announced, claims 45W sustained at 1.27 kg, 96 GB SO-DIMM — needs review verification
- LPCAMM2 laptops overview: `overviews/lpcamm2-laptops-2026.md` — 12 models tracked, mostly Intel; first AMD LPCAMM2 is ThinkPad P16s Gen 5 (96 GB, June 2026)
- Dell Pro Precision 5 14S — 1.4 kg workstation with LPCAMM2 up to 64 GB, Intel or AMD
- ThinkPad T14 Gen 7 Intel variant has LPCAMM2 (AMD variant uses SO-DIMM DDR5)
- Intel and Qualcomm research: `overviews/intel-qualcomm-linux-2026.md` — comprehensive analysis of non-AMD options for sustained Linux workloads
- Intel DPTF/DTT status update — no longer a blanket dealbreaker; Lenovo OS-agnostic firmware fix via LVFS, improved kernel int340x drivers, vendor risk assessment
- Intel Arrow Lake-H (Core Ultra 200H) — benchmarks, sustained power data by laptop (MSI Prestige 16 at 45-55W vs ASUS Zenbook Duo at 24W), ~15% behind AMD HX 370 multi-core
- Intel Lunar Lake (Core Ultra 200V) — assessed and excluded for compilation; 8C/8T max, 400MHz frequency bug on Linux "balanced" profile
- Intel Panther Lake (Core Ultra Series 3, 18A) — Phoronix Linux benchmarks show strong efficiency but HX 370 is 1.31x faster; Framework 13 Pro (1.4 kg) is best Intel option
- Qualcomm Snapdragon X Elite Linux — Phoronix EOY 2025: Tiger Lake-level performance, TUXEDO canceled X1E laptop, no KVM, frequent thermal shutdowns
- Qualcomm Snapdragon X2 Elite — impressive Windows benchmarks (CB2024 multi 1,761 @ 18C/3nm) but Linux 12-18 months away; GPU upstreaming in kernel 6.19
- Framework 13 Pro Intel (Panther Lake) — 1.4 kg, vapor chamber, LPCAMM2, open firmware, 10-15h Linux battery
- Cross-platform comparison table: AMD vs Intel vs Qualcomm for sustained Linux multi-core

### Updated
- `cpu-comparison.md` — added Gorgon Point (HX 470/475, AI 9 465, AI 7 450), Fire Range (9955HX3D/9955HX/9850HX), Gorgon Halo (Max+ PRO 495), new Strix Halo SKUs (Max+ 392/388), Intel Panther Lake/Arrow Lake/Lunar Lake, Qualcomm X Elite/X2 Elite
- `laptop-research-summary.md` — added Intel section (Framework 13 Pro as best Intel option), Qualcomm status, updated excluded models list, added cross-platform comparison and decision matrix entries
- ThinkPad P14s AMD — reconsidered: Gen 6 reviews show improved cooling, no longer excluded
- ThinkPad T14/T14s Gen 7 AMD — corrected CPU ceiling to Ryzen AI 7 PRO 450; HX PRO 470 belongs to P14s Gen 7 AMD
- Validation tooling — added pytest coverage for generated JSONL freshness and repo-relative Markdown links
- Linux kernel notes — kernel 6.14 EPP default change, 6.16 amd-pstate improvements, 7.1 dynamic EPP, avoid kernel 6.18/6.19 amdgpu bugs

### Excluded
- All Snapdragon X laptops — Linux support immature, Tiger Lake-level performance, no KVM virtualization
- Intel Lunar Lake for compilation — only 8C/8T at 37W max, 400MHz frequency bug
- Dell Pro 14 Plus — throttles HX 370 to 25W, CB R23 only 12,684 (wastes the CPU)

### Recommendations
- **TUXEDO InfinityBook Pro 14 Gen10** — new top pick for Linux: 65W sustained, 128 GB upgradeable, native Linux, from 1,199 EUR
- AMD remains the clear winner for sustained multi-core Linux workloads
- Intel Panther Lake (Framework 13 Pro) is the best Intel option but ~30% behind AMD HX 370 in throughput
- DPTF is no longer a universal Intel dealbreaker — safe with Lenovo ThinkPad, Dell XPS Dev Edition, Framework, System76
- Qualcomm: check back in late 2026/2027 for X2 Elite viability

## 2026-01-22

### Added
- Initial research: 8 laptop models reviewed for sustained CPU performance under Linux
- Lenovo ThinkPad T14 Gen 5/6 AMD — best overall balance (22.5W sustained, ~40 dB)
- Lenovo ThinkPad T14s Gen 6 AMD — lightest option (1.3 kg, 25W sustained)
- HP EliteBook 845 G11 — highest sustained power in class (41W)
- ASUS ProArt PX13 (HN7306) — fastest 13" convertible (65W sustained, HX 370)
- Lenovo Yoga Pro 7 14 AMD — highest raw power 14" (70W sustained)
- Framework 13 AMD — best Linux ecosystem, open firmware
- System76 Darter Pro — DIY/open firmware option
- ASUS ROG Flow Z13 2025 — reviewed and excluded (thermal inconsistency)
- AMD mobile CPU comparison: Strix Halo, Strix Point, Hawk Point, Krackan Point
- Excluded models list: Zenbook 14 (throttling), LG Gram 14, Framework 16, Xiaomi/Huawei (Intel DPTF), ThinkPad P14s AMD
