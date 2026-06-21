from __future__ import annotations

import re
from typing import Any

from pydantic import Field, field_serializer
from pydantic_settings import BaseSettings, SettingsConfigDict

from . import __version__


class SearchConfig(BaseSettings):
    name: str
    url: str
    recursive: bool = True


class FilterConfig(BaseSettings):
    exclude_topads: bool = True
    exclude_patterns: list[re.Pattern[str]] = Field(default_factory=list)
    price_min: int | None = None
    price_max: int | None = None

    @field_serializer("exclude_patterns")
    def serialize_exclude_patterns(self, patterns: list[re.Pattern[str]], _info: Any) -> list[str]:
        return [p.pattern for p in patterns]


class NotificationsConfig(BaseSettings):
    pushover: dict | None = None
    ntfy_sh: dict | None = None
    telegram: dict | None = None


class Config(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="EK_",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    filter: FilterConfig = Field(default_factory=FilterConfig)
    notifications: NotificationsConfig = Field(default_factory=NotificationsConfig)
    searches: list[SearchConfig] = Field(default_factory=list)

    # Global settings
    request_delay_min: float = 1.5
    request_delay_max: float = 4.0
    request_timeout: int = 30

    # Load balancing and resilience
    use_global_lock: bool = True
    lock_timeout: int = 12
    max_concurrent_pages: int = 5
    data_store_max_days: int = 7
    download_images: bool = True

if __name__ == "__main__":
    print("Config loaded successfully")
