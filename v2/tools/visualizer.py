import math
import matplotlib.pyplot as plt

class LSystemVisualizer(): 
    def __init__(self, plot_color, plot_background, parsed, turn_angle, starting_direction): 
        self.plot_color = plot_color
        self.plot_background = plot_background
        self.parsed = parsed
        self.turn_angle = turn_angle
        self.starting_direction = starting_direction

    def visualize(self): 
        x = 0
        y = 0
        stack = []
        points = [(x, y)]

        for char in self.parsed: 
            if char.isalpha() and char.isupper(): 
                x += math.cos(math.radians(self.starting_direction))
                y += math.sin(math.radians(self.starting_direction))
                points.append((x, y))
            elif char.isalpha(): 
                x += math.cos(math.radians(self.starting_direction))
                y += math.sin(math.radians(self.starting_direction))
            elif char == '+':
                self.starting_direction += self.turn_angle
            elif char == '-':
                self.starting_direction -= self.turn_angle
            elif char == '[':
                stack.append((x, y, self.starting_direction))
            elif char == ']':
                if stack: 
                    x, y, self.starting_direction = stack.pop()
                    points.append((x, y))

        x_coords, y_coords = zip(*points) # unpack the coordinates

        figure = plt.figure(figsize = (8, 8)) 
        axes = figure.add_subplot(111, aspect = 'equal')

        axes.plot(x_coords, y_coords, color = self.plot_color, linewidth=0.5)
        plt.gcf().set_facecolor(self.plot_background)

        axes.set_axis_off()

        figure.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)

        plt.show(block = True)