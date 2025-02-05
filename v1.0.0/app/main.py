from modules import menu

def intro() -> None: 
    """
    Prints welcome message once.
    """
    print(f'\n{'*' * 5}\tWelcome to v1.0.0 of my Python Lindenmayer(L)-System Parser & Visualizer\t{'*' * 5}')

def main() -> None: 
    """
    Allows for continuous use of the program via recursion.
    """
    menu()
    main()

if __name__ == '__main__': 
    intro()
    main()