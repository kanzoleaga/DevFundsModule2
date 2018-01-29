# =======================================================================

# Import the modules needed to run the script.
import sys
import os
from src.com.jalasoft.search_files.utils.validator import *

# Main definition - constants
menu_actions = {}

# =======================
#     MENUS FUNCTIONS
# =======================

# Main menu
def main_menu():
    os.system("cls")
    print("Welcome,\n")
    print("Please choose the option you want to start:")
    print("1. Search all assets from a path")
    print("2. Search all files in a path")
    print("3. Search all directories in a path")
    print("0. Quit")
    choice = input(" >>  ")
    exec_menu(choice)

    return


# Execute menu
def exec_menu(choice):
    os.system("cls")
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print
            "Invalid selection, please try again.\n"
            menu_actions['main_menu']()
    return

# Execute menu
def exec_menu1(choice):
    os.system("cls")
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu1_actions[ch]()
        except KeyError:
            print
            "Invalid selection, please try again.\n"
            menu_actions['main_menu']()
    return

# Menu 1
def menu1():
    _ = os.system("cls")
    print("Searching for assets \n")
    print("1. Find all assets")
    print("2. Find assets by name")
    print("2. Find assets by size")
    print("9. Back")
    print("0. Quit")
    choice = input(" >>  ")
    exec_menu1(choice)
    return

# Menu 2
def menu2():
    os.system("cls")
    print("Searching for files \n")
    print("1. Find files by extension")
    print("2. Find files by name")
    print("3. Find files by size")
    print("9. Back")
    print("0. Quit")
    choice = input(">>  ")
    exec_menu(choice)
    return

# Menu 3
def menu3():
    os.system("cls")
    print ("Sarching for folders \n")
    print("1. Find folders by name")
    print("2. Find folders by size")
    print("9. Back")
    print("0. Quit")
    choice = input(" >>  ")
    exec_menu(choice)
    return

def find_all_assets():
    path = input(" Enter the path >>  ")
    print("Find all assets was selected. Starting the searching process in", path)

def find_assets_by_name():
    print("Find all assets by name was selected. Starting the searching process ...")

def find_assets_by_size ():
    pass

# Back to main menu
def back():
    menu_actions['main_menu']()


# Exit program
def exit():
    sys.exit()


# =======================
#    MENUS DEFINITIONS
# =======================

# Menu definition
menu_actions = {
    'main_menu': main_menu,
    '1': menu1,
    '2': menu2,
    '3': menu3,
    '9': back,
    '0': exit,
}

menu1_actions = {
    '1': find_all_assets,
    '2': find_assets_by_name,
    '3': find_assets_by_size,
    '9': back,
    '0': exit,
}

# =======================
#      MAIN PROGRAM
# =======================

# Main Program
if __name__ == "__main__":
    # Launch main menu
    main_menu()