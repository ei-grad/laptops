# ASUS ProArt PX13 (HN7306)

## Model Variants

### 2024-2025: HN7306WV/WI/WU (Strix Point)
- **CPU:** AMD Ryzen AI 9 HX 370 (Strix Point, 12C/24T)
- **GPU:** NVIDIA RTX 4050/4060/4070 Laptop
- **RAM:** Up to 32GB LPDDR5X (soldered)

### 2026: HN7306 (Strix Halo)
- **CPU:** AMD Ryzen AI Max+ 395 (Strix Halo, 16C/32T)
- **GPU:** Integrated Radeon 8060S (40 CU) — no dGPU
- **RAM:** Up to 128GB unified memory
- **NPU:** 50 TOPS

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

#### 2026 Model (Strix Halo) Considerations

- AMD GPU driver should work (open source amdgpu)
- NPU support may be limited initially
- Kernel 6.12+ recommended for Strix Halo
- No dGPU simplifies driver setup

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

### Sources

#### Reviews
- [NotebookCheck ProArt PX13 Review](https://www.notebookcheck.net/Asus-ProArt-PX13-review-The-world-s-fastest-13-3-inch-2-in-1-thanks-to-AMD-Zen-5-and-RTX-4070-laptop.868429.0.html)
- [PCWorld ProArt PX13 Review](https://www.pcworld.com/article/2418049/asus-proart-px13-review.html)
- [UltrabookReview 12-Month Review](https://www.ultrabookreview.com/72323-asus-proart-px13-review/)
- [Windows Central ProArt PX13](https://www.windowscentral.com/laptops/asus-proart-px13-review)
- [UltrabookReview Strix Halo laptops](https://www.ultrabookreview.com/74193-asus-strix-halo-laptops-proart-tuf/)

#### Linux
- [Linux Hardware Database - PX13](https://linux-hardware.org/?probe=c0107457aa)
- [LinuxQuestions - Ubuntu 24.04 on PX13](https://www.linuxquestions.org/questions/linux-laptop-and-netbook-25/ubuntu-24-04-on-asus-proart-px13-hn7306wi_hn7306wi-4175751777-new/)
- [MT7925 Driver Documentation](https://wireless.docs.kernel.org/en/latest/en/users/drivers/mediatek.html)
- [MT7925 kernel support (LWN)](https://lwn.net/Articles/944390/)

---

