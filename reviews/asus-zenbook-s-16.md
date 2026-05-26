---
model: ASUS Zenbook S 16
slug: asus-zenbook-s-16
manufacturer: ASUS
status: recommended
form_factor: clamshell
weight_kg: 1.5
battery_wh: 78
price_usd: 1300
display:
  aspect_ratio: '16:10'
  panel: OLED
  refresh_hz: 120
  resolution: 2880x1800
  size_in: 16
  touch: true
variants:
- battery_wh: 78
  benchmarks:
    cinebench_2024_multi: 926
    cinebench_2024_single: 114
    cinebench_r23_multi: 17961
    cinebench_r23_multi_sustained: 15266
    cinebench_r23_single: 1965
    geekbench6_multi: 13389
    geekbench6_single: 2828
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
    pl1_w: 28
    pl2_w: 33
  ram_gb: 32
  ram_type: LPDDR5x-7500
  sku: UM5606WA
  year: 2024
- battery_wh: 78
  benchmarks:
    cinebench_r15_multi: 1724
    cinebench_r23_multi: 11462
    cinebench_r23_single: 1942
  cpu:
    arch: Strix Point
    boost_ghz: 5.0
    cores: 10
    name: AMD Ryzen AI 9 365
    threads: 20
  gpu:
    compute_units: 12
    name: Radeon 880M
    type: integrated
  power:
    pl1_w: 28
    pl2_w: 33
  ram_gb: 24
  ram_type: LPDDR5x
  sku: UM5606WA-365
  year: 2024
- battery_wh: 83
  benchmarks:
    cinebench_2024_multi: 953
    cinebench_2024_single: 115
    cinebench_r23_multi: 17580
    cinebench_r23_single: 1997
    geekbench6_multi: 14562
    geekbench6_single: 2834
  cpu:
    arch: Gorgon Point
    boost_ghz: 5.0
    cores: 10
    name: AMD Ryzen AI 9 465
    threads: 20
  gpu:
    compute_units: 12
    name: Radeon 880M
    type: integrated
  power:
    pl1_w: 35
    pl2_w: 45
  ram_gb: 32
  ram_type: LPDDR5x-8533
  sku: UM5606GA
  year: 2026
noise:
  balanced_dba: 36
  idle_dba: 25
  low_power_dba: 30
  max_dba: 52.5
  performance_dba: 40
linux:
  boot_params:
  - amdgpu.dcdebugmask=0x600
  issues:
  - PSR2-SU deadlocks without boot param
  - Keyboard backlight broken on Linux
  - s2idle only, no S3 deep sleep
  kernel_min: '6.14'
  status: good
sources:
- https://www.notebookcheck.net/The-perfect-everyday-laptop-with-AMD-Ryzen-400-Asus-Zenbook-S16-OLED-review.1221965.0.html
- https://www.ultrabookreview.com/68996-asus-zenbook-s16-review/
- https://www.storagereview.com/review/zen5-mobile-performance-the-amd-ryzen-ai-9-hx-370-asus-zenbook-s16-review
- https://www.notebookcheck.net/Asus-ZenBook-S-16-OLED-laptop-review-Premiere-for-Ryzen-AI-9-365-and-Radeon-880M.885785.0.html
- https://www.windowscentral.com/hardware/laptops/asus-zenbook-s-16-um5606-review
- https://wiki.archlinux.org/title/ASUS_Zenbook_UM5606
- https://www.phoronix.com/review/asus-zenbook-s16-power
- https://www.trustedreviews.com/reviews/asus-zenbook-s-16-2026
- https://www.ultrabookreview.com/74512-asus-zenbook-s16-s14/
- https://hitechcentury.com/asus-zenbook-s16-review-um5606-2026/
---
# ASUS Zenbook S 16 (UM5606)

## Model Variants

### 2024: UM5606WA (Strix Point)
- **CPU:** AMD Ryzen AI 9 HX 370 (12C/24T, 4× Zen 5 + 8× Zen 5c, up to 5.1 GHz)
- **GPU:** Radeon 890M (16 CU, RDNA 3.5)
- **RAM:** 32GB LPDDR5x-7500 (soldered)
- **Storage:** 1TB NVMe SSD

### 2024: UM5606WA (Strix Point, lower SKU)
- **CPU:** AMD Ryzen AI 9 365 (10C/20T, 4× Zen 5 + 6× Zen 5c, up to 5.0 GHz)
- **GPU:** Radeon 880M (12 CU, RDNA 3.5)
- **RAM:** 24GB LPDDR5x (soldered)

### 2026: UM5606GA (Gorgon Point)
- **CPU:** AMD Ryzen AI 9 465 (10C/20T, 4× Zen 5 + 6× Zen 5c, up to 5.0 GHz)
- **GPU:** Radeon 880M (12 CU, RDNA 3.5, up to 3.1 GHz)
- **RAM:** Up to 32GB LPDDR5x-8533 (soldered)
- **NPU:** 50 TOPS XDNA 2

---

## Common Specifications

- **Display:** 16" 3K OLED (2880×1800), 120Hz, 16:10, touch, 0.2ms response
  - DCI-P3 100%, Pantone Validated, DisplayHDR True Black 1000
  - 2024 model: ~391 cd/m² SDR, ~600 cd/m² HDR peak
  - 2026 model: ~500 cd/m² SDR, ~1,100 cd/m² HDR peak (significant upgrade)
  - PWM: 480 Hz (2024) / 960 Hz (2026)
- **Weight:** 1.5 kg (3.31 lbs)
- **Thickness:** 1.1 cm at thinnest point
- **Battery:** 78 Wh (2024) / 83 Wh (2026), 65W USB-C charger (2024) / 68W (2026)
- **Ports:** 2× USB4, 1× USB-A 3.2, HDMI 2.1, microSD UHS-II
- **Connectivity:** Wi-Fi 7 (MediaTek MT7925), Bluetooth 5.4
- **Material:** Ceraluminum lid (ceramic-aluminum composite — scratch/stain resistant, matte finish)

---

## Sustained CPU Performance

### Power Configuration

| Parameter | 2024 (HX 370) | 2024 (AI 9 365) | 2026 (AI 9 465) |
|-----------|---------------|------------------|------------------|
| PL2 (Burst) | 33W | 33W | 45W |
| PL1 (Sustained) | **28W** | **28W** | **35W** |
| Whisper mode | ~10W | ~10W | TBD |
| Standard mode | 15–28W | 15–28W | TBD |

Source: [NotebookCheck 2026 review](https://www.notebookcheck.net/The-perfect-everyday-laptop-with-AMD-Ryzen-400-Asus-Zenbook-S16-OLED-review.1221965.0.html), [UltrabookReview](https://www.ultrabookreview.com/68996-asus-zenbook-s16-review/)

### Benchmark Scores

#### 2024 Model — Ryzen AI 9 HX 370

| Benchmark | Score | Notes |
|-----------|-------|-------|
| Cinebench R23 Multi (best) | **17,961** | Single best run |
| Cinebench R23 Multi (10-min sustained) | **15,266** | ~15% drop from peak |
| Cinebench R23 Single | 1,965–2,003 | |
| Cinebench 2024 Multi (10-min) | **926** | Sustained |
| Cinebench 2024 Single | 114–115 | |
| Geekbench 6 Multi | 13,389 | |
| Geekbench 6 Single | 2,828 | |

Source: [StorageReview](https://www.storagereview.com/review/zen5-mobile-performance-the-amd-ryzen-ai-9-hx-370-asus-zenbook-s16-review), [UltrabookReview](https://www.ultrabookreview.com/68996-asus-zenbook-s16-review/)

#### 2024 Model — Ryzen AI 9 365

| Benchmark | Score | Notes |
|-----------|-------|-------|
| Cinebench R23 Multi | 11,462 | Constrained by 28W PL1 |
| Cinebench R23 Single | 1,942 | |
| Cinebench R15 Multi (loop avg) | 1,724 | Range: 1,686–1,949 |

Source: [NotebookCheck](https://www.notebookcheck.net/Asus-ZenBook-S-16-OLED-laptop-review-Premiere-for-Ryzen-AI-9-365-and-Radeon-880M.885785.0.html)

#### 2026 Model — Ryzen AI 9 465

| Benchmark | Score | Notes |
|-----------|-------|-------|
| Cinebench R23 Multi | **17,580** | Higher PL1 (35W) |
| Cinebench R23 Single | 1,997 | |
| Cinebench 2024 Multi | **953** | |
| Cinebench 2024 Single | 115 | |

Source: [NotebookCheck 2026 review](https://www.notebookcheck.net/The-perfect-everyday-laptop-with-AMD-Ryzen-400-Asus-Zenbook-S16-OLED-review.1221965.0.html)

### Throttling Behavior

- **No thermal throttling** during 30-minute Cinebench R23 loop (HX 370 model)
- Sustained 28W in Performance mode (2024); sustained 35W in Performance mode (2026)
- Thermal throttling occurs on flat surfaces during extended gaming (>85°C), with automatic power limiting for 10–15 seconds before returning to full power
- Standard and Whisper modes showed erratic power fluctuation between power caps (early firmware)
- The 10-min sustained Cinebench R23 score of ~15,266 vs burst ~17,961 shows a ~15% drop, consistent with thermal stabilization at 28W PL1

### Context for Workloads (Kernel Compilation, PySpark)

The 28W sustained PL1 on the 2024 model is the key constraint. For prolonged multi-core loads (kernel compilation, large PySpark jobs), expect performance to settle around the 15,000–16,000 Cinebench R23 multi-core range rather than the peak ~18,000. The 2026 model with 35W PL1 should sustain closer to ~17,500.

For comparison:
- Framework 16 (Ryzen 7 7840HS, 54W sustained): ~16,000 R23 multi
- ThinkPad T14s Gen 6 (Ryzen AI 7 PRO, 28W): ~12,000 R23 multi
- MacBook Pro 14 (M3 Pro): ~12,500 R23 multi

The Zenbook S 16 with HX 370 at 28W delivers competitive sustained multi-core performance for a 1.5 kg ultrabook.

---

## Thermal and Noise Data

### Cooling System Design
- 37% enlarged 3D vapor chamber (CNC-milled)
- Redesigned dual-fan array
- Additional fan chamber outlets to optimize heat dissipation
- Keyboard area temperature reduced by up to 4°C vs previous gen

### Fan Noise Measurements

| Mode/Load | Noise Level | Source |
|-----------|-------------|--------|
| Idle (fans off) | **24–26 dB(A)** | NotebookCheck |
| Whisper mode under load | **~30 dB(A)** | UltrabookReview |
| 4K video streaming | **~34.5 dB(A)** | Windows Central |
| Standard mode under load | **35–36 dB(A)** | NotebookCheck, UltrabookReview |
| Performance mode under load | **~40 dB(A)** | UltrabookReview |
| Performance mode (gaming) | **~43 dB(A)** | NotebookCheck (AI 9 365) |
| Full Speed mode (max fans) | **44–52.5 dB(A)** | Windows Central, NotebookCheck |

Note: The 2026 model with 35W PL1 has "significantly louder fans" in Performance mode according to NotebookCheck.

### Surface Temperatures

| Condition | Temperature | Notes |
|-----------|-------------|-------|
| Daily use (streaming) | <40°C | Comfortable |
| Gaming (top surface hotspot) | ~50°C | WASD area stays reasonable |
| Gaming (bottom) | ~60°C | Hot on lap |
| CPU hotspot (gaming) | Mid-80s°C | Acceptable |
| CPU (severe stress) | 90–95°C | Per NotebookCheck |
| User-contact areas | <40°C typically | Good thermal isolation |

Sources: [UltrabookReview](https://www.ultrabookreview.com/68996-asus-zenbook-s16-review/), [Windows Central](https://www.windowscentral.com/hardware/laptops/asus-zenbook-s-16-um5606-review), [NotebookCheck](https://www.notebookcheck.net/Asus-ZenBook-S-16-OLED-laptop-review-Premiere-for-Ryzen-AI-9-365-and-Radeon-880M.885785.0.html)

---

## Linux Compatibility

### Kernel Requirements

| Feature | Minimum Kernel | Notes |
|---------|---------------|-------|
| Basic boot | 6.10+ | With amdgpu workaround |
| Audio (speakers not tinny) | **6.13+** | 4-speaker array needs this |
| WiFi resume from s2idle | **6.14+** | MT7925 re-init fix |
| PSR2-SU display fix | **6.15+** (expected) | Disabled by default in future kernels |
| NPU support | 6.19-rc1+ | Plus private XRT/RyzenAI-SW branches |

**Recommended minimum: Linux 6.14+ with latest linux-firmware**

### Required Boot Parameters

```
amdgpu.dcdebugmask=0x600
```
Disables PSR2-SU (Panel Self Refresh), which causes system deadlocks every few hours without this parameter. A less aggressive option (`0x200`) disables only PSR2-SU while keeping legacy PSR enabled.

### BIOS Settings
- Set UMA buffer from "Auto" to **2GB** — required for s2idle suspend to work properly

### Component Status

| Component | Status | Notes |
|-----------|--------|-------|
| Display (OLED) | **Working** | Requires `amdgpu.dcdebugmask=0x600` to prevent PSR hangs |
| WiFi (MT7925) | **Working** (6.14+) | Unstable on older kernels; linux-firmware Sept 2024+ patch needed |
| Bluetooth (MT7925) | **Partial** | May fail after s2idle resume; needs external kernel patch on <6.14 |
| Audio (speakers) | **Working** (6.13+) | Tinny/broken on <6.13; Fedora-specific ALSA issue noted |
| Audio (4.0 routing) | **Manual fix** | Tweeters/subwoofer misidentified; needs PipeWire config for proper 4.0 routing |
| Suspend (s2idle) | **Working** (6.14+) | Only s2idle supported (no S3 deep sleep); screen freezes ~10s on resume with <6.14 |
| Keyboard backlight | **Broken** | WMI/ACPI-based; fades continuously, controls unresponsive after Linux boot |
| Touchpad | **Working** | No reported issues |
| GPU (Radeon 890M/880M) | **Working** | RDNA 3.5; amdgpu driver |
| Webcam | **Working** | No reported issues |

### Known Issues and Workarounds

1. **PSR2-SU Deadlocks** — Most critical issue. Without `amdgpu.dcdebugmask=0x600`, the machine deadlocks every couple of hours. Fixed by disabling PSR2-SU via boot parameter. Expected to be disabled by default in future kernels.

2. **WiFi instability on older kernels** — MT7925 firmware updated in linux-firmware Sept 2024 release. Consider switching from wpa_supplicant to iwd if issues persist.

3. **Bluetooth resume failure** — After s2idle resume, Bluetooth controller may vanish. Caused by aggressive USB autosuspend for the MediaTek controller during wake. Workaround: rebind the USB device after resume.

4. **Audio channel routing** — The 4 speakers are misidentified as front/rear. Fix requires manual PipeWire configuration routing stereo to 4.0 surround through ALSA device remapping.

5. **Keyboard backlight** — Connected via WMI/ACPI, not USB HID. Backlight controls do not respond after Linux boot (works after Windows reboot). EC probe investigation needed. No fix available.

6. **120Hz power consumption** — The 2880x1800@120Hz mode uses a very small vertical blanking interval, causing AMDGPU to keep GPU memory/fabric clocks high even at idle, increasing power draw. Power-saver profile + PSR can reduce idle to ~6–8W.

7. **Standby battery drain** — s2idle standby consumes ~1.0–1.1W, translating to ~30% daily drain. This is an inherent limitation of s2idle (no S3 support in BIOS).

### Distribution-Specific Notes

- **Arch Linux:** Best documented via the [ArchWiki ASUS Zenbook UM5606 page](https://wiki.archlinux.org/title/ASUS_Zenbook_UM5606). Add kernel parameter at installation time.
- **Fedora:** Specific ALSA issue with audio; `sudo dnf upgrade` resolves. Kernel 6.13+ ships in Fedora 41+. Fedora 42 (kernel 6.14+) should work well.
- **Ubuntu 24.04:** Tested with kernel 6.8 (HWE kernel) — needs manual kernel upgrade to 6.13+ for audio and 6.14+ for WiFi resume. Ubuntu 24.10 ships 6.11 (still needs audio fix). **Ubuntu 25.04+ recommended** for out-of-box experience.
- **General:** One user described reaching "almost Mac-like experience" stability as of April 2025 with kernel 6.13+ on Fedora.

### Power Management on Linux (Phoronix)

Phoronix tested platform profiles on the UM5606WA under Linux:
- **Performance mode:** +5% over balanced, ~1W higher average power, ~5W higher peak
- **Balanced mode:** "Very reasonable for the right mix of power and performance"
- **Power-saver mode:** 97% of balanced performance; similar average watts but more time in low-power states
- **Idle power (Linux):** ~6.8W minimum (60Hz, 1% brightness, KDE)

Source: [Phoronix](https://www.phoronix.com/review/asus-zenbook-s16-power)

---

## 2026 Refresh (Gorgon Point) — What Changed

The 2026 UM5606GA is a **minor refresh**, not a new generation:

| Aspect | 2024 (Strix Point) | 2026 (Gorgon Point) | Change |
|--------|--------------------|--------------------|--------|
| CPU | Ryzen AI 9 HX 370 (12C/24T) | Ryzen AI 9 465 (10C/20T) | Different SKU; 465 is refresh of 365, not HX 370 |
| PL1 sustained | 28W | **35W** | +7W headroom |
| PL2 burst | 33W | **45W** | +12W headroom |
| RAM speed | LPDDR5x-7500 | LPDDR5x-8533 | Marginal gain |
| Display (SDR) | ~391 cd/m² | **~500 cd/m²** | Significant brightness upgrade |
| Display (HDR) | ~600 cd/m² | **~1,100 cd/m²** | Nearly 2x brighter |
| PWM frequency | 480 Hz | **960 Hz** | Better for PWM-sensitive users |
| Battery | 78 Wh | **83 Wh** | +5 Wh |
| Weight | 1.5 kg | 1.53 kg | Negligible |

**Key takeaway:** Gorgon Point is a minimal Strix Point refresh — slightly higher clocks, faster memory support, but similar CPU and GPU capabilities. The real improvements are in the display (much brighter OLED, higher PWM) and increased power limits. Cinebench R23 multi-core went from ~15,266 sustained (HX 370 at 28W) to ~17,580 (AI 9 465 at 35W), a meaningful but not dramatic gain.

The top-end HX 470 (12C/24T, equivalent to HX 370 refresh) may appear in some configurations but has not been confirmed in the Zenbook S 16.

Sources: [Trusted Reviews](https://www.trustedreviews.com/reviews/asus-zenbook-s-16-2026), [UltrabookReview](https://www.ultrabookreview.com/74512-asus-zenbook-s16-s14/), [NotebookCheck](https://www.notebookcheck.net/The-perfect-everyday-laptop-with-AMD-Ryzen-400-Asus-Zenbook-S16-OLED-review.1221965.0.html), [HitechCentury](https://hitechcentury.com/asus-zenbook-s16-review-um5606-2026/)

---

## Summary Assessment

**Strengths:**
- Excellent sustained multi-core for a 1.5 kg ultrabook (28W sustained, no throttling)
- Outstanding OLED display (100% DCI-P3, 120Hz, excellent contrast)
- Premium build with scratch-resistant Ceraluminum
- Quiet under light loads; reasonable under sustained load
- Linux works well with kernel 6.14+ and proper boot parameters

**Weaknesses:**
- 28W PL1 limits absolute sustained performance (2024 model)
- Linux requires kernel parameter to prevent PSR deadlocks (critical)
- Keyboard backlight broken on Linux (no fix)
- s2idle only (no S3 deep sleep) — ~30% daily standby drain
- 32GB RAM max (soldered)
- Speakers require manual PipeWire configuration on Linux for proper channel routing

**For kernel compilation / PySpark workloads:**
The 28W sustained TDP on the 2024 HX 370 model delivers ~15,000–16,000 Cinebench R23 multi sustained, which is competitive for a thin-and-light. The 2026 model at 35W sustains ~17,500. For truly sustained heavy compilation, machines with higher PL1 (e.g., ProArt PX13 at 65W, Framework 16 at 54W) will be meaningfully faster. But for a 1.5 kg travel machine that also handles serious CPU work, the Zenbook S 16 is a strong contender.