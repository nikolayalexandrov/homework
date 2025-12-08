import json
from pathlib import Path


def load_transactions(file_path):
    """"функция, которая принимает на вход путь до JSON-файла и возвращает список
    словарей с данными о финансовых транзакциях."""

    path = Path(file_path)

    if not path.exists():
        print(f"Ошибка: Файл не найден по пути {file_path}")
        return []

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
             data = json.load(f)

        return data
    except Exception as e:
        print(e)
print(load_transactions('C:\\Users\\energ\\OneDrive\\Рабочий стол\\SkyPro\\PythonProject\\data\\operations.json'))

