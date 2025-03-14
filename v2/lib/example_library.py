def example_library(example_num): 
    match example_num: 

        case '1': 
            name = 'Binary Tree'
            axiom = 'X'
            rules = {'X' : 'F[+X][-X]FX', 
                     'F' : 'FF'}
            iterations = 8
            turn_angle = 45
            starting_direction = 90

        case '2': 
            name = 'Fractal Plant'
            axiom = '-X'
            rules = {'X' : 'F-[[X]+X]+F[+FX]-X',
                     'F' : 'FF'}
            iterations = 8
            turn_angle = 25
            starting_direction = 90
            
        case '3': 
            name = 'Bush 1'
            axiom = 'Y'
            rules = {'X' : 'X[-FFF][+FFF]FX',
                    'Y' : 'YFX[+Y][-Y]'}
            iterations = 8
            turn_angle = 25.7
            starting_direction = 90

        case '4': 
            name = 'Bush 2'
            axiom = 'F'
            rules = {'F' : 'FF+[+F-F-F]-[-F+F+F]'}
            iterations = 5
            turn_angle = 22.5
            starting_direction = 90

        case '5':
            name = 'Bush 4'
            axiom = 'VZFFF'
            rules = {'V' : '[+++W][---W]YV',
                    'W' : '+X[-W]Z',
                    'X' : '-W[+X]Z',
                    'Y' : 'YZ',
                    'Z' : '[-FFF][+FFF]F'}
            iterations = 11
            turn_angle = 20
            starting_direction = 90

        case '6': 
            name = 'Board'
            axiom = 'F+F+F+F'
            rules = {'F' : 'FF+F+F+F+FF'}
            iterations = 5
            turn_angle = 90
            starting_direction = 0

        case '7':
            name = 'Sierpinski Arrowhead'
            axiom = 'YF'
            rules = {'X' : 'YF+XF+Y', 
                    'Y' : 'XF-YF-X'}
            iterations = 8
            turn_angle = 60
            starting_direction = 0

        case '8': 
            name = 'Pentaplexity'
            axiom = 'F++F++F++F++F'
            rules = {'F' : 'F++F++F+++++F-F++F'}
            iterations = 5
            turn_angle = 36
            starting_direction = 0

        case '9':
            name = 'Dragon Curve'
            axiom = 'FX'
            rules = {'X' : 'X+YF+',
                    'Y' : '-FX-Y'
                    }
            iterations = 14
            turn_angle = 90
            starting_direction = 90
            
        case '10':
            name = 'Kolam'
            axiom = '-D--D'
            rules = {'A' : 'F++FFFF--F--FFFF++F++FFFF--F',
                     'B' : 'F--FFFF++F++FFFF--F--FFFF++F',
                     'C' : 'BFA--BFA',
                     'D' : 'CFC--CFC'}
            iterations = 20
            turn_angle = 45
            starting_direction = 0

    return [name, axiom, rules, iterations, turn_angle, starting_direction]
