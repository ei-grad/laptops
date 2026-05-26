---
model: Lenovo ThinkPad P14s Gen 6 AMD
slug: lenovo-thinkpad-p14s-gen-6-amd
manufacturer: Lenovo
status: available
form_factor: clamshell
weight_kg: 1.44
battery_wh: 57
price_usd: 1579

display:
  size_in: 14.0
  aspect_ratio: "16:10"

variants:
  - year: 2025
    cpu:
      name: AMD Ryzen AI 9 HX PRO 370
      cores: 12
      threads: 24
      arch: Strix Point
      boost_ghz: 5.1
    gpu:
      name: Radeon 890M
      type: integrated
      compute_units: 16
    ram_gb: 64
    ram_type: LPDDR5X
    ram_upgradeable: false
    power:
      pl1_w: 36
      pl2_w: 51
    benchmarks:
      cinebench_r23_multi: 18520
      cinebench_r23_single: 1939
      geekbench6_multi: 14739

noise: {}

linux:
  status: good
  issues:
    - ThinkPad track record; not specifically tested on this model
    - Gen 6 reviews report improved cooling vs earlier generations
---

# Lenovo ThinkPad P14s Gen 6 AMD

## Reassessment

Previous research excluded P14s for "unacceptable noise even silent mode at 24W". The Gen 6 AMD review contradicts this — NotebookCheck says "performance does not come at the cost of fan noise or extreme case temperatures" and "no CPU throttling on battery."

## Sustained Performance

- **36W PL1 sustained** (Best Performance mode)
- CB R23 multi 18,520 — solid for a ThinkPad
- R15 loop stable: 2,647-3,082 range
- No throttling on battery
- ISV-certified workstation

## Key Differences from T14

- Up to 64 GB LPDDR5X (soldered, not upgradeable)
- HX PRO 370 (12C/24T) — more cores than T14's PRO 360
- ISV certifications
- Slightly heavier at 1.44 kg

## Sources

- [NotebookCheck review](https://www.notebookcheck.net/Most-powerful-AMD-14-inch-ThinkPad-with-Ryzen-AI-9-HX-Lenovo-ThinkPad-P14s-Gen-6-AMD-laptop-review.1030845.0.html)
