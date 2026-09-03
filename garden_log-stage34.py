# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: GardenLog
TEMPLATE_REGISTRY = {
    "watering": "Watering {plant_name} in {plot_name} - {date}",
    "work": "Garden work in {plot_name} - {date}",
    "observation": "Observation of {plant_name} - {date}",
    "harvest": "Harvest of {plant_name} - {date}",
}

def fill_template(template_name, **kwargs):
    template = TEMPLATE_REGISTRY.get(template_name)
    if not template:
        raise ValueError(f"Unknown template: {template_name}")
    return template.format(**kwargs)
