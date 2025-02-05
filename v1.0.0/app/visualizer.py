import matplotlib.pyplot as plt # import matplotlib as the visualization package
import math # import math to handle trigonometry
import random # import random to get a random color for each plot

def get_random_color() -> str: 
    """
    Returns a random color from a predefined list of colors.

    Returns:
    str: A randomly selected color.
    """
    colors = ['red', 'green', 'blue', 'purple']
    return random.choice(colors)

def visualize(l_system, turn_angle, starting_direction) -> None: 
    """
    Visualizes the parsed string using matplotlib.

    Parameters:
    l_system (str): The parsed string.
    turn_angle (float): The angle to turn left or right.
    starting_direction (float): The starting direction of the visualization's drawing.

    Returns:
    None
    """
    x = 0
    y = 0
    position_stack = []
    direction = starting_direction
    points = [(x,y)]

    for char in l_system:
        if char.isalpha() and char.isupper(): 
            x += math.cos(math.radians(direction))
            y += math.sin(math.radians(direction))
            points.append((x, y))
        elif char.isalpha(): 
            x += math.cos(math.radians(direction))
            y += math.sin(math.radians(direction))
        elif char == '+':
            direction += turn_angle # turn counterclockwise (left)
        elif char == '-':
            direction -= turn_angle # turn clockwise (right)
        elif char == '[':
            position_stack.append((x, y, direction)) # save the current position; allows for branching
        elif char == ']':
            if position_stack: 
                x, y, direction = position_stack.pop() # return to the previous position; allows for branching
                points.append((x, y)) 

    plot_color = get_random_color()

    x_coordinates, y_coordinates = zip(*points) # unpack the coordinates

    figure = plt.figure(figsize=(8, 8)) 
    axes = figure.add_subplot(111, aspect='equal')

    axes.plot(x_coordinates, y_coordinates, color=plot_color, linewidth=0.5)

    axes.set_axis_off()

    figure.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)

    plt.show(block=False) # plot