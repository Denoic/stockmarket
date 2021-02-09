import requests
import os
import keyboard
from rich.console import Console
from rich.markdown import Markdown
from rich import print

def filecreation(stock):
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/get-detail"

    querystring = {"symbol": stock, "region": "US"}

    headers = {
        'x-rapidapi-key': "623ecea589msh70f225267987d8ep18f5c1jsn34e5895911b9",
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring)

    result = response.json()
        
    f = open("info.md","w+")
    f.write(result.get("summaryProfile").get("longBusinessSummary"))
    f.close()

def cls(): return os.system('cls')

def BusinessSummary():
    console = Console()
    with open("info.md") as info:
        markdown = Markdown(info.read())
    console.print("[bold red]Business Summary:[/bold red]")
    console.print(markdown)
    os.remove('info.md')

def Info(stock):
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/get-detail"

    querystring = {"symbol": stock, "region": "US"}

    headers = {
        'x-rapidapi-key': "623ecea589msh70f225267987d8ep18f5c1jsn34e5895911b9",
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring)

    result = response.json()
    print("[bold red]Name:[/bold red]")
    print(result.get("price").get("longName"))
    print()
    print("[bold red]Sector:[/bold red]")
    print(result.get("summaryProfile").get("sector"))
    print()
    print("[bold red]Industry:[/bold red]")
    print(result.get("summaryProfile").get("industry"))
    print()
    print("[bold red]Zip:[/bold red]")
    print(result.get("summaryProfile").get("zip"))
    print()
    print(BusinessSummary())
    print()
    print("[bold red]City:[/bold red]")
    print(result.get("summaryProfile").get("city"))
    print()
    print("[bold red]State:[/bold red]")
    print(result.get("summaryProfile").get("state"))
    print()
    print("[bold red]Country:[/bold red]")
    print(result.get("summaryProfile").get("country"))
    print()
    print("[bold red]Website:[/bold red]")
    print(result.get("summaryProfile").get("website"))
    print()
    print("Press ENTER to continue...")
    keyboard.wait('enter')
    
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
    print('Name:')
    print(result.get("finance").get(0).get("quotes").get(0).get("shortName"))
    print()
    print('Symbol:')
    print(result.get("finance").get(0).get("quotes").get(0).get("symbol"))
    print()

while True:
    cls()
    print("Info Price Trends")
    choice1 = input("Select one: ")

    cls()
    if choice1.lower() == "info":
        InpStock = input("Enter ticker: ")
        InpStock = InpStock.upper()
        cls()
        filecreation(InpStock)
        Info(InpStock)
        continue
    
    elif choice1.lower() == "price":
        InpStock = input("Enter ticker: ")
        InpStock = InpStock.upper()
        cls()
        pricetracker(InpStock)
        continue
    
    elif choice1.lower() == "trends":
        cls()
        trending()