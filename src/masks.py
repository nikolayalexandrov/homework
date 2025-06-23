def get_mask_card_number(card_number: str) -> str:
    """Функция, которая добавляет пробелы и  меняет цифры в номере карты
    на звездочки"""
    card_number_star = ""
    if len(card_number) == 16:
        card_number_star = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
    if card_number == "" or len(card_number) != 16:
        return "Введен некорректный номер карты"
    if not card_number.isdigit() or card_number == "0000000000000000":
        return "Введен некорректный номер карты"
    return card_number_star


def get_mask_account(account_number: str) -> str:
    """Функция, которая меняет цифры в номере счета
    на звездочки"""
    account_number_star = ""
    if len(account_number) == 20:
        account_number_star = "**" + account_number[-4:]
    if account_number == "" or len(account_number) != 20:
        return "Введен некорректный номер счета"
    if not account_number.isdigit() or account_number == "00000000000000000000":
        return "Введен некорректный номер счета"
    return account_number_star
