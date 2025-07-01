from typing import Iterable


def filter_by_currency(transactions: list, currency: str) -> Iterable:
    for meaning in transactions:
        if meaning["operationAmount"]["currency"]["code"] == currency:
            yield meaning


def transaction_descriptions(transactions: list) -> Iterable:
    for operations in transactions:
       yield operations["description"]


def card_number_generator(start = 1, stop = 9999999999999999 ) -> Iterable:
    """"Функция, которая генерирует номер карты в заданном диапазоне"""
    for gen_num in range(start, stop):
        len_numbers = 16 - len(str(gen_num))
        if len(str(gen_num)) <= 16:
            card_number_gen = ('0' * len_numbers) + str(gen_num)
            card_number = card_number_gen[:4] + " " + card_number_gen[4:8] + " " + card_number_gen[8:12] + " "+ card_number_gen[-4:]
            yield card_number
        else:
            print('Что-то пошло не так')
            break



for card_number in card_number_generator(1, 5):
    print(card_number)