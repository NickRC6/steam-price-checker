import sys
sys.path.insert(0, 'src')

from steam_regional_prices.steam_api import search_game

def print_block(text):
        print("-" * 40)
        print(text)
        print("-" * 40)


def main():

    while True: 
        print_block("Steam Regional Price Tool")
        app_query = input("Enter a game name: ")
        results = search_game(app_query)

        if not results:
            print_block("Invalid option.")
            choice = input("Enter K to try again or Q to quit:").lower()
            if choice.lower() == "q":
                print_block("Exiting program.")
                return
            elif choice.lower() == "k":
                continue
            print_block("Invalid option. Returning...")
            return
        else:
             print_block(f"Your selected game is: {results}. Sadly, this program is not finished yet, so I am not seraching anywhere.")
             return


if __name__ == "__main__":
    main()