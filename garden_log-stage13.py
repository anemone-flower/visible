# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: GardenLog
def search_all(collection, query):
    """Поиск записей по нескольким полям без учёта регистра."""
    if not collection or not query:
        return []
    
    results = []
    for record in collection:
        match = True
        for field in query:
            if field.lower() not in str(record).lower():
                match = False
                break
        if match:
            results.append(record)
    return results

def search_by_field(collection, field_name, value):
    """Поиск записей по одному полю без учёта регистра."""
    if not collection or not field_name or not value:
        return []
    
    results = []
    for record in collection:
        if str(record.get(field_name)).lower() == str(value).lower():
            results.append(record)
    return results

def search_by_keyword(collection, keyword):
    """Поиск записей по ключевому слову без учёта регистра."""
    if not collection or not keyword:
        return []
    
    results = []
    for record in collection:
        if keyword.lower() in str(record).lower():
            results.append(record)
    return results
