# Linux Laptop Research: Sustained CPU Performance

Research notes for selecting a Linux-compatible laptop optimized for sustained multi-core workloads (kernel compilation, PySpark data processing).

## Key Criteria

- Size: ≤14" (max 15")
- Weight: ≤1.7 kg (max 2.0 kg)
- RAM: 32 GB minimum
- Sustained clocks: ≥2.8 GHz multi-core, no throttling after heat-soak
- Noise: <45 dB(A) under load
- Linux: working out of box or with minor workarounds

## Top Picks (May 2026)

### AMD (best for sustained multi-core)

| Laptop | CPU | Sustained W | CB R23 Multi | Weight | RAM | Linux |
|--------|-----|-------------|-------------|--------|-----|-------|
| **TUXEDO InfinityBook Pro 14** | HX 370 | **65W** | 22,784 | 1.49 kg | 128 GB SO-DIMM | Excellent |
| **ASUS ProArt PX13** | HX 370 | **65W** | 23,020 | 1.39 kg | 32 GB soldered | Fair |
| **HP OmniBook Ultra 14** | HX 375 | 47W | 21,812 | 1.53 kg | 32 GB soldered | Unknown |
| **Framework 13 Pro AMD** | HX 370 | ~33W | — | 1.4 kg | 64 GB SO-DIMM | Excellent |
| **ASUS Zenbook S16** | AI 9 465 | 35W | 17,580 | 1.5 kg | 32 GB soldered | Good |

### Intel (best battery life + LPCAMM2)

| Laptop | CPU | Weight | RAM | Battery | Linux |
|--------|-----|--------|-----|---------|-------|
| **Framework 13 Pro Intel** | Core Ultra X7/X9 (Panther Lake) | 1.4 kg | 64 GB LPCAMM2 | ~16 hrs | Excellent |

~30% behind AMD HX 370 in sustained multi-core, but LPCAMM2 (+52% bandwidth), much better battery life, Ubuntu certified.

### Awaiting Reviews

| Laptop | CPU | Key Feature |
|--------|-----|-------------|
| **ASUS ExpertBook P5 G2** | HX 470 | 45W claimed @ 1.27 kg, 96 GB SO-DIMM |
| **ThinkPad T14 Gen 7 AMD** | HX PRO 470 | 75 Wh battery, SO-DIMM, RJ45 |

## Files

- [`laptop-research-summary.md`](laptop-research-summary.md) — Quick reference, comparison tables, decision matrix
- [`cpu-comparison.md`](cpu-comparison.md) — CPU benchmarks (AMD, Intel, Qualcomm)
- [`reviews/`](reviews/) — Individual laptop reviews with YAML frontmatter (16 models)
- [`overviews/`](overviews/) — Platform comparisons, LPCAMM2 guide, excluded models
- [`laptops.jsonl`](laptops.jsonl) — Structured data extracted from review frontmatter

## Key Insights

**Laptop thermal design matters more than CPU SKU.** The same HX 370 chip delivers 22,784 CB R23 multi at 65W (TUXEDO) but only 15,266 sustained at 28W (Zenbook S16).

**AMD dominates sustained multi-core under Linux.** Intel Panther Lake is competitive on efficiency and battery but ~30% behind in throughput. Qualcomm is not viable for Linux (no KVM, Tiger Lake-level performance).

**LPCAMM2 is mostly Intel-only** (as of mid-2026). First AMD LPCAMM2 laptop: ThinkPad P16s Gen 5 (June 2026).

## Sources

Data compiled from NotebookCheck, Phoronix, linux-hardware.org, and manufacturer specs. See individual files for full citations.
