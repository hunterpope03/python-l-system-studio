import math # import math for trigonometry and angles
import sys # import sys to create an QApplication class
from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QMainWindow # import PyQt graphic libraries for creating the GUI
from PyQt5.QtGui import QPen, QColor, QBrush, QPainter # import PyQt drawing libraries for drawing the system
from PyQt5.QtCore import Qt, QTimer # import PyQt core libraries for running the animation

class LSystemVisualizer(QMainWindow): 
    def __init__(self, drawing_color, background_color, parsed_system, turn_angle, starting_direction):
        if not QApplication.instance():
            self.app = QApplication(sys.argv)
            self.owns_app = True
        else:
            self.app = QApplication.instance()
            self.owns_app = False

        super().__init__()

        # Clean up previous instance if this object is being reused
        if hasattr(self, 'timer') and self.timer is not None:
            self.timer.stop()
        if hasattr(self, 'scene') and self.scene is not None:
            self.scene.clear()
        if hasattr(self, 'view') and self.view is not None:
            self.view.setScene(None)

        self.plot_color = QColor(drawing_color)
        self.plot_background = QColor(background_color)
        self.parsed = parsed_system
        self.turn_angle = turn_angle
        self.starting_direction = starting_direction
        self.path_items = []

        self.boundaries = self.set_boundaries()
        self.min_x = self.boundaries[0]
        self.max_x = self.boundaries[1]
        self.min_y = self.boundaries[2]
        self.max_y = self.boundaries[3]

        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)
        self.view.setRenderHint(QPainter.Antialiasing)
        self.setCentralWidget(self.view)

        self.scene.setBackgroundBrush(QBrush(self.plot_background))
        self.pen = QPen(self.plot_color)
        self.pen.setWidthF(0.2)

        self.set_frame()
        self.set_starting_point()

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        
        self.setWindowTitle("L-System Visualization")
        self.resize(800, 800)
            
    def set_boundaries(self): 
        x, y = 0, 0
        min_x, max_x = 0, 0
        min_y, max_y = 0, 0
        direction = self.starting_direction
        stack = []
        
        for char in self.parsed:
            if char.isalpha() and char.isupper():
                x += math.cos(math.radians(direction))
                y -= math.sin(math.radians(direction)) 
                min_x = min(min_x, x)
                max_x = max(max_x, x)
                min_y = min(min_y, y)
                max_y = max(max_y, y)
            elif char.isalpha():
                x += math.cos(math.radians(direction))
                y -= math.sin(math.radians(direction))
            elif char == '+':
                direction += self.turn_angle
            elif char == '-':
                direction -= self.turn_angle
            elif char == '[':
                stack.append((x, y, direction))
            elif char == ']':
                if stack:
                    x, y, direction = stack.pop()
                    min_x = min(min_x, x)
                    max_x = max(max_x, x)
                    min_y = min(min_y, y)
                    max_y = max(max_y, y)
        
        return [min_x, max_x, min_y, max_y]
    
    def set_frame(self):
        width = self.max_x - self.min_x
        height = self.max_y - self.min_y
        margin_x = width * 0.1
        margin_y = height * 0.1
        self.scene.setSceneRect(
            self.min_x - margin_x,
            self.min_y - margin_y,
            width + 2 * margin_x,
            height + 2 * margin_y
        )

    def set_starting_point(self): 
        self.x = 0  # Start at origin
        self.y = 0
        self.stack = []
        self.points = [(self.x, self.y)]
        self.current_index = 0

    def update_frame(self): 
        if self.current_index >= len(self.parsed):
            self.timer.stop()
            return
        
        batch_size = 1000  
        
        for _ in range(batch_size):
            if self.current_index >= len(self.parsed):
                self.timer.stop()
                return
                
            old_x, old_y = self.x, self.y
            char = self.parsed[self.current_index]
            
            if char.isalpha() and char.isupper():
                self.x += math.cos(math.radians(self.starting_direction))
                self.y -= math.sin(math.radians(self.starting_direction)) 
                self.points.append((self.x, self.y))
                # Draw line
                line = self.scene.addLine(old_x, old_y, self.x, self.y, self.pen)
                self.path_items.append(line)
            elif char.isalpha():
                self.x += math.cos(math.radians(self.starting_direction))
                self.y -= math.sin(math.radians(self.starting_direction))
            elif char == '+':
                self.starting_direction += self.turn_angle
            elif char == '-':
                self.starting_direction -= self.turn_angle
            elif char == '[':
                self.stack.append((self.x, self.y, self.starting_direction))
            elif char == ']':
                if self.stack:
                    self.x, self.y, self.starting_direction = self.stack.pop()
                    self.points.append((self.x, self.y))
                    
            self.current_index += 1

    def visualize(self): 
        self.show()
        self.view.fitInView(self.scene.sceneRect(), Qt.KeepAspectRatio)
        self.timer.start(1)

        if hasattr(self, 'app') and not self.app.startingUp():
            return self.app.exec_()