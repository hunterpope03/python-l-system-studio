def l_system_parser(axiom, rules, iterations): 
    starting_string = axiom
    for iteration in range(iterations): 
        new_string = ''
        for char in starting_string: 
            if char in rules: 
                new_string += rules[char]
            else: 
                new_string += char
        starting_string = new_string

    parsed_string = starting_string

    return parsed_string