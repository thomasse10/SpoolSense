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

#save file location
SAVEFILE = "spools.json"

#clear spools variable
spools = []

#save spools
def save_spools():
    try:
        with open(SAVEFILE, "w") as f:
            json.dump(spools, f, indent=4)
        with open(SAVEFILE, "r") as f:
            savecheck = json.load(f)
        if savecheck == spools:
            print("File saved successfully")
        else:
            print("Save file does not match memory! Please try again.")
    except Exception as e:
        debugprint(e)
        print("Failed to save. Please try again.")

#load spools
def load_spools():
    global spools
    try:
        with open(SAVEFILE, "r") as f:
            spools = json.load(f)
        if spools.strip() == []:
            print("Save file loaded successfully. \nWARNING: Save file is empty. ")
        else:
            print("Save file loaded successfully. ")
    except FileNotFoundError:
        print("Save file could not be found.")
    except Exception as e:
        debugprint(e)
        print("An error occured loading the save file. Please try again. ")
    

#create spool
def create_spool():
    global spools
    spoolused = input("Has this Spool been used before? Y/N: ")
    if spoolused.lower() == "n":
        sbrand = input("Enter brand of Filament: ").strip().lower()
        debugprint(sbrand)
        stype = input("Enter type of Filament: ").strip().lower()
        debugprint(stype)
        scolour = input("Enter colour of Filament: ").strip().lower()
        debugprint(scolour)
        sweight = float(input("Enter weight of filament in kg: ").strip())
        spools.append({"sbrand": sbrand, "stype": stype, "scolour": scolour, "sweight": sweight})
        return None


def main_menu():
    print("---Main Menu---")
    print("Please choose an option:\n1. Add new Spool \n2. View Spools\n3. Save Spools\n4. Load Spools")
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
            for s in spools:
                print(s["sbrand"], s["stype"], s["scolour"],s["sweight"])
        elif menu_choice == 3:
            save_spools()
        elif menu_choice == 4:
            load_spools()
        else:
            print("Error, try again")

main()