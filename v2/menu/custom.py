from utils import LSystemParser, LSystemVisualizer # import classes for parsing and visualizing.

class LSystemCustom(): 
    def __init__(self): 
        """
        Initializes an LSystemCustom object with empty variables that will contian the attributes of the system and a variable that contains all of the valid characters that is used for validating user input.
        """
        self.valid_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz[]+-'
        self.axiom = None
        self.rules = None
        self.iterations = None
        self.turn_angle = None
        self.starting_direction = None

    def custom_details(self): 
        """
        Collects all data values for the custom L-System from the user and validates each value with the respective validation functions.

        Returns:
        list: A list containing the system's details as formatted strings to simplify the output process.
        """
        self.axiom = self.validate_axiom()
        self.rules = self.validate_rules(self.axiom)
        self.iterations = self.validate_iterations()
        self.turn_angle = self.validate_turn_angle()
        self.starting_direction = self.validate_starting_direction() # get the validated user input.

        rules_txt = [] # create a new dictionary for outputting the rules.

        for rule in self.rules: 
            rules_txt.append('\t\t' + f'{rule} -> {self.rules[rule]}') # append each rule as a formatted string.

        return [
            '\n\n' + f'Your system has these details:'
            '\n\n\t' + f'• Axiom: {self.axiom}', 
            '\t' + '• Rules: ' + '\n',
            rules_txt, 
            '\n\t' + f'• Iterations: {self.iterations}',
            '\t' + f'• Turn Angle: {self.turn_angle}°'
            '\n\t' + f'• Starting Direction: {self.starting_direction}°' + '\n\n'
        ] # return a list containing the statements for the system's details as formatted strings. 
    
    def validate_axiom(self): 
        """
        Collects the axiom from the user and validates that it is not empty, no longer than 15 characters, does not contain spaces, and only contains valid characters.

        Returns:
        axiom (str): The validated axiom.
        """
        while True:
            try:
                axiom = input('\n\tEnter axiom: ').strip() # strip input.
                if not axiom: # check for empty input.
                    raise ValueError('Axiom cannot be empty')
                if len(axiom) > 15: # check for too long of an input.
                    raise ValueError('Axiom cannot be longer than 15 characters')
                if ' ' in axiom: # check for spaces in the input.
                    raise ValueError('Axiom cannot contain spaces')
                for char in axiom: 
                    if char not in self.valid_chars: # check for invalid character in the input.
                        raise ValueError(f'Axiom cannot contain invalid characters. Valid characters are: {self.valid_chars}')
                break
            except ValueError as e: # for any other errors, print the error message and prompt the user to try again.
                print(f'\t{e}, please try again.')

        return axiom

    def validate_rules(self, axiom):
        """
        Collects and validates transformation rules for each uppercase variable in the given axiom.

        Parameters:
        axiom (str): The axiom containing variables to be transformed.

        Returns:
        rules (dict): A dictionary mapping each variable to its transformation rule.
        """ 
        rules = {} # empty rules dictionary to add rules for variables.
        axiom_vars = {c for c in axiom if c.isupper()} # dictionary of only uppercase letters. 
        vars_to_process = sorted(axiom_vars) # sorted version of the variables to add rules for.

        while vars_to_process:
            var = vars_to_process.pop(0) # get the first variable in the dictionary and remove it.
            if var in rules:
                continue

            while True:
                try:
                    rule = input(f'\n\tEnter the transformation rule for the variable {var}: ').strip() # strip input.
                    if ' ' in rule: # check for spaces in the input.
                        raise ValueError('Your transformation rule cannot contain spaces')
                    if not all(c in  self.valid_chars for c in rule): # check for invalid character in the input.
                        raise ValueError(f'Your transformation rule contains invalid characters. Valid characters are: {self.valid_chars}')
                    
                    if rule != '': 
                        rules[var] = rule # only add a rule if it is not empty; some variables may not have transformation rules.
                    new_vars = {c for c in rule if c.isupper() and c not in rules and c not in vars_to_process} # add new variables to process if they are in a rule but have not already been processed.
                    if new_vars:
                        vars_to_process.extend(sorted(new_vars))
                    break
                except ValueError as e: # for any other errors, print the error message and prompt the user to try again.
                    print(f'\t{e}, please try again.')

        return rules

    def validate_iterations(self):
        """
        Collects the number of iterations from the user and validates that it is a non-negative integer no larger than 10.

        Returns:
        iterations (int): The validated number of iterations.
        """
        while True:
            try:
                iterations = int(input('\n\tEnter your number of iterations: ').strip()) # strip input.
                if iterations < 0: # check for negative input.
                    raise ValueError('Your number of iterations cannot be negative')
                if iterations > 10: # check for too large of input.
                    raise ValueError('Your number of iterations cannot exceed 10')
                break
            except ValueError as e:
                if 'invalid literal for int()' in str(e): # checks for non-numeric input.
                    print('\tYour number of iterations must be a valid integer, please try again.') 
                else: # for any other errors, print the error message and prompt the user to try again.
                    print(f'\t{e}, please try again.')

        return iterations

    def validate_turn_angle(self): 
        """
        Collects the turn angle from the user and validates that it is a valid floating-point number between 0° and 360°.

        Returns:
        turn_angle (float): The validated turn angle in degrees.
        """
        while True:
            try:
                turn_angle = float(input('\n\tEnter your turn angle: ').strip()) # strip input.
                if not 0 <= turn_angle <= 360: # check for too large or too small of input.
                    raise ValueError('\n\tYour turn angle must be between 0° and 360°')
                break
            except ValueError as e:
                if 'could not convert string to float' in str(e): # checks for non-numeric input.
                    print('\tYour turn angle must be a valid floating-point number, please try again.') 
                else: # for any other errors, print the error message and prompt the user to try again.
                    print(f'\t{e}, please try again.')

        return turn_angle

    def validate_starting_direction(self): 
        """
        Collects the starting direction from the user and validates that it is a valid floating-point number between 0° and 360°.

        Returns:
        starting_direction (float): The validated starting direction in degrees.
        """
        while True:
            try:
                starting_direction = float(input('\n\tEnter starting direction: ').strip()) # strip input.
                if not 0 <= starting_direction <= 360: # check for too large or too small of input.
                    raise ValueError('\n\tYour starting direction must be between 0° and 360°')
                break
            except ValueError as e:
                if 'could not convert string to float' in str(e): # checks for non-numeric input.
                    print('\tYour starting direction must be a valid floating-point number, please try again.')
                else: # for any other errors, print the error message and prompt the user to try again.
                    print(f'\t{e}, please try again.')

        return starting_direction
    
    def parse_custom(self): 
        """
        Parses the L-System associated with the current example and returns the parsed system.

        Returns:
        parsed_system(str): The parsed system.
        """
        parser_obj = LSystemParser(self.axiom, self.rules, self.iterations) # create LSystemParser object found in utils/parser.py and give it the current example's attributes.
        parsed_system = parser_obj.parse() # parse the system.
        return parsed_system # return the parsed system.
    
    def visualize_custom(self, drawing_color, background_color, parsed): 
        """
        Visualizes the L-System and returns the visualization.

        Parameters:
        drawing_color (str): The drawing color from the LSystemStudio object.
        background_color (str): The background colorfrom the LSystemStudio object.
        parsed (str): The parsed system.
        """
        visualizer_obj = LSystemVisualizer(drawing_color, background_color, parsed, self.turn_angle, self.starting_direction) # create LSystemVisualizer object found in utils/visualizer.py and give it the current example's attributes.
        visualization = visualizer_obj.visualize() # visualize the system.
        return visualization # return the visualization.