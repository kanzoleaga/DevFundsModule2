import sys
import os
from src.com.jalasoft.search_files.search.search import *


class Menu():
    def __init__(self):
        # Define dictionaries for menus - constants
        self.menu_actions = {}

    # =======================
    #     MENU FUNCTIONS
    # =======================

    # Main menu
    def main_menu(self):
        os.system("cls")
        print("Please choose the option you want to start:")
        print("1. Basic search")
        print("2. Advanced search")
        print("0. Quit")
        choice = input(" >>  ")
        Menu.exec_menu(self, choice)

    # Execute main menu
    def exec_menu(self, choice):
        os.system("cls")
        ch = choice.lower()
        if ch == '':
            Menu.menu_actions['main_menu'](self)
        else:
            try:
                Menu.menu_actions[ch](self)
            except KeyError:
                print("Invalid selection, please try again.\n")
                Menu.menu_actions['main_menu'](self)
        return


    # Main menu Actions:
    def basic_search(self):
        path = str(input("Enter the path >>  "))
        while not os.path.isdir(path):
            path = input("Invalid path. Please enter a valid path >>  ")
        name = input("Enter the name of the file (empty for all) >>  ")
        if str(name) == '':
            name = None
        extension = input("Enter the extension (empty for all) >>  ")
        if str(extension) == '':
            extension = None
        asset_type = input("Enter the asset_type (dir/file/empty for all) >>  ")
        if str(asset_type) == '':
            asset_type = None
        search = Search()
        search.set_basic_search_criteria(path, name, extension, asset_type)
        search.search_by_criteria()
        print(search.result)



        Menu.main_menu(self)

    def advanced_search(self):
        pass

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
        '1': basic_search,
        '2': advanced_search,
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