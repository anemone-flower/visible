# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: GardenLog
def backup_data_file(filepath):
    """Создаёт резервную копию файла данных."""
    try:
        import shutil
        backup_path = filepath + ".bak"
        shutil.copy2(filepath, backup_path)
        print(f"Резервная копия создана: {backup_path}")
        return backup_path
    except Exception as e:
        print(f"Ошибка резервного копирования: {e}")
        return None
