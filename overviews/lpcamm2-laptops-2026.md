# LPCAMM2 Laptops (2024-2026)

**Date:** 2026-05-26

LPCAMM2 (Low Power Compression Attached Memory Module 2) gives LPDDR5X bandwidth and efficiency with SO-DIMM-like upgradeability. Currently dominated by Intel platforms; AMD adoption just starting.

## LPCAMM2 vs SO-DIMM DDR5 vs Soldered LPDDR5X

| Metric | SO-DIMM DDR5-5600 | LPCAMM2 (LPDDR5X-8533) | Soldered LPDDR5X-8533 |
|--------|-------------------|------------------------|----------------------|
| Peak bandwidth | 89.6 GB/s | ~136 GB/s | ~136 GB/s |
| Bandwidth advantage | Baseline | +52% | +52% |
| Latency | ~90 ns | ~110 ns | ~110 ns |
| Power draw | ~4.5 W (dual DIMM) | ~2.8 W (single) | ~2.5 W |
| Voltage | 1.1 V | 1.05 V | 1.05 V |
| Upgradeable | YES | YES | NO |
| Max capacity (current) | 64 GB (2x32 GB) | 96 GB (1 module) | 32-64 GB typical |

LPCAMM2 gives soldered-class bandwidth with upgradeable form factor. Trade-off: ~20 ns higher latency than DDR5 SO-DIMM, but bandwidth advantage dominates in multi-threaded and memory-bound workloads.

## All LPCAMM2 Laptops Under 2 kg

### Available / Shipping

| Model | Weight | CPU | LPCAMM2 Max | Price | Linux | Notes |
|-------|--------|-----|-------------|-------|-------|-------|
| **Framework 13 Pro** | 1.41 kg | Intel Panther Lake | 64 GB @ 7467 | $1,199 DIY | Excellent | Best Linux; AMD variant uses SO-DIMM |
| **ThinkPad T14 Gen 7 Intel** | 1.31-1.38 kg | Intel Panther Lake | 64 GB @ 8533 | €1,399+ | Good | AMD variant uses SO-DIMM! iFixit 10/10 |
| **ThinkPad T16 Gen 5 Intel** | ~1.76 kg | Intel Panther Lake | 64 GB @ 8533 | $1,628+ | Good | 16", borderline on weight |
| **ThinkPad P1 Gen 8** | 1.76 kg | Intel Arrow Lake | 64 GB @ 7467 | $2,500+ | Good | 16" OLED workstation, RTX PRO 2000 |
| **Dell Pro Precision 5 14S** | **1.4 kg** | Intel PTL or AMD GP | 64 GB @ 8533 | TBD | Good (Dell) | Lightest workstation, ISV-certified |
| **Dell Pro 5 Series 14** | ~1.82 kg | Intel Panther Lake | 64 GB @ 8533 | TBD | Good (Dell) | LPCAMM2 only on Arc GPU variants |

### Announced / Coming Soon

| Model | Weight | CPU | LPCAMM2 Max | Notes |
|-------|--------|-----|-------------|-------|
| **ThinkPad P16s Gen 5 AMD** | 1.75 kg | AMD Gorgon Point | **96 GB** @ 8533 | First AMD LPCAMM2! Optional RTX Pro 2000. June 2026 |
| **Dell Pro Precision 5 16S** | ~1.8 kg | Intel PTL or AMD | 64 GB @ 8533 | 16" variant |
| **ThinkBook 14+** (China only) | ~1.5 kg | Intel Panther Lake | 32 GB @ 8533 | First consumer LPCAMM2 |

### NOT LPCAMM2 (common misconceptions)

- ThinkPad T14s Gen 7 — soldered LPDDR5X
- ThinkPad X1 Carbon Gen 14 — soldered
- ThinkPad T14 Gen 7 **AMD** — SO-DIMM DDR5 (not LPCAMM2)
- Framework 13 Pro **AMD** — SO-DIMM DDR5 (not LPCAMM2; only Intel has LPCAMM2)
- HP EliteBook / ZBook 2026 — HP has not adopted LPCAMM2
- ASUS — no LPCAMM2 laptops
- Samsung — makes modules but no LPCAMM2 laptops

## Retail LPCAMM2 Modules

### Crucial (only retail supplier)

| Module | Capacity | Speed | Price |
|--------|----------|-------|-------|
| CT32G85C2LP5X | 32 GB | 8533 MT/s | ~$233 |
| CT64G85C2LP5X | 64 GB | 8533 MT/s | ~$452 |
| CT32G75C2LP5X | 32 GB | 7500 MT/s | ~$180 |
| CT64G75C2LP5X | 64 GB | 7500 MT/s | ~$330 |

### Samsung (OEM only, not retail yet)

- 96 GB @ 9600 MT/s — mass production H2 2026
- 32/64 GB @ 8533 MT/s — shipping to OEMs

No 128 GB or 16 GB modules exist yet.

## Sources

- [iFixit: LPCAMM2 Is Finally Here](https://www.ifixit.com/News/95078/lpcamm2-memory-is-finally-here)
- [ThinkPad T14 Gen 7 LPCAMM2 - VideoCardz](https://videocardz.com/newz/lenovo-expands-thinkpad-series-at-mwc2026-thinkpad-t14-with-lpcamm2-memory)
- [ThinkPad P16s Gen 5 AMD - NotebookCheck](https://www.notebookcheck.net/AMD-CPUs-Nvidia-GPUs-LPCAMM2-Redesigned-Lenovo-ThinkPad-P16s-Gen-5-with-AMD-Ryzen-9-HX-400-announced.1251695.0.html)
- [Framework 13 Pro - frame.work](https://frame.work/laptop13pro)
- [Dell Pro Precision 5 14S/16S - NotebookCheck](https://www.notebookcheck.net/Thinnest-and-lightest-Dell-Pro-Precision-5-14S-and-Pro-Precision-16S-mobile-workstations-debut.1258671.0.html)
- [Crucial LPCAMM2 - crucial.com](https://www.crucial.com/memory/ddr5/ct64g85c2lp5x)
- [Samsung 96GB LPCAMM2 - TechSpot](https://www.techspot.com/news/111331-samsung-readies-lpcamm2-lpddr5x-modules-up-96gb-9600.html)
- [LPCAMM2 vs SO-DIMM LLM Benchmark - TechRxiv](https://www.techrxiv.org/doi/10.36227/techrxiv.176591390.00588709)
