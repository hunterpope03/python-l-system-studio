from .utils import validate_menu, print_system_details
from lib.example_library import example_library

class LSystemExamples(): 
    def __init__(self): 
        print('\n\n' + '***** Example Systems *****')

    def menu(self): 
        print('\n\n' + 'Choose an example option below to view the system\'s details and plot the system:')

        print('\n\t' + '1. Binary Tree')
        print('\t' + '2. Fractal Plant')
        print('\t' + '3. Bush 1')
        print('\t' + '4. Bush 2')
        print('\t' + '5. Bush 4')
        print('\t' + '6. Board')
        print('\t' + '7. Sierpinski Arrowhead')
        print('\t' + '8. Pentaplexity')
        print('\t' + '9. Dragon Curve')
        print('\t' + '10. Kolam')

        user = validate_menu(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])

        return user

    def get_details(self, user): 
        details = example_library(user)
        return details 
    
    def print_details(self, name): 
        print('\n\n' + f'System: {name}')