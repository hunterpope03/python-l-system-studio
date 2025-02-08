from tkinter import *

class Window: 
    def __init__(self, window): 
        self.window = window

        self.window_width = int(window.winfo_screenwidth())
        self.window_height = int(window.winfo_screenheight() * 0.875)

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
            font=('System', 55, 'bold', 'underline'),
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
        self.system_headline= Label(
            self.system_frame,
            text='Creating an L-System',
            font=('System', 40, 'bold'),
            bg='black',
            fg='white',
            anchor='center',
            justify='center',
            wraplength=int(self.window_width * 0.3)
        )
        self.system_headline.pack(side='top', fill='both', expand=True)
        #region system key
        self.system_key_headline= Label(
            self.system_frame,
            text='L-System Character Key',
            font=('System', 25, 'bold'),
            bg='black',
            fg='white',
            anchor='center',
            justify='center',
            wraplength=int(self.window_width * 0.3)
        )
        self.system_key_headline.pack(side='top', fill='both', expand=True)
        self.system_key_header= Label(
            self.system_frame,
            text='Character\t\t\tCommand\n\n',
            font=('System', 15, 'bold', 'underline'), 
            bg='black',
            fg='white',
            anchor='center',
            justify='center',
            wraplength=int(self.window_width * 0.3)
        )
        self.system_key_header.pack(side='top', fill='both', expand=True)
        self.system_key_header= Label(
            self.system_frame,
            text='Uppercase Letter\t\t\tMove Forward while Drawing\nLowercase Letter\t\t\tMove Forward without Drawing\n+\t\t\t\tTurn Right\n-\t\t\t\tTurn Left\n[\t\t\t\tStart New Branch\n]\t\t\t\tReturn to Previous Branch',
            font=('System', 11), 
            bg='black',
            fg='white',
            anchor='center',
            justify='left',
            wraplength=int(self.window_width * 0.3)
        )
        self.system_key_header.pack(side='top', fill='both', expand=True)
        #endregion system key
        #region system selection
        self.system_selection_frame = Frame(self.system_frame)
        self.system_selection_frame.config(
            bg='black',
        )
        self.system_selection_example = Button(
            self.system_selection_frame, 
            text='See an Example', 
            command=self.selection_initilization(1), 
            font=("Helvetica", 12, 'bold'), 
            bg="black", 
            fg="black",
            highlightbackground="black", 
            highlightcolor="white", 
            relief="flat",
            highlightthickness=2
        )
        self.system_selection_example.pack(
            side='left',  
            fill='y',     
            expand=True   
        )
        self.system_selection_custom = Button(
            self.system_selection_frame, 
            text='Create my Own', 
            command=self.selection_initilization(2), 
            font=("Helvetica", 12, 'bold'), 
            bg="black", 
            fg="black",
            highlightbackground="black", 
            highlightcolor="white", 
            relief="flat",
            highlightthickness=2
        )
        self.system_selection_custom.pack(
            side='right',  
            fill='y',     
            expand=True   
        )
        self.system_selection_frame.pack(
            side='bottom',  
            fill='x',     
            expand=True   
        )
        #endregion system selection
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

    def selection_initilization(self, selection): 
        pass
    def select_example(self):
        pass

    def select_custom(self):
        pass