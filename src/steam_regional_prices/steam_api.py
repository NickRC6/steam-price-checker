import requests
store_search_URL = "https://store.steampowered.com/api/storesearch/"

def build_api_url(app_id, region):
    base_steam_url = "https://store.steampowered.com/api/appdetails?appids="
    full_api_url = base_steam_url + str(app_id) + "&cc=" + region

    return full_api_url

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