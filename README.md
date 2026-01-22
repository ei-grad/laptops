# Linux Laptop Research: Sustained CPU Performance

Research notes for selecting a Linux-compatible laptop optimized for sustained multi-core workloads (kernel compilation, PySpark data processing).

## Key Criteria

- Size: ≤14" (max 15")
- Weight: ≤1.7 kg (max 2.0 kg)
- RAM: 32 GB minimum
- Sustained clocks: ≥3.0 GHz multi-core
- Noise: <45 dB(A) under load
- No thermal throttling after heat-soak

## Top Picks

| Laptop | CPU | Sustained Power | Weight | Noise |
|--------|-----|-----------------|--------|-------|
| **ThinkPad T14 Gen 5/6 AMD** | Ryzen 7 PRO 8840U / AI 7 PRO 360 | 22.5W | 1.46 kg | ~40 dB |
| **HP EliteBook 845 G11** | Ryzen 7 PRO 8840HS | **41W** | 1.5 kg | Quiet |
| **ThinkPad T14s Gen 6 AMD** | Ryzen AI 7 PRO 360 | 25W | 1.3 kg | Low |
| **ASUS ProArt PX13** | Ryzen AI 9 HX 370 | **65W** | 1.39 kg | ~53 dB |

## Files

- `laptop-research-summary.md` — Quick reference and recommendations
- `laptop-detailed-reviews.md` — Full review data per model
- `cpu-comparison.md` — AMD mobile CPU benchmarks (Strix Point, Hawk Point, Strix Halo)
- `reviews/` — Individual laptop files

## Key Insight

**Laptop thermal design matters more than CPU SKU.** A well-cooled Hawk Point (8840HS at 41W) outperforms a thermally-limited Strix Point (HX 370 at 28W) in sustained workloads.

## Sources

Data compiled from NotebookCheck, Phoronix, linux-hardware.org, and manufacturer specs. See individual files for full citations.
