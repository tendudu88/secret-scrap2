#!/usr/bin/env python3
import argparse
import json
from pathlib import Path

BASE_DIR = Path("/app")

def get_frequency_key(seconds: int) -> str:
    if seconds <= 60:
        return f"high_{seconds}s"
    elif seconds <= 900:
        return f"medium_{seconds//60}m"
    else:
        return f"low_{seconds//60}m"

# ... (rest of the management script with lock and supervisor support)

print("Management script loaded")
