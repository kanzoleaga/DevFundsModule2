# =======================================================================

# Import the modules needed to run the script.
import sys
import os
from src.com.jalasoft.search_files.utils.validator import *

# Main definition - constants
menu_actions = {}
menu1_actions = {}
menu2_actions = {}
menu3_actions = {}


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


# Execute main menu
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

# Execute menu1
def exec_menu1(choice):
    os.system("cls")
    ch = choice.lower()
    if ch == '':
        menu1_actions['main_menu']()
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

# Menu1 Actions:
def find_all_assets():
    path = input("Enter the path >>  ")
    print("Find all assets was selected. Starting the searching process in", path)

def find_assets_by_name():
    path = input("Enter the path >>  ")
    name = input("Enter the name of the asset>>  ")
    print("Find all assets by name was selected. Starting the searching process ...")

def find_assets_by_size():
    path = input("Enter the path >>  ")
    size = input("Enter the size of the name of the asset>>  ")
    print("Find all assets by name was selected. Starting the searching process ...")

# Menu2 Actions:
def find_files_by_extetion():
    path = input("Enter the path >>  ")
    ext = input("Enter the extention >>  ")
    print("Find all files by extention was selected. Starting the searching process ...")


def find_files_by_name():
    path = input("Enter the path >>  ")
    ext = input("Enter file name >>  ")
    print("Find all files by name was selected. Starting the searching process ...")


def find_files_by_size():
    path = input("Enter the path >>  ")
    ext = input("Enter the size >>  ")
    print("Find all files by size was selected. Starting the searching process ...")

# Menu3 Actions:
def find_folders_by_name():
    path = input("Enter the path >>  ")
    ext = input("Enter the folder name >>  ")
    print("Find folders by name was selected. Starting the searching process ...")


def find_folders_by_size():
    path = input("Enter the path >>  ")
    ext = input("Enter the folder size >>  ")
    print("Find folders by size was selected. Starting the searching process ...")


# Back to main menu
def back(menu):
    if menu == "main_menu":
        menu_actions['main_menu']()
    elif menu == menu1:
        menu1_actions['main_menu']()
    # elif menu == menu2:
    #     menu2_actions['main_menu']()
    # elif menu == menu3:
    #     menu3_actions['main_menu']

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
    '9': back("main_menu"),
    '0': exit,
}

menu1_actions = {
    'main_menu': menu1,
    '1': find_all_assets,
    '2': find_assets_by_name,
    '3': find_assets_by_size,
    '9': back('menu1'),
    '0': exit,
}


menu2_actions = {
    'main_menu': menu2,
    '1': find_files_by_extetion,
    '2': find_files_by_name,
    '3': find_files_by_size,
    '9': back(menu2),
    '0': exit,
}

menu3_actions = {
    'main_menu': menu3,
    '1': find_folders_by_name,
    '2': find_folders_by_size,
    '9': back(menu3),
    '0': exit,
}

# =======================
#      MAIN PROGRAM
# =======================

# Main Program
if __name__ == "__main__":
    # Launch main menu
    main_menu()