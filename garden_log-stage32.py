# === Stage 32: Добавь журнал действий пользователя ===
# Project: GardenLog
class ActionLog:
    def __init__(self):
        self._log = []

    def log(self, action_type: str, details: dict):
        self._log.append({"time": datetime.now().isoformat(), "action": action_type, **details})

    def get_recent(self, count: int = 10):
        return self._log[-count:]

    def get_by_action(self, action_type: str):
        return [a for a in self._log if a["action"] == action_type]
