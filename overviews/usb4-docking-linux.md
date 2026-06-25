# Thunderbolt 4/5 and eGPU Docks for AMD Linux Laptops

## TB5 vs TB4 at a Glance

| | Thunderbolt 4 | Thunderbolt 5 |
|--|--|--|
| Bandwidth | 40 Gbps (PCIe 3.0 x4) | 80 Gbps (PCIe 4.0 x4), 120 Gbps asymmetric for display |
| PD | 100W max (PD 3.0) | 140-240W (PD 3.1 EPR); most docks deliver 140W, Lenovo 7500 delivers 180W |
| Display | DP 1.4 — dual 4K@60Hz | DP 2.1 — triple 4K@144Hz or dual 8K@60Hz |
| AMD compat | AMD USB4 (40 Gbps) — works, some MST issues | Falls back to USB4 speeds (40 Gbps); PD and tunneling work |
| Price range | $200-400 | $300-650 |
| Maturity | Mature, widely tested | Early adoption, limited Linux testing |

**TB5 docks work with AMD USB4 laptops** — they fall back to 40 Gbps. The main advantage for AMD users is higher PD wattage (140W vs 100W), not bandwidth.

## PD Requirements

| Laptop Charger | Minimum Dock PD | Recommended Dock PD | Notes |
|----------------|-----------------|---------------------|-------|
| ≤65W (T14, T14s, P14s, EliteBook) | 65W | 65W+ | Most docks work fine |
| 65-100W (TUXEDO IB Pro 14) | 100W | 100W+ | Standard 100W docks sufficient |
| >100W via proprietary profile (TUXEDO IB Pro 15 — 20V/7.5A 150W) | 100W | 100W+ with headroom | No dock supplies the non-standard 150W profile — docks cap the laptop at 100W; a 140W+ PD 3.1 dock only adds voltage stability, not wattage. See note below. |

AMD laptops with >100W chargers disconnect from most docks under sustained CPU load due to PD voltage drops. This is not Linux-specific but hits Linux users harder (sustained compilation workloads, no vendor PD policy managers).

**Proprietary >100W profiles are a trap.** Some laptops advertise ">100W USB-C charging" but use a non-standard PD profile — e.g. the TUXEDO InfinityBook Pro 15's **20V/7.5A (150W)**, which is outside the USB-PD spec (PD tops out at 20V/5A = 100W; PD 3.1 EPR goes higher only at 28/36/48V). No dock or third-party charger can supply such a profile, so these laptops fall back to **100W on any dock**. Worse, if the laptop's *only* USB4/Thunderbolt port is also its only high-watt port (as on the IB Pro 15 — rear USB4 is the sole TB port and sole 150W port; the side USB-C is 100W and not TB), then **Thunderbolt docking and full-power charging become mutually exclusive even with two cables.** When buying for single-cable docking, require full-power charging over *standard* USB-C PD — SPR (≤100W) or PD 3.1 EPR (140W/180W/240W at 28/36/48V) — and prefer that all USB-C ports are USB4. (A standards-compliant 150W laptop would use 28V+ EPR; TUXEDO kept 20V and raised current past the 5A connector limit instead.) Caveat: EPR reaches 240W in spec, but most docks deliver only 140W — 180W+ is rare (Lenovo 7500 180W, Dell 240W) — so even a >140W *standard* laptop narrows your dock options.

*Untested edge case:* no dock implements the 20V/7.5A profile (7.5A exceeds the USB-C 5A connector limit — it needs a non-standard cable), so simultaneous **150W charging + an active Thunderbolt data link has never been exercised** on this hardware: the 150W only ever comes from the bundled power-only charger, and data only ever comes from a ≤100W dock. USB-C carries power (VBUS) and USB4 data on independent lines, so there is no protocol reason they couldn't coexist — but even if such a dock were built, it is unverified whether the laptop would request the 150W profile from anything but its bundled charger (proprietary high-current modes are often gated to a charger handshake). Treat 150W+TB as *unproven*, not merely unavailable.

## Thunderbolt 5 Docks

### Comparison Table

| Dock | Price | PD | Adapter | TB5 ↓ | HDMI | DP | USB-A | USB-C | Ethernet | M.2 | Notes |
|------|------:|----:|--------:|------:|-----:|---:|------:|------:|---------:|----:|-------|
| **Plugable TBT-UDT3** | $300 | 140W | 180W | 3 | — | — | 3 | — | 2.5G | — | PCWorld Editor's Choice |
| **Kensington SD5000T5** | $300 | 140W | 180W | 3 | — | — | 3 | — | 2.5G | — | Early TB5 dock; one port 60W |
| **WAVLINK UTD58** | $300 | 140W | 180W | 3 | — | — | 4 | — | 2.5G | — | Budget; M variant adds M.2 |
| **StarTech TB5** | $300 | 140W | 180W | 1 | 1 | 1 | 3 | 2 | 2.5G | — | Most video output types |
| **OWC TB5 Dock** | $330 | 140W | 180W | 3 | — | — | 3 | — | 2.5G | — | Fanless/silent |
| **Razer TB5 Chroma** | $400 | 140W | 250W | 1 | — | — | 2 | 1 | 1G | Yes | Only 1 TB5 downstream; 1G Ethernet |
| **CalDigit TS5** | $400 | 140W | 240W | 3 | — | — | 2 | 3 | 2.5G | — | |
| **Anker Prime TB5** | $400 | 140W | 250W | 2 | 1* | 1* | 3 | 2 | 2.5G | — | *HDMI/DP mutually exclusive |
| **Targus DOCK230** | $400 | 140W | 180W | 3 | — | — | 4 | — | 2.5G | — | Includes 2x USB-C→HDMI adapters |
| **Satechi CubeDock** | $400 | 140W | 180W | 3 | — | — | 2 | 2 | 2.5G | Yes | M.2 PCIe 4.0 |
| **Sonnet Echo 13** | $400+ | 140W | 180W | 3 | — | — | 4 | — | 2.5G | Built-in | Ships with 1-4TB SSD |
| **iVANKY Pro 3** | $450 | 140W | 180W | 3 | — | — | — | — | 2.5G | — | |
| **Kensington SD7100T5** | $450 | 140W | ~180W | 3 | — | — | 4 | 2 | 2.5G | Yes | CF+SD+microSD; optical audio |
| **ASUS DC510** | $460 | 140W | 180W | 2 | — | — | 4 | — | 2.5G | Yes | |
| **CalDigit TS5 Plus** | $500 | 140W | 330W | 2 | — | 1 | 5 | 5 | **10G** | — | Only TB5 dock with 10 GbE |
| **Dell WD25TB5** | $500 | 240W† | 330W | 2 | 1 | 2 | 4 | 1 | 2.5G | — | †300W to Dell laptops |
| **Lenovo 7500 (40BA)** | $550 | **180W** | 265W | 2 | 1 | 2 | 3 | 2 | 2.5G | — | Only dock listing Linux support; fwupd |
| **Dell SD25TB5** | $625 | 240W† | 330W | 2 | 1 | 2 | 4 | 2 | 2.5G | — | †300W to Dell; remote management |
| **iVANKY Ultra** | $650 | 140W | large | 4 | 1 | 1 | 4 | 7 | **10G** | — | 26 ports; Mac-focused |

### Picks

**For laptops with proprietary >100W profiles (TUXEDO IB Pro 15):** no dock delivers the 150W profile — you are capped at 100W on any dock (see the proprietary-profile note above). Pick a dock with PD headroom well above 100W so its 100W rail doesn't sag under CPU-load transients: the Lenovo ThinkPad TB5 Smart Dock 7500 ($550, 180W PD 3.1, only dock officially listing Linux support, fwupd) or a 140W PD 3.1 dock (Plugable TBT-UDT3, CalDigit TS5). For full 150W you must use the bundled charger directly — and then forgo the Thunderbolt dock entirely, since the IB Pro 15's only USB4 port is also its only 150W port. A user with the **IBP 14 Gen10** (65W) reports the Lenovo 7500 running fully stable single-cable under sustained CPU+GPU load; the **IBP 15** (90W) is *not* confirmed — TUXEDO support says 100W won't reach full performance on the 15 ([r/tuxedocomputers reports](https://www.reddit.com/r/tuxedocomputers/comments/1poqpe3/random_dock_resets_on_infinitybook_pro_14_amd_gen/)).

**For ≤100W laptops:** Plugable TBT-UDT3 ($300) — 3x TB5 downstream (drives USB-C monitors directly), 140W PD 3.1, 2.5GbE.

**10GbE:** CalDigit TS5 Plus ($500) — only TB5 dock with 10 GbE, 10 USB ports total, DP 2.1.

**Built-in M.2:** Satechi CubeDock ($400) or Kensington SD7100T5 ($450).

## Thunderbolt 4 Docks (Still Relevant in 2026)

TB4 docks remain practical — very few laptops have native TB5. For AMD USB4 laptops with ≤100W chargers, TB4 is sufficient.

### Comparison Table

| Dock | Price | PD | TB4 ↓ | HDMI | DP | USB-A | USB-C | Ethernet | Notes |
|------|------:|----:|------:|-----:|---:|------:|------:|---------:|-------|
| **StarTech TB4CDOCK** | $200 | 96W | 3 | — | — | 4 | — | 1G | Clearance pricing |
| **OWC TB4 Dock** | $230 | 96W | 3 | — | — | 4 | — | 1G | Fanless; best for USB-C monitors |
| **Plugable TBT4-UDZ** | $270 | 100W | 0 | 2 | 2 | 6 | 1 | 2.5G | No TB downstream — can't drive Studio Display |
| **Belkin INC006** | $280 | 90W | 2 | 2 | — | 4 | 1 | 1G | |
| **Kensington SD5780T** | $300 | 96W | 3 | 1 | — | 4 | — | 2.5G | Out of stock; restock July 2026 |
| **Lenovo 40B0** | $280 | 100W | 1 | 1 | 2 | 4 | 1 | 1G | Official Linux support; fwupd |
| **HP TB4 G4 (120W)** | $329 | 100W | 1 | 1 | 2 | 4 | 2 | 2.5G | No audio, no SD; HP Sure Start |
| **CalDigit TS4** | $330 | 98W | 3 | — | 1 | 5 | 3 | 2.5G | 18 ports; most Linux community reports |
| **Lenovo 40BE Gen 2** | $360 | 100W | 1 | 1 | 2 | 4 | 2 | 2.5G | Newer; 8K@60Hz |
| **Dell WD22TB4** | EOL | 90W | 2 | 1 | 2 | 3 | 1 | 1G | EOL; problematic on Linux |

### Picks

**USB-C monitors:** CalDigit TS4 ($330) or OWC TB4 Dock ($230) — 3x TB4 downstream ports, drives Apple Studio Display / LG UltraFine directly.

**Linux support:** Lenovo 40B0/40BE — official Linux compatibility, fwupd firmware updates. Display-on-resume issues exist but documented with workarounds.

**Avoid:** Dell WD22TB4 (xhci_hcd failures on Linux, EOL), Plugable TBT4-UDZ (no TB4 downstream — cannot drive USB-C monitors).

## eGPU Docks (with PD)

eGPU docks that also function as laptop docking stations — providing PD charging, USB ports, Ethernet, and/or display outputs alongside a discrete GPU.

### eGPU Interfaces

| Interface | Spec | PCIe Lanes | Bandwidth | Perf Loss vs Desktop | Hot-plug | On Laptops? |
|-----------|------|-----------|-----------|---------------------|----------|-------------|
| **TB4 / USB4 v1** | USB4 40 Gbps | PCIe 3.0 x4 | 32 Gbps | 30-40% | Yes | Common (AMD USB4, Intel TB4) |
| **TB5 / USB4 v2** | USB4 80 Gbps | PCIe 4.0 x4 | 64 Gbps | **19-25%** | Yes | Rare (few laptops have TB5 natively) |
| **OCuLink** | SFF-8612 | PCIe 4.0 x4 | 64 Gbps | **5-15%** | **No** | Rare (GPD, some mini PCs; most laptops lack it) |
| **MCIO 8i** | PCIe 4.0 x8 | PCIe 4.0 x8 | 128 Gbps | **~2%** | No | Almost none (GPD BOX only) |
| Native PCIe | x16 slot | PCIe 4.0 x16 | 256 Gbps | baseline | No | N/A |

**Thunderbolt / USB4** is the only interface relevant for docking — it carries PD charging, USB data, display, and PCIe tunneling over one cable. TB5 doubles TB4 bandwidth but AMD USB4 laptops still connect at 40 Gbps (USB4 v1). Supports hot-plug (with caveats on Linux — see below).

**OCuLink and MCIO** are raw PCIe connectors with no PD, no USB, no display tunneling — just GPU data. They appear on some eGPU products as a secondary port alongside TB5/USB4 for higher GPU bandwidth. OCuLink (PCIe 4.0 x4) is found on GPD handhelds and some mini PCs. MCIO 8i (PCIe 4.0 x8, used by GPD G2) achieves near-native performance but currently only GPD BOX has the port. Neither is hot-pluggable. For docking purposes, TB5/USB4 is always the primary connection; OCuLink/MCIO are optional performance upgrades when the host supports them.

### Integrated GPU Products

| Product | Price | GPU | Interface | PD | Dock Ports | Weight |
|---------|------:|-----|-----------|---:|------------|-------:|
| **GPD G1 (2024)** | $700 | RX 7600M XT 8GB | OCuLink + USB4 | 65W | 3xUSB-A, SD, HDMI, 2xDP | 920g |
| **AORUS RTX 5060 Ti AI BOX** | $700 | RTX 5060 Ti 16GB | TB5 | 100W | USB-A/C, Eth, 3xDP, HDMI, 2xTB5 | ~2 kg |
| **OneXGPU 2** | $839 | RX 7800M 12GB | OCuLink + USB4 | 100W | 2xUSB, Eth, 2xHDMI, 2xDP, M.2 | 1.6 kg |
| **MOREFINE G2** | $1,100 | RTX 5060 Ti 16GB | TB5 + OCuLink | 100W | HDMI, DP, 3xUSB-A | 700g |
| **ASUS ROG XG Mobile** | $1,300 | RTX 5070 Ti Laptop | TB5 (120 Gbps) | yes | 2xUSB-A, Eth, SD, HDMI, DP, TB5 | 950g |

**AORUS RTX 5060 Ti AI BOX ($700)** — desktop RTX 5060 Ti at ~5% perf loss via TB5, has Ethernet, TB5 daisy-chain, multiple USB. Closest to a dock replacement.

**MOREFINE G2 ($1,100)** — 700g with desktop RTX 5060 Ti, but $400 more than AORUS for fewer ports.

### BYO GPU Enclosures with PD

| Product | Price | Interface | PSU | PD | Dock Ports |
|---------|------:|-----------|----:|---:|------------|
| **Minisforum DEG2** | $240 | TB5 + OCuLink | BYO | 140W | 2xTB5, 2xUSB, 2.5GbE, M.2 |
| **Sonnet BB 850 T5** | $500 | TB5 | 850W | 100W | 3xUSB-A, 5GbE, TB5 downstream |

**Minisforum DEG2 ($240 + your PSU)** — TB5, OCuLink, 140W PD 3.1, 2.5GbE, M.2 slot. Add a ~$100 SFX PSU → $340 total for dock+eGPU.

Bare enclosures without PD or dock ports (Razer Core X V2, Minisforum DEG1, AOOSTAR AG03, EXP GDC TH5P4) are not dock replacements — you'd need a separate dock on top.

### GPD G2

**Announced, not released.** MCIO 8i interface (PCIe 4.0 x8) promises only ~2% perf loss, but requires a host with MCIO (currently only GPD BOX mini PC). For standard laptops, falls back to USB4 v2 — same as any TB5 enclosure. 800W PSU, 100W PD, minimal dock ports. Not recommended to wait for.

### eGPU on Linux

**What works:** AMD eGPU via `amdgpu` driver (hot-plug detection on Wayland, `DRI_PRIME=1`). NVIDIA eGPU via proprietary driver (`AllowExternalGpus "True"`, PRIME offload). AMD iGPU + NVIDIA eGPU PRIME offloading works; `all-ways-egpu` tool automates GPU selection on Wayland.

**What does NOT work:**
- **Hot-unplug crashes the system** — both AMD and NVIDIA. Always shut down before disconnecting.
- **Suspend/resume is broken** — NVIDIA best on kernel 6.13.7; AMD has VRAM eviction deadlocks. Unplug eGPU before sleeping.
- **OCuLink is not hot-pluggable** — requires boot with connection.
- **AMD USB4 PCIe Gen 1 fallback** — some laptops (Framework 13 Ryzen AI 300 on BIOS 03.05) fall back to Gen 1 x1, killing eGPU performance. BIOS updates may fix.

## AMD USB4 Compatibility

AMD USB4 works with TB4, TB5, and eGPU docks, but with caveats.

### What Works
- USB peripherals, Ethernet, audio, charging — generally reliable on kernel 6.5+
- Single display via DP tunneling — stable on kernel 6.10+ for Strix Point
- Apple Studio Display at 5K@60Hz — confirmed via CalDigit TS4 on AMD (Beelink SER8, Arch)

### Known Issues

**MST (Multi-Stream Transport) is fragile on AMD.** Docks that use MST for multi-display (most HDMI/DP output docks) have display detection failures on AMD — monitors default to 640x480 or aren't detected at all. Prefer docks with TB downstream ports over HDMI/DP.

**Kernel regressions are frequent.** Each major kernel release (6.9, 6.10, 6.11) introduced AMD USB4 display regressions:
- Kernel 6.9: MST crash (NULL pointer in `drm_dp_atomic_find_time_slots`)
- Kernel 6.10-rc: dual 4K — one monitor stays black over USB4
- Kernel >6.11.5: dock stops working entirely on some systems

**Kernel 7.0+** is the most stable so far for AMD USB4 docking.

**Hot-plug unreliable.** CalDigit TS4 on AMD Framework: system freezes during boot/shutdown with GNOME. USB dead on wake from sleep until dock is physically replugged.

**Thunderbolt authorization needed.** Some docks fail because TB PCIe tunneling is unauthorized by default. Fix with a udev rule for auto-authorization when IOMMU DMA protection is active.

### Recommendations for AMD USB4
- **Kernel 7.0+ recommended** (or latest stable)
- **Avoid MST-dependent docks** — prefer TB downstream ports for displays
- **Keep BIOS and dock firmware updated** — MST reliability varies more between firmware versions than on Intel
- **Budget ~$500 for a dock** if laptop charger >100W

### Key Developer
Mario Limonciello at AMD is the primary engineer driving USB4/Thunderbolt Linux improvements for AMD platforms.

## USB-C Monitor Compatibility

Apple Studio Display and LG UltraFine require USB-C/Thunderbolt input. HDMI/DP adapters do not work.

| Dock Type | Can Drive USB-C Monitors? |
|-----------|--------------------------|
| Docks with TB4/TB5 downstream ports | Yes — connect directly |
| Docks with only HDMI/DP outputs | No — incompatible |
| Docks with USB-C data-only ports | No — no video signal |

Each 5K display consumes one full TB4 link. Dual 5K requires two TB downstream ports.

**Docks with 3+ TB downstream ports** (best for USB-C monitors): CalDigit TS4/TS5, OWC TB4/TB5, Kensington SD5000T5/SD5780T, Plugable TBT-UDT3, StarTech TB4CDOCK.

## Sources

- [Framework Community: AMD Dock Compatibility](https://community.frame.work/t/dock-compatibility-amd-usb-c-thunderbolt/38378)
- [Framework Community: CalDigit TS4 AMD Monitor Issues](https://community.frame.work/t/responded-amd-mainboard-caldigit-ts4-dock-monitors-not-identified/39228)
- [Framework Community: USB4 eGPU PCIe Gen1 Issue](https://community.frame.work/t/usb4-egpu-limited-to-pcie-gen1-x1-on-framework-13-ryzen-ai-300-bios-03-05/79190)
- [Arch Wiki: Thunderbolt](https://wiki.archlinux.org/title/Thunderbolt)
- [Phoronix: AMD USB4 DP Tunneling](https://www.phoronix.com/news/AMD-USB4-Display-Port-Tunneling)
- [Phoronix: AMDGPU Hot-Unplug Patches](https://www.phoronix.com/news/AMDGPU-Hot-Unplug-V2)
- [Tom's Hardware: OCuLink vs TB5 Benchmarks](https://www.tomshardware.com/pc-components/gpus/oculink-outpaces-thunderbolt-5-in-nvidia-rtx-5070-ti-tests-latter-up-to-14-percent-slower-on-average-in-gaming-benchmarks)
- [NotebookCheck: TB5 eGPU Performance](https://www.notebookcheck.net/Thunderbolt-5-Peladn-Link-S-3-eGPU-performance-compared-with-OCuLink-and-native-desktop-system.1130786.0.html)
- [NotebookCheck: GPD G1 Review](https://www.notebookcheck.net/GPD-G1-eGPU-review-External-AMD-Radeon-RX-7600M-XT-with-8-GB-of-VRAM-uses-USB4-or-OCuLink.780524.0.html)
- [eGPU.io Buyer's Guide](https://egpu.io/best-egpu-buyers-guide/)
- [Botmonster: Best USB-C Docking Stations for Linux 2026](https://botmonster.com/self-hosting/best-usb-c-docking-stations-dual-monitor-linux-2026/)
- r/tuxedocomputers — dock compatibility with InfinityBook Pro Gen9/Gen10
