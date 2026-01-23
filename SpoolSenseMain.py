#MAIN SCRIPT
#Created by thomasse10 on GitHub

#imports
import json

#clear spools variable
spools = []

#create spool
def create_spool():
    print("--Create Spool--")
    sbrand = input("Enter brand of Filament: ").strip()
    stype = input("Enter type of Filament: ").strip()
    scolour = input("Enter colour of Filament: ").strip()
    sweight = input("Enter weight of spool: ").strip()


def main_menu():
    print("---Main Menu---")
    print("Please choose an option:\n1. Add new Spool \n2. Change Spool weight")
    choice = input("> ").strip()

    if not choice.isdigit():
        return None
    return int(choice)

def main():
    while True:
        menu_choice = main_menu()
        if menu_choice == 1:
            create_spool()
        elif menu_choice == 2:
            print("2 has been selected")
        else:
            print("Error, try again")

main()