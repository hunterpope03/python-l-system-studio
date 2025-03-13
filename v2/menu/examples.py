from .utils import validate
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

        user = validate(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])

        return user

    def get_details(self, user): 

        details = example_library(user)

        name = details[0]
        axiom = details[1]
        rules = details[2]
        iterations = details[3]
        turn_angle = details[4]
        starting_direction = details[5]

        return [name, axiom, rules, iterations, turn_angle, starting_direction]
    
    def print_details(self, details): 

        print('\n\n' + f'System: {details[0]}')
        print('\n\t' + f'• Axiom: {details[1]}')
        print('\t' + '• Rules: ' , '\n')
        for rule in details[2]: 
            print('\t\t' + f'{rule} -> {details[2][rule]}')
        print('\n\t' + f'• Iterations: {details[3]}')   
        print('\t' + f'• Turn Angle: {details[4]}°')
        print('\t' + f'• Starting Direction: {details[5]}°' + '\n\n')