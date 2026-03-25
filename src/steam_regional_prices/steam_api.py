
def build_api_url(app_id, region):
        base_steam_url = "https://store.steampowered.com/api/appdetails?appids="
        full_api_url = base_steam_url + str(app_id) + "&cc=" + region

        return full_api_url

def search_game(app_query):
    pass 
