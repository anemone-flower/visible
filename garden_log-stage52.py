# === Stage 52: Добавь экспорт краткого отчёта в текстовом формате ===
# Project: GardenLog
def export_report():
    if not garden:
        print("Сад пуст")
        return
    lines = []
    lines.append("Отчёт о саде")
    lines.append("=" * 30)
    lines.append(f"Растений: {len(plants)}")
    lines.append(f"Участков: {len(sections)}")
    lines.append(f"Поливов: {len(waterings)}")
    lines.append(f"Работ: {len(jobs)}")
    lines.append(f"Наблюдений: {len(observations)}")
    lines.append("")
    for p in plants:
        lines.append(f"Растение: {p.name}, {p.count} шт.")
    for w in waterings[-5:]:
        lines.append(f"Полив: {w.date}, {len(w.section_plants)} растений")
    for j in jobs[-5:]:
        lines.append(f"Работа: {j.name}, дата: {j.date}")
    for o in observations[-5:]:
        lines.append(f"Наблюдение: {o.text}, дата: {o.date}")
    report = "\n".join(lines)
    print(report)
    with open("garden_report.txt", "w", encoding="utf-8") as f:
        f.write(report)
    print("Отчёт сохранён в garden_report.txt")
