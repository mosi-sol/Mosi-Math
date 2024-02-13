import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QHeaderView, QScrollArea
from PyQt5.QtCore import Qt
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

def is_prime(n):
    """Check if n is a prime number."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

class MplCanvas(FigureCanvas):
    """A canvas for matplotlib plots."""
    def __init__(self, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        super().__init__(self.fig)

class PrimeFinder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Prime Number Finder')
        self.setGeometry(100, 100, 1200, 600)  # Adjusted for better visibility of both sides

        # Central Widget and Layout
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.mainLayout = QHBoxLayout()  # Main layout is now QHBoxLayout
        self.centralWidget.setLayout(self.mainLayout)

        # Layout for inputs and table
        self.leftLayout = QVBoxLayout()
        self.mainLayout.addLayout(self.leftLayout)
        
        self.mainLayout.setStretch(0, 1) 

        # Input for range x to y
        self.leftLayout.addWidget(QLabel('Enter range X to Y:'))
        self.xInput = QLineEdit()
        self.yInput = QLineEdit()
        self.leftLayout.addWidget(self.xInput)
        self.leftLayout.addWidget(self.yInput)

        # Button
        self.button = QPushButton('Find Primes')
        self.button.clicked.connect(self.find_primes)
        self.leftLayout.addWidget(self.button)

        # Table for results
        self.table = QTableWidget()
        self.table.setColumnCount(1)
        self.table.setHorizontalHeaderLabels(['Prime Numbers'])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.leftLayout.addWidget(self.table)

        # Right Layout for Charts
        self.rightLayout = QVBoxLayout()
        self.mainLayout.addLayout(self.rightLayout)
        
        self.mainLayout.setStretch(1, 2)

        # Matplotlib canvas for plots
        self.canvasDistribution = MplCanvas(width=5, height=4, dpi=100)
        self.canvasGap = MplCanvas(width=5, height=4, dpi=100)
        self.rightLayout.addWidget(self.canvasDistribution)
        self.rightLayout.addWidget(self.canvasGap)

    def find_primes(self):
        x = int(self.xInput.text())
        y = int(self.yInput.text())
        primes = [n for n in range(x, y+1) if is_prime(n)]

        # Display primes in table
        self.table.setRowCount(len(primes))
        for i, prime in enumerate(primes):
            self.table.setItem(i, 0, QTableWidgetItem(str(prime)))

        # Plot prime distribution
        self.canvasDistribution.axes.clear()
        self.canvasDistribution.axes.hist(primes, bins=10, color='skyblue', edgecolor='black')
        self.canvasDistribution.axes.set_title('Prime Distribution')
        self.canvasDistribution.draw()

        # Plot gaps between consecutive primes
        gaps = [primes[i] - primes[i-1] for i in range(1, len(primes))]
        self.canvasGap.axes.clear()
        self.canvasGap.axes.plot(primes[1:], gaps, marker='o', linestyle='-', color='orange')
        self.canvasGap.axes.set_title('Gap Between Consecutive Primes')
        self.canvasGap.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PrimeFinder()
    window.show()
    sys.exit(app.exec_())
