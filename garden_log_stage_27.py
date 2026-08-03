# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: GardenLog
def reset_demo_data():
    """Сбросить все данные к демо-состоянию."""
    global plants, plots, watering_logs, work_logs, observations, active_plot_id
    demo_plants = [
        {"id": 1, "name": "Томат", "species": "Cherry Tomato", "sown_date": "2024-05-10"},
        {"id": 2, "name": "Огурец", "species": "F1 Hybrid", "sown_date": "2024-05-12"},
        {"id": 3, "name": "Морковь", "species": "Nantes", "sown_date": "2024-06-01"},
    ]
    demo_plots = [
        {"id": 1, "name": "Северный", "area_sqm": 4.5},
        {"id": 2, "name": "Южный", "area_sqm": 3.8},
    ]
    watering_logs = []
    work_logs = [
        {"date": "2024-07-15", "description": "Высажены томаты и огурцы"},
        {"date": "2024-07-20", "description": "Прополка и рыхление"},
    ]
    observations = []
    active_plot_id = 1
    plants = demo_plants
    plots = demo_plots


def clear_all_state():
    """Полная очистка: удалить все данные."""
    global plants, plots, watering_logs, work_logs, observations, active_plot_id
    plants.clear()
    plots.clear()
    watering_logs.clear()
    work_logs.clear()
    observations.clear()
    active_plot_id = None
