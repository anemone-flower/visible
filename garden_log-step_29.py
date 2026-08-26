# === Stage 29: Добавь конфигурацию приложения через словарь настроек ===
# Project: GardenLog
APP_CONFIG = {
    "app_name": "GardenLog",
    "version": "0.1.0",
    "language": "ru",
    "max_plants_per_plot": 9,
    "water_interval_days": 3,
    "default_plot_width": 10,
    "default_plot_height": 10,
    "log_file": "garden_log.txt",
    "notifications": {
        "enabled": True,
        "dry_soil_days": 5,
        "growth_days": 7,
        "weather_days": 3,
    },
    "ui": {
        "theme": "light",
        "font_size": 14,
        "show_plot_grid": True,
    },
}
