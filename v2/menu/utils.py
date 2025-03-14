VALID_CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+-[]'
VALID_COLORS = ['red', 'green', 'blue', 'yellow', 'purple', 'orange', 'pink', 'black', 'white']

def validate_menu(valid): 
    while True: 
        user = input(f'\nEnter choice {[i for i in valid]}: ').strip()
        if user in valid: 
            return user
        else: 
            print('\nInvalid.', end=' ')

def get_axiom(): 
    while True:
        try:
            axiom = input('\n\tEnter axiom: ').strip()
            if not axiom:
                raise ValueError('Axiom cannot be empty')
            if len(axiom) > 10:
                raise ValueError('Axiom cannot be longer than 10 characters')
            if ' ' in axiom:
                raise ValueError('Axiom cannot contain spaces')
            if not all(c in VALID_CHARS for c in axiom):
                raise ValueError(f'Axiom cannot contain invalid characters. Valid characters are: {VALID_CHARS}')
            break
        except ValueError as e:
            print(f'\t{e}, please try again.')

    return axiom

def get_rules(axiom):
    rules = {}
    axiom_vars = {c for c in axiom if c.isupper()}
    vars_to_process = sorted(axiom_vars)

    while vars_to_process:
        var = vars_to_process.pop(0)
        if var in rules:
            continue

        while True:
            try:
                rule = input(f'\n\tEnter the transformation rule for the variable {var}: ').strip()
                if ' ' in rule:
                    raise ValueError('Your transformation rule cannot contain spaces')
                if not all(c in VALID_CHARS for c in rule):
                    raise ValueError(f'Your transformation rule contains invalid characters. Valid characters are: {VALID_CHARS}')
                
                rules[var] = rule
                new_vars = {c for c in rule if c.isupper() and c not in rules and c not in vars_to_process}
                if new_vars:
                    vars_to_process.extend(sorted(new_vars))
                break
            except ValueError as e:
                print(f'\t{e}, please try again.')

    return rules

def get_iterations():
    while True:
        try:
            iterations = int(input('\n\tEnter your number of iterations: ').strip())
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

def get_turn_angle(): 
    while True:
        try:
            turn_angle = float(input('\n\tEnter your turn angle: ').strip())
            if not 0 <= turn_angle <= 360:
                raise ValueError('\n\tYour turn angle must be between 0° and 360°.')
            break
        except ValueError as e:
            if 'could not convert string to float' in str(e):
                print('\tYour turn angle must be a valid floating-point number, please try again.') # catches non-numeric input
            else:
                print(f'\t{e}, please try again.')

    return turn_angle

def get_starting_direction(): 
    while True:
        try:
            starting_direction = float(input('\n\tEnter starting direction: ').strip())
            if not 0 <= starting_direction <= 360:
                raise ValueError('\n\tYour starting direction must be between 0° and 360°.')
            break
        except ValueError as e:
            if 'could not convert string to float' in str(e):
                print('\tYour starting direction must be a valid floating-point number, please try again.') # catches non-numeric input
            else:
                print(f'\t{e}, please try again.')

    return starting_direction

def print_system_details(axiom, rules, iterations, turn_angle, starting_direction): 
    print('\n\t' + f'• Axiom: {axiom}')
    print('\t' + '• Rules: ' , '\n')
    for rule in rules: 
        print('\t\t' + f'{rule} -> {rules[rule]}')
    print('\n\t' + f'• Iterations: {iterations}')   
    print('\t' + f'• Turn Angle: {turn_angle}°')
    print('\t' + f'• Starting Direction: {starting_direction}°' + '\n\n')

def get_plot_color(): 
    while True:
        try:
            color = input('\n\n' + 'Enter the preferred color in lowercase for the drawing (default is red): ').strip()
            if color == '':
                color = 'red'
            elif color not in VALID_COLORS:
                raise ValueError(f'Invalid color. Valid colors are: {VALID_COLORS}')
            break
        except ValueError as e:
            print(f'\t{e}, please try again.')

    return color

def get_plot_background_color(): 
    while True:
        try:
            color = input('\n\n' + 'Enter the preferred color in lowercase for the background (default is black): ').strip()
            if color == '':
                color = 'black'
            elif color not in VALID_COLORS:
                raise ValueError(f'Invalid color. Valid colors are: {VALID_COLORS}')
            break
        except ValueError as e:
            print(f'\t{e}, please try again.')

    return color