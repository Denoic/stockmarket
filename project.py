import requests
import os
import keyboard
from rich.console import Console
from rich.markdown import Markdown
from rich import print
import json
from info import Info

def cls(): return os.system('cls')

def pricetracker(stock):
    print()
                
def trending():
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/get-trending-tickers"

    querystring = {"region":"US"}

    headers = {
        'x-rapidapi-key': "623ecea589msh70f225267987d8ep18f5c1jsn34e5895911b9",
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    result = response.json()

    print(result)
    print()
    print()
    print()
    print()
    print(result.get('finance')['result'])

def news():
    print('news')

while True:
    choice1 = ""
    while choice1 == "":
        cls()
        print("Info Price Trends News")
        choice1 = input("Select one: ")

    cls()
    if choice1.lower() == "info":
        InpStock = input("Enter ticker: ")
        InpStock = InpStock.upper()
        cls()
        Info(InpStock)
    
    elif choice1.lower() == "price":
        InpStock = input("Enter ticker: ")
        InpStock = InpStock.upper()
        cls()
        pricetracker(InpStock)
    
    elif choice1.lower() == "trends":
        cls()
        trending()
    
    elif choice1.lower() == "news":
        cls()

    print("Press ENTER to continue...")
    keyboard.wait("enter")