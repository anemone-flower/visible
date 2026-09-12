# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: GardenLog
import argparse

def main():
    parser = argparse.ArgumentParser(description="GardenLog CLI")
    sub = parser.add_subparsers(dest="cmd")

    p_add_plant = sub.add_parser("add-plant")
    p_add_plant.add_argument("name", help="Название растения")
    p_add_plant.add_argument("--type", default="herb", choices=["herb", "flower", "vegetable", "tree"])

    p_water = sub.add_parser("water")
    p_water.add_argument("name", help="Название растения")

    p_work = sub.add_parser("work")
    p_work.add_argument("description", help="Описание работы")

    p_observe = sub.add_parser("observe")
    p_observe.add_argument("name", help="Название растения")
    p_observe.add_argument("--note", required=True, help="Примечание")

    p_add_section = sub.add_parser("add-section")
    p_add_section.add_argument("name", help="Название участка")
    p_add_section.add_argument("--size", type=int, default=1)

    args = parser.parse_args()
    if args.cmd == "add-plant":
        add_plant(args.name, args.type)
    elif args.cmd == "water":
        water_plant(args.name)
    elif args.cmd == "work":
        add_work(args.description)
    elif args.cmd == "observe":
        add_observation(args.name, args.note)
    elif args.cmd == "add-section":
        add_section(args.name, args.size)
    else:
        parser.print_help()
