# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: GardenLog
def sort_records(records, key='date', reverse=True):
    if not records: return []
    def get_sort_key(r):
        try:
            d = r['date']
            p = r.get('priority', 0)
            n = r.get('name', '')
            if isinstance(d, str): d = datetime.strptime(d, '%Y-%m-%d').timestamp()
            return (d, -p, n.lower())
        except: return float('inf'), 0, ''
    sorted_records = sorted(records, key=get_sort_key)
    if reverse and key == 'date':
        sorted_records.reverse()
    elif not reverse and key != 'date':
        sorted_records.sort(key=lambda x: (x.get('priority', 0), -1 if isinstance(x['name'], str) else 0))
    return sorted_records
