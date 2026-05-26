# Changelog

## 2026-05-26

### Added
- Intel and Qualcomm research: `reviews/intel-qualcomm-linux-2026.md` — comprehensive analysis of non-AMD options for sustained Linux workloads
- Intel DPTF/DTT status update — no longer a blanket dealbreaker; Lenovo OS-agnostic firmware fix via LVFS, improved kernel int340x drivers, vendor risk assessment
- Intel Arrow Lake-H (Core Ultra 200H) — benchmarks, sustained power data by laptop (MSI Prestige 16 at 45-55W vs ASUS Zenbook Duo at 24W), ~15% behind AMD HX 370 multi-core
- Intel Lunar Lake (Core Ultra 200V) — assessed and excluded for compilation; 8C/8T max, 400MHz frequency bug on Linux "balanced" profile
- Intel Panther Lake (Core Ultra Series 3, 18A) — Phoronix Linux benchmarks show strong efficiency but HX 370 is 1.31x faster; Framework 13 Pro (1.4 kg) is best Intel option
- Qualcomm Snapdragon X Elite Linux — Phoronix EOY 2025: Tiger Lake-level performance, TUXEDO canceled X1E laptop, no KVM, frequent thermal shutdowns
- Qualcomm Snapdragon X2 Elite — impressive Windows benchmarks (CB2024 multi 1,761 @ 18C/3nm) but Linux 12-18 months away; GPU upstreaming in kernel 6.19
- Framework 13 Pro Intel (Panther Lake) — 1.4 kg, vapor chamber, LPCAMM2, open firmware, 10-15h Linux battery
- Cross-platform comparison table: AMD vs Intel vs Qualcomm for sustained Linux multi-core

### Updated
- `cpu-comparison.md` — expanded Intel/Qualcomm sections with Panther Lake Phoronix data, X2 Elite benchmarks, DPTF status, Lunar Lake issues, and cross-platform summary table
- `laptop-research-summary.md` — added Intel section (Framework 13 Pro as best Intel option), Qualcomm status, updated excluded models list, added cross-platform comparison and decision matrix entries

### Excluded
- All Snapdragon X laptops — Linux support immature, Tiger Lake-level performance, no KVM virtualization
- Intel Lunar Lake for compilation — only 8C/8T at 37W max, 400MHz frequency bug

### Recommendations
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
