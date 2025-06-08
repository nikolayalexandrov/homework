def get_mask_card_number(card_number: str) -> str:
    """Функция, которая добавляет пробелы и  меняет цифры в номере карты
    на звездочки"""

    card_number_star = card_number[:4] + " " + card_number[5:7] + "** **** " + card_number[-4:]

    return card_number_star


def get_mask_account(account_number: str) -> str:
    """Функция, которая меняет цифры в номере счета
    на звездочки"""

    account_number_star = "**" + account_number[-4:]
    return account_number_star
