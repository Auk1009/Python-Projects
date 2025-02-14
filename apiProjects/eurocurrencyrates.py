import requests
import tkinter as tk

def eurocurrency():
    Api_key = 'a81f9719bd384e78056c461d82fc4b09'
    base_URL = 'https://api.exchangeratesapi.io/v1/'
    symbols = 'INR,USD,AUD,AED'

    complete_URL = f'{base_URL}latest?access_key={Api_key}&symbols={symbols}&format=1'

    response = requests.get(complete_URL)
    if response.status_code == 200:
        data = response.json()
        current_date = data['date']
        base_currency = data['base']
        rates = data['rates']

        print(f"Date: {current_date}")
        print(f"Base currency: {base_currency}")
        print(f"Exchange Rates: {rates}")
    else:
        print(f'Something went wrong --> Status code: {response.status_code}')

root = tk.Tk()

root.geometry("300x600")

