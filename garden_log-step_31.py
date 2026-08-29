# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: GardenLog
# GardenLog — Этап 31: Переключение активного пользовательского профиля
# Добавь этот блок в конец файла.

import json
from pathlib import Path

PROFILES_FILE = "profiles.json"
ACTIVE_PROFILE_FILE = "active_profile.json"

def load_profiles():
    if not Path(PROFILES_FILE).exists():
        return {"default": {"name": "default", "language": "ru"}}
    return json.loads(Path(PROFILES_FILE).read_text())

def save_profiles(profiles):
    Path(PROFILES_FILE).write_text(json.dumps(profiles, ensure_ascii=False, indent=2))

def save_active(active):
    Path(ACTIVE_PROFILE_FILE).write_text(json.dumps(active, ensure_ascii=False))

def get_active_profile():
    try:
        return json.loads(Path(ACTIVE_PROFILE_FILE).read_text())
    except Exception:
        return {"name": "default", "language": "ru"}

def switch_profile(profile_name):
    profiles = load_profiles()
    if profile_name not in profiles:
        profiles[profile_name] = {"name": profile_name, "language": "ru"}
    save_profiles(profiles)
    active = get_active_profile()
    active["name"] = profile_name
    save_active(active)
    return active

def list_profiles():
    return load_profiles()
