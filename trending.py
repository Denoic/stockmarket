import requests

def trends():
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/get-trending-tickers"

    querystring = {"region":"US"}

    headers = {
        'x-rapidapi-key': "623ecea589msh70f225267987d8ep18f5c1jsn34e5895911b9",
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    result = response.json()

    print(result)
    print()
    print()
    print()
    print()
    print(result.get('finance')['result'])
    #still in work