# === Stage 55: Добавь мягкую проверку дубликатов при создании записей ===
# Project: GardenLog
def _is_duplicate(new_item, existing_items, key_attr, exclude_id=None):
    if exclude_id is not None:
        existing_items = [i for i in existing_items if i.get('id') != exclude_id]
    for existing in existing_items:
        if existing.get(key_attr) == new_item.get(key_attr):
            return True
    return False


def add_record(record_type, data, records_by_type, id_counter, key_attr=None):
    record_id = id_counter.pop()
    new_record = {'id': record_id, **data}
    existing = records_by_type.get(record_type, [])
    if key_attr and _is_duplicate(new_record, existing, key_attr):
        print(f"Запись с дублирующимся {key_attr} уже существует.")
        return None
    existing.append(new_record)
    return new_record
