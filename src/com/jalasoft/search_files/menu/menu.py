import sys
from src.com.jalasoft.search_files.utils.validator import *
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
        name = input("Enter the name of the file (empty to search all files and directories) >>  ")
        if str(name) == '':
            name = None
        extension = input("Enter the extension (.exe/.py) (empty to search all files and directories) >>  ")
        if str(extension) == '':
            extension = None
        # Asset type will only be asked if extension was not set, we assume directories do not have extension
        if extension == None:
            asset_type = input("Enter the asset_type (dir/file/empty to search all files and directories) >>  ")
            if str(asset_type) == '':
                asset_type = None
        else:
            asset_type = 'file'
        search = Search()
        search.set_basic_search_criteria(path, name, extension, asset_type)
        search.search_any_criteria()
        print(search.result)
        Menu.main_menu(self)

    def advanced_search(self):
        path = str(input("Enter the path >>  "))
        while not os.path.isdir(path):
            path = input("Invalid path. Please enter a valid path >>  ")
        name = input("Enter the name of the file (empty for all) >>  ")
        if str(name) == '':
            name = None
        extension = input("Enter the extension (.exe/.py) (empty for all) >>  ")
        if str(extension) == '':
            extension = None
        owner = input("Enter the owner (empty for any) >>  ")
        if str(owner) == '':
            owner = None
        # Asset type will only be asked if extension or owner were not set,
        # we assume directories do not have extension nor owner option is allowed for them
        if extension == None and owner == None:
            asset_type = input("Enter the asset_type (dir/file/empty for all) >>  ")
            if str(asset_type) == '':
                asset_type = None
        else:
            asset_type = 'file'

        size = input("Size less than KB (empty for any size) >>  ")
        size_less_than = True
        if str(size) == '':
            size = None
            size_less_than = None
        if size is not None:
            while not is_number(size):
                size = input("Enter a valid number for size less than (empty for any size) >> ")
        # Ask for greater than only if less than was not entered:
        if size is None:
            size = input("Size greater than KB (empty for any size) >>  ")
            size_less_than = False
            if str(size) == '':
                size = None
                size_less_than = None
                if size is not None:
                    while not is_number(size):
                        size = input("Enter a valid number for size greater than (empty for any size) >> ")
        # Changing unit type to KB
        if size is not None:
            size = int(size)*1024

        create_date = input("Enter the creation date of the file (YYYY-MM-DD hh:mm) (empty for any) >>  ")
        if str(create_date) == '':
            create_date = None
        else:
            while not is_date_time(create_date):
                size = input("Enter a valid creation date (empty for any date) >> ")

        modify_date = input("Enter the modified date of the file (YYYY-MM-DD hh:mm) (empty for any) >>  ")
        if str(modify_date) == '':
            modify_date = None
        else:
            while not is_date_time(modify_date):
                modify_date = input("Enter a valid modify date (empty for any date) >> ")

        last_access_date = input("Enter the last access date of the file (YYYY-MM-DD hh:mm) (empty for any) >>  ")
        if str(last_access_date) == '':
            last_access_date = None
        else:
            while not is_date_time(last_access_date):
                last_access_date = input("Enter a valid last access date (empty for any date) >> ")

        content = input("Enter content to search (empty for all) >>  ")
        if str(content) == '':
            content = None

        search = Search()
        search.set_advanced_search_criteria(path, name, extension, asset_type, size, size_less_than, owner, create_date, modify_date, last_access_date, content)
        search.search_any_criteria()
        Menu.main_menu(self)

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
