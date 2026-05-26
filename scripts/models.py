from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

LaptopStatus = Literal[
    "recommended", "available", "not_recommended", "announced", "excluded"
]


class StrictModel(BaseModel):
    model_config = ConfigDict(extra="forbid")


class CPU(StrictModel):
    name: str
    cores: int
    threads: int
    arch: str
    boost_ghz: float | None = None


class GPU(StrictModel):
    name: str
    type: Literal["integrated", "discrete"]
    compute_units: int | None = None


class PowerLimits(StrictModel):
    pl1_w: float
    pl2_w: float
    battery_w: float | None = None


class Benchmarks(StrictModel):
    cinebench_r23_multi: int | None = None
    cinebench_r23_multi_sustained: int | None = None
    cinebench_r23_single: int | None = None
    cinebench_r15_multi: int | None = None
    cinebench_2024_multi: int | None = None
    cinebench_2024_single: int | None = None
    geekbench6_multi: int | None = None
    geekbench6_single: int | None = None


class Variant(StrictModel):
    year: int
    sku: str | None = None
    status: LaptopStatus | None = None
    weight_kg: float | None = None
    cpu: CPU
    gpu: GPU | None = None
    ram_gb: int
    ram_type: str | None = None
    ram_upgradeable: bool = False
    battery_wh: float | None = None
    power: PowerLimits
    benchmarks: Benchmarks = Field(default_factory=Benchmarks)


class Display(StrictModel):
    size_in: float
    resolution: str | None = None
    panel: str | None = None
    refresh_hz: int | None = None
    touch: bool = False
    aspect_ratio: str | None = None
    brightness_nits: int | None = None
    contrast: int | None = None


class NoiseLevel(StrictModel):
    """Fan noise at different power profiles.

    idle_dba: fans off / desktop idle (often ≈ ambient)
    low_power_dba: whisper / silent / power-saver mode under load
    balanced_dba: standard / balanced mode under load
    performance_dba: performance / high-performance mode under load
    max_dba: turbo / full-speed / stress test peak
    """

    idle_dba: float | None = None
    low_power_dba: float | None = None
    balanced_dba: float | None = None
    performance_dba: float | None = None
    max_dba: float | None = None


class LinuxCompat(StrictModel):
    """Linux compatibility assessment.

    Status levels:
      excellent — works out of box on major distros, no workarounds, official support
      good — works with standard kernel, minor issues or easy workarounds
      fair — needs custom kernel, boot params, or has significant unresolved issues
      poor — major functionality broken, significant effort to get working
      unknown — not tested on Linux
    """

    status: Literal["excellent", "good", "fair", "poor", "unknown"]
    kernel_min: str | None = None
    boot_params: list[str] = Field(default_factory=list)
    notes: list[str] = Field(default_factory=list)
    issues: list[str] = Field(default_factory=list)


class Laptop(StrictModel):
    model: str
    slug: str
    manufacturer: str
    form_factor: Literal["clamshell", "convertible", "tablet"]
    status: LaptopStatus
    weight_kg: float
    battery_wh: float | None = None
    price_usd: int | None = None
    display: Display
    variants: list[Variant]
    noise: NoiseLevel = Field(default_factory=NoiseLevel)
    linux: LinuxCompat = Field(default_factory=lambda: LinuxCompat(status="unknown"))
    sources: list[str] = Field(default_factory=list)
