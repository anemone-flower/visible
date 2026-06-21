# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: GardenLog
class GardenModel:
    def __init__(self):
        self.plants = {}
        self.pots = {}
        self.watering_logs = []
        self.works = []
        self.observations = []

    def validate_name(self, name: str) -> bool:
        return isinstance(name, str) and len(name.strip()) > 0

    def add_pot(self, pot_id: int, plant_type: str):
        if not self.validate_name(plant_type):
            raise ValueError("Тип растения должен быть непустой строкой")
        if pot_id in self.pots:
            raise ValueError(f"Участок {pot_id} уже существует")
        self.pots[pot_id] = {"type": plant_type, "watered": False}

    def water_pot(self, pot_id: int) -> bool:
        if pot_id not in self.pots:
            return False
        self.pots[pot_id]["watered"] = True
        self.watering_logs.append({"pot_id": pot_id, "timestamp": datetime.now()})
        return True

    def add_work(self, pot_id: int, description: str):
        if not self.validate_name(description):
            raise ValueError("Описание работы должно быть непустой строкой")
        self.works.append({"pot_id": pot_id, "description": description, "timestamp": datetime.now()})

    def add_observation(self, pot_id: int, note: str):
        if not self.validate_name(note):
            raise ValueError("Примечание должно быть непустой строкой")
        self.observations.append({"pot_id": pot_id, "note": note, "timestamp": datetime.now()})
