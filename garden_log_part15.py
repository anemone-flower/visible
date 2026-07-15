# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: GardenLog
def weekly_stats(entries):
    """Group entries by week and return dict: 'week_start' -> list of entry dicts."""
    if not entries:
        return {}
    
    groups = {}
    for e in sorted(entries, key=lambda x: x['date']):
        d = datetime(e['year'], e['month'], e['day'])
        week_start = (d - timedelta(days=d.weekday())).strftime('%Y-%m-%d')
        if week_start not in groups:
            groups[week_start] = []
        entry_copy = dict(e)
        entry_copy['date'] = d
        groups[week_start].append(entry_copy)
    
    return groups
