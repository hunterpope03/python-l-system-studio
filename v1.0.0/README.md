# Python L-System Parser and Visualizer v1.0.0
#### Format: Deployable
#### Technologies & Frameworks: Python, matplotlib, unittest
## How to Use
1. Visit the [Releases](https://github.com/hunterpope03/python-l-system-parser-and-visualizer/releases/tag/v1.0.0) section of this repository
2. Download the _.zip_ file
3. Locate the _.zip_ file on your system and extract / unzip it
4. Open the folder in an IDE or navigate to it on the command line
5. Download the required dependencies found in **_requirements.txt_**
6. Run the **_main.py_** file
## Description
This personal project explores the uses of L-Systems and how they can be used to visualize plants, shapes, textile designs, and more. Developed completely in Python, this program allows a user to: 
* View a tutorial / guide on L-Systems and how to navigate the program
* View the data and visualizations of popular L-Systems
* Enter in custom data values to create a personalized L-System visualization

Using Paul Bourke's [L-System Manual](https://paulbourke.net/fractals/lsys/) as a guiding tool, I developed a simple parser, utilized matplotlib to visualize the results, and implementd unittest's testing software to ensure proper parsing behavior.

This program features solely variables and logic organized into modules. I anticipate v2.0.0 to feature a GUI setup with object-oriented-programming for back-end logic, and v3.0.0 to feature a full-stack website with a much more responsive, clean user interface.

  Extensive data on L-Systems can be found within this program and on this [repository's homepage](https://github.com/hunterpope03/python-l-system-parser-and-visualizer). 

## Directory Structure
##### / app - contains all of the application files
* **_main.py_** - Runs the program.
* **_modules.py_** - Contains all of the modules and logic for the program to function.
* **_example_library.py_** - Contains all of the data values for eight example L-Systems.
* **_parser.py_** - Contains a function to parse an L-System.
* **_visualizer.py_** - Contains a function to visualize a parsed L-System (with matplotlib). 
##### / tests - contains all of the test files
##### requirements.txt - contains dependencies necessary to download before running
## References & Attribution
* [Paul Bourke's 1991 L-System Manual](https://paulbourke.net/fractals/lsys/)
* [Lindemayer & Prusinkiewicz's 2004 _The Algorithmic Beauty of Plants_](https://algorithmicbotany.org/papers/abop/abop.pdf)
* [Matplotlib Documentation](https://matplotlib.org/stable/index.html)
* [Unittest Documentation](https://docs.python.org/3/library/unittest.html)

  ##### Additional documentation and commentary are included directly within the code files. 


  
