import requests
from bs4 import BeautifulSoup

def trends():
    url = 'https://finance.yahoo.com/trending-tickers/'

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

