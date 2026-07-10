# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: GardenLog
import json, os


def load_garden_data(filepath):
    if not os.path.exists(filepath):
        print(f"Файл не найден: {filepath}")
        return None
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, dict):
            keys = sorted(data.keys())
            print(f"Загружено из JSON ({len(keys)} секций): {keys}")
            return data
        else:
            print("Ожидается словарь в файле")
            return None
    except json.JSONDecodeError as e:
        print(f"Ошибка JSON: {e}")
        return None
    except PermissionError:
        print("Нет доступа к файлу")
        return None
