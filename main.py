import sys
sys.path.insert(0, 'src')

from steam_regional_prices.steam_api import search_game
from steam_regional_prices.setup_regions import setup_regions
from steam_regional_prices.print_block import print_block

def main():
    print_block("Steam Regional Price Tool")
    print("Welcome. Pick two regions to compare pricing.")
    set_up = setup_regions()
    print(set_up)

    while set_up != None: 
        app_query = input("Enter a game name: ")
        results = search_game(app_query)

        if not results:
            print_block("Invalid option.")
            choice = input("Enter K to try again or Q to quit:").lower()
            if choice == "q":
                print_block("Exiting program.")
                return
            elif choice == "k":
                continue
            print_block("Invalid option. Returning...")
            return
        else:
             print_block(f"Your selected game is: {results}. Sadly, this program is not finished yet, so I am not seraching anywhere.")
             return


if __name__ == "__main__":
    main()