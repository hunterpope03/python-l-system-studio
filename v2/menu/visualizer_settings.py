from .utils import get_plot_color, get_plot_background_color

class LSystemVisualizerSettings:
    def __init__(self): 
        print('\n\n' + '***** Visualizer Settings *****')
        self.valid_colors = ['red', 'green', 'blue', 'black', 'white', 'yellow', 'purple', 'orange']

    def menu(self): 
        print('\n\n' + 'Here you can change the visualize drawing and background color. The valid colors are:' + '\n')
        for color in self.valid_colors: 
            print('\t' + f'• {color}')

    def get_data(self): 
        drawing = get_plot_color()
        background = get_plot_background_color()

        return (drawing, background)


