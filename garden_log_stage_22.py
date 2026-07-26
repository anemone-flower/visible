# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: GardenLog
def check_overdue_reminders(reminders):
    today = datetime.date.today()
    overdue = [r for r in reminders if r.get("date") and r["date"] < today]
    return overdue
