def introduction():
    print('\n\n' + '***** Introduction *****' + '\n')

    print('\n' + '1) An L-system is a mathematical model that can be used to create plots of fractals, plants, textiles, and more.')
    print('\n' + '2) This studio features two parts: a parser to create an L-string and a visualizer to plot an L-string.')

    print('\n' + '3) The parser works by repeatedly applying transformation rules to a string to create a longer, more complex string. It requires the following information:')
    print('\n\t' + '• Axiom - a starting character or string (e.g. F)')
    print('\t' + '• Transformation Rules - rules that define how to transform each character or substring (e.g. F -> F+F)')
    print('\t' + '• Iterations - the number of times the transformation rules are applied (e.g. 5)')
    print('\n\t' + 'The fully parsed string can grow to be thousands of characters long and is fed into a visualizer for plotting.')

    print('\n' + '4) The visualizer works by interpreting each character in the parsed string as some command. It requires some command key and the following information:')
    print('\n\t' + '• Starting Direction - the angle to start drawing at; allows for rotation (e.g 0°)')
    print('\t' + '• Turn Angle - the angle at which to turn left or right (e.g. 90°)')
    print('\n\t' + 'A key defines what command each character in the parsed string represents.')

    null = input('\n\n' + 'Enter anything to view the program key: ')
    return null

def program_key():
    print('\n\n' + '***** Program Key *****' + '\n')

    print('\n' + '1) Variables represent any value that is replaced by a transformation rule.')
    print('\n\t' + '• Uppercase Letters: command to move forward while drawing')
    print('\t' + '• Lowercase Letters: command to move forward without drawing')

    print('\n' + '2) Constants represent any value that is not replaced by a transformation rule; these are geometric commands.')
    print('\n\t' + '• +: command to turn left at the turn angle')
    print('\t' + '• -: command to turn right at turn angle')
    print('\t' + '• [: command to save state to stack (used in branching)')
    print('\t' + '• ]: command to remove state to stack (used in branching)')

    null = input('\n\n' + 'Enter anything to view input restrictions in creating a custom L-system: ')
    return null

def input_restrictions():
    print('\n\n' + '***** Input Restrictions *****' + '\n')

    print('\n' + '1) Axioms cannot be empty, longer than 8 characters, contain spaces, or contain any characters other than those defined in the program key')
    print('\n' + '2) Transformation rules cannot contain spaces or any characters other than those defined in the program key')
    print('\n' + '3) The number of iterations must be a positive integer less than 10')
    print('\n' + '4) Both the turn angle and starting direction must be numbers in the range [0, 360]')

    null = input('\n\n' + 'Enter anything to proceed back to the menu: ')
    return null

def tutorial():
    introduction()
    program_key()
    input_restrictions()
    return None

# if __name__ == '__main__':
#     tutorial()