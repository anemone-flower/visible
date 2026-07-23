# === Stage 20: Добавь восстановление записей из архива ===
# Project: GardenLog
import json, os

def restore_from_archive(archive_path):
    if not archive_path or not os.path.exists(archive_path):
        return 0
    try:
        with open(archive_path, 'r', encoding='utf-8') as f:
            records = json.load(f)
        for rec in records:
            existing = next((r for r in garden_log if r['id'] == rec.get('id')), None)
            if not existing:
                garden_log.append(rec)
    except Exception:
        pass
    return len(garden_log) - 1 if garden_log else 0
