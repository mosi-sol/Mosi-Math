# M zoo (NWNM)= (2*sin(x)) * cos(x)
# M zoo = -(1/2) * sin(2*x) + cos(y)
# M zoo = cos(y - (x - 2) * x-y) / 3
# M zoo = sin(y - (x - 2) * x-y) / 3
# M zoo = (cos(y - (x - 2) * x-y) / 3 ) - (sin(y - (x - 2) * x-y) / 3)

# roof tail = sin(x) -  cos(x) - y

# bear market = (sin(y) +  cos(y) ) * y

# mandala = sin(x*y)
# mandala = cos(x*y)* log(x-y)

import sys
import numpy as np
import sympy as sp
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit, QPushButton, QRadioButton, QButtonGroup, QLabel, QMessageBox
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from mpl_toolkits.mplot3d import Axes3D

class AlgebraicEquationVisualizer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Algebraic Equation Visualizer")
        self.setGeometry(100, 100, 800, 600)  # x, y, width, height

        self.initUI()

    def initUI(self):
        # Central Widget and Layout
        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)
        self.layout = QVBoxLayout(self.centralWidget)

        # Equation Input
        self.equationInput = QLineEdit(self)
        self.equationInput.setPlaceholderText("Enter your equation here...")
        self.layout.addWidget(self.equationInput)

        # Radio Buttons for Plot Mode
        self.radio2D = QRadioButton("2D")
        self.radio3D = QRadioButton("3D")
        self.radio2D.setChecked(True)  # Default to 2D
        self.plotModeGroup = QButtonGroup(self)
        self.plotModeGroup.addButton(self.radio2D)
        self.plotModeGroup.addButton(self.radio3D)
        self.layout.addWidget(self.radio2D)
        self.layout.addWidget(self.radio3D)

        # Plot Button
        self.plotButton = QPushButton("Plot Equation")
        self.plotButton.clicked.connect(self.plotEquation)
        self.layout.addWidget(self.plotButton)

    def plotEquation(self):
        equationInput = self.equationInput.text()
        if self.radio2D.isChecked():
            self.plot2DEquation(equationInput)
        elif self.radio3D.isChecked():
            self.plot3DEquation(equationInput)

    def plot2DEquation(self, equationInput):
        try:
            x = sp.symbols('x')
            equationParsed = sp.sympify(equationInput)
            xVals = np.linspace(-10, 10, 400)
            yVals = np.array([equationParsed.subs(x, val) for val in xVals], dtype='float')

            fig = Figure()  # Create a new Figure
            ax = fig.add_subplot(111)  # Add a subplot to the figure
            ax.plot(xVals, yVals, label=equationInput)
            ax.axhline(0, color='black', lw=1)
            ax.axvline(0, color='black', lw=1)
            ax.legend()
            ax.grid(True)

            # Embedding the plot
            self.addMatplotlibFigure(fig)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {e}")


    def plot3DEquation(self, equationInput):
        try:
            x, y = sp.symbols('x y')
            equationParsed = sp.sympify(equationInput)

            xVals, yVals = np.meshgrid(np.linspace(-10, 10, 100), np.linspace(-10, 10, 100))
            zVals = sp.lambdify((x, y), equationParsed, 'numpy')(xVals, yVals)

            fig = Figure()
            ax = fig.add_subplot(111, projection='3d')
            ax.plot_surface(xVals, yVals, zVals, cmap='viridis')

            # Embedding the plot
            self.addMatplotlibFigure(fig)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {e}")

    def addMatplotlibFigure(self, fig):
        # Remove existing figure canvas if present
        for i in reversed(range(self.layout.count())): 
            widgetToRemove = self.layout.itemAt(i).widget()
            if isinstance(widgetToRemove, FigureCanvas):
                self.layout.removeWidget(widgetToRemove)
                widgetToRemove.deleteLater()
        
        canvas = FigureCanvas(fig)
        self.layout.addWidget(canvas)
        canvas.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = AlgebraicEquationVisualizer()
    mainWin.show()
    sys.exit(app.exec_())
