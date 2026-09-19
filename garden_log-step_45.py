# === Stage 45: Добавь восстановление из резервной копии ===
# Project: GardenLog
def restore_backup(source_path, target_path):
    """Restore saved backup file to the current state."""
    if not os.path.exists(source_path):
        print(f"Backup not found: {source_path}")
        return False
    try:
        with open(source_path, 'w') as f:
            f.write(json.dumps(garden_data, indent=2))
        print(f"Backup restored to: {target_path}")
        return True
    except Exception as e:
        print(f"Restore failed: {e}")
        return False
