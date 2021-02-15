from cls import cls
import requests
from bs4 import BeautifulSoup
from rich import print
import msvcrt

def pricetracker(stock):
    
    PositiveChange = False
    NegativeChange = False

    url = f'https://finance.yahoo.com/quote/{stock}?p={stock}&.tsrc=fin-srch'


    while True:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')

        price = soup.find("div", {"class": "D(ib) Mend(20px)"}).find_all('span')[0].text
        try:
            change = soup.find("div", {"class": "D(ib) Mend(20px)"}).find_all('span')[1]
        except IndexError:
            change = soup.find("div", {"class": "D(ib) Mend(20px)"}).find_all('span')[1]
        except AttributeError:
            change = soup.find("div", {"class": "D(ib) Mend(20px)"}).find_all('span')[1] 
        except KeyError:
            change = soup.find("div", {"class": "D(ib) Mend(20px)"}).find_all('span')[1]

        print(change)
        print(change.text)
        input()
        cls()
        if change == f'<span class="Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($negativeColor)" data-reactid="33">{change.text}</span>':
            print(f"{stock}  {price}  [bold red]{change.text}[/bold red]")
        else:
            print("kur")