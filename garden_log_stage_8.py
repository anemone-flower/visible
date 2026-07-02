# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: GardenLog
def show_menu():
    print("\n=== Меню GardenLog ===")
    print("1. Добавить растение")
    print("2. Добавить участок")
    print("3. Записать полив")
    print("4. Записать работу/наблюдение")
    print("5. Показать все растения")
    print("6. Выход")
    try:
        choice = input("Выберите действие (1-6): ")
        if choice == "1":
            add_plant()
        elif choice == "2":
            add_plot()
        elif choice == "3":
            log_watering()
        elif choice == "4":
            log_activity()
        elif choice == "5":
            list_all_plants()
        elif choice == "6":
            print("Выход из программы.")
            return False
    except KeyboardInterrupt:
        pass
    return True
