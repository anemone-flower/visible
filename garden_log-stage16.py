# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: GardenLog
def monthly_stats(records):
    stats = {}
    for r in records:
        if 'date' not in r or r['date'] is None:
            continue
        month_key = f"{r['date'][0]}-{r['date'][1]}"
        if month_key not in stats:
            stats[month_key] = {'count': 0, 'types': set()}
        stats[month_key]['count'] += 1
        if r.get('type'):
            stats[month_key]['types'].add(r['type'])
    return {k: dict(v=v) for k, v in stats.items()}
