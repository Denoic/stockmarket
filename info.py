from rich.console import Console
from rich.markdown import Markdown
from rich import print
import os
import requests
import yfinance as yf


def filecreation(stock):
    tickerdata = yf.Ticker(stock)
    tickerinfo = tickerdata.info

    f = open("info.md", "w+")
    f.write(tickerinfo.get("longBusinessSummary"))
    f.close()


def BusinessSummary():
    console = Console()
    with open("info.md") as info:
        markdown = Markdown(info.read())
    console.print("[bold red]Business Summary:[/bold red]")
    console.print(markdown)
    os.remove('info.md')


def Info(stock):
    tickerdata = yf.Ticker(stock)
    tickerinfo = tickerdata.info
    print("[bold red]Name:[/bold red]")
    print(tickerinfo.get("longName"))
    print()
    print("[bold red]Sector:[/bold red]")
    print(tickerinfo.get("sector"))
    print()
    print("[bold red]Industry:[/bold red]")
    print(tickerinfo.get('industry'))
    print()
    print("[bold red]Zip:[/bold red]")
    print(tickerinfo.get('zip'))
    print()
    BusinessSummary()
    print()
    print("[bold red]City:[/bold red]")
    print(tickerinfo.get("city"))
    print()
    print("[bold red]State:[/bold red]")
    print(tickerinfo.get("state"))
    print()
    print("[bold red]Country:[/bold red]")
    print(tickerinfo.get("country"))
    print()
    print("[bold red]Website:[/bold red]")
    print(tickerinfo.get("website"))
    print()
    print("[bold red]Employees:[/bold red]")
    print(tickerinfo.get('fullTimeEmployees'))
    print()
