import requests
from steam_regional_prices.print_block import print_block

def build_exchange_url(from_currency, to_currency, amount):
    base_url = "https://api.frankfurter.app/latest"
    return f"{base_url}?amount={amount}&from={from_currency}&to={to_currency}"

def currency_processor(dual_price, dual_currency, regions):
    exchange_request_url = build_exchange_url(dual_currency[0], dual_currency[1], dual_price[0])
    r = requests.get(exchange_request_url)

    data = r.json()

    #print(data["rates"][f"{dual_currency[1]}"], dual_currency[1])
    discount_calculator(data, dual_price, dual_currency, regions)

def discount_calculator(data, dual_price, dual_currency, regions):

    if (data["rates"][f"{dual_currency[0]}"] > dual_price[1]):
        print(f"{regions[1].upper()} has a better deal.")
        print(data["rates"][f"{dual_currency[1]}"], dual_currency[1])
    elif (data["rates"][f"{dual_currency[0]}"] < dual_price[1]):
        print(f"{regions[0].upper()} has a better deal.")
    elif (data["rates"][f"{dual_currency[0]}"] == dual_price[1]):
        print(f"{regions[0].upper()} has the same price as {regions[1].upper()}.")
    else:
        print("There was an error calculating the best deal, returning...")
        return
    
    # i need to deformat "data"