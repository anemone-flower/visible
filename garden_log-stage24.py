# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: GardenLog
def show_record(record):
    """Компактный вывод одной записи с деталями."""
    print(f"=== {record['type']} ({record.get('date', '?')}) ===")
    for k, v in record.items():
        if k not in ('id', 'timestamp'):
            print(f"  {k}: {v}")
