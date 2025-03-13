class LSystemParser():
    def __init__(self, axiom, rules, iterations): 
        self.axiom = axiom
        self.rules = rules
        self.iterations = iterations  
        
    def parse(self): 
        for iteration in range(self.iterations):
            new_string = '' 
            for char in self.axiom: 
                if char in self.rules:
                    new_string += self.rules[char]
                else:
                    new_string += char
            self.axiom = new_string

        return self.axiom