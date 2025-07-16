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
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

@pytest.fixture
def sort_date():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

@pytest.fixture
def filter_by_currency():
    yield "Нет заданной валюты"

@pytest.fixture
def filter_by_currency():
    yield "Список пуст"

@pytest.fixture
def sort_transactions():
    yield {
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "USD",
                  "code": "USD"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
      }

@pytest.fixture
def sort_transaction_oper():
    yield 'Перевод организации'

@pytest.fixture
def sort_transactions_oper():
    yield "Список пуст"


@pytest.fixture
def new_card_number():
    yield '0000 0000 0000 0001'

@pytest.fixture
def new_card_number_1():
    yield '0000 0000 0000 0002'
