from validate import validate
from example_library import example_library

class Examples(): 
    def __init__(self): 
        print('\n\n' + '***** Example Systems *****' + '\n\n')
        self.menu()

    def menu(self): 

        print('Choose an example option below to view the system\'s details and plot the system:' + '\n')

        print('\t' + '1. Binary Tree')
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

        self.print_details(user)

    def print_details(self, user): 
        
        details = example_library(user)

        name = details[0]
        axiom = details[1]
        rules = details[2]
        iterations = details[3]
        turn_angle = details[4]
        starting_direction = details[5]

        print('\n\n' + f'System: {name}')
        print('\n\t' + f'• Axiom: {axiom}')
        print('\t' + f'• Rules: {rules}')
        print('\t' + f'• Iterations: {iterations}')   
        print('\t' + f'• Turn Angle: {turn_angle}')
        print('\t' + f'• Starting Direction: {starting_direction}')

        null = input('\n\n' + 'Enter anything to parse the L-string: ')
        
if __name__ == '__main__':
    Examples()