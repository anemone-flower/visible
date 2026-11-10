# === Stage 51: Добавь журнал изменений данных с отметками времени ===
# Project: GardenLog
class ChangeLog:
    def __init__(self):
        self._entries = []

    def log(self, action, entity, detail="", ts=None):
        self._entries.append({
            "ts": ts or datetime.now().isoformat(timespec="seconds"),
            "action": action,
            "entity": entity,
            "detail": detail,
        })

    def add(self, action, entity, detail=""):
        self.log(action, entity, detail)

    def history(self, limit=20):
        return self._entries[-limit:]

    def save(self, path):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self._entries, f, ensure_ascii=False, indent=2)

    def load(self, path):
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                self._entries = json.load(f)

    def clear(self):
        self._entries = []
