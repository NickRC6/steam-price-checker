import requests
from steam_regional_prices.print_block import print_block

def build_exchange_url(from_currency, to_currency, amount):
    base_url = "https://api.frankfurter.app/latest"
    return f"{base_url}?amount={amount}&from={from_currency}&to={to_currency}"

def currency_processor(dual_price, dual_currency, regions_names):
    exchange_request_url = build_exchange_url(dual_currency[0], dual_currency[1], dual_price[0])
    r = requests.get(exchange_request_url)

    data = r.json()

    discount_calculator(data, dual_price, dual_currency, regions_names)

def discount_calculator(data, dual_price, dual_currency, regions_names):

    saved = None

    if "rates" not in data:
        print("It seems as the exchange API does not support this currency!\nTherefore, I cannot automatically give you the converted amount you'd be saving.")
        return 
    
    if (dual_currency[0] == dual_currency[1]):
        print(f"{regions_names[0]} has the same currency as {regions_names[1]}. The price is the same in both regions.")
        return

    if (data["rates"].get(dual_currency[1]) > dual_price[1]):
        saved = abs(data["rates"].get(dual_currency[1]) - dual_price[1])
        print_block(f"{regions_names[1]} has a better deal.\nYou are saving the equivalent of {saved:.2f} {dual_currency[1]} when using Steam's {regions_names[1]} store.")
    elif (data["rates"].get(dual_currency[1]) < dual_price[1]):
        saved = abs(data["rates"].get(dual_currency[1]) - dual_price[1])
        print_block(f"{regions_names[0]} has a better deal.\nYou are saving the equivalent of {saved:.2f} {dual_currency[1]} when using Steam's {regions_names[0]} store.")
    elif (data["rates"].get(dual_currency[1]) == dual_price[1]):
        print(f"Steam's {regions_names[0]} store has the same price as Steam's {regions_names[1]} store.")
    else:
        print("There was an error calculating the best deal, returning...")
        return
    