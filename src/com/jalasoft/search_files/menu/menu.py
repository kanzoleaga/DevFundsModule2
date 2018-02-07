# =======================================================================

# Import the modules needed to run the script.
import sys
import os
from src.com.jalasoft.search_files.utils.validator import *
from  src.com.jalasoft.search_files.search.search import Search

class Menu():
    def __init__(self):
        # Define dictionaries for menus - constants
        self.main_menu_actions = {}
        self.menu_option1_actions = {}
        self.menu_option2_actions = {}
        self.menu_option3_actions = {}

    # =======================
    #     MENU FUNCTIONS
    # =======================

    # Main menu
    def main_menu(self):
        os.system("cls")
        print("MAIN MENU - Choose an option to start:")
        print("1. Search all assets from a path")
        print("2. Search all files in a path")
        print("3. Search all directories in a path")
        print("0. Quit")
        choice = input(" >>  ")
        Menu.exec_actions_on_main_menu(self, choice)

    # Execute main menu
    def exec_actions_on_main_menu(self, choice):
        os.system('cls')
        menu_option = choice.lower()
        if menu_option != '1' and menu_option != '2' and menu_option != '3' and menu_option != '0':
            os.system("cls")
            print("Invalid selection, please try again.\n")
            Menu.main_menu_actions['main_menu'](self)
        else:
            try:
                Menu.main_menu_actions[menu_option](self)
            except KeyError:
                print("Invalid selection, please try again.\n")
                Menu.main_menu_actions['main_menu'](self)

    # Main menu - Option 1
    def menu1_search_all_assets(self):
        print("\n")
        print("Searching for assets in a path \n")
        print("1. Find all assets")
        print("2. Find assets by name")
        print("3. Find assets by size less than - KB")
        print("4. Find assets by size greater than - KB")
        print("9. Back")
        print("0. Quit")
        choice = input(" >>  ")
        Menu.exec_actions_on_menu_option1(self, choice)

    # Execute action on main menu option 1 - Search all assets from a path
    def exec_actions_on_menu_option1(self, choice):
        menu_option = choice.lower()
        if menu_option != '1' and menu_option != '2' and menu_option != '3' and menu_option != '4' and menu_option != '9' and menu_option != '0':
            os.system("cls")
            print("Invalid selection, please try again.\n")
            Menu.menu_option1_actions['main_menu'](self)
        else:
            try:
                Menu.menu_option1_actions[menu_option](self)
            except KeyError:
                print("Invalid selection, please try again.\n")
                Menu.menu_option1_actions['main_menu'](self)

    # Menu option 1 Actions:
    def find_all_assets(self):
        path = input("Enter full path >>  ")
        while not os.path.isdir(path):
            path = input("Invalid path. Please enter a valid full path >>  ")
        print("Find all assets from selected path. Starting the searching process in ", path)
        search = Search()
        search.set_basic_search_criteria(path)
        print(search.search_files_and_directories())
        # Return to menu option 1
        Menu.menu1_search_all_assets(self)

    def find_assets_by_name(self):
        path = input("Enter the path >>  ")
        while not os.path.isdir(path):
            path = input("Invalid path. Please enter a valid path >>  ")
        name = str(input("Enter the name of the asset >>  "))
        while not len(name) > 0:
            name = str(input("Enter the name of the asset >>  "))
        print("Find all assets by name from selected path. Starting the searching process in ", path)
        search = Search()
        search.set_basic_search_criteria(path, name)
        print(search.search_files_and_directories_by_name())
        # Return to menu option 1
        Menu.menu1_search_all_assets(self)

    def find_assets_by_size_less_than(self):
        path = input("Enter the path >>  ")
        while not os.path.isdir(path):
            path = input("Invalid path. Please enter a valid path >>  ")
        size = int(input("Enter the size in KB >>  "))
        while not is_number(size):
            size = int(input("Invalid size. Please enter a number >>  "))
        print("Find all assets less than selected size. Starting the searching process in ", path)
        search = Search()
        search.set_advanced_search_criteria(path, name=None, extension=None, size=size)
        search.criteria.get_criteria_value('size')
        print(search.search_files_and_directories_less_than_size_bytes())
        # Return to menu option 1
        Menu.menu1_search_all_assets(self)

    def find_assets_by_size_greater_than(self):
        path = input("Enter the path >>  ")
        while not os.path.isdir(path):
            path = input("Invalid path. Please enter a valid path >>  ")
        size = int(input("Enter the size in KB >>  "))
        while not is_number(size):
            size = int(input("Invalid size. Please enter a number >>  "))
        print("Find all assets greater than selected size. Starting the searching process in ", path)
        search = Search()
        search.set_advanced_search_criteria(path, size=size)
        print(search.search_files_and_directories_greater_than_size_bytes())
        # Return to menu option 1
        Menu.menu1_search_all_assets(self)

    # Main menu - Option 2
    def menu2_search_all_files(self):
        print("\n")
        print("Searching for files in a path \n")
        print("1. Find all files")
        print("2. Find files by extension")
        print("3. Find files by name")
        print("4. Find files by size less than -KB")
        print("5. Find files by size greater than -KB")
        print("9. Back")
        print("0. Quit")
        choice = input(" >>  ")
        Menu.exec_actions_on_menu_option2(self, choice)

    # Execute action on main menu option 2 - Search all files in a path
    def exec_actions_on_menu_option2(self, choice):
        menu_option = choice.lower()
        if menu_option != '1' and menu_option != '2' and menu_option != '3' and menu_option != '4' and menu_option != '5' and menu_option != '9' and menu_option != '0':
            os.system("cls")
            print("Invalid selection, please try again.\n")
            Menu.menu_option2_actions['main_menu'](self)
        else:
            try:
                Menu.menu_option2_actions[menu_option](self)
            except KeyError:
                print("Invalid selection, please try again.\n")
                Menu.menu_option2_actions['main_menu'](self)

    # Menu option 2 Actions:
    def find_all_files(self):
        path = input("Enter the path >>  ")
        while not os.path.isdir(path):
            path = input("Invalid path. Please enter a valid path >>  ")
        print("Find all files including sub directories. Starting the searching process in ", path)
        search = Search()
        search.set_basic_search_criteria(path)
        print(search.search_all_files())
        # Return to menu option 2
        Menu.menu2_search_all_files(self)

    def find_files_by_extension(self):
        path = input("Enter the path >>  ")
        while not os.path.isdir(path):
            path = input("Invalid path. Please enter a valid path >>  ")
        extension = input("Enter the extension >>  ")
        print("Find all files by extension. Starting the searching process in ", path)
        search = Search()
        search.set_basic_search_criteria(path,extension=extension)
        print(search.search_files_by_extension())
        # Return to menu option 2
        Menu.menu2_search_all_files(self)

    ## Missing from here
    def find_files_by_name(self):
        search = Search()
        path = input("Enter the path >>  ")
        while not os.path.isdir(path):
            path = input("Invalid path. Please enter a valid path >>  ")
        name = str(input("Enter file name >>  "))
        while not len(name) > 0:
            name = str(input("Enter file name >>  "))
        print("Find all files by name from selected path. Starting the searching process in ", path)
        search.set_basic_search_criteria(path, name)
        print(search.search_files_by_name(name))
        # Return to menu option 2
        Menu.menu2_search_all_files(self)

    def find_files_by_size_less_than(self):
        path = input("Enter the path >>  ")
        while not os.path.isdir(path):
            path = input("Invalid path. Please enter a valid path >>  ")
        size = int(input("Enter the size in KB >>  "))
        while not is_number(size):
            size = int(input("Invalid size. Please enter a number >>  "))
        print("Find all files less than selected size. Starting the searching process in ", path)
        search = Search()
        search.set_advanced_search_criteria(path, size=size)
        print(search.search_files_less_than_size_bytes())
        # Return to menu option 2
        Menu.menu2_search_all_files(self)

    def find_files_by_size_greater_than(self):
        path = input("Enter the path >>  ")
        while not os.path.isdir(path):
            path = int(input("Invalid path. Please enter a valid path >>  "))
        size = input("Enter the size in KB >>  ")
        while not is_number(size):
            size = int(input("Invalid size. Please enter a number >>  "))
        print("Find all files greater than selected size. Starting the searching process in ", path)
        search = Search()
        search.set_advanced_search_criteria(path, size=size)
        print(search.search_files_greater_than_size_bytes())
        # Return to menu option 2
        Menu.menu2_search_all_files(self)

    # Main menu - Option 3
    def menu3_search_all_directories(self):
        print("\n")
        print("Sarching for folders in a path \n")
        print("1. Find all folders")
        print("2. Find folders by name")
        print("3. Find count files in folders")
        print("4. Find folders by size less than - KB")
        print("5. Find folders by size greater than - KB")
        print("9. Back")
        print("0. Quit")
        choice = input(" >>  ")
        Menu.exec_actions_on_menu_option3(self, choice)

    # Execute action on main menu option 3 - Search all folders in a path
    def exec_actions_on_menu_option3(self, choice):
        menu_option = choice.lower()
        if menu_option != '1' and menu_option != '2' and menu_option != '3' and menu_option != '4' and menu_option != '5' and menu_option != '9' and menu_option != '0':
            os.system("cls")
            print("Invalid selection, please try again.\n")
            Menu.menu_option3_actions['main_menu'](self)
        else:
            try:
                Menu.menu_option3_actions[menu_option](self)
            except KeyError:
                print("Invalid selection, please try again.\n")
                Menu.menu_option3_actions['main_menu'](self)

    # Menu option 3 Actions:
    def find_folders_by_name(self):
        path = input("Enter the path >>  ")
        while not os.path.isdir(path):
            path = input("Invalid path. Please enter a valid path >>  ")
        name = input("Enter the folder name >>  ")
        while not len(str(name)) > 0:
            name = input("Enter a non empty folder name >>  ")
        print("Find folders by name was selected. Starting the searching process ...")
        Menu.menu3_search_all_directories(self)

    def find_folders_by_size(self):
        path = input("Enter the path >>  ")
        while not os.path.isdir(path):
            path = int(input("Invalid path. Please enter a valid path >>  "))
        size = int(input("Enter the folder size >>  "))
        while not is_number(size):
            size = int(input("Invalid size. Please enter a number >>  "))
        print("Find folders by size was selected. Starting the searching process ...")
        Menu.menu3_search_all_directories(self)

    # Back to main menu
    def back(self):
        Menu.main_menu_actions['main_menu'](self)


    # Exit program
    def exit(self):
        sys.exit()


    # =======================
    #    MENUS DEFINITIONS
    # =======================

    # Menu definition
    main_menu_actions = {
        'main_menu': main_menu,
        '1': menu1_search_all_assets,
        '2': menu2_search_all_files,
        '3': menu3_search_all_directories,
        '0': exit,
    }

    menu_option1_actions = {
        'main_menu': menu1_search_all_assets,
        '1': find_all_assets,
        '2': find_assets_by_name,
        '3': find_assets_by_size_less_than,
        '4': find_assets_by_size_greater_than,
        '9': back,
        '0': exit,
    }

    menu_option2_actions = {
        'main_menu': menu2_search_all_files,
        '1': find_all_files,
        '2': find_files_by_extension,
        '3': find_files_by_name,
        '4': find_files_by_size_less_than,
        '5': find_files_by_size_greater_than,
        '9': back,
        '0': exit,
    }

    menu_option3_actions = {
        'main_menu': menu3_search_all_directories,
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