# === Stage 53: Добавь импорт отчёта или списка записей из простого текстового формата ===
# Project: GardenLog
import json

def parse_plants(text):
    plants = []
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        parts = line.split('|')
        if len(parts) >= 4:
            plants.append({
                'name': parts[0].strip(),
                'type': parts[1].strip(),
                'planted': parts[2].strip(),
                'notes': parts[3].strip()
            })
    return plants

def parse_logs(text):
    logs = []
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        parts = line.split('|')
        if len(parts) >= 5:
            logs.append({
                'date': parts[0].strip(),
                'plant': parts[1].strip(),
                'action': parts[2].strip(),
                'hours': int(parts[3].strip()) if parts[3].strip().isdigit() else 0,
                'notes': parts[4].strip()
            })
    return logs

def parse_text_file(path, fmt='logs'):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    if fmt == 'plants':
        return parse_plants(content)
    return parse_logs(content)

def save_text_export(items, path, fmt='logs'):
    lines = ['# Exported from GardenLog', '']
    for item in items:
        if fmt == 'plants':
            lines.append('|' + '|'.join([
                str(item.get('name', '')),
                str(item.get('type', '')),
                str(item.get('planted', '')),
                str(item.get('notes', ''))
            ]) + '|')
        else:
            lines.append('|' + '|'.join([
                str(item.get('date', '')),
                str(item.get('plant', '')),
                str(item.get('action', '')),
                str(item.get('hours', 0)),
                str(item.get('notes', ''))
            ]) + '|')
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')
