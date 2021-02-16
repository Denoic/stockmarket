from cls import cls
import requests
from bs4 import BeautifulSoup
from rich import print



def currentmarket(stock):

    url = f'https://finance.yahoo.com/quote/{stock}?p={stock}&.tsrc=fin-srch'

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    price = soup.find("div", {"class": "D(ib) Mend(20px)"}).find_all('span')[0].text

    change = soup.find("div", {"class": "D(ib) Mend(20px)"}).find_all('span')[1]

    cls()
    value = change.text
    bracketIndex = value.find('(')
    result1 = value[0:bracketIndex].strip(' ')
    result2 = value[bracketIndex:].replace('(', '').replace(
        ')', '').replace('%', '').strip(' ')
    print(result1)
    changevalue = float(result1)
    changepercent = float(result2)
    if changevalue < 0:
        print(f"{stock} [bold red] {changevalue} {changepercent} [/bold red]")
        input()
    elif changevalue > 0:
        print(f"{stock} [bold green] {changevalue} ({changepercent}%) [/bold green]")

def postmarketprice(stock):

    url = f'https://finance.yahoo.com/quote/{stock}?p={stock}&.tsrc=fin-srch'

def pricetracker(stock):
    print("")