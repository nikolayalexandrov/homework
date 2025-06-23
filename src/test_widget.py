import pytest

from src.masks import get_mask_card_number
from src.masks import get_mask_account

def mask_account_card(card_account):
    assert get_mask_card_number('Visa Platinum 7000792289606361') == card_account

def get_date(account_date):
    assert get_mask_account('2024-03-11T02:26:18.671407') == account_date