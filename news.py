import yahoo_fin.stock_info as si

def news():
    quote = si.get_quote_table('nflx')
    print(quote)
    #still in work