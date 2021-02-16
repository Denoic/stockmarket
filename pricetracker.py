from cls import cls
import requests
from bs4 import BeautifulSoup
from rich import print
import msvcrt

def pricetracker(stock):
    

    url = f'https://finance.yahoo.com/quote/{stock}?p={stock}&.tsrc=fin-srch'


    while True:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')

        price = soup.find("div", {"class": "D(ib) Mend(20px)"}).find_all('span')[0].text
        
        change = soup.find("div", {"class": "D(ib) Mend(20px)"}).find_all('span')[1]
        
        print(change)
        print(change.text)
        input()
        cls()
        spanclass = "Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($negativeColor)"
        spanreactid = "33"
        span = "<span class=\"" + spanclass + "\" data-reactid=\""+ spanreactid +"\">" + change.text + "</span>"
        print(span)
        input()
        if change == span:
            print(f"{stock}  {price}  [bold red]{change.text}[/bold red]")
        else:
            print("Test")