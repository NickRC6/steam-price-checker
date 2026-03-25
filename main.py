import sys
sys.path.insert(0, 'src')

from steam_regional_prices.steam_api import search_game
from steam_regional_prices.setup_regions import setup_regions
from steam_regional_prices.print_block import print_block
from steam_regional_prices.price_fetcher import price_fetcher

def main():
    print_block("Steam Regional Price Tool")
    print("Welcome. Pick two regions to compare pricing.")
    regions = setup_regions()
    print(f"Your selected regions are: {regions}")

    while regions != None: 
        game_name = input("Enter a game name: ")
        app_id = search_game(game_name)

        if not app_id:
            print_block("Invalid option or game not found")
            choice = input("Enter K to try again or Q to quit:").lower()
            if choice == "q":
                print_block("Exiting program.")
                return
            elif choice == "k":
                continue
            print_block("Invalid option. Returning...")
            return
        else:
             print_block(f"Your selected game is: {game_name}. Steam App ID: {app_id}.")
             price_fetcher(app_id, regions)
             return


if __name__ == "__main__":
    main()