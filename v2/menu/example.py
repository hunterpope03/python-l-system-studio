from utils import validate_menu, LSystemParser, LSystemVisualizer # import function for menu validation and classes for parsing and visualizing.
from lib import example_data # import function for getting example data.

class LSystemExample(): 
    def __init__(self) -> None: 
        """
        Initializes an LSystemExample object with empty variables that will contain the attributes of the system.
        """
        self.name = None
        self.axiom = None
        self.rules = None
        self.iterations = None
        self.turn_angle = None
        self.starting_direction = None

    def example_menu(self) -> str: 
        """
        Prints the example menu and validates the user's input with the validate_menu function found in utils/validation.py.

        Returns:
        user (str): The validated user choice as a string from the menu options.
        """
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
        print('\t' + '10. Hexagonal Gosper') # menu options that correspond with the example_data function's entries.

        user = validate_menu(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']) # get validated user input.

        return user

    def example_details(self, example_num) -> list: 
        """
        Retrieves and stores the selected example's attributes and returns a list containing the system's details as formatted strings to simplify the output process.

        Parameters:
        example_num (str): The number of the example to retrieve data for.

        Returns:
        list: A list containing the system's details.
        """
        example_details = example_data(example_num) # get example details based on the user selection.

        self.name = example_details[0]
        self.axiom = example_details[1]
        self.rules = example_details[2]
        self.iterations = example_details[3]
        self.turn_angle = example_details[4]
        self.starting_direction = example_details[5] # assign example details to instance variables.

        rules_txt = [] # create a new dictionary for outputting the rules

        for rule in self.rules: 
            rules_txt.append('\t\t' + f'{rule} -> {example_details[2][rule]}') # append each rule as a formatted string.

        return [
            '\n\n' + f'System: {self.name}'
            '\n\n\t' + f'• Axiom: {self.axiom}', 
            '\t' + '• Rules: ' + '\n',
            rules_txt, 
            '\n\t' + f'• Iterations: {self.iterations}',
            '\t' + f'• Turn Angle: {self.turn_angle}°'
            '\n\t' + f'• Starting Direction: {self.starting_direction}°' + '\n\n'
        ] # return a list containing the statements for the system's details as formatted strings. 
    
    def parse_example(self) -> str: 
        """
        Parses the L-System associated with the current example and returns the parsed system.

        Returns:
        parsed_system(str): The parsed system.
        """
        parser_obj = LSystemParser(self.axiom, self.rules, self.iterations) # create LSystemParser object found in utils/parser.py and give it the current example's attributes.
        parsed_system = parser_obj.parse() # parse the system.
        return parsed_system # return the parsed system.
    
    def visualize_example(self, drawing_color, background_color, parsed) -> None: 
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
