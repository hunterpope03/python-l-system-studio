INTRODUCTION = [ # introduction text with formatted strings to simplify the output process.
    '\n\n' + '***** Tutorial *****',
    '\n\n' + '** Introduction **',
    '\n\n' + '1 An L-System is a mathematical model that can be used to create plots of fractals, plants, textiles, and more.',
    '2 This studio features two parts: a parser to construct an L-System string and a visualizer to plot an L-System.',
    '3 The parser works by repeatedly applying transformation rules to a string to create a longer, more complex string. It requires the following information to start:',
    '\n\t' + '• Axiom - a starting character or string (e.g. F',
    '\t' + '• Transformation Rules - rules that define how to transform each character or substring (e.g. F -> F+F',
    '\t' + '• Iterations - the number of times the transformation rules are applied (e.g. 5',
    '\n\t' + 'The fully parsed string can grow to be thousands of characters long and is fed into a visualizer for plotting.',
    '\n' + '4 The visualizer works by interpreting each character in the parsed string as some command. It requires some command key and the following information:',
    '\n\t' + '• Starting Direction - the angle to start drawing at; allows for rotation (e.g 0°',
    '\t' + '• Turn Angle - the angle at which to turn left or right (e.g. 90°',
    '\n\tA key defines what command each character in the parsed string represents.' + '\n\n'
]

PROGRAM_KEY = [ # program key text with formatted strings to simplify the output process.
    '\n\n' + '** Program Key **',
    '\n\n' + '1 Variables represent any value that is replaced by a transformation rule.',
    '\n\t' + '• Uppercase Letters: command to move forward while drawing',
    '\t' + '• Lowercase Letters: command to move forward without drawing',
    '\n' + '2 Constants represent any value that is not replaced by a transformation rule; these are geometric commands the visualizer uses to plot the L-System.',
    '\n\t' + '• +: command to turn left at the turn angle',
    '\t' + '• -: command to turn right at turn angle',
    '\t' + '• [: command to save state to stack (used in branching)',
    '\t' + '• ]: command to remove state from stack (used in branching)' + '\n\n'
]

INPUT_RESTRICTIONS = [ # input restrictions text with formatted strings to simplify the output process.
    '\n\n' + '** Input Restrictions **' + '\n\n'
    '1 Axioms cannot be empty, longer than 15 characters, contain spaces, or contain any characters other than those defined in the program key',
    '2 Transformation rules cannot contain spaces or any characters other than those defined in the program key',
    '3 The number of iterations must be a positive integer less than 10',
    '4 Both the turn angle and starting direction must be numbers in the range [0, 360]' + '\n\n'
]

class LSystemTutorial:
    def __init__(self): 
        """
        Initializes an LSystemTutorial object with predefined sections of the tutorial.
        """
        self.introduction = INTRODUCTION
        self.program_key = PROGRAM_KEY
        self.input_restrictions = INPUT_RESTRICTIONS
    
    def tutorial_text(self): 
        """
        Returns a dictionary mapping the different sections of the tutorial to their corresponding text.
        
        Returns:
        dict: A dictionary containing the three sections of the tutorial.
        """
        tutorial_map = {
            'introduction' : self.introduction, 
            'program_key' : self.program_key, 
            'input_restrictions' : self.input_restrictions, 
        }

        return tutorial_map
    
    def cont_intro(self): 
        """
        Blank input continue point that allows the user to enter anything to continue with the program.
        Includes a custom note to guide the user through the tutorial.
        """
        cont = input('Press Enter to view the program key: ')
        return cont
    
    def cont_key(self): 
        """
        Blank input continue point that allows the user to enter anything to continue with the program.
        Includes a custom note to guide the user through the tutorial.
        """
        cont = input('Press Enter to view input restrictions in creating a custom L-System: ')
        return cont
    
    def cont_restrictions(self): 
        """
        Blank input continue point that allows the user to enter anything to continue with the program.
        Includes a custom note to guide the user through the tutorial.
        """
        cont = input('Press Enter to return back to the menu: ')
        return cont
