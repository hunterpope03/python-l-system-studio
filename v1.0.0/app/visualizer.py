import matplotlib.pyplot as plt
import math
import random

def get_random_color(): 
    colors = ['red', 'green', 'blue', 'purple']
    return random.choice(colors)

def visualize(l_system, turn_angle, starting_direction): 
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
            direction += turn_angle
        elif char == '-':
            direction -= turn_angle
        elif char == '[':
            position_stack.append((x, y, direction))
        elif char == ']':
            if position_stack: 
                x, y, direction = position_stack.pop()
                points.append((x, y))

    plot_color = get_random_color()

    x_coordinates, y_coordinates = zip(*points)

    figure = plt.figure(figsize=(8, 8)) 
    axes = figure.add_subplot(111, aspect='equal')

    axes.plot(x_coordinates, y_coordinates, color=plot_color, linewidth=0.5)

    axes.set_axis_off()

    figure.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)

    plt.show(block=False)