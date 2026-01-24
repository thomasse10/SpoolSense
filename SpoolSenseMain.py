#MAIN SCRIPT
#Created by thomasse10 on GitHub

#Unfinished main script

#Debug
debug = True
def debugprint(msg):
    if debug:
        print(f"[DEBUG] {msg}")

#imports
import json

#clear spools variable
spools = []

#create spool
def create_spool():
    print("--Create Spool--")
    sbrand = input("Enter brand of Filament: ").strip()
    while not sbrand:
        sbrand = input("Cannot be empty.\nEnter brand of Filament: ").strip()
    if sbrand:
        sbrand = sbrand.lower()
        debugprint(sbrand)
    stype = input("Enter type of Filament: ").strip()
    while not stype:
        stype = input("Cannot be empty.\nEnter type of Filament: ").strip()
    if stype:
        stype = stype.lower()
        debugprint(stype)
    scolour = input("Enter colour of Filament: ").strip()
    while not scolour:
        scolour = input("Cannot be empty.\nEnter colour of Filament: ").strip()
    if scolour:
        scolour = scolour.lower()
        debugprint(scolour)
#    sweight = input("Enter weight of spool: ").strip()
#    while not sweight:
#        sweight = input("Enter weight of Filament: ").strip()
#    if sweight:
#        sweight = sweight.lower()
    newspool = sbrand, stype, scolour
    debugprint(newspool)
    return newspool


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