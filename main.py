#импорт функций

from src.masks import get_mask_card_number

from src.masks import get_mask_account

from src.widget import mask_account_card

from src.widget import get_date

from src.processing import filter_by_state

from src.processing import sort_by_date

from src.decorators import log

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

# Пример использования
@log("mylog.txt")  # Логи в файл
def calculate_division(a: int, b: int) -> float:
    """Пример функции с логированием"""
    return a / b

@log()  # Логи в консоль
def calculate_sum(a: int, b: int) -> int:
    """Другая функция с логированием"""
    return a + b

result = calculate_division(4, 2)
print(result)