# Linux Laptop Research: Sustained CPU Performance

Research notes for selecting a Linux-compatible laptop optimized for sustained multi-core workloads (kernel compilation, PySpark data processing).

## Key Criteria

- Weight: ≤1.6 kg
- RAM: 32 GB minimum
- Sustained clocks: ≥2.8 GHz multi-core, no throttling after heat-soak
- Noise: <45 dB(A) under load
- Linux: working out of box or with minor workarounds
- Charging/docking: full-power charging over **standard USB-C PD** — SPR (≤100W), or PD 3.1 EPR for more (140/180/240W at 28/36/48V) — not a proprietary out-of-spec profile (e.g. 20V/7.5A) that no dock can supply. Note most docks cap at 140W (180W+ rare: Lenovo 7500 180W, Dell 240W), so a >140W laptop still narrows dock choice. Prefer the charging port to also be USB4/Thunderbolt

## Top Picks (May 2026)

### AMD (reviewed, Linux confirmed)

| Laptop | CPU | Size | Sustained W | CB R23 Multi | Weight | RAM | Linux |
|--------|-----|------|-------------|-------------|--------|-----|-------|
| **TUXEDO InfinityBook Pro 14** | HX 370 | 14" | **65W** | 22,784 | 1.49 kg | 128 GB DDR5 SO-DIMM | Excellent |
| **ASUS ProArt PX13** | HX 370 | 13.3" | **65W** | 23,020 | 1.39 kg | 32 GB LPDDR5X | Fair ¹ |
| **ASUS Zenbook S 16** | AI 9 465 | 16" | 35W | 17,580 | 1.5 kg | 32 GB LPDDR5x-8533 | Good |
| **ThinkPad P14s Gen 6** | HX PRO 370 | 14" | 36W | 18,520 | 1.44 kg | 64 GB LPDDR5X | Good |
| **Framework 13 AMD** | HX 370 | 13.5" | ~33W | — | 1.3 kg | 64 GB DDR5 SO-DIMM | Excellent |
| **HP ZBook Ultra G1a 14** | Max+ PRO 395 | 14" | **66W** | **30,706** | 1.586 kg | 128 GB LPDDR5X | Good ² |
| **ASUS ProArt PX13 GoPro** | Max+ 395 | 13.3" | **70W** | **30,403** | **1.39 kg** | 128 GB LPDDR5X | Fair ³ |

¹ ProArt PX13 (2024 HX 370) needs xanmod kernel; stock Ubuntu has WiFi/backlight/fan issues.
² Ubuntu-certified, CPU work fully supported on kernel 6.14+. **Highest sustained multi-core in the set.** Held back from a top pick mainly by **price (~$4,000) and soldered RAM** (vs the TUXEDO 14's upgradeable 128 GB SO-DIMM), plus a 140W charger needing a dock. Noise (~48 dB peak) is in the same class as other high-power machines here, not a disqualifier. Strix Halo's iGPU/bandwidth is wasted on compilation — see [Strix Halo overview](overviews/strix-halo-linux.md).
³ ProArt PX13 GoPro Edition (2026 Strix Halo): **lightest reviewed Strix Halo (1.39 kg)**, ~$3,000, CB R23 30,403 (10-min) — essentially matches the ZBook in a smaller/cheaper chassis. Linux **fair**: needs a 7.0 mainline kernel, boot params, and manual speaker-firmware extraction; 60 Hz OLED; 200W charger → dock. See [Strix Halo overview](overviews/strix-halo-linux.md).

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
- [`reviews/`](reviews/) — Individual laptop reviews with YAML frontmatter (18 models)
- [`overviews/`](overviews/) — Platform comparisons, LPCAMM2 guide, [Strix Halo on Linux](overviews/strix-halo-linux.md), [TB4/TB5 and eGPU docks](overviews/usb4-docking-linux.md), excluded models
- [`laptops.jsonl`](laptops.jsonl) — Structured data extracted from review frontmatter

## Key Insights

**Laptop thermal design matters more than CPU SKU.** The same HX 370 chip delivers 22,784 CB R23 multi at 65W (TUXEDO) but only 15,266 sustained at 28W (Zenbook S16).

**AMD dominates sustained multi-core under Linux.** Intel Panther Lake is competitive on efficiency and battery but ~30% behind in throughput. Qualcomm is not viable for Linux (no KVM, Tiger Lake-level performance).

**LPCAMM2 is mostly Intel-only** (as of mid-2026). First AMD LPCAMM2 laptop: ThinkPad P16s Gen 5 (June 2026).

**Strix Halo is overkill for compilation.** The Ryzen AI Max+ 395's value is its 40-CU iGPU and 256 GB/s unified memory (local LLMs, GPU compute) — wasted on CPU-bound compilation/PySpark. Two reviewed models meet the weight criterion: the HP ZBook Ultra G1a (1.586 kg, Ubuntu-certified, turnkey Linux) and the lighter/cheaper ASUS ProArt PX13 GoPro (1.39 kg, but Linux needs a 7.0 kernel + manual firmware). The rest are heavy/loud gaming or unvalidated on Linux. See [Strix Halo on Linux](overviews/strix-halo-linux.md).

**>100W charging is often a proprietary profile that no dock can supply.** Laptops like the TUXEDO IB Pro 15 charge at 150W only via a non-standard 20V/7.5A profile (outside USB-PD) — on any dock they fall back to 100W, and if their sole USB4 port is also the sole high-watt port, Thunderbolt docking and full-power charging become mutually exclusive. Standard 100W docks can also disconnect under CPU-load transients (PD sag); a higher-headroom dock holds 100W steadier but never exceeds it. Prefer laptops that charge at full power over standard USB-C PD. See [`overviews/usb4-docking-linux.md`](overviews/usb4-docking-linux.md).

## Sources

Data compiled from NotebookCheck, Phoronix, linux-hardware.org, and manufacturer specs. See individual files for full citations.
