import pytest

from src.masks import get_mask_card_number
from src.masks import get_mask_account


def test_get_mask_card_number(card_number):
    assert get_mask_card_number('7000792289606361') == card_number

def test_get_mask_account(account_number):
    assert get_mask_account('73654108430135874305') == account_number
