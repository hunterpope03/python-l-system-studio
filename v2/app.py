import sys
sys.dont_write_bytecode = True

from menu import * 
from tools import *

class LStudio: 
    def __init__(self): 
        self.plot_color = 'red'
        self.plot_background = 'black'
    
    def menu(self):
        print('\n\n' + 'Select a menu option to continue.' + '\n')

        print('\t' + '1. Tutorial')
        print('\t' + '2. Example Systems')
        print('\t' + '3. Custom System')
        print('\t' + '4. Plot Settings')
        print('\t' + '5. Quit')

        user = validate(['1', '2', '3', '4', '5'])

        return user
    
    # def tutorial_choice(): 

def main(): 
    print('\n\n' + '***** L-Studio v2.0.0 *****')

    while True: 
        app = LStudio()
        user = app.menu()

        match user: 
            case '1': 
                tutorial()
            case '2':
                ex = LSystemExamples()

                user = ex.menu()

                details = ex.get_details(user)
                name = details[0]
                axiom = details[1]
                rules = details[2]
                iterations = details[3]
                turn_angle = details[4]
                starting_direction = details[5]

                ex.print_details(details)

                parser = LSystemParser(axiom, rules, iterations)

                null = input('Enter anything to parse the L-System: ')

                parsed = parser.parse()

                print('\n\n' + f'The parsed L-System is {len(parsed)} character long.' + '\n\n')

                visualizer = LSystemVisualizer(app.plot_color, app.plot_background, parsed, turn_angle, starting_direction)
                null = input('Enter anything to visualize the L-System: ')
                print('\n')
                visualizer.visualize()

        #     case '3':
        #     case '4':
            case '5': 
                break
        
if __name__ == '__main__':
    main()