---
model: ASUS ProArt PX13
slug: asus-proart-px13
manufacturer: ASUS
status: recommended
form_factor: convertible
weight_kg: 1.39
battery_wh: 73
price_usd: 2000
display:
  aspect_ratio: '16:10'
  panel: OLED
  refresh_hz: 60
  resolution: 2880x1800
  size_in: 13.3
  touch: true
variants:
- benchmarks:
    cinebench_2024_multi: 769
    cinebench_2024_single: 114
    cinebench_r15_multi: 3489
    cinebench_r23_multi: 23020
  cpu:
    arch: Strix Point
    cores: 12
    name: AMD Ryzen AI 9 HX 370
    threads: 24
  gpu:
    name: NVIDIA RTX 4050/4060/4070
    type: discrete
  power:
    battery_w: 55
    pl1_w: 65
    pl2_w: 80
  ram_gb: 32
  ram_type: LPDDR5X
  sku: HN7306WV
  year: 2024
- benchmarks:
    cinebench_r23_multi: 30841
    cinebench_r23_multi_sustained: 30403
    cinebench_2024_multi: 1642
    geekbench6_multi: 18956
    geekbench6_single: 2938
  cpu:
    arch: Strix Halo
    cores: 16
    name: AMD Ryzen AI Max+ 395
    threads: 32
  gpu:
    compute_units: 40
    name: Radeon 8060S
    type: integrated
  power:
    pl1_w: 70.0
    pl2_w: 95.0
  ram_gb: 128
  ram_type: LPDDR5X-8000
  sku: HN7306 (GoPro Edition)
  year: 2026
noise:
  balanced_dba: 43
  max_dba: 53
linux:
  issues:
  - WiFi MT7925 requires kernel 6.7+
  - Keyboard backlight inconsistent
  - Fan control erratic on stock kernel
  - HDMI may not work without xanmod
  kernel_min: '6.7'
  status: fair
sources:
- https://dl.xanmod.org/archive.key
- http://deb.xanmod.org
- https://www.linuxquestions.org/questions/linux-laptop-and-netbook-25/ubuntu-24-04-on-asus-proart-px13-hn7306wi_hn7306wi-4175751777-new/
- https://linux-hardware.org/?probe=c0107457aa
- https://www.notebookcheck.net/Asus-ProArt-PX13-review-The-world-s-fastest-13-3-inch-2-in-1-thanks-to-AMD-Zen-5-and-RTX-4070-laptop.868429.0.html
- https://www.pcworld.com/article/2418049/asus-proart-px13-review.html
- https://www.ultrabookreview.com/72323-asus-proart-px13-review/
- https://www.windowscentral.com/laptops/asus-proart-px13-review
- https://www.ultrabookreview.com/74193-asus-strix-halo-laptops-proart-tuf/
- https://www.ultrabookreview.com/74980-asus-proart-px13-gopro-review/
- https://www.techpowerup.com/review/asus-proart-gopro-edition-px13/
- https://gist.github.com/cryptob1/f62aaf8517df2e540f447347f42c7a03
- https://wireless.docs.kernel.org/en/latest/en/users/drivers/mediatek.html
- https://lwn.net/Articles/944390/
---
# ASUS ProArt PX13 (HN7306)

## Model Variants

### 2024-2025: HN7306WV/WI/WU (Strix Point)
- **CPU:** AMD Ryzen AI 9 HX 370 (Strix Point, 12C/24T)
- **GPU:** NVIDIA RTX 4050/4060/4070 Laptop
- **RAM:** Up to 32GB LPDDR5X (soldered)

### 2026: HN7306 GoPro Edition (Strix Halo) — reviewed
- **CPU:** AMD Ryzen AI Max+ 395 (Strix Halo, 16C/32T); Max+ 388 entry config
- **GPU:** Integrated Radeon 8060S (40 CU) — no dGPU
- **RAM:** Up to 128GB LPDDR5X-8000 unified memory (soldered)
- **NPU:** 50 TOPS
- 70W sustained (Performance), CB R23 30,403 (10-min) — lightest reviewed Strix Halo at 1.39 kg
- See the [2026 GoPro Edition section](#2026-gopro-edition-strix-halo--reviewed) below for full data

---

## Common Specifications
- **Display:** 13.3" 3K ASUS Lumina OLED (2880×1800), 60Hz, touch, convertible
- **Weight:** 1.39 kg (1.84 kg with charger)
- **Ports:** 2× USB4 (40Gbps), HDMI 2.1, UHS-II microSD
- **Connectivity:** Wi-Fi 7 (MediaTek MT7925), Bluetooth 5.4

### Power Configuration
- **PL2 (Burst):** 80W
- **PL1 (Sustained):** **65W**
- Battery mode: 55W max (~10% performance drop)

### Benchmark Scores
- **Cinebench R15:** 3,489 (multi)
- **Cinebench R23:** 23,020 (multi) — fastest 13.3" laptop
- **Cinebench 2024:** 769 (CPU multi), 114 (single)

### Thermal & Noise Data

| Mode | Noise | Notes |
|------|-------|-------|
| Idle/Light | Silent | Fans off |
| Medium load | Low-40s dB(A) | Acceptable |
| Full load | **~53 dB(A)** | Gaming/stress |
| Whisper mode | Quiet | Reduced performance |

- "Manages to avoid thermal throttling, maintaining consistent performance"
- "Didn't get nearly as hot and loud during demanding tasks as expected"
- Fans can be "slightly high pitched" — more noticeable than similar volume
- After BIOS updates, fan behavior improved significantly
- Surface stays thermally controlled

### Stress Test Behavior
- Processor briefly uses 80W, settles to **65W sustained**
- "Drop in performance remains low but results fluctuate slightly"
- Performance fluctuation due to short Cinebench R15 test catching different power phases
- "Even in 'worst' case, HX 370 is the fastest chip"
- 14% faster than Ryzen 9 8945HS on average

### Linux Compatibility

#### Component Status

| Component | Status | Notes |
|-----------|--------|-------|
| CPU/RAM/NVMe | ✓ Works | |
| AMD Radeon (iGPU) | ✓ Works | amdgpu driver |
| NVIDIA RTX (dGPU) | ⚠️ Needs driver | nvidia 530.41.03+ / nvidia-prime |
| **WiFi (MT7925)** | ⚠️ Kernel 6.7+ | Driver merged in kernel 6.7 |
| Keyboard backlight | ⚠️ Inconsistent | Fixed with OEM/newer kernel |
| Fan control | ⚠️ Erratic on stock | Fixed with OEM/newer kernel |
| HDMI output | ⚠️ May not work | Fixed with xanmod kernel |
| Touchscreen | ✓ Works | |

#### Recommended Kernel (Ubuntu 24.04)

Stock kernel has issues with WiFi, keyboard backlight, and fan control. Solutions:

```bash
# Option 1: Ubuntu OEM kernel (good baseline)
sudo apt install linux-oem-24.04c

# Option 2: Xanmod kernel (recommended - fixes HDMI, WiFi, backlight)
wget -qO - https://dl.xanmod.org/archive.key | sudo gpg --dearmor -vo /etc/apt/keyrings/xanmod-archive-keyring.gpg
echo 'deb [signed-by=/etc/apt/keyrings/xanmod-archive-keyring.gpg] http://deb.xanmod.org releases main' | sudo tee /etc/apt/sources.list.d/xanmod-release.list
sudo apt update && sudo apt install --no-install-recommends linux-xanmod-x64v3
```

#### User Reports (HN7306WI with RTX 5070, Ubuntu 24.04)

From [LinuxQuestions thread](https://www.linuxquestions.org/questions/linux-laptop-and-netbook-25/ubuntu-24-04-on-asus-proart-px13-hn7306wi_hn7306wi-4175751777-new/):
- **Initial issues:** Keyboard backlight erratic, fan running high at idle, random screen blackouts
- **linux-oem-24.04c:** Fixed keyboard backlight, stabilized fan, no hangs
- **xanmod kernel:** Fixed HDMI output, improved WiFi

#### 2026 GoPro Edition (Strix Halo) — Reviewed

The 2026 refresh (marketed as the **ProArt PX13 GoPro Edition**) drops the NVIDIA dGPU for
the Ryzen AI Max+ 395's integrated Radeon 8060S (40 CU) and up to 128 GB LPDDR5X-8000
unified memory. Independently reviewed (UltrabookReview / TechPowerUp / TrustedReviews),
it is now one of only a handful of Strix Halo laptops with real sustained data — and at
**1.39 kg it is the lightest reviewed Strix Halo laptop**, lighter than the
[HP ZBook Ultra G1a](./hp-zbook-ultra-g1a.md) (1.586 kg).

- **Sustained power:** Silent 35W → Standard 50-60W → **Performance 70W** → Manual 95W
  sustained / 115W burst. Default Performance mode holds 70W with minimal throttle.
- **CB R23 multi:** 30,841 peak / **30,403 over 10 min** — essentially matching the ZBook
  (29,203 sustained) in a smaller, lighter, cheaper chassis.
- **CB 2024 multi:** 1,642. **Geekbench 6:** 2,938 single / 18,956 multi.
- **Noise:** Silent <35 dBA, Standard 38-42, **Performance 45-48**, Manual 49-52 dBA (at
  head level). Performance mode just exceeds the 45 dB target; Standard mode stays under.
- **Charger:** 200W barrel (USB-C PD up to 100W) — >100W, so the dock caveat applies, see
  [USB4 Docking](../overviews/usb4-docking-linux.md).
- **Price:** ~$2,999 / ~€3,200 (Max+ 395); a Max+ 388 entry config is ~$1,899.

**Linux (Strix Halo variant) — needs bleeding-edge kernel:**

- **Kernel 7.0 mainline is required.** Stock 6.19.x lacks the **AMD ACP70 PX13 audio
  quirks**, which landed in mainline on **2026-03-16**.
- For full 128 GB unified-memory GPU allocation, boot params:
  `iommu=pt amdgpu.gttsize=126976 ttm.pages_limit=32505856` (raises GTT to ~124 GiB).
- **Internal speakers (TAS2783)** work but need manual firmware-blob extraction from the
  Windows driver (`1714-1-8.bin`, `1714-1-B.bin`) — not yet in linux-firmware.
- Headphone jack (RT721), HDMI audio, Bluetooth audio all work. Automatic headphone-jack
  detection does not (manual sink switching); PDM microphone array untested.
- iGPU (amdgpu/gfx1151), CPU, NVMe, Wi-Fi 7 (MT7925) work on recent kernels.

This is a **fair** Linux story — strong hardware, but it needs a 7.0 mainline kernel,
boot params, and a manual firmware-extraction step for speakers. The ZBook Ultra G1a
(Ubuntu-certified) remains the better turnkey Linux Strix Halo machine; the PX13 wins on
weight and price. See the [Strix Halo overview](../overviews/strix-halo-linux.md).

#### Hardware Probe Data

[Linux Hardware Database probe](https://linux-hardware.org/?probe=c0107457aa) (HN7306WV, Linux Mint 21.3, kernel 6.5):
- AMD Ryzen AI 9 HX 370 + Radeon 890M detected
- Samsung LPDDR5 RAM working
- SanDisk NVMe SSD working
- WiFi required kernel 6.7+ (not available in test)

### Caveats
- 13.3" 2-in-1 form factor — compact but less cooling headroom than 14" clamshells
- RTX GPU adds heat/power complexity
- OLED 60Hz (no high refresh option)
- Whisper mode reduces performance significantly

### Best Use Case
Excellent for sustained workloads if you accept ~53 dB noise under full load. The 65W sustained power and 12-core HX 370 make it the most powerful sub-14" convertible. Good for compilation if noise isn't critical.