# === Stage 17: Добавь группировку записей по категориям ===
# Project: GardenLog
def get_records_by_category(records, category):
    return [r for r in records if r.get("category") == category]
