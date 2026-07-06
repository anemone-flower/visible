# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: GardenLog
import json, datetime

def export_to_json(garden):
    now = garden.now or datetime.date.today().isoformat()
    data = {
        "garden": garden.name,
        "location": garden.location,
        "created": garden.created.isoformat() if hasattr(garden.created, 'isoformat') else str(garden.created),
        "last_updated": now,
        "stats": {"plants": len(garden.plants), "plots": len(garden.plots)},
        "plants": [
            {
                "id": p.id,
                "name": p.name,
                "plot_id": p.plot_id,
                "sown_date": p.sown_date.isoformat() if hasattr(p.sown_date, 'isoformat') else str(p.sown_date),
                "days_to_harvest": p.days_to_harvest,
                "harvested": p.harvested,
                "notes": p.notes or "",
            } for p in garden.plants
        ],
        "plots": [
            {
                "id": pl.id,
                "name": pl.name,
                "area_m2": pl.area_m2,
                "plants": [p.id for p in pl.plants],
            } for pl in garden.plots
        ],
        "waterings": [
            {
                "id": w.id,
                "plant_id": w.plant_id,
                "date": w.date.isoformat() if hasattr(w.date, 'isoformat') else str(w.date),
                "amount_ml": w.amount_ml,
            } for w in garden.waterings
        ],
        "works": [
            {
                "id": wrk.id,
                "plot_id": wrk.plot_id,
                "date": wrk.date.isoformat() if hasattr(wrk.date, 'isoformat') else str(wrk.date),
                "description": wrk.description or "",
            } for wrk in garden.works
        ],
        "observations": [
            {
                "id": obs.id,
                "plant_id": obs.plant_id,
                "date": obs.date.isoformat() if hasattr(obs.date, 'isoformat') else str(obs.date),
                "description": obs.description or "",
            } for obs in garden.observations
        ],
    }
    return json.dumps(data, indent=2, ensure_ascii=False)
