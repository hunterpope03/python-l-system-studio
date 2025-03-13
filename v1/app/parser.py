def l_system_parser(axiom, rules, iterations) -> str: 
    """
    A function that parses a given L-System and returns the parsed string.

    Parameters:
    axiom (str): The starting string.
    rules (dict): A dictionary of the rules.
    iterations (int): The number of times to apply the rules.

    Returns:
    parsed_string (str): The parsed string.
    """
    starting_string = axiom
    for iteration in range(iterations): # iterate the proper number of times
        new_string = ''
        for char in starting_string: 
            if char in rules: # replace a character if it has a transformation rule
                new_string += rules[char]
            else: 
                new_string += char
        starting_string = new_string

    parsed_string = starting_string

    return parsed_string