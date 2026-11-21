# === Stage 56: Добавь массовое обновление выбранных записей ===
# Project: GardenLog
def mass_update_records(self, updates):
    """Массовое обновление выбранных записей по ключу."""
    if not updates:
        return
    for rec in self.records.values():
        key = rec.get("key")
        if key in updates:
            data = updates[key]
            for field, value in data.items():
                if field in rec and field != "key":
                    rec[field] = value
    self._notify("mass_update", len(updates))
    self.save()
