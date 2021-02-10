import keyboard
import json
from info import Info
from pricetracker import pricetracker
from trending import trends
from news import news
from info import filecreation
from cls import cls
from exit import exit

  
while True:
    cls()
    print("Info Price Trends News")
    choice = input("Select one: ")
    choice = choice.lower()

    cls()
    if choice == "info":
        InpStock = input("Enter ticker: ")
        InpStock = InpStock.upper()
        cls()
        filecreation(InpStock)
        Info(InpStock)
    
    elif choice == "price":
        InpStock = input("Enter ticker: ")
        InpStock = InpStock.upper()
        cls()
        pricetracker(InpStock)
    
    elif choice == "trends":
        cls()
        trends()
    
    elif choice == "news":
        news()


    print("Press SPACE to continue...")
    keyboard.wait("space")
    choice = "" 