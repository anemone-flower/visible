# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: GardenLog
def archive_records(records, cutoff_days=180):
    """Archive records older than cutoff_days and return the list of archived entries."""
    from datetime import datetime, timedelta
    now = datetime.now()
    cutoff = (now - timedelta(days=cutoff_days)).date()
    archived = [r for r in records if isinstance(r.get("date"), str) and datetime.strptime(r["date"], "%Y-%m-%d").date() < cutoff]
    active = [r for r in records if isinstance(r.get("date"), str) and datetime.strptime(r["date"], "%Y-%m-%d").date() >= cutoff]
    return {"archived": archived, "active": active}
