"""Search URL Generator for kleinanzeigen.de"""
from __future__ import annotations

import urllib.parse
from typing import Optional

def generate_search_url(
    keyword: str,
    location: Optional[str] = None,
    price_min: Optional[int] = None,
    price_max: Optional[int] = None,
    category: Optional[str] = None,
    sort: str = "date",
) -> str:
    """Generate kleinanzeigen.de search URL."""
    # ... (full implementation)
    pass
