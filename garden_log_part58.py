# === Stage 58: Добавь простую систему пользовательских представлений списка ===
# Project: GardenLog
def get_view(data, title, get_id, get_title, get_created, sort_key=None, order='asc', limit=None):
    """Простое пользовательское представление списка."""
    items = sorted(data, key=sort_key, reverse=(order == 'desc')) if sort_key else list(data)
    rows = []
    for item in items:
        rid = get_id(item)
        title_ = get_title(item)
        created = get_created(item)
        rows.append(f"[{rid}] {title_} ({created})")
    if limit:
        rows = rows[:limit]
    print(f"\n==== {title} ====")
    for r in rows:
        print(r)
    print(f"Всего: {len(items)}")
    print()
    return rows
