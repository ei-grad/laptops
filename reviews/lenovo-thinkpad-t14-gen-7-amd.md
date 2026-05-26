---
model: Lenovo ThinkPad T14 Gen 7 AMD
slug: lenovo-thinkpad-t14-gen-7-amd
manufacturer: Lenovo
status: announced
form_factor: clamshell
weight_kg: 1.28
battery_wh: 75
price_usd: 1500

display:
  size_in: 14
  panel: OLED
  aspect_ratio: "16:10"

variants:
  - year: 2026
    cpu:
      name: AMD Ryzen AI 9 HX PRO 470
      cores: 12
      threads: 24
      arch: Gorgon Point
    gpu:
      name: Radeon 890M
      type: integrated
      compute_units: 16
    ram_gb: 64
    ram_type: DDR5 SO-DIMM
    ram_upgradeable: true
    battery_wh: 75
    power:
      pl1_w: 30
      pl2_w: 45

linux:
  status: unknown
  issues:
    - Not yet reviewed on Linux
    - Gorgon Point uses same Zen 5 / RDNA 3.5 as Strix Point, kernel 6.12+ expected
---

# Lenovo ThinkPad T14 Gen 7 AMD (Gorgon Point)

**Status:** Announced MWC 2026 (March), available April 2026
**Price:** From EUR 1,400

## Specifications

| Spec | Value |
|------|-------|
| CPU | AMD Ryzen AI 5/7/9 PRO 400 (Gorgon Point) |
| Weight | 1.28 kg (60Wh) / 1.32 kg (75Wh) WLAN |
| Battery | 60 Wh or **75 Wh** (up from 57 Wh max) |
| RAM | Up to 64 GB DDR5 SO-DIMM (user-upgradeable) |
| Display | 14" options incl. OLED |
| Ports | 2x Thunderbolt 4 (USB PD/DP 2.1), 2x USB-A, HDMI 2.1, RJ45 |
| Charging | 65W USB-C |

## Key Improvements over Gen 5/6

- 75 Wh battery option (31% larger than previous 57 Wh)
- Modular USB-C charging ports
- Tool-less battery removal (two release buttons)
- User-replaceable SSD, 5G card, keyboard
- Easier bottom cover removal

## Sustained Power

Not yet reviewed. Expect 25-35W range based on chassis design (similar to Gen 5/6).

## Assessment

Strong candidate. The SO-DIMM RAM upgradability + 75 Wh battery + RJ45 Ethernet make this the most practical business ultrabook. Wait for sustained power reviews.

### Sources

- [Notebookcheck: ThinkPad T14 Gen 7 + T16 Gen 5](https://www.notebookcheck.net/New-Lenovo-ThinkPad-T14-Gen-7-and-T16-Gen-5-come-with-75-Wh-battery-Intel-Panther-Lake-or-AMD-Gorgon-Point.1239024.0.html)
- [Lenovo PSREF: ThinkPad T14 Gen 7 AMD](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_T14_Gen_7_AMD/ThinkPad_T14_Gen_7_AMD_Spec.pdf)
- [Ubergizmo: ThinkPad T14 Gen 7 Repairability](https://www.ubergizmo.com/2026/03/lenovo-thinkpad-t14-t16-gen-5/)

---
