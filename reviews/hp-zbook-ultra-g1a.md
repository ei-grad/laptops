---
model: HP ZBook Ultra G1a 14
slug: hp-zbook-ultra-g1a
manufacturer: HP
status: available
form_factor: clamshell
weight_kg: 1.586
battery_wh: 74.5
price_usd: 4000
display:
  aspect_ratio: '16:10'
  panel: OLED
  refresh_hz: 120
  resolution: 2880x1800
  size_in: 14.0
  touch: true
  brightness_nits: 389
variants:
- benchmarks:
    cinebench_r23_multi: 30706
    cinebench_r23_multi_sustained: 29203
    cinebench_2024_multi: 1643
    geekbench6_multi: 16855
    geekbench6_single: 2756
  cpu:
    arch: Strix Halo
    boost_ghz: 5.1
    cores: 16
    name: AMD Ryzen AI Max+ PRO 395
    threads: 32
  gpu:
    compute_units: 40
    name: Radeon 8060S
    type: integrated
  power:
    pl1_w: 66.0
    pl2_w: 81.0
  ram_gb: 128
  ram_type: LPDDR5X-8533
  sku: AI Max+ PRO 395
  year: 2025
noise:
  max_dba: 48.0
linux:
  status: good
  kernel_min: '6.14'
  notes:
  - Ubuntu 24.04 LTS certified (AI Max+ PRO 395 and AI Max 385 configs)
  - Works out of box on kernel 6.14+ / Mesa 25.0+ (amdgpu drives Radeon 8060S / gfx1151)
  - LVFS/fwupd firmware updates work
  - Wi-Fi 7 MediaTek MT7925 (mt7925e) well supported
  issues:
  - IR webcam needs AMD ISP4 driver, not upstream until ~kernel 6.18
  - NPU (XDNA2) amdxdna driver immature, firmware/toolchain mismatch
  - ROCm fragile on gfx1151 (works on Ubuntu 24.04 HWE, breaks on some upstream kernels)
  - amd-smi reports no power/temp/clock/fan telemetry on gfx1151
sources:
- https://www.notebookcheck.net/HP-ZBook-Ultra-G1a-14-review-Powerful-MacBook-Pro-alternative-for-work-and-game.994758.0.html
- https://www.notebookcheck.net/HP-ZBook-Ultra-G1a-14.1068565.0.html
- https://www.phoronix.com/review/hp-zbook-ultra-g1a/2
- https://ubuntu.com/certified/202411-36033/24.04%20LTS
- https://ubuntu.com/certified/202411-36043/24.04%20LTS
- https://linux-hardware.org/?probe=025a994391
- https://www.hp.com/us-en/workstations/zbook-ultra.html
- https://hothardware.com/reviews/hp-zbook-ultra-g1a-128gb-review
---
# HP ZBook Ultra G1a 14

The only Strix Halo laptop that meets this project's ≤1.6 kg weight criterion, and the
highest sustained multi-core score in the entire comparison set. See the
[Strix Halo overview](../overviews/strix-halo-linux.md) for the full platform context.

## Why It Matters Here

HP's 14" mobile workstation pairs the flagship **Ryzen AI Max+ PRO 395** (16C/32T Zen 5)
with a 256-bit LPDDR5X-8533 memory subsystem (~256 GB/s) and up to 128 GB of unified
RAM. At a measured **66 W PL1 / 81 W PL2**, the NotebookCheck review unit holds Cinebench
R23 multi around **29,200 sustained** (30,706 peak) with minimal throttling — roughly
**+30% over the best HX 370 implementation** in this set ([TUXEDO InfinityBook Pro 14](./tuxedo-infinitybook-pro-14.md)
at 22,784). For sustained kernel compilation and PySpark, nothing else here is close.

## Linux Status — Good (Ubuntu Certified)

- **Officially Ubuntu 24.04 LTS certified** in both AI Max+ PRO 395 and AI Max 385 configs.
- Works out of box on **kernel 6.14+ with Mesa 25.0+**; Phoronix called it an excellent
  Linux workstation. LVFS/fwupd firmware updates work.
- Wi-Fi 7 is MediaTek **MT7925** (mt7925e) — well supported on recent kernels.
- **Only consistently confirmed gap: the IR webcam**, which needs the AMD ISP4 driver
  (upstreaming targeted around kernel 6.18 / late 2026).
- **GPU compute / NPU caveats** (not relevant to CPU compile workloads): the in-tree
  `amdxdna` NPU driver is immature with firmware/toolchain mismatches; ROCm on gfx1151 is
  fragile (works on the Ubuntu 24.04 HWE stack, breaks on some upstream kernels); `amd-smi`
  reports no power/temp/clock/fan telemetry. CPU multi-core work is unaffected by these.
- One unverified HP-forum report of high APU PPT + broken suspend on Linux exists, but
  Phoronix did not reproduce it — treat as config/kernel-specific, not a platform defect.

## Specifications

- **CPU:** AMD Ryzen AI Max+ PRO 395 (16C/32T, up to 5.1 GHz, Zen 5). Also offered as
  AI Max PRO 390 (12C) and AI Max 385 (8C, Radeon 8050S 32 CU).
- **iGPU:** Radeon 8060S (40 CU, RDNA 3.5) — no discrete GPU.
- **RAM:** 32 / 64 / 128 GB LPDDR5X-8533, **soldered**, 256-bit / ~256 GB/s. Not upgradeable.
- **Display:** 14.0" 16:10, 2880×1800 Samsung OLED, 120 Hz, 10-point touch, ~389 nits.
  A 2K IPS matte option is also offered.
- **Battery:** 74.5 Wh.
- **Weight:** 1.586 kg (just under the 1.6 kg ceiling). 140 W USB-C PSU adds ~503 g.
- **Ports:** 2× USB4 40 Gbps (Thunderbolt), 2× USB 3.2 Gen2, HDMI, 3.5 mm. Wi-Fi 7 + BT 5.4.

## Noise

Fans off at idle. HotHardware measured **~47–49 dBA under load at ~12" (≈30 cm)** and HP-forum
owners report **~44–45 dB in normal use**. Note the methodology gap: HotHardware's 12" distance
reads ~3–4 dB lower than the 15 cm NotebookCheck/TUXEDO standard, so the peak is comparable to
the [TUXEDO InfinityBook Pro 15](./tuxedo-infinitybook-pro-15.md) (47.9 dB max) rather than
clearly worse. It is **not quiet under full fan**, but for a 66 W sustained CPU load it is in
the same acoustic class as the rest of the high-power field — noise is not the reason this
laptop falls short of "recommended." Some owners report firmware-level random fan spikes.

## Docking and Power Delivery

Ships with a **140 W USB-C charger**. Per project policy this is a hidden cost: standard
100 W USB-C docks will drop the laptop under sustained CPU load due to PD voltage drops.
Stable single-cable docking needs a ≥140 W PD dock (e.g. a Thunderbolt 5 dock, ~$550).
See [USB4 Docking on Linux](../overviews/usb4-docking-linux.md).

## Trade-offs

- **Price** — ~$4,000 USD as reviewed (395 / 128 GB / 2 TB); a 64 GB / 1 TB config is
  closer to ~£2,100. Far more expensive than the HX 370 field. *(Primary holdback.)*
- **Soldered RAM** — capacity is a buy-time decision (up to 128 GB), no upgrades later.
  The [TUXEDO InfinityBook Pro 14](./tuxedo-infinitybook-pro-14.md) offers 128 GB on
  upgradeable DDR5 SO-DIMM for a fraction of the price. *(Primary holdback.)*
- **140 W charger** → dock cost (see Docking section).
- **Overkill for CPU work** — the 40-CU iGPU and 256 GB/s memory bandwidth are unused by
  compilation/PySpark; you pay for capability this project doesn't exercise.
- Noise (~48 dB peak) is comparable to other high-power machines here, not a disqualifier.

Net: the performance and Linux-support king of this set, held back from a "recommended"
rating mainly by **price and soldered memory**, not acoustics. Best fit when raw sustained
throughput and large unified RAM outweigh cost.

## Sources

- [NotebookCheck full review (Windows benchmarks)](https://www.notebookcheck.net/HP-ZBook-Ultra-G1a-14-review-Powerful-MacBook-Pro-alternative-for-work-and-game.994758.0.html)
- [NotebookCheck specs](https://www.notebookcheck.net/HP-ZBook-Ultra-G1a-14.1068565.0.html)
- [Phoronix Linux review](https://www.phoronix.com/review/hp-zbook-ultra-g1a/2)
- [Ubuntu certification — AI Max+ PRO 395](https://ubuntu.com/certified/202411-36033/24.04%20LTS), [AI Max 385](https://ubuntu.com/certified/202411-36043/24.04%20LTS)
- [linux-hardware.org probe](https://linux-hardware.org/?probe=025a994391)
- [HP ZBook Ultra product page](https://www.hp.com/us-en/workstations/zbook-ultra.html)
- [HotHardware review (fan noise)](https://hothardware.com/reviews/hp-zbook-ultra-g1a-128gb-review)
