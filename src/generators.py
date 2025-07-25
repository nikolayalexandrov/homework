from typing import Iterable


def filter_by_currency(transactions_filter: list, currency: str) -> Iterable:
    """ "Функция возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной"""
    if currency == "":
        yield "Нет заданной валюты"
    if transactions_filter == list():
        yield "Список пуст"
    else:
        for meaning_filter in transactions_filter:
            if meaning_filter["operationAmount"]["currency"]["code"] == currency:
                yield meaning_filter


def transaction_descriptions(transactions_desc: list) -> Iterable:
    """ "Функция принимает список словарей с транзакциями и
    возвращает описание каждой операции по очереди"""
    if transactions_desc == list():
        yield "Список пуст"
    else:
        for operations_desc in transactions_desc:
            yield operations_desc["description"]


def card_number_generator(start=1, stop=9999999999999999) -> Iterable:
    """Функция, которая генерирует номер карты в заданном диапазоне"""
    for gen_num in range(start, stop):
        len_numbers = 16 - len(str(gen_num))
        if len(str(gen_num)) <= 16:
            card_number_gen = ("0" * len_numbers) + str(gen_num)
            new_card_number = (
                card_number_gen[:4]
                + " "
                + card_number_gen[4:8]
                + " "
                + card_number_gen[8:12]
                + " "
                + card_number_gen[-4:]
            )
            if new_card_number == "0000 0000 0000 0000":
                yield "Нельзя начинать с нуля"
            yield new_card_number
        if len(str(gen_num)) > 16:
            yield "Слишком длинный номер"
