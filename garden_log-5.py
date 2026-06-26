# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: GardenLog
def delete_record(record_id: int, record_type: str) -> bool:
    if not records or record_type not in records:
        print(f"Ошибка: тип записи '{record_type}' не найден.")
        return False
    
    target_records = records[record_type]
    if record_id not in target_records:
        print(f"Ошибка: запись с ID {record_id} для типа '{record_type}' не найдена.")
        return False
    
    del target_records[record_id]
    print(f"Успешно удалена запись #{record_id} из раздела '{record_type}'.")
    return True

if __name__ == "__main__":
    # Пример использования: удаление полива с ID 5
    delete_record(5, "irrigation")
