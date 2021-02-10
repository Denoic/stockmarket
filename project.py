import requests
import os
import keyboard
from rich.console import Console
from rich.markdown import Markdown
from rich import print
import json
from info import Info
from pricetracker import pricetracker
from trending import trends
from news import news

def cls(): return os.system('cls')
                
while True:
    choice1 = ""
    while choice1 == "":
        cls()
        print("Info Price Trends News")
        choice1 = input("Select one: ")
        choice1 = choice1.lower()

    cls()
    if choice1 == "info":
        InpStock = input("Enter ticker: ")
        InpStock = InpStock.upper()
        cls()
        Info(InpStock)
    
    elif choice1 == "price":
        InpStock = input("Enter ticker: ")
        InpStock = InpStock.upper()
        cls()
        pricetracker(InpStock)
    
    elif choice1 == "trends":
        cls()
        trends()
    
    elif choice1 == "news":
        news()

    print("Press ENTER to continue...")
    keyboard.wait("enter")