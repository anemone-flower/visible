# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: GardenLog
def dry_run(operation, *args, **kwargs):
    """Выполняет операцию в режиме dry-run, не сохраняя изменения."""
    if operation == "add_plant":
        plant = Plant(**kwargs)
        return f"[DRY-RUN] Добавлено растение: {plant.name} (ID: {plant.id})"
    elif operation == "add_plot":
        plot = Plot(**kwargs)
        return f"[DRY-RUN] Добавлен участок: {plot.name} (ID: {plot.id})"
    elif operation == "water_plot":
        plot = Plot(**kwargs)
        return f"[DRY-RUN] Полив участка: {plot.name} на {plot.area} м²"
    elif operation == "add_work":
        work = Work(**kwargs)
        return f"[DRY-RUN] Добавлена работа: {work.name} (ID: {work.id})"
    elif operation == "add_observation":
        obs = Observation(**kwargs)
        return f"[DRY-RUN] Добавлено наблюдение: {obs.text} для растения {obs.plant_name}"
    elif operation == "delete_plant":
        return f"[DRY-RUN] Удалено растение: {args[0]}"
    elif operation == "delete_plot":
        return f"[DRY-RUN] Удален участок: {args[0]}"
    elif operation == "delete_work":
        return f"[DRY-RUN] Удалена работа: {args[0]}"
    elif operation == "delete_observation":
        return f"[DRY-RUN] Удалено наблюдение: {args[0]}"
    else:
        return f"[DRY-RUN] Неизвестная операция: {operation}"
