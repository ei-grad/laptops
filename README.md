# Linux Laptop Research: Sustained CPU Performance

Research notes for selecting a Linux-compatible laptop optimized for sustained multi-core workloads (kernel compilation, PySpark data processing).

## Key Criteria

- Size: ≤14" (max 15")
- Weight: ≤1.7 kg (max 2.0 kg)
- RAM: 32 GB minimum
- Sustained clocks: ≥3.0 GHz multi-core
- Noise: <45 dB(A) under load
- No thermal throttling after heat-soak

## Top Picks (May 2026)

| Laptop | CPU | Sustained Power | CB R23 Multi | Weight | Noise | Linux |
|--------|-----|-----------------|-------------|--------|-------|-------|
| **TUXEDO InfinityBook Pro 14** | HX 370 | **65W** | 22,784 | 1.49 kg | 34 dB | Excellent |
| **ASUS ProArt PX13** | HX 370 | **65W** | 23,020 | 1.39 kg | 43 dB | Fair |
| **HP OmniBook Ultra 14** | HX 375 | 47W | 21,812 | 1.53 kg | ~40 dB | Unknown |
| **HP EliteBook 845 G11** | 8840HS | 41W | — | 1.5 kg | Quiet | Good |
| **Framework 13 Pro AMD** | HX 370 | ~33W | — | 1.4 kg | ~41 dB | Excellent |
| **ASUS Zenbook S16 (2026)** | AI 9 465 | 35W | 17,580 | 1.5 kg | 36 dB | Good |

## Files

- `laptop-research-summary.md` — Quick reference and recommendations
- `laptop-detailed-reviews.md` — Full review data per model
- `cpu-comparison.md` — CPU benchmarks (AMD, Intel, Qualcomm)
- `reviews/` — Individual laptop review files (with YAML frontmatter)
- `overviews/` — Thematic overview articles
- `laptops.jsonl` — Structured data extracted from review frontmatter

## Key Insight

**Laptop thermal design matters more than CPU SKU.** A well-cooled HX 370 at 65W (TUXEDO) delivers 22,784 CB R23 multi, while the same chip at 28W (Zenbook S16) delivers only 15,266 sustained.

## Sources

Data compiled from NotebookCheck, Phoronix, linux-hardware.org, and manufacturer specs. See individual files for full citations.
