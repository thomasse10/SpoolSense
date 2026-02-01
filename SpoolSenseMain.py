#MAIN SCRIPT
#Created by thomasse10 on GitHub

#Unfinished main script

#Debug Mode
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
        if spools == []:
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
    spoolused = input("Has this Spool been used before? Y/N: ").strip()
    if spoolused.lower() == "n":
        sbrand = input("Enter brand of Filament: ").lower()
        debugprint(sbrand)
        stype = input("Enter type of Filament: ").strip().lower()
        debugprint(stype)
        scolour = input("Enter colour of Filament: ").strip().lower()
        debugprint(scolour)
        if spoolused.lower() == "y":
            knownemptyspoolw = input("Do you know the empty spool weight? Y/N: ").strip()
            if knownemptyspoolw == "y":
                emptyspoolw = input("please enter empty spool weight in g: ")
            sremainingw = input("Enter approximate remaining filament in g: ").strip()
        else:
            sremainingw = float(input("Enter weight of filament in g: ").strip())
        spools.append({"sbrand": sbrand, "stype": stype, "scolour": scolour, "sremainingw": sremainingw})
        return None
        

#update spool weight

def update_spool():
    global spools
    if spools:
        print("Select a spool:")
        for i,s in enumerate(spools,start=1):
            print(f"{i}.",s["sbrand"], s["stype"], s["scolour"],s["sremainingw"],"g")
        choice = input("> ").strip()
        index = int(choice) - 1
        print("What would you like to edit:\n1. Spool weight\n2. Spool brand\n3. Spool colour\n4. Spool type")
        edit_choice = input("> ").strip()
        if int(edit_choice) == 1:
            new_weight = float(input("Please enter new weight in grams: "))
            spools[index]["sremainingw"] = new_weight
            debugprint(spools)
        elif int(edit_choice) == 2:
            new_brand = input("Please enter new brand name: ")
            spools[index]["sbrand"] = new_brand
            debugprint(spools)
        elif int(edit_choice) == 3:
            new_colour = input("Please enter new colour: ")
            spools[index]["scolour"] = new_colour
            debugprint(spools)
        elif int(edit_choice) == 4:
            new_type = input("Please enter new filament type: ")
            spools[index]["sbrand"] = new_type
            debugprint(spools)
        else:
            print("Error, Try again")
    else: 
        print("No spools could be found. ")

    

def main_menu():
    print("---Main Menu---")
    print("Please choose an option:\n1. Add new Spool \n2. View Spools\n3. Save Spools\n4. Load Spools\n5. Edit spools")
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
                print(s["sbrand"], s["stype"], s["scolour"],s["sremainingw"],"g")
        elif menu_choice == 3:
            save_spools()
        elif menu_choice == 4:
            load_spools()
        elif menu_choice == 5:
            update_spool()
        else:
            print("Error, try again")

main()