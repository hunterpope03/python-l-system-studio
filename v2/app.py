import sys
sys.dont_write_bytecode = True

from menu import LSystemTutorial, LSystemCustom, LSystemExample, LSystemSettings # import classes for menu options
from utils import validate_menu # import function for menu_validation

class LSystemStudio:
    def __init__(self): 
        """
        Initializes an LSystemStudio object with default visualization settings.
        """
        self.visualizer_drawing_color = 'red'
        self.visualizer_background_color = 'black'

    def main_menu(self): 
        """
        Displays the main menu for the L-System Studio application and validates user input with the validate_menu function found in utils/validation.py.

        Returns:
        str: The validated user choice as a string from the menu options.
        """
        print('\n\n' + 'Select a menu option below (press CTRL + C to exit the program at any time):' + '\n') # adds a note to guide the user to quit the program at any time

        print('\t' + '1. Tutorial')
        print('\t' + '2. Example Systems')
        print('\t' + '3. Custom System')
        print('\t' + '4. Visualizer Settings')
        print('\t' + '5. Quit')

        user = validate_menu(['1', '2', '3', '4', '5']) # get validated user input.

        return user
    
    def parsed_system_length(self, parsed_system): 
        """
        Takes in a parsed L-system and returns the number of characters in the string.

        Parameters:
        parsed_system (str): The parsed L-System string.

        Returns:
        str: A formatted string indicating the length in the parsed L-System.
        """
        length_txt = f'The parsed L-System is {len(parsed_system)} characters long.' + '\n\n'
        return length_txt
    
    def cont_parsed(self): 
        """
        Blank input continue point that allows the user to enter anything to continue with the program.
        Provides a note as to how to continue with the program after the visualization appears. 
        """
        cont = input('Press Enter to visualize the L-System.\n(close the GUI window to proceed with the program): ')
        return cont
    
def main():
    app = LSystemStudio() # create LSystemStudio object only once.

    print('\n\n' + '***** L-Studio v2.0.0 *****') # print program title only once.

    while True: 
        try: 
            user = app.main_menu() # continously display menu and gather user input.

            match user: 

                # handle 'tutorial' menu option
                case '1':
                    tutorial_obj = LSystemTutorial() # create LSystemTutorial object found in menu/tutorial.py.
                    text = tutorial_obj.tutorial_text() # get tutorial text.
                    for section in text: 
                        for line in text[section]: 
                            print(line) # print each line of each section of the text.
                        if section == 'introduction': 
                            tutorial_obj.cont_intro() # after printing the introduction section, show a blank input continue point.
                        elif section == 'program_key': 
                            tutorial_obj.cont_key() # after printing the porgram key section, show a blank input continue point.
                        else: 
                            tutorial_obj.cont_restrictions() # after printing the inpput_restrictions section, show a blank input continue point.

                # handle 'example systems' menu option
                case '2': 
                    example_obj = LSystemExample() # create LSystemExample object found in menu/example.py.
                    user = example_obj.example_menu() # display example menu and gather user input.
                    details = example_obj.example_details(user) # get example details.
                    for section in details: # print out details via formatted strings.
                        if isinstance(section, list): # for the variable, which is a list, print out the rule of each entry in the list separately.
                            for line in section: 
                                print(line)
                        else: 
                            print(section) # if not the rules variable, simply print the section.
                    parsed_system = example_obj.parse_example() # parse the system.
                    length = app.parsed_system_length(parsed_system) # get the system length.
                    print(length) # print the system length.
                    app.cont_parsed() # blank input continue point.
                    visualized_system = example_obj.visualize_example(app.visualizer_drawing_color, app.visualizer_background_color, parsed_system) # visualize the system.

                # handle 'custom system' menu option
                case '3': 
                    custom_obj = LSystemCustom() # create LSystemCustom object found in menu/custom.py.
                    tutorial_obj = LSystemTutorial() # create an LSystemTutorial object as well to print the program key and input restrictions.
                    text = tutorial_obj.tutorial_text() # get the tutorial text.
                    for section in text: # print the tutorial text - the introduction section.
                        if section != 'introduction': 
                            for line in text[section]: 
                                print(line)
                    details = custom_obj.custom_details() # get the custom details.
                    for section in details: # print the details via formatted strings.
                        if isinstance(section, list): 
                            for line in section: 
                                print(line)
                        else: 
                            print(section)
                    parsed_system = custom_obj.parse_custom() # parse the system.
                    length = app.parsed_system_length(parsed_system) # get the system length.
                    print(length) # print the system length.
                    app.cont_parsed() # blank input continue point.
                    visualized_system = custom_obj.visualize_custom(app.visualizer_drawing_color, app.visualizer_background_color, parsed_system) # visualize the system.

                # handle 'visualizer settings' menu option
                case '4':
                    settings_obj = LSystemSettings() # create LSystemSettings object found in menu/settings.py.
                    drawing_user = settings_obj.drawing_menu() # display the drawing settings menu and gather user input.
                    background_user = settings_obj.background_menu() # display the background settings menu and gather user input.
                    app.visualizer_drawing_color = drawing_user 
                    app.visualizer_background_color = background_user # update the Studio object's color settings.

                # handle 'quit' menu option.
                case '5':
                    print('\n')
                    break
                
        except Exception as e: # print error message and break in the instance of any error.
            print('\n\n' + f'Error: {e}' + '\n\n')
            break

if __name__ == '__main__':
    main()