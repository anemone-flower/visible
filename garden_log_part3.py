# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: GardenLog
class GardenLog:
    def __init__(self):
        self.plots = []
        self.plants = {}
        self.watering_logs = []
        self.work_logs = []
        self.observation_logs = []

    def add_plot(self, name, area_sqm):
        plot_id = len(self.plots) + 1
        self.plots.append({"id": plot_id, "name": name, "area_sqm": area_sqm})
        return plot_id

    def register_plant(self, plot_id, plant_name, species, date_added=None):
        if not date_added:
            from datetime import datetime
            date_added = datetime.now().strftime("%Y-%m-%d")
        key = f"{plot_id}_{plant_name}"
        self.plants[key] = {
            "id": len(self.plants) + 1,
            "plot_id": plot_id,
            "name": plant_name,
            "species": species,
            "date_added": date_added
        }

    def log_watering(self, plant_key, amount_liters):
        self.watering_logs.append({
            "plant_key": plant_key,
            "amount_liters": amount_liters,
            "timestamp": datetime.now().isoformat()
        })

    def log_work(self, plot_id, task_description, duration_minutes=None):
        entry = {
            "plot_id": plot_id,
            "task": task_description,
            "duration_minutes": duration_minutes or 0,
            "timestamp": datetime.now().isoformat()
        }
        self.work_logs.append(entry)

    def log_observation(self, plant_key, notes):
        self.observation_logs.append({
            "plant_key": plant_key,
            "notes": notes,
            "timestamp": datetime.now().isoformat()
        })
