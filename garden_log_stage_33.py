# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: GardenLog
import copy

def undo_last_action(state: list) -> None:
    if not state:
        return
    last = state[-1]
    if last["type"] == "add":
        state.pop()
    elif last["type"] == "remove":
        state.pop()
        state.append(last)
    elif last["type"] == "update":
        state.pop()
        state.append(last)
    elif last["type"] == "log":
        state.pop()
