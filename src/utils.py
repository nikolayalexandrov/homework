import json


def load_transactions(file_path):
    """"функциz, которая принимает на вход путь до JSON-файла и возвращает список
    словарей с данными о финансовых транзакциях."""
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

        return data

#print(load_transactions('C:\\Users\\energ\\OneDrive\\Рабочий стол\\SkyPro\\PythonProject\\data\\operations.json'))

