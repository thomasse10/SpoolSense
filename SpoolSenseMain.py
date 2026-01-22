#MAIN CODE
#Created by thomasse10 on GitHub

#testing out main loop

#imports
import json

#create spool
def create_spool():
    pass

def main_menu():
    print("Please choose an option:\n1. Hello \n2. World")
    choice = input("> ").strip()

    if not choice.isdigit():
        return None
    return int(choice)

def main():
    while True:
        menu_choice = main_menu()
        if menu_choice == 1:
            print("hello")
        elif menu_choice == 2:
            print("world")
        else:
            print("Error, try again")

main()