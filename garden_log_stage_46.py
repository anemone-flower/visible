# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: GardenLog
def migrate_v1_to_v2(old_data):
    """
    Миграция структуры данных с версии 1 на версию 2.
    
    В версии 1:
    - растения: список словарей с полями: id, name, latin_name, sowing_date, description, care_notes
    
    В версии 2:
    - растения: список словарей с полями: id, name, latin_name, sowing_date, description, care_notes, last_watered, last_water_date
    
    Также добавляем поля к участкам: id, name, size, description, plants, last_watered, last_water_date
    
    В версии 1 у растений нет полей last_watered и last_water_date.
    При миграции эти поля устанавливаются в None.
    """
    migrated_plants = []
    for plant in old_data.get('plants', []):
        new_plant = {
            'id': plant.get('id'),
            'name': plant.get('name'),
            'latin_name': plant.get('latin_name'),
            'sowing_date': plant.get('sowing_date'),
            'description': plant.get('description'),
            'care_notes': plant.get('care_notes'),
            'last_watered': plant.get('last_watered', None),
            'last_water_date': plant.get('last_water_date', None)
        }
        migrated_plants.append(new_plant)
    
    migrated_plots = []
    for plot in old_data.get('plots', []):
        new_plot = {
            'id': plot.get('id'),
            'name': plot.get('name'),
            'size': plot.get('size'),
            'description': plot.get('description'),
            'plants': plot.get('plants', []),
            'last_watered': plot.get('last_watered', None),
            'last_water_date': plot.get('last_water_date', None)
        }
        migrated_plots.append(new_plot)
    
    new_data = {
        'version': 2,
        'created_at': old_data.get('created_at'),
        'updated_at': old_data.get('updated_at'),
        'plants': migrated_plants,
        'plots': migrated_plots,
        'irrigations': old_data.get('irrigations', []),
        'works': old_data.get('works', []),
        'observations': old_data.get('observations', [])
    }
    return new_data
