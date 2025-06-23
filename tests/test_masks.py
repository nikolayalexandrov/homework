import pytest
from src.masks import get_mask_card_number
from src.masks import get_mask_account


def test_get_mask_card_number(card_number):
    assert get_mask_card_number('7000792289606361') == card_number

def test_get_mask_card_number_1(card_number_1):
    assert get_mask_card_number('') == card_number_1

def test_get_mask_card_number_2(card_number_2):
    assert get_mask_card_number('70007922896063611') == card_number_2

@pytest.mark.parametrize('card_number, expected', [
        ('0000000000000000', 'Введен некорректный номер карты'),
        ('1234*3654-786.58', 'Введен некорректный номер карты'),
        ('sadal;ksdafjkkfd', 'Введен некорректный номер карты'),
        ('                ', 'Введен некорректный номер карты'),
        ('1', 'Введен некорректный номер карты'),
])

def test_get_mask_card_number_3(card_number, expected):
    assert get_mask_card_number(card_number) == expected

def test_get_mask_account(account_number):
    assert get_mask_account('73654108430135874305') == account_number

def test_get_mask_account_1(account_number_1):
    assert get_mask_account('') == account_number_1

def test_get_mask_account_2(account_number_2):
    assert get_mask_account('736541084301358743051') == account_number_2

@pytest.mark.parametrize('account_number, expected_num', [
        ('00000000000000000000', 'Введен некорректный номер счета'),
        ('1234*3654-786.582978', 'Введен некорректный номер счета'),
        ('asdiuhmvndhr,kdidyeh', 'Введен некорректный номер счета'),
        ('                    ', 'Введен некорректный номер счета'),
        ('1', 'Введен некорректный номер счета')
])

def test_get_mask_account_3(account_number, expected_num):
    assert get_mask_account(account_number) == expected_num

