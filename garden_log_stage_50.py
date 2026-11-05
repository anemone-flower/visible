# === Stage 50: Сделай аккуратную финальную полировку сообщений, названий функций и комментариев ===
# Project: GardenLog
def _format_status(message):
    """Приводит текст к аккуратному виду с нормальными пробелами."""
    text = message.strip()
    return text[0].upper() + text[1:] if text else message
