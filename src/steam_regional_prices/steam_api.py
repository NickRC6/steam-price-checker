import requests

from steam_regional_prices.regions import STEAM_REGIONS
from steam_regional_prices.print_block import print_block
from steam_regional_prices.currency_exchange import currency_processor

store_search_URL = "https://store.steampowered.com/api/storesearch/"
app_details_URL = "https://store.steampowered.com/api/appdetails"

def search_game(game_name):
    params = {
        "term": game_name,
        "l": "english",
        "cc": "us"
    }

    response = requests.get(store_search_URL, params=params)
    response.raise_for_status()

    data = response.json()

    if data["items"]:
        return data["items"][0]["id"]

    return None

def price_fetcher(game_name, app_id, regions):

    dual_price = []
    dual_currency = []

    for region in regions:
        params = {
            "appids": app_id,
            "cc": region,
            "filters": "price_overview"
        }
    
        r = requests.get(app_details_URL, params=params)
        data = r.json()
        currency =  data[str(app_id)]["data"]["price_overview"]["currency"]
        price = data[str(app_id)]["data"]["price_overview"]["final"] / 100 

        region_name = STEAM_REGIONS.get(region, region.upper())

        print_block(f"Price information of {game_name} in {region_name}:")
        print_block(price)
        dual_price.append(price)
        dual_currency.append(currency)
    currency_processor(dual_price, dual_currency, regions)
