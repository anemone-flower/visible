# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: GardenLog
import json, os
from dataclasses import dataclass, field
from datetime import date
from typing import Optional

@dataclass
class Plant:
    name: str
    species: str
    location: str
    watered: bool = False
    last_watered: Optional[date] = None
    
    def to_dict(self): return {"name": self.name, "species": self.species, "location": self.location, "watered": self.watered, "last_watered": self.last_watered.isoformat() if self.last_watered else None}
    
@dataclass  
class GardenLog:
    plants: list[Plant] = field(default_factory=list)
    logs: list[str] = field(default_factory=list)
    
    def save(self): os.makedirs("garden", exist_ok=True); path="garden/data.json"; json.dump([p.to_dict() for p in self.plants], open(path, "w"), indent=2, default=str)
    
def init_demo():
    app = GardenLog()
    demo_plants = [Plant("Tomato Bush", "Solanum lycopersicum", "Bed A-1", True, date(2024, 6, 15)), Plant("Rose Bush", "Rosa gallica", "Bed B-3", False, None)]
    app.plants.extend(demo_plants)
    app.logs.append(f"Init: Loaded {len(app.plants)} demo plants.")
    app.save()
    return app

if __name__ == "__main__": print("GardenLog initialized."); app = init_demo(); print(f"Current logs:\n{app.logs}")
