from __future__ import annotations

import logging
import pathlib
from typing import Any

import pydantic

_logger = logging.getLogger(__name__)

class AdItem(pydantic.BaseModel):
    id: str
    url: str
    title: str
    description: str
    location: str
    price: str
    is_top_ad: bool
    image_url: str | None = None
    pruneable: bool = pydantic.Field(default=True, exclude=True)

class DataStore:
    # ... (full implementation with pruning for last 7 days)

    def prune(self) -> None:
        # Aggressive pruning
        pass
