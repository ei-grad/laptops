# ODM Barebones Behind Linux Laptops (2024-2026)

**Date:** 2026-06-02

Most "Linux laptop" brands do not design or build their own machines. They buy a finished
chassis (a *barebone*) from one of three Taiwanese/Chinese ODMs, then customize firmware,
RAM/SSD, keyboard layout, branding, and the shipped OS. Two laptops from different brands
can be the **same hardware** — same motherboard, same cooling, same thermal envelope.

This matters for this project because:

1. **Sustained performance is a property of the barebone**, not the brand. The 90 W cooling
   ceiling of the TUXEDO InfinityBook Pro 15 is the Tongfang GX5 chassis ceiling — XMG EVO 15
   and Schenker Vision 15 hit the same wall.
2. **Out-of-the-box Linux support is a property of the brand.** The same Tongfang chassis
   ships with working fan control and keyboard backlight from TUXEDO (they author the drivers)
   but needs community tooling if bought from a Windows-only reseller.
3. **PD/docking quirks travel with the chassis** — see [USB4 Docking on Linux](./usb4-docking-linux.md).

## The three ODMs

| ODM | Identity | Strength | DMI / board codes |
|-----|----------|----------|-------------------|
| **Tongfang** (清华同方 / Tsinghua Tongfang) | **Uniwill is Tongfang's laptop ODM arm — same company.** "Uniwill barebone" = "Tongfang barebone". | Thin-and-light ultrabooks (GX series) + gaming (GM / X6AR series) | Current: `GX4`/`GX5`, board names `X4SP4NAL`, `X5..4NAx`, `X6AR5..`. Legacy ultrabooks used `PHxxxx` codes |
| **Clevo** | Separate, competing ODM | Mainstream-performance and desktop-replacement chassis; some thin-and-lights (NS/V series) | `V540TU1`, `V560TU`, `NS50/NS70`, `X370SNW`, `X580` |
| **Quanta / Compal / Pegatron** | Mega-ODMs for Lenovo/HP/Dell/ASUS | Not sold as boutique barebones | (not in scope) |

**Key clarification:** TUXEDO and XMG/Schenker buy from *both* Tongfang/Uniwill and Clevo
depending on the line. The `tuxedo-drivers` kernel package contains both `uniwill-*` and
`clevo-*` modules for this reason — driver coverage spans both ODMs, but a given model uses
only one. The legacy `PHxxxx` Uniwill codes (e.g. `PH4PRX1`) belong to the **pre-2024**
ultrabook generation; current ultrabooks moved to the `GX4`/`GX5` naming.
Source: [Phoronix — Uniwill driver](https://www.phoronix.com/news/Uniwill-Driver-cTGP-Linux-7.0),
[Gentoo wiki — TongFang X4SP4NAL](https://wiki.gentoo.org/wiki/TongFang_X4SP4NAL).

## Tongfang / Uniwill barebones

### Thin-and-light, iGPU (in this project's scope)

| Barebone | Size | Platform | RAM | Weight | Sustained / cooling | In project |
|----------|------|----------|-----|--------|---------------------|------------|
| **GX4** (`X4SP4NAL`) | 14" | AMD Strix Point (Ryzen AI 9 HX 370 / AI 9 365 / AI 7 350), iGPU | 2× DDR5-5600 SO-DIMM, 128 GB | ~1.49 kg | ~50 W sustained / 65 W burst, 80 Wh | [IB Pro 14](../reviews/tuxedo-infinitybook-pro-14.md) |
| **GX5** | 15.3" | AMD Strix Point **and** Intel Arrow Lake-H (Core Ultra 7 255H) | 2× DDR5-5600 SO-DIMM, 128 GB (Intel: CSO-DIMM up to 6400) | ~1.75 kg | **90 W** Overboost, 99 Wh | [IB Pro 15](../reviews/tuxedo-infinitybook-pro-15.md) |
| **GX4/GX5 Gen9** (`GXxMRXx`, `GXxHRXx`) | 14"/15.3" | AMD Hawk Point (R7 8845HS) / Intel Meteor Lake (155H) | DDR5 SO-DIMM, 96 GB | ~1.6 kg | Prior gen | — |
| **Pulse 14** (`PULSE1403/1404`) | 14" | AMD Hawk/Strix | **Soldered LPDDR5X-6400, 32 GB fixed** | ~1.4 kg | Not upgradeable | — |

GX4 vs GX5 is the most important distinction for this project: **GX4 is the 14" (≤1.6 kg),
GX5 is the 15.3" (1.75 kg, exceeds the weight criterion but has the 90 W ceiling and 99 Wh
battery).** Same CPU options, materially different cooling envelope.

### Performance / DTR, dGPU (out of scope — >2 kg)

Listed for mapping completeness only:

| Barebone | Size | Platform | Rebrands |
|----------|------|----------|----------|
| **GM6 / GM7** (`GM6IXxB`, `GM7IXxN`) | 16"/17" | Intel HX + RTX 40/50 | TUXEDO Stellaris 16 Gen6, XMG NEO 16 (E24), Maingear Vector Pro, Eluktronics MAX-17 |
| **X6AR5 / X6FR5** | 16" | AMD Fire Range (R9 9955HX) / Intel ARL-HX (Ultra 9 275HX) + RTX 5070 Ti–5090 | TUXEDO Stellaris 16 Gen7, XMG NEO 16 A25 |
| **CORE M25 board** | 15.3"/16" | AMD Strix + RTX 5060/5070 | XMG CORE 15/16 M25 |

## Clevo barebones

### Thin-and-light / mainstream (potentially in scope)

| Barebone | Size | Platform | RAM | Weight | PD-in | In project |
|----------|------|----------|-----|--------|-------|------------|
| **V540TU1** | 14" | Intel Arrow Lake-H, Arc iGPU | 2× DDR5-5600 SO-DIMM, up to 128 GB | ~1.5 kg | USB-C PD (TB4) | — |
| **V560TU / V560TU1** | 16" | Intel Core Ultra 7 255H (ARL-H), Arc iGPU | 2× DDR5-5600 SO-DIMM, 96 GB | 1.8 kg | TB4 PD-in (90 W adapter) | [System76 Darter Pro](../reviews/system76-darter-pro.md) (darp11) |
| **V560EU** | 16" | AMD Ryzen 5 240 / 7 260, Radeon 760M/780M | 2× DDR5-5600 SO-DIMM, 96 GB | 1.9 kg | USB4 PD-in (90 W) | — |
| **NS50 / NS70** | 15.6"/17.3" | Intel 13th-gen (RPL), Iris Xe | DDR5-4800, 64 GB | ~2.0–2.25 kg | USB-C PD (≥87 W) | — |

**System76 Darter Pro (darp11) = Clevo V560TU** (motherboard PN `6-77-V560TU00-D02-4F`).
Source: [System76 tech-docs darp11](https://tech-docs.system76.com/models/darp11/README.html).
No independent NotebookCheck sustained-power review exists for the current V540/V560 boards —
PL1/PL2 numbers are unconfirmed; treat as "est." if added to a review.

### Performance / DTR, dGPU (out of scope — barrel-charged, >2 kg)

`X370SNW` (17.3", i9-14900HX + RTX 4090; Sager NP9371W, Eurocom), `X580` (18", ARL-HX + RTX 50,
192 GB DDR5, dual TB5 — CES 2025 leak). Barrel-only chargers (230–420 W), no USB-C PD at full load.

## Brand → ODM mapping

| Brand | Region | ODM(s) | Ships Linux OOB | Notes |
|-------|--------|--------|-----------------|-------|
| **TUXEDO** | DE | Tongfang/Uniwill (ultrabooks + most gaming) + some Clevo | **Yes** (Ubuntu / TUXEDO OS) | Authors `tuxedo-drivers` + Control Center |
| **System76** | US | Clevo (Darter, Gazelle) + others | **Yes** (Pop!_OS) | System76 Open Firmware (coreboot) on many models |
| **NovaCustom** | NL | Clevo (V54/V56, NS70) | **Yes** | Dasharo coreboot, Qubes-certified |
| **Laptop with Linux** | NL | Tongfang (GX4/GX5) + Clevo | **Yes** (distro choice) | Sells the raw barebones directly |
| **XMG / Schenker** (bestware) | DE | Tongfang/Uniwill (EVO, CORE, NEO) | No | Same HW as TUXEDO → `tuxedo-drivers` usually work |
| **Eluktronics** | US | Tongfang/Uniwill | No | Community Linux |
| **Sager** | US | Clevo | No | — |
| **Eurocom** | CA | Clevo | Partial | — |
| **Metabox** | AU | Clevo | No | — |
| **Aftershock** | SG/AU | Tongfang | No | — |
| **Monster** (Abra/Tulpar) | TR | Tongfang | No | — |
| **Mechrevo** | CN | Tongfang | No | — |
| **PCSpecialist / Mifcom** | UK / DE | Both | No | Mixed lineup |

### Confirmed "same chassis" twins

- TUXEDO InfinityBook Pro 14 Gen10 ≡ XMG EVO 14 E25 ≡ Schenker Vision 14 ≡ **Tongfang GX4 / X4SP4NAL**
- TUXEDO InfinityBook Pro 15 Gen10 ≡ XMG EVO 15 (E25 AMD / M25 Intel) ≡ Schenker Vision 15 ≡ **Tongfang GX5**
- System76 Darter Pro (darp11) ≡ **Clevo V560TU**
- TUXEDO Stellaris 16 Gen7 ≡ XMG NEO 16 A25 ≡ **Tongfang X6AR5**

## Linux support: it depends on the brand, not just the chassis

The same barebone is a very different Linux experience depending on who sold it:

- **`tuxedo-drivers`** (formerly `tuxedo-keyboard`) is the DKMS package providing keyboard
  backlight, Fn keys, fan/performance profiles, and charging thresholds. It bundles
  `uniwill-*` (Tongfang) and `clevo-*` modules. On **TUXEDO-branded** units everything is
  pre-patched in TUXEDO OS; on the **same chassis from XMG/Schenker/Mechrevo** the drivers
  usually load but are not guaranteed OOB, and a UEFI "Manufacturer == TUXEDO" check may need
  bypassing. Current GX4/GX5 and Stellaris boards use newer `tuxedo_nb02`/`tuxedo_nb05` EC
  paths rather than the legacy WMI interface.
- **Open firmware** is a System76 / NovaCustom differentiator: System76 Open Firmware
  (coreboot + EDK2) on Darter Pro etc., and **Dasharo coreboot** on NovaCustom Clevo models
  (optional ME disable, Heads, fwupd). No Tongfang ultrabook ships coreboot.
- **Per-chassis caveats** (Tongfang GX4 / X4SP4NAL): keyboard function keys need a recent
  kernel, and the **Motorcomm YT6801 2.5GbE controller has no in-kernel driver** (out-of-tree
  module needed) — pre-handled on TUXEDO OS.
  Source: [Gentoo wiki — TongFang X4SP4NAL](https://wiki.gentoo.org/wiki/TongFang_X4SP4NAL).
- **Wi-Fi**: GX4/GX5 ship Intel AX210 (Wi-Fi 6E, in-kernel, no Wi-Fi 7); some configs use
  MediaTek MT7922/MT7925 (kernel ≥6.7). M.2 slot is replaceable.
- **Suspend**: AMD Strix Point and Intel Core Ultra thin-lights use s2idle (modern standby);
  generally works on recent kernels, the usual source of AMD s2idle wake/power quirks.

## PD / charging

- **Tongfang GX4/GX5 and thin-light Clevo (V5xx, NS5x/NS7x) charge over USB-C PD-in.** This is
  friendlier to single-cable USB4/PD-dock workflows than barrel-jack workstations. **But** the
  GX4/GX5 bundle 140–150 W USB-C bricks for the HX 370 — exceeding the 100 W ceiling of cheap
  docks, so under sustained CPU load a 100 W dock will throttle or disconnect. This matches the
  PD-sensitivity already documented for the InfinityBook Pro series.
- **dGPU/DTR barebones (GM/X6AR5, Clevo X370/X580) are barrel-charged** (230–420 W). USB-C PD-in,
  where present, is capped (~140 W) and cannot sustain full GPU power — not single-cable laptops.
- Whether the GX4/GX5 EC tolerates sub-spec PD sources gracefully (charge-but-throttle vs refuse)
  under CPU load is **unverified** — flagged for hands-on testing.

See [USB4 Docking on Linux](./usb4-docking-linux.md) for tested docks and recommendations.

## Takeaways

- **Buy the barebone from a Linux vendor.** TUXEDO, System76, NovaCustom, and Laptop with Linux
  ship working Linux + firmware; the identical XMG/Schenker/Eluktronics chassis is a Windows
  product you make work yourself.
- **Sustained performance follows the chassis code, not the brand.** Compare GX4 vs GX5 (or
  V540 vs V560), not "TUXEDO vs XMG".
- **GX5's 90 W ceiling and 99 Wh battery** are the reason it was chosen despite the 1.77 kg
  weight exclusion — see [excluded models](./excluded-models.md).

## Sources

- [Phoronix — Uniwill driver upstreaming](https://www.phoronix.com/news/Uniwill-Driver-cTGP-Linux-7.0)
- [Gentoo wiki — TongFang X4SP4NAL (= XMG EVO 14 E25 = IB Pro 14 Gen10)](https://wiki.gentoo.org/wiki/TongFang_X4SP4NAL)
- [Laptop with Linux — TongFang GX4](https://laptopwithlinux.com/product/tongfang-gx4/) / [GX5](https://laptopwithlinux.com/product/tongfang-gx5/) / [Clevo V560](https://laptopwithlinux.com/product/clevo-v560/) / [V560EU](https://laptopwithlinux.com/product/clevo-v560eu/)
- [System76 tech-docs — Darter Pro darp11 (= Clevo V560TU)](https://tech-docs.system76.com/models/darp11/README.html)
- [NotebookCheck — TUXEDO InfinityBook Pro 14 Gen10 review](https://www.notebookcheck.net/Tuxedo-Infinity-Book-Pro-14-Gen10-Review-Linux-ultrabook-with-AMD-Zen-5-128-GB-RAM.1095463.0.html)
- [NotebookCheck — XMG EVO 15 lineup (AMD Ryzen AI + Intel Core Ultra 200H)](https://www.notebookcheck.net/XMG-updates-the-EVO-15-ultrabook-lineup-with-AMD-Ryzen-AI-and-Intel-Core-Ultra-200H-processors.1097952.0.html)
- [NotebookCheck — TUXEDO Stellaris 16 (RTX 5090 / 128 GB)](https://www.notebookcheck.net/Tuxedo-Stellaris-16-Powerful-workstation-notebook-with-optional-GeForce-RTX-5090-and-up-to-128-GB-RAM.1026634.0.html)
- [NovaCustom — V56 (Clevo, Dasharo coreboot)](https://novacustom.com/product/v56-series/)
- [bestware — XMG/SCHENKER series differences](https://help.bestware.com/hc/en-gb/articles/30750888623901-What-are-the-differences-between-the-various-XMG-and-SCHENKER-laptop-series)
- [tuxedo-drivers (board DMI tables, uniwill/clevo modules)](https://github.com/tuxedocomputers/tuxedo-drivers)
- [NotebookTalk — Uniwill (TongFang) subforum](https://notebooktalk.net/forum/138-uniwill-tongfang/)
