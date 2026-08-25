# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: GardenLog
def metrics_report(garden, plants, plots, watering_logs, works, observations):
    """Compact metrics block: returns a dict of key project statistics."""
    stats = {
        "total_plants": len(plants),
        "total_plots": len(plots),
        "watering_count": len(watering_logs),
        "works_count": len(works),
        "observations_count": len(observations),
        "plants_per_plot_avg": round(len(plants) / max(len(plots), 1), 1),
        "watering_per_day_avg": len(watering_logs) / max(1, sum(1 for _ in watering_logs)),
        "works_per_day_avg": len(works) / max(1, sum(1 for _ in works)),
        "observations_per_day_avg": len(observations) / max(1, sum(1 for _ in observations)),
    }
    return stats
