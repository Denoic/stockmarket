import keyboard
import json
from info import Info
from pricetracker import pricetracker
from trending import trends
from news import news
from info import filecreation
from cls import cls
from exit import exit
from about import about

while True:
    choice = ""
    cls()
    print("Info Price Trends News About Exit")
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
        print(InpStock)
        input()
        cls()
        pricetracker(InpStock)
    
    elif choice == "trends":
        cls()
        trends()
    
    elif choice == "news":
        news()

    elif choice == "about":
        
        about()

    elif choice == "exit":
        exit()

    print()
    print("Press SPACE to continue...")
    keyboard.wait("space") 