import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLineEdit, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QTextEdit, QGridLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import networkx as nx

# Collatz functions
def reverse_collatz_step(n):
    predecessors = []
    predecessors.append((n * 2, 'even'))
    if (n - 1) % 3 == 0 and ((n - 1) // 3) % 2 == 1 and (n - 1) // 3 != 1:
        predecessors.append(((n - 1) // 3, 'odd'))
    return predecessors

def find_reverse_collatz_paths(n, depth, current_path=[], all_paths=[]):
    if depth == 0:
        all_paths.append(current_path[::-1])
        return all_paths
    predecessors = reverse_collatz_step(n)
    for pred, operation in predecessors:
        find_reverse_collatz_paths(pred, depth - 1, current_path + [(n, operation)], all_paths)
    return all_paths

def display_paths_as_text(paths):
    paths_text = ""
    for path_index, path in enumerate(paths):
        paths_text += f"Path {path_index + 1}:\n"
        for step_number, (value, operation) in enumerate(path):
            paths_text += f"{step_number}. Value: {value}, Operation: {operation}\n"
    return paths_text
    
# Function to draw paths chart
def draw_paths_chart(paths):
    G = nx.DiGraph()
    for path in paths:
        for i in range(len(path) - 1):
            G.add_edge(path[i + 1][0], path[i][0])  # Reverse direction for correct visualization
    fig = Figure()
    ax = fig.add_subplot(111)
    nx.draw(G, ax=ax, with_labels=True, node_size=500, node_color="lightblue", font_weight='bold', font_size=8)
    return fig

class CollatzGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Reverse Collatz Explorer')
        self.setGeometry(100, 100, 1024, 768)  # Adjusted for a larger default size
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        grid_layout = QGridLayout(self.central_widget)

        # Inputs and text output area
        self.number_input = QLineEdit(self)
        self.number_input.setPlaceholderText('Enter a number')
        
        self.depth_input = QLineEdit(self)
        self.depth_input.setPlaceholderText('Enter the number of steps to reverse')
        
        self.execute_button = QPushButton('Execute', self)
        self.execute_button.clicked.connect(self.execute)
        
        self.results_display = QTextEdit(self)
        self.results_display.setReadOnly(True)
        
        input_layout = QVBoxLayout()
        input_layout.addWidget(QLabel('Number:'))
        input_layout.addWidget(self.number_input)
        input_layout.addWidget(QLabel('Depth:'))
        input_layout.addWidget(self.depth_input)
        input_layout.addWidget(self.execute_button)
        input_layout.addWidget(self.results_display)
        
        # Chart area
        self.figure_canvas = FigureCanvas(Figure(figsize=(5, 3)))
        
        # Splitting the layout
        #grid_layout.addLayout(input_layout, 0, 0, 1, 1)  # Inputs on the left
        #grid_layout.addWidget(self.figure_canvas, 0, 1, 1, 2)  # Chart on the right
        self.toolbar = None  # Placeholder if you want to add a matplotlib toolbar

        # Adding layouts and widgets to the grid
        grid_layout.addLayout(input_layout, 0, 0)  # Inputs on the left
        grid_layout.addWidget(self.figure_canvas, 0, 1)  # Chart on the right

        # Set column stretch factors
        grid_layout.setColumnStretch(0, 1)  # Left column (input) with default stretch
        grid_layout.setColumnStretch(1, 2)  # Right column (chart) with double the stretch of the left
        #--------------
        
        self.central_widget.setLayout(grid_layout)
        
    def execute(self):
        number = int(self.number_input.text())
        depth = int(self.depth_input.text())
        paths = find_reverse_collatz_paths(number, depth, current_path=[], all_paths=[])
        
        paths_text = display_paths_as_text(paths)
        self.results_display.setText(paths_text)
        
        fig = draw_paths_chart(paths)
        self.figure_canvas.figure.clf()  # Clear the current figure
        self.figure_canvas.figure = fig
        self.figure_canvas.draw()

def main():
    app = QApplication(sys.argv)
    ex = CollatzGUI()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

