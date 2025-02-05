from example_library import example_details # import example library for the examples() function
from parser import l_system_parser # import parser for the parse_system() function
from visualizer import visualize # import visualizer for the visualize_system() function

def validate(valid) -> str: 
    """
    Validates user input given a list of valid inputs.

    Parameters:
    valid (list): List of valid inputs.

    Returns:
    user_input (str): Validated user input.

    Raises:
    EOFError: If user terminates the program.
    KeyboardInterrupt: If user terminates the program.
    """
    while True:
        try:
            user_input = input(f'Enter your choice {[int(i) for i in valid]}: ').strip()
            if user_input in valid:
                return user_input
            print('Invalid entry, please try again.\n')
        except (EOFError, KeyboardInterrupt):
            print('\nProgram terminated by user.')
            exit()

def parse_system(axiom, rules, iterations) -> str: 
    """
    Parses the L-System (see parser.py).

    Parameters:
    axiom (str): The starting string. 
    rules (dict): A dictionary of the rules. 
    iterations (int): The number of times to apply the rules.

    Returns:
    parsed (str): The parsed string. 
    """
    parsed = l_system_parser(axiom, rules, iterations)
    print(f'\nThe length of the resulting string after {iterations} iterations is {len(parsed)}!\n') # prints the length of the fully parsed string
    return parsed

def visualize_system(parsed, turn_angle, starting_direction) -> None:
    """
    Visualizes the parsed string and shows the plot (see visualizer.py).

    Parameters:
    parsed (str): The fully parsed string.
    turn_angle (float): The angle to turn left or right.
    starting_direction (float): The starting direction of the visualization's drawing.

    Returns:
    None
    """
    null = input('Enter anything to view the visualization: ') # empty input to pause the visualization appearing
    visualize(parsed, turn_angle, starting_direction)
    pass

def menu() -> None: 
    """
    Prints the main menu and validates user input to navigate to other parts of the program.
    """
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

def tutorial() -> None: 
        """
        Prints a tutorial on L-Systems and this program.
        """
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

        null = input('Enter anything to continue: ') # empty input to allow the reader to view the tutorial
        pass 

def examples() -> None: 
    """
    Handles all logic for the examples menu selection. 

    Prints examples of L-Systems and validates user input for the selected example. 
    Retrieves and prints the selected example's data.
    Parses the selected example's data and sends it to the visualizer.
    Visualizes the selected example.
    """
    def display_example(name, axiom, rules, iterations, turn_angle, starting_direction) -> None: 
        """
        Prints the selected example's data.

        Parameters:
        name (str): The name of the example.
        axiom (str): The example's axiom.
        rules (dict): The example's rules.
        iterations (int): The example's number of iterations.
        turn_angle (float): The example's turn angle.
        starting_direction (float): The example's starting direction.

        Returns:
        None
        """
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
    starting_direction = example_data[5] # assigns the values in the returned list to new variables to be sent to the parser and visualizer

    display_example(name, axiom, rules, iterations, turn_angle, starting_direction)
    parsed = parse_system(axiom, rules, iterations)
    visualize_system(parsed, turn_angle, starting_direction)

    pass

def custom() -> None: 
    """
    Handles all logic for the custom menu selection. 

    Prints the key for this program.
    Collects all data values for the custom L-System.
    Parses the user's inputted data and sends it to the visualizer.
    Visualizes the custom L-System.
    """
    valid_chars = set('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuzwxyz+-[]') # defines a list of the allowed characters in the axioms and rules

    def custom_key() -> None: 
        """
        Prints the key that displays the allowed characters and their uses.
        """
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
        print(f'\t\t• Inputted axioms cannot be empty, be longer than 10 characters, contain spaces, or contain invalid characters (see above)')
        print(f'\t\t• Inputted transformation rules cannot contain spaces or contain invalid characters')
        print(f'\t\t• Inputted number of iterations cannot be negative or be larger than 10 (to prevent memory overflow)')
        print(f'\t\t• Both the inputted turn angle & starting direction cannot be negative or fall outside the range of [0, 360]')

        null = input('Enter anything to continue: ') # empty input to allow the reader to view the key

    def custom_axiom() -> str: 
        """
        Collects the axiom from the user and validates that it is not empty, no longer than 10 characters, does not contain spaces, and only contains valid characters.

        Returns:
        axiom (str): The validated axiom.
        """
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

    def custom_rules() -> dict: 
        """
        Collects the transformation rules for each variable from the user and validates that each rule is not empty, does not contain spaces, and only contains valid characters.

        Returns:
        rules (dict): A validated dictionary mapping each variable to its transformation rule.
        """
        while True: 
            try:
                rules = {}
                axiom_vars = {c for c in axiom if c.isalpha()} # only provide rules for variables, which can be upper and lower case letters
                
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

    def custom_iterations() -> int: 
        """
        Collects the number of iterations from the user and validates that it is not negative, larger than 10, and is an integer.

        Returns:
        iterations (int): The validated number of iterations.
        """
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
                    print('\tYour number of iterations must be a valid integer, please try again.') # catches non-numeric input
                else:
                    print(f'\t{e}, please try again.')

        return iterations

    def custom_turn_angle() -> float: 
        """
        Collects the turn angle from the user and validates that it is a valid floating-point number between 0° and 360°.

        Returns:
        turn_angle (float): The validated turn angle in degrees.
        """
        while True:
            try:
                turn_angle = float(input('\n\tEnter your turn angle: '))
                if not 0 <= turn_angle <= 360:
                    raise ValueError('\n\tYour turn angle must be between 0° and 360°.')
                break
            except ValueError as e:
                if 'could not convert string to float' in str(e):
                    print('\tYour turn angle must be a valid floating-point number, please try again.') # catches non-numeric input
                else:
                    print(f'\t{e}, please try again.')

        return turn_angle

    def custom_starting_direction() -> float:
        """
        Collects the starting direction from the user and validates that it is a valid floating-point number between 0° and 360°.

        Returns:
        starting_direction (float): The validated starting direction in degrees.
        """
        while True:
            try:
                starting_direction = float(input('\n\tEnter starting direction: '))
                if not 0 <= starting_direction <= 360:
                    raise ValueError('\n\tYour starting direction must be between 0° and 360°.')
                break
            except ValueError as e:
                if 'could not convert string to float' in str(e):
                    print('\tYour starting direction must be a valid floating-point number, please try again.') # catches non-numeric input
                else:
                    print(f'\t{e}, please try again.')

        return starting_direction

    print(f'\n{'*' * 5}\tPython L-System Parser & Visualizer v1.0.0 Custom L-System Creator\t{'*' * 5}')
    custom_key()

    axiom = custom_axiom()
    rules = custom_rules()
    iterations = custom_iterations()
    turn_angle = custom_turn_angle()
    starting_direction = custom_starting_direction() # calls each function to get user inputted values

    parsed = parse_system(axiom, rules, iterations)
    visualize_system(parsed, turn_angle, starting_direction)

    pass
