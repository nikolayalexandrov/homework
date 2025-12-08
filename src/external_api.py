import json
import os

from dotenv import load_dotenv

import requests

load_dotenv()
API_KEY = os.getenv('API_KEY')



def pay_transactions(transaction: dict) -> float:
    """"функцию, которая принимает на вход транзакцию и возвращает сумму транзакции"""
    try:

        if transaction['operationAmount']['currency']['code'] == 'RUB':
            return f'Сумма: {transaction['operationAmount']['amount']} RUB'
        else:
            code_amount = transaction['operationAmount']['currency']['code']
            sum_amount = transaction['operationAmount']['amount']
            from_conv_amount = 'RUB'

            print(f'сумма и валюта для конвертации: {sum_amount} {code_amount}')

            conv_amount = f"https://api.apilayer.com/exchangerates_data/convert?to={from_conv_amount}&from={code_amount}&amount={sum_amount}"

            headers = {"apikey": API_KEY}

            response = requests.get(conv_amount, headers=headers)

            data = json.loads(response.text)
            sum_conv = data['result']


        return f'Сумма после конвертации: {sum_conv} RUB'

    except Exception as e:
        print (e)


val = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "EUR"
      }
    }}

print(pay_transactions(val))
