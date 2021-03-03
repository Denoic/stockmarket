import pandas as pd
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
from cls import cls
import keyboard
import time

def gainers():
    res = requests.get("https://finance.yahoo.com/gainers")
    soup = BeautifulSoup(res.content, 'lxml')
    table = soup.find_all('table')[0]
    df = pd.read_html(str(table))
    cls()
    print(tabulate(df[0], headers='keys', tablefmt='psql', showindex='never'))



def losers():
    res = requests.get("https://finance.yahoo.com/losers")
    soup = BeautifulSoup(res.content, 'lxml')
    table = soup.find_all('table')[0]
    df = pd.read_html(str(table))
    cls()
    print(tabulate(df[0], headers='keys', tablefmt='psql', showindex='never'))
