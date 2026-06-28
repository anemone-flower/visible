# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: GardenLog
def filter_logs(status=None, category=None, tags=None):
    filtered = []
    for log in logs:
        if status and log.get('status') != status: continue
        if category and log.get('category') != category: continue
        if tags:
            log_tags = set(log.get('tags', [])).intersection(tags)
            if not log_tags: continue
        filtered.append(log)
    return filtered
