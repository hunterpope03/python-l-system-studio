import sys
sys.dont_write_bytecode = True

from menu import * 
from tools import *

PLOT_COLOR = 'red'
BACKGROUND_COLOR = 'black'

class LStudio: 
    def __init__(self): 
        pass

    def menu(self):
        print('\n\n' + 'Select a menu option to continue.' + '\n')

        print('\t' + '1. Tutorial')
        print('\t' + '2. Example Systems')
        print('\t' + '3. Custom System')
        print('\t' + '4. Plot Settings')
        print('\t' + '5. Quit')

        user = validate_menu(['1', '2', '3', '4', '5'])

        return user
    
    def tutorial_selection(self): 
        tutorial()

    def examples_selection(self): 
        ex = LSystemExamples()
        user = ex.menu()
        details = ex.get_details(user)
        ex.print_details(details[0])
        self.print_system_details(details[1], details[2], details[3], details[4], details[5])
        parser = LSystemParser(details[1], details[2], details[3])
        null = input('Enter anything to parse the L-System: ')
        parsed = parser.parse()
        print(parsed)
        self.print_length(parsed)
        visualizer = LSystemVisualizer(PLOT_COLOR, BACKGROUND_COLOR, parsed, details[4], details[5])
        null = input('Enter anything to visualize the L-System: ')
        visualizer.visualize()

    def custom_selection(self): 
        custom = CustomLSystem()
        custom.key_restrictions()
        data = custom.get_data()
        print(data)
        custom.print_details()
        self.print_system_details(data[0], data[1], data[2], data[3], data[4])
        parser = LSystemParser(data[0], data[1], data[2])
        null = input('Enter anything to parse the L-System: ')
        parsed = parser.parse()
        self.print_length(parsed)
        visualizer = LSystemVisualizer(PLOT_COLOR, BACKGROUND_COLOR, parsed, data[3], data[4])
        null = input('Enter anything to visualize the L-System: ')
        visualizer.visualize()

    def visualizer_settings(self): 
        settings = LSystemVisualizerSettings()
        settings.menu()
        colors = settings.get_data()
        global PLOT_COLOR
        PLOT_COLOR = colors[0]
        global BACKGROUND_COLOR
        BACKGROUND_COLOR = colors[1] 
        
    def print_system_details(self, axiom, rules, iterations, turn_angle, starting_direction): 
            print('\n\t' + f'• Axiom: {axiom}')
            print('\t' + '• Rules: ' , '\n')
            for rule in rules: 
                print('\t\t' + f'{rule} -> {rules[rule]}')
            print('\n\t' + f'• Iterations: {iterations}')   
            print('\t' + f'• Turn Angle: {turn_angle}°')
            print('\t' + f'• Starting Direction: {starting_direction}°' + '\n\n')

    def print_length(self, parsed): 
        print('\n\n' + f'The parsed L-System is {len(parsed)} character long.' + '\n\n')

def main(): 
    print('\n\n' + '***** L-Studio v2.0.0 *****')

    while True: 
        app = LStudio()
        user = app.menu()

        match user: 
            case '1': 
                app.tutorial_selection()
            case '2':
                app.examples_selection()
            case '3':
                app.custom_selection()
            case '4':
                app.visualizer_settings()
            case '5': 
                break
        
if __name__ == '__main__':
    main()