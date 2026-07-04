# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: GardenLog
import json, sys

def load_initial_data(json_string):
    try:
        data = json.loads(json_string)
        if not isinstance(data, dict):
            raise ValueError("JSON должен содержать объект")
        
        # Валидация структуры (минимум: участки и растения)
        required_keys = {"plots", "plants"}
        missing = required_keys - set(data.keys())
        if missing:
            raise KeyError(f"Отсутствуют ключи: {missing}")
        
        # Нормализация типов данных для надежности
        for plot in data.get("plots", []):
            if not isinstance(plot, dict) or "id" not in plot:
                raise ValueError("Некорректный формат участка")
            
        for plant in data.get("plants", []):
            if not isinstance(plant, dict) or "plot_id" not in plant:
                raise ValueError("Некорректный формат растения")

        return data
    except json.JSONDecodeError as e:
        print(f"[Ошибка] Неверный JSON: {e}")
        sys.exit(1)

# Пример использования с тестовой строкой (замените на ваш источник данных)
initial_json = '''
{
  "plots": [
    {"id": "P001", "name": "Грядка №1", "area_sqm": 4.5, "status": "active"},
    {"id": "P002", "name": "Парник", "area_sqm": 6.0, "status": "planned"}
  ],
  "plants": [
    {"id": "PLT_01", "plot_id": "P001", "species": "tomato_siberian", "age_days": 45, "watered_at": null},
    {"id": "PLT_02", "plot_id": "P001", "species": "pepper_bell", "age_days": 30, "watered_at": "2023-10-27"}
  ],
  "logs": [
    {"id": "LOG_001", "plant_id": "PLT_01", "type": "observation", "content": "Первые плоды завязались", "timestamp": "2023-10-26T14:30"}
  ]
}'''

# Загрузка и вывод структуры данных
garden_data = load_initial_data(initial_json)
print(f"Загружено {len(garden_data['plots'])} участков и {len(garden_data['plants'])} растений.")
