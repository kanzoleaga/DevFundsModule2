# =======================================================================

# Import the modules needed to run the script.
import sys
import os
from src.com.jalasoft.search_files.utils.validator import *
from  src.com.jalasoft.search_files.search.search import Search

class Menu():
    def __init__(self):
        # Define dictionaries for menus - constants
        self.menu_actions = {}
        self.menu1_actions = {}
        self.menu2_actions = {}
        self.menu3_actions = {}

    # =======================
    #     MENU FUNCTIONS
    # =======================

    # Main menu
    def main_menu(self):
        os.system("cls")
        print("Please choose the option you want to start:")
        print("1. Search all assets from a path")
        print("2. Search all files in a path")
        print("3. Search all directories in a path")
        print("0. Quit")
        choice = input(" >>  ")
        Menu.exec_menu(self, choice)

    # Execute main menu
    def exec_menu(self, choice):
        os.system('cls')
        menu_option = choice.lower()
        if menu_option != '1' and menu_option != '2' and menu_option != '3' and menu_option != '0':
            os.system("cls")
            print("Invalid selection, please try again.\n")
            Menu.menu_actions['main_menu'](self)
        else:
            try:
                Menu.menu_actions[menu_option](self)
            except KeyError:
                print("Invalid selection, please try again.\n")
                Menu.menu_actions['main_menu'](self)

    # Execute menu1
    def exec_menu1_search_assets(self, choice):
        menu_option = choice.lower()
        if menu_option != '1' and menu_option != '2' and menu_option != '3' and menu_option != '9' and menu_option != '0':
            os.system("cls")
            print("Invalid selection, please try again.\n")
            Menu.menu1_actions['main_menu'](self)
        else:
            try:
                Menu.menu1_actions[menu_option](self)
            except KeyError:
                print("Invalid selection, please try again.\n")
                Menu.menu1_actions['main_menu'](self)
        return

    def exec_menu2(self, choice):
        os.system("cls")
        ch = choice.lower()
        if ch == '':
            Menu.menu2_actions['main_menu'](self)
        else:
            try:
                Menu.menu2_actions[ch](self)
            except KeyError:
                print("Invalid selection, please try again.\n")
                Menu.menu2_actions['main_menu'](self)
        return

    # Execute menu1
    def exec_menu3(self, choice):
        os.system("cls")
        ch = choice.lower()
        if ch == '':
            Menu.menu3_actions['main_menu'](self)
        else:
            try:
                Menu.menu3_actions[ch](self)
            except KeyError:
                print
                "Invalid selection, please try again.\n"
                Menu.menu3_actions['main_menu'](self)
        return

    # Menu 1
    def menu1_search_assets(self):
        print("\n")
        print("Searching for assets in a path \n")
        print("1. Find all assets")
        print("2. Find assets by name")
        print("3. Find assets by size")
        print("9. Back")
        print("0. Quit")
        choice = input(" >>  ")
        Menu.exec_menu1_search_assets(self, choice)
        return

    # Menu 2
    def menu2(self):
        _= os.system("cls")
        print("Searching for files in a path \n")
        print("1. Find files by extension")
        print("2. Find files by name")
        print("3. Find files by size")
        print("9. Back")
        print("0. Quit")
        choice = input(">>  ")
        Menu.exec_menu2(self, choice)
        return

    # Menu 3
    def menu3(self):
        os.system("cls")
        print ("Sarching for folders in a path \n")
        print("1. Find folders by name")
        print("2. Find folders by size")
        print("9. Back")
        print("0. Quit")
        choice = input(" >>  ")
        Menu.exec_menu3(self, choice)
        return

    # Menu1 Actions:
    def find_all_assets(self):
        path = input("Enter full path >>  ")
        while not os.path.isdir(path):
            path = input("Invalid path. Please enter a valid full path >>  ")
        print("Find all assets that were selected. Starting the searching process in ", path)
        search = Search(path)
        print(search.search_files_and_directories())

        Menu.menu1_search_assets(self)

    def find_assets_by_name(self):
        path = input("Enter the path >>  ")
        while not os.path.isdir(path):
            path = input("Invalid path. Please enter a valid path >>  ")
        name = input("Enter the name of the asset>>  ")
        print("Find all assets by name was selected. Starting the searching process ...")
        Menu.menu1_search_assets(self)

    def find_assets_by_size(self):
        path = input("Enter the path >>  ")
        while not os.path.isdir(path):
            path = input("Invalid path. Please enter a valid path >>  ")
        size = input("Enter the size of the asset>>  ")
        while not is_number(size):
            size = input("Invalid size. Please enter a number >>  ")
        print("Find all assets by size was selected. Starting the searching process ...")
        Menu.menu1_search_assets(self)

    # Menu2 Actions:
    def find_files_by_extetion(self):
        path = input("Enter the path >>  ")
        while not os.path.isdir(path):
            path = input("Invalid path. Please enter a valid path >>  ")
        ext = input("Enter the extension >>  ")
        print("Find all files by extension was selected. Starting the searching process ...")
        Menu.menu2(self)


    def find_files_by_name(self):
        path = input("Enter the path >>  ")
        while not os.path.isdir(path):
            path = input("Invalid path. Please enter a valid path >>  ")
        name = input("Enter file name >>  ")
        print("Find all files by name was selected. Starting the searching process ...")
        Menu.menu2(self)

    def find_files_by_size(self):
        path = input("Enter the path >>  ")
        while not os.path.isdir(path):
            path = input("Invalid path. Please enter a valid path >>  ")
        size = input("Enter the size of the file >>  ")
        while not is_number(size):
            size = input("Invalid size. Please enter a number >>  ")
        print("Find all files by size was selected. Starting the searching process ...")
        Menu.menu2(self)

    # Menu3 Actions:
    def find_folders_by_name(self):
        path = input("Enter the path >>  ")
        while not os.path.isdir(path):
            path = input("Invalid path. Please enter a valid path >>  ")
        name = input("Enter the folder name >>  ")
        print("Find folders by name was selected. Starting the searching process ...")
        Menu.menu3(self)

    def find_folders_by_size(self):
        path = input("Enter the path >>  ")
        while not os.path.isdir(path):
            path = input("Invalid path. Please enter a valid path >>  ")
        size = input("Enter the folder size >>  ")
        while not is_number(size):
            size = input("Invalid size. Please enter a number >>  ")
        print("Find folders by size was selected. Starting the searching process ...")
        Menu.menu3(self)

    # Back to main menu
    def back(self):
        Menu.menu_actions['main_menu'](self)


    # Exit program
    def exit(self):
        sys.exit()


    # =======================
    #    MENUS DEFINITIONS
    # =======================

    # Menu definition
    menu_actions = {
        'main_menu': main_menu,
        '1': menu1_search_assets,
        '2': menu2,
        '3': menu3,
        '0': exit,
    }

    menu1_actions = {
        'main_menu': menu1_search_assets,
        '1': find_all_assets,
        '2': find_assets_by_name,
        '3': find_assets_by_size,
        '9': back,
        '0': exit,
    }

    menu2_actions = {
        'main_menu': menu2,
        '1': find_files_by_extetion,
        '2': find_files_by_name,
        '3': find_files_by_size,
        '9': back,
        '0': exit,
    }

    menu3_actions = {
        'main_menu': menu3,
        '1': find_folders_by_name,
        '2': find_folders_by_size,
        '9': back,
        '0': exit,
    }

# =======================
#      MAIN PROGRAM
# =======================

# Main Program
if __name__ == "__main__":
    # Launch main menu
    menu = Menu()
    menu.main_menu()