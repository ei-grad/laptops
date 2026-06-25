---
model: TUXEDO InfinityBook Pro 15
slug: tuxedo-infinitybook-pro-15
manufacturer: TUXEDO
status: excluded
form_factor: clamshell
weight_kg: 1.77
battery_wh: 99.0
price_usd: 1850
display:
  aspect_ratio: '16:10'
  panel: IPS
  refresh_hz: 300
  resolution: 2560x1600
  size_in: 15.3
  brightness_nits: 545
variants:
- benchmarks: {}
  cpu:
    arch: Strix Point
    boost_ghz: 5.1
    cores: 12
    name: AMD Ryzen AI 9 HX 370
    threads: 24
  gpu:
    compute_units: 16
    name: Radeon 890M
    type: integrated
  power:
    pl1_w: 65.0
    pl2_w: 90.0
  ram_gb: 128
  ram_type: DDR5 SO-DIMM
  ram_upgradeable: true
  year: 2025
noise:
  balanced_dba: 32.9
  max_dba: 47.9
  performance_dba: 36.3
linux:
  issues: []
  kernel_min: '6.10'
  notes:
  - Ships with Ubuntu 24.04 or TUXEDO OS
  - TUXEDO Control Center for fan profiles
  status: excellent
sources:
- https://www.tuxedocomputers.com/en/TUXEDO-InfinityBook-Pro-15-Gen10-AMD.tuxedo
- https://www.notebookcheck.net/Tuxedo-InfinityBook-Pro-15-Gen-10-Premium-Linux-laptop-with-Ryzen-AI-9-240-Hz-display-and-99-Wh-battery.1071854.0.html
- https://www.notebookcheck.net/XMG-Evo-15-M25-laptop-review-A-good-Windows-alternative-to-the-MacBook-Air-15.1211981.0.html
---
# TUXEDO InfinityBook Pro 15 Gen10

**Excluded: weight (1.77 kg) exceeds the ≤1.6 kg criterion.**

## Overview

Same Tongfang **GX5** barebone as XMG EVO 15 (E25 AMD / M25 Intel) / Schenker Vision 15. Ships with TUXEDO OS (Ubuntu-based) or Ubuntu 24.04. 15.3" sibling of the [InfinityBook Pro 14](./tuxedo-infinitybook-pro-14.md) (Tongfang GX4). See [ODM barebones overview](../overviews/odm-barebones-linux.md) for the full brand↔chassis mapping.

## Sustained Performance

Chassis cooling rated for **90W** at full fan speed (confirmed on Intel variant in XMG EVO 15 M25 NotebookCheck review). The AMD variant at 90W sustained has not been independently benchmarked — the 65W PL1 in frontmatter is a conservative estimate matching the reviewed 14" sibling with the same CPU.

The 15" chassis should score higher than the 14" at 90W — estimated CB R23 multi ~24,000-25,000 based on the 14" result of 22,784 at 65W. Frontmatter benchmarks left empty pending independent review.

## Key Specs

- 2x SO-DIMM DDR5-5600 — upgradeable to **128 GB**
- 99 Wh battery — largest in the lineup
- 15.3" 2.5K IPS display, 545 nits peak, 300 Hz (AMD) / 240 Hz (Intel)
- Wi-Fi 6E (AMD RZ616), Bluetooth 5.2
- 1x USB4 (rear, 40 Gbit/s) — DP 2.1; the **only** Thunderbolt/USB4 port. PD-in 60–100W over standard PD, plus a proprietary **20V/7.5A = 150W** profile (TUXEDO charger only)
- 1x USB-C 3.2 Gen2 (left, 10 Gbit/s) — DP 1.4a, PD-in up to 20V/5A = 100W; **not** USB4/Thunderbolt
- From ~€1,714 (base HX 370 config); fully configured (64 GB Crucial, 2 TB Samsung 990 PRO, custom branding): €2,717 per unit

## Docking and Power Delivery

**The 150W charging is a proprietary, non-standard profile.** The bundled charger is **20V/7.5A = 150W over USB-C** (TUXEDO spec). 20V/7.5A is *outside* the USB-PD standard: USB PD 3.0 caps at 20V/5A = 100W, and PD 3.1 EPR exceeds 100W only at higher voltages (28/36/48V), never at 20V/7.5A. No dock or third-party charger — not even a 140W/180W PD 3.1 TB5 dock — can supply this profile.

**Consequences:**

- **Any dock caps the laptop at 100W.** A standard PD source negotiates the highest profile both sides support; the highest *standard* one this laptop accepts is 20V/5A = 100W. A 140W or 180W PD 3.1 dock does **not** deliver 150W here — its extra headroom only helps it hold 100W without voltage sag; it does not raise the ceiling.
- **PD sensitivity → the dock resets under load (confirmed by users).** Multiple first-hand r/tuxedocomputers reports describe the laptop dropping the *entire* dock (monitors + USB + Ethernet at once) under CPU-load transients once total draw nears the dock's PD ceiling — the InfinityBook is sensitive to voltage sag. Seen on Kensington SD5700T, Dell WD22TB4, Belkin/i-tec 96W and the TUXEDO Triple Dock. Confirmed workarounds: plug the original charger into the *second* USB-C port (dock on rear + charger on side), or cap TDP in TUXEDO Control Center below the dock's rating.
- **100W docked ≠ full performance on the 15.** TUXEDO support told an IBP 15 Gen10 buyer the device "will not run with full performance when there is only 100W power provision," and could not name a fully-compatible or 150W-capable dock. (A TUXEDO rep elsewhere called the 100W↔150W gap "negligible due to CPU power limits / diminishing returns" — so it's the top of the 90W envelope you lose, not a cliff — but it is not full power, and the battery can discharge under max load.) Contrast the **IBP 14 Gen10** (65W ceiling), where TUXEDO confirms 100W = full performance and a user runs it single-cable, fully stable under sustained CPU+GPU load on a Lenovo ThinkPad TB5 Smart Dock 7500. The 15's 90W ceiling is exactly what 100W can't fully feed.
- **Thunderbolt and 150W are mutually exclusive — even with two cables.** The rear USB4 port is the *only* Thunderbolt/USB4 port **and** the only port that accepts 150W. The left USB-C 3.2 Gen2 port tops out at 100W and is not USB4/TB (DP 1.4a, data only). So you either put the 150W charger on the rear port (no port left for a TB dock — the side port isn't TB) **or** put a TB dock on the rear port (power capped at 100W). No configuration gives both.

**Net:** single-cable docked operation is capped at 100W; full 150W requires the bundled charger on the rear port with no Thunderbolt dock attached. See [USB4 Docking on Linux](../overviews/usb4-docking-linux.md). **This is exactly the proprietary-charger trap to avoid in future purchases — prefer laptops that charge at full power over standard USB-C PD (SPR ≤100W, or PD 3.1 EPR at 140/180/240W via 28/36/48V), not a 20V/7.5A out-of-spec hack.** A standards-compliant 150W design would step up to 28V+ EPR; TUXEDO instead kept 20V and raised current past the connector's 5A limit, which is why no dock can match it.

**Community reports (r/tuxedocomputers):** [port allocation / 150W-vs-dock on the IBP 15](https://www.reddit.com/r/tuxedocomputers/comments/1ph88dq/usbc_port_allocation_on_the_ibp_15_amd_gen10/) · [WD22TB4 resets under load, fixed with a 2nd charger; later stable single-cable on a Lenovo 7500 (IBP 14)](https://www.reddit.com/r/tuxedocomputers/comments/1poqpe3/random_dock_resets_on_infinitybook_pro_14_amd_gen/) · [PD clarification: 150W PSU but 100W ports; 14 reaches full perf on 100W](https://www.reddit.com/r/tuxedocomputers/comments/1tnasr3/infinitybook_pro_14_gen_10_power_delivery/) · [voltage-sag disconnects near the dock PD ceiling](https://www.reddit.com/r/tuxedocomputers/comments/1no9pms/ibp_14_gen_10_disconnects_randomly_with_docking/)

## Why Excluded (and Why Bought Anyway)

Exceeds the 1.6 kg weight criterion (1.77 kg). Chosen as a work laptop due to:
- 99 Wh battery (vs 80 Wh on the 14")
- 90W cooling headroom (vs 65W on the 14")
- 15.3" screen for daily work
- Native Linux support, Russian keyboard layout, B2B ordering with custom branding

## Sources

- [TUXEDO product page](https://www.tuxedocomputers.com/en/TUXEDO-InfinityBook-Pro-15-Gen10-AMD.tuxedo)
- [NotebookCheck announcement](https://www.notebookcheck.net/Tuxedo-InfinityBook-Pro-15-Gen-10-Premium-Linux-laptop-with-Ryzen-AI-9-240-Hz-display-and-99-Wh-battery.1071854.0.html)
- [NotebookCheck XMG EVO 15 M25 review](https://www.notebookcheck.net/XMG-Evo-15-M25-laptop-review-A-good-Windows-alternative-to-the-MacBook-Air-15.1211981.0.html) (same Tongfang GX5 chassis)
