from tkinter import *

class Window: 
    def __init__(self, window): 
        self.window = window

        self.window_width = window.winfo_screenwidth()
        self.window_height = window.winfo_screenheight()

        #region title
        self.title_frame = Frame(self.window)
        self.title_frame.config(
            height=int(self.window_height * 0.3),
            width=int(self.window_width),
            bg='black', 
            bd=2, 
            relief='solid', 
            highlightbackground='white', 
            highlightthickness=2
        )
        self.title_label = Label(
            self.title_frame,
            text='L-System Parser & Visualizer',
            font=('System', 45, 'bold', 'underline'),
            bg='black',
            fg='white',
            anchor='center'  
        )
        self.title_label.pack(
            expand=True,  
            fill='both'  
        )
        self.title_frame.pack(
            side='top',
            fill='x',  
            ipadx=0,   
            ipady=int(self.window_height * 0.01) 
        )
        #endregion title

        #region tutorial
        self.tutorial_frame = Frame(self.window)
        self.tutorial_frame.config(
            height=int(self.window_height * 0.7),
            width=int(self.window_width * 0.25),
            bg='black',
            bd=2,
            relief='solid',
            highlightbackground='pink',
            highlightthickness=2
        )
        self.tutorial_intro_headline= Label(
            self.tutorial_frame,
            text='What is an L-System?',
            font=('System', 25, 'bold'),
            bg='black',
            fg='white',
            anchor='center',
            justify='center',
            wraplength=int(self.window_width * 0.20)
        )
        self.tutorial_intro_headline.pack(side='top', fill='both', expand=True)
        self.tutorial_intro = Label(
            self.tutorial_frame,
            text='A Lindenmayer(L)-System is a mathematical theory that creates complex patterns through repeated transformations.\n\nStarting with an initial character or string, called an axiom, transformation rules are applied to the axiom that define how to change a certain character into a more complex string. \n After the transformation rules are applied once, they are again applied to the resulting string for a given number of iterations. \n Aristid Lindenmayer, a hungarian botanist and biologist, invented the L-System in 1968 to model the growth of algae and bacteria. \nThe visualized results often represent plant growth, fractals, textiles, or other geometric figures.',
            font=('System', 11),
            bg='black',
            fg='white',
            anchor='center',
            justify='center',
            wraplength=int(self.window_width * 0.20)
        )
        self.tutorial_intro.pack(side='top', fill='both', expand=True)
        self.tutorial_parser_headline = Label(
            self.tutorial_frame,
            text='What is an L-System Parser?',
            font=('System', 25, 'bold'),
            bg='black',
            fg='white',
            anchor='center',
            justify='center',
            wraplength=int(self.window_width * 0.20)
        )
        self.tutorial_parser_headline.pack(side='top', fill='both', expand=True)
        self.tutorial_parser = Label(
            self.tutorial_frame,
            text='In an L-System Parser, transformation rules are applied for a given number of iterations.\n\nThe resulting "parsed" string can be thousands of character long and is usually fed into a visualizer for plotting',
            font=('System', 11),
            bg='black',
            fg='white',
            anchor='center',
            justify='center',
            wraplength=int(self.window_width * 0.20)
        )
        self.tutorial_parser.pack(side='top', fill='both', expand=True)
        self.tutorial_visualizer_headline = Label(
            self.tutorial_frame,
            text='What is an L-System Visualizer?',
            font=('System', 25, 'bold'),
            bg='black',
            fg='white',
            anchor='center',
            justify='center',
            wraplength=int(self.window_width * 0.20)
        )
        self.tutorial_visualizer_headline.pack(side='top', fill='both', expand=True)
        self.tutorial_visualizer = Label(
            self.tutorial_frame,
            text='In an L-System visualizer, each character in the parsed string is some command that tells the visualizer how to move, draw, turn, start a new branch, etc. \n Variables are values that can be changed in a transformation rule, while constants are values that are not changed but rather tell the visualizer some geometric action. \n Most programs have a specified key to define variables and constants (see right).',
            font=('System', 11),
            bg='black',
            fg='white',
            anchor='center',
            justify='center',
            wraplength=int(self.window_width * 0.20)
        )
        self.tutorial_visualizer.pack(side='top', fill='both', expand=True)
        self.tutorial_frame.pack(
            side='left',
            fill='y',
            expand=True
        )
        self.tutorial_frame.pack_propagate(False)
        #endregion tutorial

        #region system
        self.system_frame = Frame(self.window)
        self.system_frame.config(
            height=int(self.window_height * 0.7),  
            width=int(self.window_width * 0.35),    
            bg='black',
            bd=2,
            relief='solid',
            highlightbackground='red',
            highlightthickness=2
        )
        self.tutorial_intro_headline= Label(
            self.system_frame,
            text='Creating an L-System',
            font=('System', 25, 'bold'),
            bg='black',
            fg='white',
            anchor='center',
            justify='center',
            wraplength=int(self.window_width * 0.20)
        )
        self.tutorial_intro_headline.pack(side='top', fill='both', expand=True)
        self.system_frame.pack(
            side='left',  
            fill='y',     
            expand=True   
        )
        self.system_frame.pack_propagate(False)
        #endregion system

        #region visualization
        self.visualization_frame = Frame(self.window)
        self.visualization_frame.config(
            height=int(self.window_height * 0.7),  
            width=int(self.window_width * 0.4),    
            bg='black',
            bd=2,
            relief='solid',
            highlightbackground='orange',
            highlightthickness=2
        )
        self.visualization_frame.pack(
            side='left',  
            fill='y',     
            expand=True   
        )
        #endregion visualization
