# === Stage 48: Проведи рефакторинг: разнеси крупные функции, сохрани совместимость публичных команд ===
# Project: GardenLog
def _compact_entry_summary(entry: dict) -> str:
    parts = [
        entry.get("title", "Без заголовка"),
        entry.get("date"),
        entry.get("content", ""),
    ]
    return " | ".join(p for p in parts if p)

def _compact_entry_summary_list(entries: list) -> str:
    return "\n".join(_compact_entry_summary(e) for e in entries if e)

def _compact_entry_summary_json(entries: list) -> str:
    return "\n".join(_compact_entry_summary(e) for e in entries if e)
