from example_library import example_details
from parser import l_system_parser
from visualizer import visualize

def validate(valid): 
    while True:
        try:
            user_input = input(f'Enter your choice {[int(i) for i in valid]}: ').strip()
            if user_input in valid:
                return user_input
            print('Invalid entry, please try again.\n')
        except (EOFError, KeyboardInterrupt):
            print('\nProgram terminated by user.')
            exit()

def parse_system(axiom, rules, iterations): 
    parsed = l_system_parser(axiom, rules, iterations)
    print(f'\nThe length of the resulting string after {iterations} iterations is {len(parsed)}!\n')
    return parsed

def visualize_system(parsed, turn_angle, starting_direction):
    null = input('Enter anything to view the visualization: ') 
    visualize(parsed, turn_angle, starting_direction)
    pass

def menu(): 
    print(f'\nChoose a menu option below to continue:')
    print(f'\n\t1) View a Tutorial on L-Systems and This Program')
    print(f'\t2) See Examples of Popular L-Systems')
    print(f'\t3) Create a Custom L-System\n')

    menu_input = validate(['1', '2', '3'])
    if menu_input == '1': 
        tutorial()
        pass
    elif menu_input == '2':
        examples()
        pass
    else:
         custom()
         pass

def tutorial(): 
        print(f'\n{'*' * 5}\tPython L-System Parser & Visualizer v1.0.0 Tutorial \t{'*' * 5}\n')

        print('A Lindenmayer(L)-System is a mathematical model founded by the Hungrian botanist and biologist Aristid Lindenmayer in 1968, originally developed to study algae growth.')
        print('An L-System works by repeateadly transforming a character or string (e.g. F) into a more complex string through transformation rules (e.g. F -> FGF).')
        print('After each iteration, the string grown more and more complex. After many iterations, the string can grow to thousands of characters long.\n')

        print('In an L-System parser, the program applies these transformation rules to a string through loops and the result in a long, complex "parsed" string.')
        print('In an L-System visualizer, after a string is fully parsed, each character is assigned some command (to draw, to turn, etc.) and fed into a visualization program to create a geometric pattern.')
        print('Such patterns can be fractals, plant-like structures, and other geometric objects.\n')  

        print('My program has three main components:\n')

        print('\t1) Get Necessary Data from the User\n')

        print('\t\t• An axiom or seed defines the initial starting string (e..g. F)')
        print('\t\t• Transformation rule(s) define how to change each character or string in each iteration (e.g. F -> FGF)')
        print('\t\t• Iteration(s) define how many times to apply the transformation rule(s) (the limit for this program is 10 to prevent memory overflow)')
        print('\t\t• The Turn Angle defines which degree to turn at (commonly 90°, 45°, 120°, etc.)')
        print('\t\t• The Starting Direction defines which degree to start drawing at and allows for rotations of the visualization (commonly 0º)\n')
    
        print('\t2) Parse the L-System \n')
        print('\t\t• Send the necessary data values (axiom, rules & iterations) to the parser')
        print('\t\t• Apply the proper transformation rules for each iteration')
        print('\t\t• Send the parsed string and other necessary data values (turn angle & starting direction) to the visualizer\n')

        print('\t3) Visualize the Parsed String\n')
        print('\t\t• Using a key (the key for this program is in the CUSTOM menu option), the visualizer decodes each character in the parsed string')
        print('\t\t• Each character represents a specific action, like how to move, turn, and draw')
        print('\t\t• After the visualization completes, the plot is displayed the user to see\n')

        null = input('Enter anything to continue: ')
        pass 

def examples(): 
    def display_example(name, axiom, rules, iterations, turn_angle, starting_direction): 
        print(f'\nThe {name} example has the following data values:\n')

        print(f'\tAxiom: {axiom}')
        print(f'\tRules: {rules}')
        print(f'\tIterations: {iterations}')
        print(f'\tTurn Angle: {turn_angle}°')
        print(f'\tStarting Direction: {starting_direction}°')
    
        pass

    print(f'\n{'*' * 5}\tPython L-System Parser & Visualizer v1.0.0 Examples\t{'*' * 5}\n')
    print(f'Choose an example option below (all examples come from Paul Bourke):\n')
    print(f'\t1) L-System Bush 2')
    print(f'\t2) L-System Bush 4')
    print(f'\t3) Quadratic Gosper')
    print(f'\t4) Board')
    print(f'\t5) Sierpinski Triangle')
    print(f'\t6) Pentaplexity')
    print(f'\t7) Dragon Curve')
    print(f'\t8) Hexagonal Gosper\n')
    
    example_input = validate(['1', '2', '3', '4', '5', '6', '7', '8'])

    example_data = example_details(example_input)
    name = example_data[0]
    axiom = example_data[1]
    rules = example_data[2]
    iterations = example_data[3]
    turn_angle = example_data[4]
    starting_direction = example_data[5]

    display_example(name, axiom, rules, iterations, turn_angle, starting_direction)
    parsed = parse_system(axiom, rules, iterations)
    visualize_system(parsed, turn_angle, starting_direction)

    pass

def custom(): 

    valid_chars = set('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuzwxyz+-[]')

    def custom_key(): 

        print(f'\nPlease acknowledge and adhere to the below key to ensure proper use. Automatic validation will occur.\n')

        print(f'\t1) Variables: represent any value that is replaced in a transformation rule\n')
        print(f'\t\t• Uppercase Letters (F, X, S): command to draw and move forward')
        print(f'\t\t• Lowercase Letters (f, x, s): command to move forward without drawing')

        print(f'\n\t2) Constants: represent any value that is not changed in a transformation rule\n')
        print(f'\t\t• +: command to turn left at specified turn angle')
        print(f'\t\t• +: command to turn right at specified turn angle')
        print(f'\t\t• [: save state to stack (used to create the start of a branch)')
        print(f'\t\t• ]: remove state from stack (used to remove branch start)')

        print(f'\n\t3) Input Restrictions\n')
        print(f'\t\t• Axioms cannot: be empty, be longer than 10 characters, contain spaces, or contain invalid characters (see above)')
        print(f'\t\t• Transformation rules cannot: contain spaces or contain invalid characters')
        print(f'\t\t• Number of iterations cannot: be negative or be larger than 10 (to prevent memory overflow)')
        print(f'\t\t• Both the Turn Angle & Starting Direction cannot: be negative or fall outside the range of [0, 360]')

    def custom_axiom(): 

        while True:
            try:
                axiom = input('\n\tEnter your axiom: ')
                if not axiom:
                    raise ValueError('Your axiom cannot be empty')
                if len(axiom) > 10:
                    raise ValueError('Your axiom cannot be longer than 10 characters')
                if ' ' in axiom:
                    raise ValueError('Your axiom cannot contain spaces')
                if not all(c in valid_chars for c in axiom):
                    raise ValueError(f'Your axiom contains invalid characters. Valid characters are: {valid_chars}')
                break
            except ValueError as e:
                print(f'\t{e}, please try again.')

        return axiom

    def custom_rules(): 

        while True: 
            try:
                rules = {}
                axiom_vars = {c for c in axiom if c.isalpha()}
                
                for var in sorted(axiom_vars):
                    while True:
                        try:
                            rule = input(f'\n\tEnter the transformation rule for the variable {var}: ')
                            if ' ' in rule:
                                raise ValueError('Your transformation rule cannot contain spaces')
                            if not all(c in valid_chars for c in rule):
                                raise ValueError(f'Your transformation rule contains invalid characters. Valid characters are: {valid_chars}')
                            rules[var] = rule
                            break
                        except ValueError as e:
                            print(f'\t{e}, please try again.')
                break
                    
            except ValueError as e:
                print(f'\tError {e}, please try again.')

        return rules

    def custom_iterations(): 
        
        while True:
            try:
                iterations = int(input('\n\tEnter your number of iterations: '))
                if iterations < 0:
                    raise ValueError('Your number of iterations cannot be negative')
                if iterations > 10:
                    raise ValueError('Your number of iterations cannot exceed 10 (to prevent memory overflow)')
                break
            except ValueError as e:
                if 'invalid literal for int()' in str(e):
                    print('\tYour number of iterations must be a valid integer, please try again.')
                else:
                    print(f'\t{e}, please try again.')

        return iterations

    def custom_turn_angle(): 
        
        while True:
            try:
                turn_angle = float(input('\n\tEnter your turn angle: '))
                if not 0 <= turn_angle <= 360:
                    raise ValueError('\n\tYour turn angle must be between 0° and 360°.')
                break
            except ValueError as e:
                if 'could not convert string to float' in str(e):
                    print('\tYour turn angle must be a valid floating-point number, please try again.')
                else:
                    print(f'\t{e}, please try again.')

        return turn_angle

    def custom_starting_direction():

        while True:
            try:
                starting_direction = float(input('\n\tEnter starting direction: '))
                if not 0 <= starting_direction <= 360:
                    raise ValueError('\n\tYour starting direction must be between 0° and 360°.')
                break
            except ValueError as e:
                if 'could not convert string to float' in str(e):
                    print('\tYour starting direction must be a valid floating-point number, please try again.')
                else:
                    print(f'\t{e}, please try again.')

        return starting_direction

    print(f'\n{'*' * 5}\tPython L-System Parser & Visualizer v1.0.0 Custom L-System Creator\t{'*' * 5}')
    custom_key()

    axiom = custom_axiom()
    rules = custom_rules()
    iterations = custom_iterations()
    turn_angle = custom_turn_angle()
    starting_direction = custom_starting_direction()

    parsed = parse_system(axiom, rules, iterations)
    visualize_system(parsed, turn_angle, starting_direction)

    pass
