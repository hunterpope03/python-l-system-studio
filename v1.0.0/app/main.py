from modules import menu

def intro(): 
    print(f'\n{'*' * 5}\tWelcome to v1.0.0 of my Python Lindenmayer(L)-System Parser & Visualizer\t{'*' * 5}')

def main(): 
    menu()
    main()

if __name__ == '__main__': 
    intro()
    main()