import os
import sys

from src.com.jalasoft.search_files.utils.validator import *

class Menu(object):
    def __init__(self, name, options, welcome, parent = None):
        self.name = name
        self.options = options
        self.welcome = welcome
        self.parent = parent

    def show(self):
        os.system("cls")

        print(self.welcome, "\n")
        for elem in self.options.items():
            print(elem[0] + "." + elem[1])
        choice = input(" >>  ")
        self.exec_menu(choice)
        return

    def exec_menu(self, choice):
        os.system("cls")
        ch = choice.lower()
        if ch == '':
            menu_actions['main_menu']()
        else:
            if is_number(ch):
                try:
                    menu_actions[ch]()
                except KeyError:
                    print
                    "Invalid selection, please try again.\n"
                    menu_actions['main_menu']()
            return


options = {
    '1': "Search by Path",
    '2': "Quit"
}
main_menu = Menu('main', options, "Main menu. Please select an option: ")
main_menu.show()