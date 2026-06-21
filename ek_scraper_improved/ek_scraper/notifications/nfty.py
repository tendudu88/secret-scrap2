from __future__ import annotations

import logging
from typing import Sequence

import httpx

from ..config import NtfyShConfig
from ..scraper import Result

_logger = logging.getLogger(__name__)

async def send_notifications(results: Sequence[Result], config: NtfyShConfig) -> None:
    """Send notifications via ntfy.sh."""
    # ... (full implementation)
    pass
