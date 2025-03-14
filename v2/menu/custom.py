from .tutorial import program_key, input_restrictions
from .utils import * 

class CustomLSystem(): 
    def __init__(self): 
        print('\n\n' + '***** Custom System *****')

    def key_restrictions(self): 
        program_key()
        input_restrictions()

    def get_data(self): 
        print('\n\n' + 'Enter the following information following the program key and input restrictions. Automatic validation will occur.')

        axiom = get_axiom()
        rules = get_rules(axiom)
        iterations = get_iterations()
        turn_angle = get_turn_angle()
        starting_direction = get_starting_direction()

        return ([axiom, rules, iterations, turn_angle, starting_direction])

    def print_details(self):
        print('\n\n' + 'Your system has the following attributes: ')