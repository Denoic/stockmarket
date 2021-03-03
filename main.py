import keyboard
from movers import gainers
from movers import losers
from info import Info
from pricetracker import pricetracker
from trending import trends
from info import filecreation
from cls import cls
from exit import exit
from about import about
from etf import etf
from currencies import currencies


while True:
    choice = ""
    InpStock = ""
    cls()
    print("Info(1) Price(2) Trends(3) Movers(4) ETFs(5) Currencies(6) About(7) Exit(8)")
    choice = input("Select one: ")
    choice = choice.lower()

    
    cls()
    if choice == "info" or choice == "1":
        InpStock = input("Enter ticker: ")
        InpStock = InpStock.upper()
        cls()
        filecreation(InpStock)
        Info(InpStock)
        print()
        print("Press ESC to continue...")
        keyboard.wait("esc")

    elif choice == "price" or choice == "2":
        InpStock = input("Enter ticker: ")
        cls()
        pricetracker(InpStock.upper())

    elif choice == "trends" or choice == "3":
        trends()
        print()
        print("Press ESC to continue...")
        keyboard.wait("esc")

    elif choice == "movers" or choice == "4":
        while True:
            mover = input("Gainers(1) or Losers(2): ")
            mover = mover.lower()

            cls()

            if mover == "gainers" or mover == "1":
                gainers()
                break

            elif mover == 'losers' or mover == "2":
                losers()
                break

            else:
                print('Invalid choice')
        print()
        print("Press ESC to continue...")
        keyboard.wait("esc")

    elif choice == "etfs" or choice == "5":
        etf()
        print()
        print("Press ESC to continue...")
        keyboard.wait("esc")

    elif choice == "currencies" or choice == "6":
        currencies()
        print()
        print("Press ESC to continue...")
        keyboard.wait("esc")

    elif choice == "about" or choice == "7":
        about()
        print()
        print("Press ESC to continue...")
        keyboard.wait("esc")

    elif choice == "exit" or choice == "8":
        exit()

    else:
        print("Invalid. Please Try again with a valid option")
        print()
        print("Press ESC to continue...")
        keyboard.wait("esc")
