# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: GardenLog
def generate_summary(garden):
    """Генерирует краткую текстовую сводку по текущему состоянию сада."""
    lines = ["=== 🌱 СВОДКА ПО САДУ ===\n"]
    
    # Подсчёт растений
    plants_count = len(garden.get("plants", []))
    if plants_count:
        species = set(p["species"] for p in garden["plants"])
        lines.append(f"Растения: {plants_count} шт. ({', '.join(sorted(species))})\n")
    
    # Подсчёт участков и статус полива
    plots = garden.get("plots", [])
    if plots:
        watered_plots = [p for p in plots if p.get("watered")]
        lines.append(f"Участки: {len(plots)} шт. ({len(watered_plots)} политы)\n")
    
    # Последние работы
    works = garden.get("works", [])
    recent_works = works[-3:] if len(works) >= 3 else works
    if recent_works:
        lines.append(f"Последние работы:\n")
        for w in reversed(recent_works):
            date = w.get("date", "без даты")
            desc = w.get("description", "")
            lines.append(f"• {desc} ({date})\n")
    
    # Последние наблюдения
    observations = garden.get("observations", [])
    recent_obs = observations[-3:] if len(observations) >= 3 else observations
    if recent_obs:
        lines.append(f"Последние наблюдения:\n")
        for o in reversed(recent_obs):
            date = o.get("date", "без даты")
            desc = o.get("description", "")
            lines.append(f"• {desc} ({date})\n")
    
    return "".join(lines)
