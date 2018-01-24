# =======================================================================

# Import the modules needed to run the script.
import sys
import os

# Main definition - constants
menu_actions = {}


# =======================
#     MENUS FUNCTIONS
# =======================

# Main menu
def main_menu():
    os.system("cls")

    print("Welcome,\n")
    print ("Please choose the menu you want to start:")
    print ("1. Search Path")
    print ("2. Serach File")
    print ("\n0. Quit")
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


# Menu 1
def menu1():
    print ("path found !\n")
    print ("9. Back")
    print ("0. Quit")
    choice = input(" >>  ")
    exec_menu(choice)
    return


# Menu 2
def menu2():
    print ("File foundd"
           " !\n")
    print ("9. Back")
    print ("0. Quit")
    choice = input(" >>  ")
    exec_menu(choice)
    return


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