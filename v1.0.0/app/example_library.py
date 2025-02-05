def example_details(example_num): 
    if example_num == '1': 
        name = 'L-System Bush 2'
        axiom = 'F'
        rules = {'F' : 'FF+[+F-F-F]-[-F+F+F]'}
        iterations = 5
        turn_angle = 22.5
        starting_direction = 90
    elif example_num == '2': 
        name = 'L-System Bush 4'
        axiom = 'VZFFF'
        rules = {'V' : '[+++W][---W]YV',
                 'W' : '+X[-W]Z',
                 'X' : '-W[+X]Z',
                 'Y' : 'YZ',
                 'Z' : '[-FFF][+FFF]F'
                 }
        iterations = 12
        turn_angle = 20
        starting_direction = 90
    elif example_num == '3': 
        name = 'Quadratic Gosper'
        axiom = '-YF'
        rules = {'X' : 'XFX-YF-YF+FX+FX-YF-YFFX+YF+FXFXYF-FX+YF+FXFX+YF-FXYF-YF-FX+FX+YFYF-', 
                 'Y' : '+FXFX-YF-YF+FX+FXYF+FX-YFYF-FX-YF+FXYFYF-FX-YFFX+FX+YF-YF-FX+FX+YFY'
                 }
        iterations = 3
        turn_angle = 90
        starting_direction = 0
    elif example_num == '4': 
        name = 'Board'
        axiom = 'F+F+F+F'
        rules = {'F' : 'FF+F+F+F+FF'}
        iterations = 5
        turn_angle = 90
        starting_direction = 0
    elif example_num == '5': 
        name = 'Sierpinski Triangle'
        axiom = 'YF'
        rules = {'X' : 'YF+XF+Y', 
                 'Y' : 'XF-YF-X'}
        iterations = 8
        turn_angle = 60
        starting_direction = 0
    elif example_num == '6': 
        name = 'Pentaplexity'
        axiom = 'F++F++F++F++F'
        rules = {'F' : 'F++F++F+++++F-F++F'}
        iterations = 5
        turn_angle = 36
        starting_direction = 0
    elif example_num == '7': 
        name = 'Dragon Curve'
        axiom = 'FX'
        rules = {'X' : 'X+YF+',
                 'Y' : '-FX-Y'
                 }
        iterations = 14
        turn_angle = 90
        starting_direction = 90
    else: 
        name = 'Hexagonal Gosper'
        axiom = 'XF'
        rules = {'X' : 'X+YF++YF-FX--FXFX-YF+', 
                 'Y' : '-FX+YFYF++YF+FX--FX-Y'
                 }
        iterations = 5
        turn_angle = 60
        starting_direction = 0

    return [name, axiom, rules, iterations, turn_angle, starting_direction]
    