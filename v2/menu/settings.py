class LSystemSettings(): 
    def __init__(self) -> None: 
        """
        Initializes an LSystemSettings object with a list of valid colors that will be used for validating user input.
        """
        self.valid_colors = ['black', 'white', 'red', 'orange', 'yellow', 'green', 'blue', 'purple']

    def drawing_menu(self) -> str: 
        """
        Displays a menu for changing the drawing color of the visualization.
        
        Returns:
        str: The validated drawing color chosen by the user.
        """
        print('\n\n' + 'Here you can change the drawing and background color of the visualization. Valid colors are:' + '\n')
        for color in self.valid_colors: 
            print('\t' + f'• {color.title()}') # print greeting message and list of valid colors.

        color = self.validate_drawing_color(self.valid_colors)

        return color
    
    def background_menu(self) -> str: 
        """
        Displays a menu for changing the background color of the visualization.
        
        Returns:
        str: The validated background color chosen by the user.
        """        
        color = self.validate_background_color(self.valid_colors)

        return color
    
    def validate_drawing_color(self, valid_colors) -> str: 
        """
        Collects the drawing color from the user and validates that it is a valid color.

        Returns:
        axiom (str): The validated drawing color.
        """
        while True:
            try:
                color = input('\n' + 'Enter the preferred color in lowercase for the drawing of the visualization (leave blank to keep the default color red): ').strip()
                if color == '': # if left blank, keep the default color.
                    color = 'red'
                elif color not in valid_colors: # check for invalid color.
                    raise ValueError(f'Invalid color. Valid colors are: {valid_colors}')
                break
            except ValueError as e: # for any other errors, print the error message and prompt the user to try again.
                print(f'{e}, please try again.')

        return color

    def validate_background_color(self, valid_colors) -> str: 
        """
        Collects the backgrounds color from the user and validates that it is a valid color.

        Returns:
        axiom (str): The validated background color.
        """
        while True:
            try:
                color = input('\n\n' + 'Enter the preferred color in lowercase for the background of the visualization (leave blank to keep the default color black): ').strip()
                if color == '': # if left blank, keep the default color.
                    color = 'black'
                elif color not in valid_colors: # check for invalid color.
                    raise ValueError(f'Invalid color. Valid colors are: {valid_colors}')
                break
            except ValueError as e: # for any other errors, print the error message and prompt the user to try again.
                print(f'{e}, please try again.')

        return color