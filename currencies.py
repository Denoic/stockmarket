import pandas as pd
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
import keyboard
from cls import cls

def currencies():
    res = requests.get("https://finance.yahoo.com/currencies")
    soup = BeautifulSoup(res.content, 'lxml')
    table = soup.find_all('table')[0]
    df = pd.read_html(str(table))
    cls()
    print(tabulate(df[0], headers='keys', tablefmt='psql', showindex='never'))