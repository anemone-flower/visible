# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: GardenLog
import json, os

DB_FILE = "garden_log.json"

def save_to_file(items):
    with open(DB_FILE, 'w') as f:
        json.dump(items, f, indent=2)
    print(f"[GardenLog] Данные сохранены в {DB_FILE} ({len(items)} записей)")
