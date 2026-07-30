# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: GardenLog
def parse_date(date_str):
    """Разрешённые форматы: YYYY-MM-DD, DD.MM.YYYY, D/M/YYYY."""
    import datetime
    for fmt in ("%Y-%m-%d", "%d.%m.%Y", "%d/%m/%Y"):
        try:
            return datetime.date.fromisoformat(date_str.replace(".", "-").replace("/", "-"))
        except ValueError:
            continue
    raise ValueError(f"Некорректная дата: '{date_str}'. Используйте YYYY-MM-DD, DD.MM.YYYY или D/M/YYYY.")
