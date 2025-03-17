class LSystemParser():
    def __init__(self, axiom, rules, iterations) -> None: 
        """
        Initializes an LSystemParser object with the given axiom, rules, and number of iterations.

        Parameters:
        axiom (str): The starting string of the L-System.
        rules (dict): A dictionary where keys are characters in the axiom that have transformation rules and values are the corresponding transformation strings.
        iterations (int): The number of iterations to apply the transformation rules.
        """
        self.axiom = axiom
        self.rules = rules
        self.iterations = iterations  
        
    def parse(self) -> str: 
        """
        Parses the L-System according to the given rules and number of iterations.

        This function implements the L-System parsing algorithm. It iterates the given number of times, 
        replacing each character in the axiom with the corresponding transformation rule each time. The 
        resulting string is returned.

        Returns:
        parsed (str): The parsed L-System string.
        """
        for iteration in range(self.iterations):
            new_string = '' 
            for char in self.axiom: # check each character in the axiom.
                if char in self.rules:
                    new_string += self.rules[char] # if a character has transformation rules, replace it with the corresponding transformation rule. 
                else:
                    new_string += char # if a character does not have transformation rules, keep it the same.
            self.axiom = new_string

        return self.axiom