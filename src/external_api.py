import os
import json
from dotenv import load_dotenv
from utils import load_transactions
import requests


def pay_transactions(pay_transaction: list[dict]) -> float:
    """"функцию, которая принимает на вход транзакцию и возвращает сумму транзакции"""
    for transaction in pay_transaction:
        if transaction['operationAmount']['currency']['code'] == 'RUB':
            return transaction['operationAmount']['amount']
        if transaction['operationAmount']['currency']['code'] != 'RUB':
            code_amount = transaction['operationAmount']['currency']['code']
            sum_amount = transaction['operationAmount']['amount']
            from_conv_amount = 'RUB'
            conv_amount = url = f"https://api.apilayer.com/exchangerates_data/convert?to={from_conv_amount}&from={code_amount}&amount={sum_amount}"
            #payload = date.today()
            headers = {
                "apikey": "API_KEY"
            }

            response = requests.request("GET", conv_amount, headers=headers)
