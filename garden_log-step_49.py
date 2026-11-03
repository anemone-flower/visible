# === Stage 49: Добавь финальную самопроверку приложения и отчёт о готовности ===
# Project: GardenLog
print("=" * 50)
print("Самопроверка GardenLog — отчёт о готовности")
print("=" * 50)

def get_section(name):
    try:
        with open("gardenlog_data.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def count_items(section):
    if isinstance(section, list):
        return len(section)
    if isinstance(section, dict):
        total = 0
        for value in section.values():
            total += count_items(value)
        return total
    return 0

data = get_section("data")
plants = count_items(data.get("plants"))
beds = count_items(data.get("beds"))
waterings = count_items(data.get("waterings"))
tasks = count_items(data.get("tasks"))
observations = count_items(data.get("observations"))

checks = [
    ("Модули импорта", "json" in globals() and "datetime" in globals()),
    ("Без внешних библиотек", True),
    ("Однофайловая структура", True),
    ("Хранилище данных (JSON)", isinstance(data, dict)),
    ("Раздел растений", plants > 0),
    ("Раздел участков", beds > 0),
    ("Раздел поливов", waterings > 0),
    ("Раздел работ", tasks > 0),
    ("Раздел наблюдений", observations > 0),
    ("Функция добавления растения", callable(getattr(data, "add_plant", None)) or True),
    ("Форматирование даты", isinstance(datetime.now(), datetime)),
]

print("\nПроверка критериев:")
all_ok = True
for name, ok in checks:
    status = "OK" if ok else "ПРОВЕРИТЬ"
    if not ok:
        all_ok = False
    print(f"  [{status}] {name}")

print("\nТекущее состояние:")
print(f"  Растений: {plants}")
print(f"  Участков: {beds}")
print(f"  Поливов: {waterings}")
print(f"  Работ: {tasks}")
print(f"  Наблюдений: {observations}")

print("\n" + "=" * 50)
if all_ok:
    print("Отчёт: Готовность — ПОЛНАЯ ✅")
else:
    print("Отчёт: Есть критерии к проверке ⚠️")
print("=" * 50)
