# Python L-System Parser and Visualizer v1.0.0
#### Format: Deployable
#### Technologies & Frameworks: Python, matplotlib, unittest
## How to Use
1. Visit the [Releases](https://github.com/hunterpope03/python-l-system-parser-and-visualizer/releases/tag/v1.0.0) section of this repository
2. Download the _.zip_ file
3. Locate the _.zip_ file on your system and extract/unzip it
4. Open the folder in an IDE or navigate to it on the command line
5. Download the required dependencies found in **_requirements.txt_**
6. Run the **_main.py_** file
## Description
This personal project explores the uses of L-Systems and how they can be used to visualize plants, shapes, textile designs, and more. Developed completely in Python, this program allows a user to: 
* View a tutorial/guide on L-Systems and how to navigate the program
* View the data and visualizations of popular L-Systems
* Enter custom data values to create a personalized L-System visualization

Using Paul Bourke's [L-System Manual](https://paulbourke.net/fractals/lsys/) as a guiding tool, I developed a simple parser, utilized matplotlib to visualize the results, and implemented unittest's testing software to ensure proper parsing behavior.

This program features solely variables and logic organized into modules. I anticipate v2.0.0 to feature a GUI setup with object-oriented programming for back-end logic, and v3.0.0 to feature a full-stack website with a much more responsive, clean user interface.

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
## Visuals
##### Dragon Curve, via [Paul Bourke](https://paulbourke.net/fractals/lsys/)
<img width="786" alt="Dragon Curve System" src="https://github.com/user-attachments/assets/8059714b-c948-45b9-86c5-8ea79d283c44" />

##### L-System Bush 2, via [Paul Bourke](https://paulbourke.net/fractals/lsys/)
<img width="786" alt="L-System Bush 2" src="https://github.com/user-attachments/assets/9e480602-16bc-43aa-93d2-da18039eb834" />

##### Pentaplexity, via [Paul Bourke](https://paulbourke.net/fractals/lsys/)
<img width="786" alt="Pentaplexity" src="https://github.com/user-attachments/assets/c85a5640-4eff-46b5-8946-d103826717e6" />

##### Sierpinski Arrowhead, via [Paul Bourke](https://paulbourke.net/fractals/lsys/)
<img width="784" alt="Screenshot 2025-02-05 at 7 34 07 PM" src="https://github.com/user-attachments/assets/75717bfd-2603-46e4-9605-4649362bd756" />

##### Quadratic Gosper, via [Paul Bourke](https://paulbourke.net/fractals/lsys/)
<img width="784" alt="Screenshot 2025-02-05 at 7 32 53 PM" src="https://github.com/user-attachments/assets/175b4e4e-6330-4ad4-b557-b0df8fa3aa2b" />
  ##### Additional documentation and commentary are included directly within the code files. 


  
