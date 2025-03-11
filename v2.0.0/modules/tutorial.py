class Tutorial: 
    def __init__(self):
        print(f'\n***** Tutorial *****\n')

        print(f'\nAn L-system is a mathematical model that can be used to create plots of fractals, plants, textiles, and more. ')
        print(f'This studio features two parts: a parser to create an L-string and a visualizer to plot the L-string.')   

        print(f'\nThe parser works by repeatedly applying transformation rules to a string to create a longer, more complex string. The parser requires the following information:')
        print(f'\n\t• Axiom - a starting character or string (e.g. F)')
        print(f'\t• Transformation Rules - rules that define how to transform each character or substring (e.g. F -> F+F)')
        print(f"\t• Iterations - the number of times the transformation rules are applied (e.g. 5)")
        print(f'\nThe fully parsed string is commonly thousands of characters long and is fed into a visualizer for plotting.')

        print(f'\nThe visualizer works by interpreting each character in the parsed string as some command. It requires a command key and the following information:')
        print(f'\n\t• Starting Direction - the angle to start drawing at; allows for rotation (e.g 0°)')
        print(f'\t• Turn Angle - the angle at which to turn left or right (e.g. 90°)')
        print(f'\nA key defines what command each character in the parsed string represents.')

        print('\nThe key for this program is as follows: ')

        print(f'\nVariables represent any value that is replaced by a transformation rule.')
        print(f'\n\t• Uppercase Letters: command to move forward while drawing')
        print(f'\n\t• Lowercase Letters: command to move forward without drawing')

        print(f'\nConstants represent any value that is not replaced by a transformation rule; these are geometric commands.')
        print(f'\n\t• +: command to turn left at the turn angle')
        print(f'\n\t• -: commmand to turn right at turn angle')
        print(f'\n\t• [: command to save state to stack (used in branching)')
        print(f'\n\t• ]: command to remove state to stack (used in branching)')

    def __str__(self): 
        return 'hhh'
    

if __name__ == '__main__':
    Tutorial()
        