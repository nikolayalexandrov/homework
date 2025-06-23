from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(user_details: str) -> str:
    """ "Функция, которая проверяет что ввел пользователь(карту или счет) и маскирует"""
    disguise_user_details = ""
    number = ""
    word = ""

    for symbol in user_details:
        if symbol.isdigit():
            number += symbol
        elif not symbol.isdigit():
            word += symbol
    if len(number) == 16:
        number_mask = get_mask_card_number(number)
    else:
        number_mask = get_mask_account(number)
    if word[-1] == " ":
        disguise_user_details = word[:-1] + " " + number_mask
    else:
        disguise_user_details = word + " " + number_mask

    return disguise_user_details


def get_date(current_date: str) -> str:
    """'Функция, которая показывает дату операции"""
    data = current_date[:10]
    data_used = data.split("-")[::-1]

    return ".".join(data_used)
