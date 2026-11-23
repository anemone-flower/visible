# === Stage 57: Добавь массовое удаление с подтверждением через параметр ===
# Project: GardenLog
def bulk_delete(items, confirm=True):
    if confirm:
        print(f"Удалить {len(items)} элементов? (y/n): ", end="")
        response = input().strip().lower()
        if response != 'y':
            return 0
    for item in items:
        del item
    print(f"Удалено элементов: {len(items)}")
    return len(items)
