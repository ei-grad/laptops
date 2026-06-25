# Excluded Models (Details)

### ASUS Zenbook 14 AMD
- Cinebench R23: Started at 13,843, dropped to high 8,000s
- Power drops from 50W → 28W over 5-6 minutes
- "Throttles hard on looped Cinebench test"
- Source: [Tom's Hardware](https://www.tomshardware.com/laptops/ultrabooks-ultraportables/asus-zenbook-14-oled-ux3405m-review)

### LG Gram 14
- "Thermal throttling is the worst case I've seen for P-series"
- Frame rate drops from 15 to 10 FPS under load
- Source: [NotebookCheck LG Gram Style 14](https://www.notebookcheck.net/LG-Gram-Style-14-laptop-review-Elegant-fast-and-too-hot.744925.0.html)

### Xiaomi / Huawei Laptops
- Intel DPTF not supported on Linux
- Up to 50% performance loss vs Windows
- Limited sustained-load review data
- Source: [Phoronix Lenovo Thermal Throttling](https://www.phoronix.com/news/Lenovo-Linux-Thermal-Throttling)

### ThinkPad P14s AMD (Gen 5 and earlier)
- Even silent mode runs at 24W ("windmill")
- "Unacceptable noise" per user reports
- Profiles unbalanced vs T14
- Source: [Fedora Linux on P14s Gen 5](https://www.bovender.de/posts/2024/08/experience-with-running-fedora-linux-on-a-thinkpad-p14s-gen-5/)
- **Note:** Gen 6 AMD (HX PRO 370) and Gen 7 AMD (HX PRO 470) are reconsidered — improved cooling and stronger specs, see `reviews/lenovo-thinkpad-p14s-amd.md`

### TUXEDO InfinityBook Pro 15 Gen10
- Weight 1.77 kg exceeds ≤1.6 kg criterion
- Same Tongfang GX5 barebone as XMG EVO 15, same HX 370 CPU as the recommended 14" sibling
- Excellent specs: 90W cooling capacity, 99 Wh battery, 128 GB DDR5 SO-DIMM, native Linux
- 150W charging uses a proprietary 20V/7.5A profile (outside USB-PD) — no dock supplies it, so any dock caps the laptop at 100W; and its only USB4/TB port is also its only 150W port, so Thunderbolt docking and 150W charging are mutually exclusive (see review)
- Chosen as a work laptop despite weight exclusion (battery, screen size, cooling headroom)
- See `reviews/tuxedo-infinitybook-pro-15.md`
