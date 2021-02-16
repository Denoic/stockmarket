from cls import cls
import requests
from bs4 import BeautifulSoup
from rich import print
from datetime import time, datetime
import pytz

def currentmarket(stock):

    url = f'https://finance.yahoo.com/quote/{stock}?p={stock}&.tsrc=fin-srch'

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    price = soup.find("div", {"class": "D(ib) Mend(20px)"}).find_all('span')[0].text

    change = soup.find("div", {"class": "D(ib) Mend(20px)"}).find_all('span')[1]

    while True:
        valueprice = price
        valuechange = change.text
        bracketIndex = valuechange.find('(')
        result1 = valueprice[0:bracketIndex].strip(' ')
        result2 = valuechange[bracketIndex:].replace('(', '').replace(
            ')', '').replace('%', '').strip(' ')
        print(result1)
        changevalue = float(result1)
        changepercent = float(result2)
        cls()
        if changevalue < 0:
            print(f"{stock} [bold red] {changevalue} ({changepercent}%) [/bold red]")
        elif changevalue > 0:
            print(f"{stock} [bold green] {changevalue} ({changepercent}%) [/bold green]")

        else:
            print(f"{stock} {changevalue} ({changepercent}%)")

def postmarketprice(stock):

    url = f'https://finance.yahoo.com/quote/{stock}?p={stock}&.tsrc=fin-srch'

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    try:
        afterprice = soup.find("p", {"class": "Fz(12px) C($tertiaryColor) My(0px) D(ib) Va(b)"}).find_all('span')[0].text
        afterchange = soup.find("p", {"class": "Fz(12px) C($tertiaryColor) My(0px) D(ib) Va(b)"}).find_all('span')[1]
    except AttributeError:
        afterprice = "0"
        afterchange = "0"


    while True:
        valueprice = afterprice
        valuechange = afterchange
        bracketIndex = valuechange.find('(')
        result1 = valueprice[0:bracketIndex].strip(' ')
        result2 = valuechange[bracketIndex:].replace('(', '').replace(
            ')', '').replace('%', '').strip(' ')
        try:
            changevalue = float(result1)
            changepercent = float(result2)
        except ValueError:
            changevalue = 0
            changepercent = 0
        cls()
        if changevalue < 0:
            print(f"{stock} [bold red] {changevalue} ({changepercent}%) [/bold red]")
            input()
        elif changevalue > 0:
            print(f"{stock} [bold green] {changevalue} ({changepercent}%) [/bold green]")
        else:
            print(f"{stock}  {changevalue} ({changepercent}%)")

def pricetracker(InputStock):
    EST = pytz.timezone('America/New_York')
    time = datetime.now(EST)
    timehour = int(time.strftime("%H"))
    timeminutes = int(time.strftime("%M"))

    while True:
        if timehour > 9 and timehour <= 16:
            if timeminutes >= 30 and timehour == 4:
                postmarketprice(InputStock)
            else:
                currentmarket(InputStock)

        elif timehour == 9:
            if timeminutes >= 30:
                currentmarket(InputStock)

        else:
            postmarketprice()