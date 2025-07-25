

from src.widget import mask_account_card
from src.widget import get_date


def test_mask_account_card(card_account):
    assert mask_account_card('Visa Platinum 7000792289606361') == card_account

def test_get_date(account_date):
    assert get_date('2024-03-11T02:26:18.671407') == account_date