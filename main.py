#импорт функций

from src.masks import get_mask_card_number

from src.masks import get_mask_account

from src.widget import mask_account_card

from src.widget import get_date

from src.processing import filter_by_state

from src.processing import sort_by_date

#маскируем номер карты
card_number = input("ВВедите номере карты: ")
print(get_mask_card_number(card_number))

#маскируем номер счета
account = input("ВВедите номере счета: ")
print(get_mask_account(account))

#маскируем номер карты или счета
account_card = input("ВВедите номере счета или номер карты: ")
print(mask_account_card(account_card))

#вывод даты
date = input("Введите данные: ")
print(get_date(date))

#фильтруем по значению
state_use = input("Введите данные: ")
print(filter_by_state(state_use))

#сортируем по дате
sort_date = input("Введите данные: ")
print(sort_by_date(sort_date))
