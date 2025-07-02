from typing import Iterable


def filter_by_currency(transactions: list, currency: str) -> Iterable:
    """"Функция возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной """
    for meaning in transactions:
        if meaning["operationAmount"]["currency"]["code"] == currency:
            yield meaning


def transaction_descriptions(transactions: list) -> Iterable:
    """"Функция принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    for operations in transactions:
        yield operations["description"]


def card_number_generator(start=1, stop=9999999999999999) -> Iterable:
    """ "Функция, которая генерирует номер карты в заданном диапазоне"""
    for gen_num in range(start, stop):
        len_numbers = 16 - len(str(gen_num))
        if len(str(gen_num)) <= 16:
            card_number_gen = ("0" * len_numbers) + str(gen_num)
            card_number = (
                card_number_gen[:4]
                + " "
                + card_number_gen[4:8]
                + " "
                + card_number_gen[8:12]
                + " "
                + card_number_gen[-4:]
            )
            yield card_number
        else:
            print("Что-то пошло не так")
            break


for card_number in card_number_generator(1, 15):
    print(card_number)

transactions = (
    [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]
)

for meaning in filter_by_currency(transactions, "USD"):
    print(meaning)

for operations in transaction_descriptions(transactions):
    print(operations)