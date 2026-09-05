# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: GardenLog
def next_action(recs):
    """Recommend next action based on current state of garden.
    recs: list of dicts with keys: plant, area, action, priority, note
    Returns the highest priority action string or 'No urgent actions'.
    """
    if not recs:
        return "No urgent actions. Enjoy your garden!"
    recs.sort(key=lambda r: r['priority'], reverse=True)
    top = recs[0]
    action = top['action']
    note = top.get('note', '')
    if note:
        return f"{action}: {note}"
    return action
