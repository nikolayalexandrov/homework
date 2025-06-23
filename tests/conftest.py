import pytest

@pytest.fixture
def card_number():
    return '7000 79** **** 6361'

@pytest.fixture
def card_number_1():
    return 'Введен некорректный номер карты'

@pytest.fixture
def card_number_2():
    return 'Введен некорректный номер карты'

@pytest.fixture
def account_number():
    return '**4305'

@pytest.fixture
def account_number_1():
    return 'Введен некорректный номер счета'

@pytest.fixture
def account_number_2():
    return 'Введен некорректный номер счета'

@pytest.fixture
def card_account():
    return 'Visa Platinum 7000 79** **** 6361'

@pytest.fixture
def account_date():
    return '11.03.2024'

@pytest.fixture
def filter_state():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

@pytest.fixture
def sort_date():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]