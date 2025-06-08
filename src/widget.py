from src.masks import get_mask_card_number

from src.masks import get_mask_account


def mask_account_card(user_details: str) -> str:
    """"Функция, которая проверяет что ввел пользователь(карту или счет) и маскирует"""
    disguise_user_details = ''
    number = ''
    word = ''

    for symbol in user_details:
        if symbol.isdigit():
            number += symbol
        elif symbol.isalpha():
            word += symbol
    if len(number) == 16:
        number_mask = get_mask_card_number(number)
    else:
        number_mask = get_mask_account(number)

    disguise_user_details = word +' ' + number_mask

    return disguise_user_details
