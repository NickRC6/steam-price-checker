from .regions import STEAM_REGIONS
from .print_block import print_block

def setup_regions():
    picked_regions = []
    setup_completed = False
    print_block("Pick the two regions (country codes) you want to compare.\nExample: 'US', 'JP'.\nInput 'SETUP' to add the country codes.\nOr if you don't know, input 'LIST'.")
    while setup_completed == False:
        choice = input("Input 'SETUP' or 'LIST'...").lower()
        if choice == "setup":
            region1 = input("Region 1: ").lower()
            region2 = input("Region 2: ").lower()
            if region1 in STEAM_REGIONS and region2 in STEAM_REGIONS:
                picked_regions.append(region1)
                picked_regions.append(region2)
                setup_completed = True
            else:
                print("One or both region codes are invalid. Type LIST to see valid codes.")
        elif choice == "list":
            for code, country in STEAM_REGIONS.items():
                print(f"{code} - {country}")
        else:
            print("Invalid input.")

    return picked_regions