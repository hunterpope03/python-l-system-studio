# Python L-System Studio v2.0.0
#### Format: Executable
#### Technologies & Frameworks: Python, PyQt5, unittest
## Visuals 
![board_red](https://github.com/user-attachments/assets/3d01dd27-d8fc-4114-bd81-bfb96299d253)
##### Example L-System, "Board", via [Paul Bourke](https://paulbourke.net/fractals/lsys/)
![leaf_orange](https://github.com/user-attachments/assets/d57b6c5d-5a6d-41a4-95f8-827492111a5d)
##### Example L-System, "Fractal Tree", via [Wikipedia](https://en.wikipedia.org/wiki/L-system)
![green_bush](https://github.com/user-attachments/assets/fecf561c-bf0e-43b2-acca-344d31a5ccc5)
##### Example L-System, "L-System Bush 4", via [Paul Bourke](https://paulbourke.net/fractals/lsys/)
![penta_blue](https://github.com/user-attachments/assets/79e5b297-4602-4655-988f-c1f3cb2da531)
##### Example L-System, "Pentaplexity", via [Paul Bourke](https://paulbourke.net/fractals/lsys/)
![purple_sierpinski](https://github.com/user-attachments/assets/72fe3919-5fd1-4474-a83f-35e589c92cc1)
##### Example L-System, "Sierpinski Arrowhead", via [Paul Bourke](https://paulbourke.net/fractals/lsys/)
## How to Use
1. Visit the [Releases](https://github.com/hunterpope03/python-l-system-parser-and-visualizer/releases) section of this repository
2. Download the appropriate _.zip_ file based on your operating system
3. Unzip the file and to reveal the executable
4. Run the executable
## New Features
Version 2.0.0 of my Python L-System Studio contains the following new features: 
* Animated visualizations
* Functionality to allow a user to change the visualization's drawing and background color
## Code Revisions
Building off of v1.0.0 of this project, this version of L-System Studio contains the following revisions:
* Object-oriented programming for all backend logic
* Modularization of code into packages
* New animated visualization software created using PyQt5 that can plot nearly 1000 commands in one-tenth of a second
* Thorough testing for all validation methods
## Directory Structure
* **app.py** - main file that runs the program
* **_/menu/..._** - package containing a class for each menu option
* **_/utils/..._** - package containing the classes for validating menu input and for parsing and visualizing an L-System
* **_/lib/..._** - package containing data for example L-Systems
* **_/tests/..._** - package containing tests for validation and parsing methods
## References & Attribution
* [Paul Bourke's 1991 L-System Manual](https://paulbourke.net/fractals/lsys/)
* [Lindemayer & Prusinkiewicz's 2004 _The Algorithmic Beauty of Plants_](https://algorithmicbotany.org/papers/abop/abop.pdf)
* [PyQt5 Widget Documentation](https://www.pythonguis.com/tutorials/pyqt-basic-widgets/)
* [Unittest Documentation](https://docs.python.org/3/library/unittest.html)
#### Additional documentation and commentary are included directly within the code files. 
