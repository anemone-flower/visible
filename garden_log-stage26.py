# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: GardenLog
def demo():
    print("=== GardenLog Demo ===")
    demo_plants = [Plant(name="Ромашка", latin_name="Chamomilla", height=0.3, needs_water=True),
                   Plant(name="Пеларгония", latin_name="Pelargonium", height=0.5, needs_water=False)]
    for p in demo_plants: print(p)
    demo_plots = [Plot(name="Северная грядка", area=2.5, soil_type="суглинок"),
                  Plot(name="Западный балкон", area=1.0, soil_type="торф")]
    for pl in demo_plots: print(pl)
    DemoWatering("Ромашка").do()
    print(DemoWork("Прополка", "Северная грядка", date="2026-05-14").to_dict())
    for p in demo_plants:
        Obs(p, note="Первые листья!", date="2026-05-13").save()
        Obs(p, note="Полив через 2 дня", date="2026-05-17").save()
    print("Демо завершён.")
