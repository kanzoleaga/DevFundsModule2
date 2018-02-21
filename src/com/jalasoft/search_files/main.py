from src.com.jalasoft.search_files.menu.menu import Menu

# =======================
#      MAIN PROGRAM
# =======================

# Main class
def main():
    try:
        # Launch main menu
        menu = Menu()
        menu.main_menu()
    except:
        return 1

if __name__ == "__main__":
    main()

