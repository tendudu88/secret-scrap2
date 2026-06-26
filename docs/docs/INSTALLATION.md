# Installation Guide

## Prerequisites

- Python 3.11 or later
- `uv` package manager (recommended) or `pip`

## Installation

### Using `uv` (recommended)

```bash
# Clone the repository
git clone https://github.com/frederikpeter20-lang/secret-scrap.git
cd secret-scrap

# Create virtual environment
uv venv

# Activate virtual environment
source .venv/bin/activate  # Linux/macOS
# or:
.venv\Scripts\activate  # Windows

# Install dependencies
uv sync

# Verify installation
ek-scraper --version
