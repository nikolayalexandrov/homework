import os
import json
from http.client import responses

from dotenv import load_dotenv
from utils import load_transactions
import requests

load_dotenv()
API_KEY = os.getenv('API_KEY')

def pay_transactions(load_transaction: dict) -> float:
    """"функцию, которая принимает на вход транзакцию и возвращает сумму транзакции"""
    try:
        for transaction in load_transaction:
            if transaction['operationAmount']['currency']['code'] == 'RUB':
             print(transaction['operationAmount']['amount'])
            if transaction['operationAmount']['currency']['code'] != 'RUB':
                code_amount = transaction['operationAmount']['currency']['code']
                sum_amount = transaction['operationAmount']['amount']
                from_conv_amount = 'RUB'
                conv_amount = f"https://api.apilayer.com/exchangerates_data/convert?to={from_conv_amount}&from={code_amount}&amount={sum_amount}"
            #payload = date.today()
                headers = {
                    "apikey": "API_KEY"
                }

                response = requests.request("GET", conv_amount, headers=headers)
        return response
    except Exception as e:
        print (e)