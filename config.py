"""Configuration management for Auto Apply."""
import json
import os
from pathlib import Path
from typing import Any, Dict

DEFAULT_CONFIG = {
    "api_key": os.getenv("OPENAI_API_KEY", ""),
    "letters_dir": "letters",
}


_CONFIG_PATH = Path("config.json")


def load_config() -> Dict[str, Any]:
    if _CONFIG_PATH.exists():
        with open(_CONFIG_PATH, "r") as f:
            data = json.load(f)
            DEFAULT_CONFIG.update(data)
    return DEFAULT_CONFIG
