import keyboard
from movers import gainers
from movers import losers
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
    InpStock = ""
    cls()
    print("Info Price Trends News Movers About Exit")
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
        trends()

    elif choice == "news":
        news()

    elif choice == "movers":
        while True:
            mover = input("Gainers or Losers: ")
            mover = mover.lower()

            cls()

            if mover == "gainers":
                gainers()
                break

            elif mover == 'losers':
                losers()
                break

            else:
                print('Invalid choice')


    elif choice == "about":
        about()

    elif choice == "exit":
        exit()

    else:
        cls()
        print("Invalid. Please Try again with a valid option")

    print()
    print("Press ESC to continue...")
    keyboard.wait("esc")
