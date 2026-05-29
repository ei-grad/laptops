# Linux Laptop Research: Sustained CPU Performance

Research notes for selecting a Linux-compatible laptop optimized for sustained multi-core workloads (kernel compilation, PySpark data processing).

## Key Criteria

- Weight: ≤1.6 kg
- RAM: 32 GB minimum
- Sustained clocks: ≥2.8 GHz multi-core, no throttling after heat-soak
- Noise: <45 dB(A) under load
- Linux: working out of box or with minor workarounds

## Top Picks (May 2026)

### AMD (reviewed, Linux confirmed)

| Laptop | CPU | Size | Sustained W | CB R23 Multi | Weight | RAM | Linux |
|--------|-----|------|-------------|-------------|--------|-----|-------|
| **TUXEDO InfinityBook Pro 14** | HX 370 | 14" | **65W** | 22,784 | 1.49 kg | 128 GB DDR5 SO-DIMM | Excellent |
| **ASUS ProArt PX13** | HX 370 | 13.3" | **65W** | 23,020 | 1.39 kg | 32 GB LPDDR5X | Fair ¹ |
| **ASUS Zenbook S 16** | AI 9 465 | 16" | 35W | 17,580 | 1.5 kg | 32 GB LPDDR5x-8533 | Good |
| **ThinkPad P14s Gen 6** | HX PRO 370 | 14" | 36W | 18,520 | 1.44 kg | 64 GB LPDDR5X | Good |
| **Framework 13 AMD** | HX 370 | 13.5" | ~33W | — | 1.3 kg | 64 GB DDR5 SO-DIMM | Excellent |

¹ ProArt PX13 needs xanmod kernel; stock Ubuntu has WiFi/backlight/fan issues.

### Promising (strong specs, Linux not yet verified)

| Laptop | CPU | Size | Sustained W | CB R23 Multi | Weight | RAM | Price |
|--------|-----|------|-------------|-------------|--------|-----|-------|
| **ASUS VivoBook S 14 OLED** | HX 370 | 14" | 54W | 21,058 | 1.31 kg | 32 GB LPDDR5X | $1,200 |
| **HP OmniBook Ultra 14** | HX 375 | 14" | 47W | 21,812 | 1.53 kg | 32 GB LPDDR5X | $1,050 |

### Awaiting Reviews

| Laptop | CPU | Size | Comment |
|--------|-----|------|-------------|
| **Framework 13 Pro Intel** | Core Ultra X7/X9 (Panther Lake) | 13.5" | 64 GB LPCAMM2, ~16 hrs battery, open firmware |
| **ASUS ExpertBook P5 G2** | HX 470 | 14" | 45W claimed @ 1.27 kg, 96 GB DDR5 SO-DIMM |
| **ThinkPad P14s Gen 7 AMD** | HX PRO 470 | 14" | 96 GB DDR5 SO-DIMM, 75 Wh, RJ45, ISV workstation |
| **ThinkPad T14 Gen 7 AMD** | AI 7 PRO 450 | 14" | 75 Wh battery, 96 GB DDR5 SO-DIMM, RJ45; not HX-class |
| **ThinkPad T14s Gen 7 AMD** | AI 7 PRO 450 | 14" | 1.09 kg, 64 GB LPDDR5X; AMD variant not yet reviewed |

## Files

- [`laptop-research-summary.md`](laptop-research-summary.md) — Quick reference, comparison tables, decision matrix
- [`cpu-comparison.md`](cpu-comparison.md) — CPU benchmarks (AMD, Intel, Qualcomm)
- [`reviews/`](reviews/) — Individual laptop reviews with YAML frontmatter (17 models)
- [`overviews/`](overviews/) — Platform comparisons, LPCAMM2 guide, [TB4/TB5 and eGPU docks](overviews/usb4-docking-linux.md), excluded models
- [`laptops.jsonl`](laptops.jsonl) — Structured data extracted from review frontmatter

## Key Insights

**Laptop thermal design matters more than CPU SKU.** The same HX 370 chip delivers 22,784 CB R23 multi at 65W (TUXEDO) but only 15,266 sustained at 28W (Zenbook S16).

**AMD dominates sustained multi-core under Linux.** Intel Panther Lake is competitive on efficiency and battery but ~30% behind in throughput. Qualcomm is not viable for Linux (no KVM, Tiger Lake-level performance).

**LPCAMM2 is mostly Intel-only** (as of mid-2026). First AMD LPCAMM2 laptop: ThinkPad P16s Gen 5 (June 2026).

**Laptops with >100W chargers need expensive docks.** Standard 100W USB-C docks disconnect under CPU load due to PD voltage drops. A ThinkPad TB5 Smart Dock (~$550) or similar 140W+ dock is required for stable single-cable operation — factor this into TCO. See [`overviews/usb4-docking-linux.md`](overviews/usb4-docking-linux.md).

## Sources

Data compiled from NotebookCheck, Phoronix, linux-hardware.org, and manufacturer specs. See individual files for full citations.
