from cls import cls
import requests
from bs4 import BeautifulSoup
from rich import print
from datetime import time, datetime
import pytz
import time
import keyboard



def currentmarket(stock):
    while True:

        time.sleep(1)
        if keyboard.is_pressed('esc'):
            break


        else:
            url = f'https://finance.yahoo.com/quote/{stock}?p={stock}&.tsrc=fin-srch'

            r = requests.get(url)
            soup = BeautifulSoup(r.text, 'html.parser')

            price = soup.find("div", {"class": "D(ib) Mend(20px)"}).find_all('span')[0].text

            change = soup.find("div", {"class": "D(ib) Mend(20px)"}).find_all('span')[1].text

            bracketIndex = change.find('(')
            result1 = price[0:bracketIndex].strip(' ')
            result2 = change[bracketIndex:].replace('(', '').replace(
                ')', '').replace('%', '').strip(' ')

            changevalue = float(result1)
            changepercent = float(result2)

            cls()
            if changevalue < 0:
                print(f"{stock} [bold red] {changevalue} ({changepercent}%) [/bold red]")
                print("To go back hold ESC")

            elif changevalue > 0:
                print(f"{stock} [bold green] {changevalue} ({changepercent}%) [/bold green]")
                print("To go back hold ESC")

            else:
                print(f"{stock} {changevalue} ({changepercent}%)")
                print("To go back hold ESC")

def postmarketprice(stock):
    while True:
        time.sleep(1)
        if keyboard.is_pressed('esc'):
            break

        else:
            url = f'https://finance.yahoo.com/quote/{stock}?p={stock}&.tsrc=fin-srch'

            r = requests.get(url)
            soup = BeautifulSoup(r.text, 'html.parser')

            try:
                afterprice = soup.find("p", {"class": "Fz(12px) C($tertiaryColor) My(0px) D(ib) Va(b)"}).find_all('span')[0].text
                afterchange = soup.find("p", {"class": "Fz(12px) C($tertiaryColor) My(0px) D(ib) Va(b)"}).find_all('span')[1].text
            except AttributeError:
                afterprice = "0"
                afterchange = "0"



            try:
                bracketIndex = afterchange.find('(')
                result1 = afterprice[0:bracketIndex].strip(' ')
                result2 = afterchange[bracketIndex:].replace('(', '').replace(
                    ')', '').replace('%', '').strip(' ')

            except TypeError:
                result1 = 0
                result2 = 0

            try:
                changevalue = float(result1)
                changepercent = float(result2)

            except ValueError:
                changevalue = 0
                changepercent = 0
            cls()

            if changepercent < 0:
                print(f"{stock} [bold red] {changevalue} ({changepercent}%) [/bold red]")
                print("To go back hold ESC")

            elif changepercent > 0:
                print(f"{stock} [bold green] {changevalue} ({changepercent}%) [/bold green]")
                print("To go back hold ESC")

            else:
                print(f"{stock}  {changevalue} ({changepercent}%)")
                print("To go back hold ESC")


def pricetracker(InputStock):
    EST = pytz.timezone('America/New_York')
    time = datetime.now(EST)
    timehour = int(time.strftime("%H"))
    timeminutes = int(time.strftime("%M"))


    if timehour > 9 and timehour <= 16:
        if timeminutes >= 30 and timehour == 16:
            postmarketprice(InputStock)
        else:
            currentmarket(InputStock)

    elif timehour == 9:
        if timeminutes >= 30:
            currentmarket(InputStock)

        else:
            postmarketprice(InputStock)

    else:
        postmarketprice(InputStock)


