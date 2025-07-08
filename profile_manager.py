"""Utilities for saving and loading user profiles."""
import json
from pathlib import Path
from typing import Any, Dict


def load_profile(path: str) -> Dict[str, Any]:
    """Load a profile from a JSON file."""
    with open(path, "r") as f:
        return json.load(f)


def save_profile(path: str) -> Dict[str, Any]:
    """Interactively create a profile and save it to ``path``.

    Returns the created profile.
    """
    profile: Dict[str, Any] = {}
    profile["name"] = input("Name: ")
    profile["email"] = input("Email: ")
    skills = input("Comma-separated skills: ")
    profile["skills"] = [s.strip() for s in skills.split(",") if s.strip()]
    profile["experience"] = []
    while True:
        company = input("Company (leave blank to finish): ")
        if not company:
            break
        role = input("Role: ")
        years = input("Years: ")
        profile["experience"].append({"company": company, "role": role, "years": int(years)})

    with open(path, "w") as f:
        json.dump(profile, f, indent=2)
    return profile
