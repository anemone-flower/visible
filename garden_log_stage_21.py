# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: GardenLog
REMINDERS = []

def add_reminder(task: str, date: str):
    """Добавляет напоминание с датой."""
    REMINDERS.append({"task": task, "date": date})
    print(f"✅ Добавлено напоминание: {task} (дата: {date})")

def list_reminders():
    """Выводит все напоминания."""
    if not REMINDERS:
        print("📭 Напоминаний нет.")
    else:
        for i, r in enumerate(REMINDERS, 1):
            print(f"{i}. {r['task']} — {r['date']}")

def mark_done(index: int):
    """Отмечает напоминание как выполненное."""
    if not REMINDERS or index < 1:
        print("❌ Некорректный индекс.")
        return
    print(f"✅ {REMINDERS[index - 1]['task']} — отмечено как сделано")

if __name__ == "__main__":
    add_reminder("Попробовать новый сорт томатов", "2025-06-01")
    add_reminder("Подкормить розы", "2025-06-10")
    list_reminders()

    print("\n--- Тест mark_done ---")
    mark_done(1)
    list_reminders()
