# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: GardenLog
def check_and_repair_data():
    """Проверяет целостность данных и пытается исправить простые проблемы."""
    issues = []
    if not garden:
        issues.append("garden is empty")
        return issues
    for plant in garden:
        if not plant['name']:
            plant['name'] = 'Unknown Plant'
            issues.append(f"Plant at {plant['position']} had empty name")
        for key in ['species', 'age', 'health', 'watered', 'notes']:
            if key not in plant:
                plant[key] = None
                issues.append(f"Plant at {plant['position']} missing key: {key}")
    for plot in garden:
        if not plot.get('position'):
            plot['position'] = 'Unknown'
            issues.append(f"Plot had empty position")
    if issues:
        print(f"Found {len(issues)} issue(s) and auto-repaired them.")
    else:
        print("Data integrity check passed: no issues found.")
    return issues
