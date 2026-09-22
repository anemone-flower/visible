# === Stage 47: Добавь финальную функцию demo(), которая показывает основной пользовательский сценарий ===
# Project: GardenLog
def demo():
    print("=== GardenLog Demo ===")
    garden = Garden()

    garden.add_plot("Зона А", 6.0)
    garden.add_plot("Зона Б", 4.5)

    garden.add_plant("tomato", plot="Зона А", count=3)
    garden.add_plant("basil", plot="Зона А", count=1)
    garden.add_plant("carrot", plot="Зона Б", count=20)
    garden.add_plant("lettuce", plot="Зона Б", count=12)

    garden.water("tomato")
    garden.water("basil")
    garden.water("carrot")

    garden.log_work("Выкопал грядку", "Зона Б")
    garden.log_work("Посадил семена", "Зона Б")

    observation = garden.log_observation("Ростки томатов, 3 см", "Зона А")
    print(f"Наблюдение: {observation}")

    garden.prune("tomato")
    garden.prune("basil")

    garden.add_disease("tomato", "Белая плесень")
    garden.add_disease("carrot", "Мокрая гниль")

    print("\nСтатус сада:")
    garden.print_status()

    print("\nЗаписи в дневник:")
    garden.print_log()

    print("\nДеревья (закрытые растения):")
    garden.print_trees()
