# pip install PyQt5
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QScrollArea, QTextEdit, QFileDialog

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_twin_primes(start, end):
    twin_primes = []
    for i in range(start, end):
        if is_prime(i) and is_prime(i+2):
            twin_primes.append((i, i+2))
    return twin_primes

def digital_root(n):
    while n > 9:
        n = sum(int(digit) for digit in str(n))
    return n

class TwinPrimeFinder(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('Twin Prime Finder with Digital Root Check')
        self.setGeometry(100, 100, 600, 400)
        
        layout = QVBoxLayout()
        
        self.rangeLabel = QLabel('Enter range (from - to):')
        layout.addWidget(self.rangeLabel)
        
        self.fromInput = QLineEdit()
        self.toInput = QLineEdit()
        
        layout.addWidget(self.fromInput)
        layout.addWidget(self.toInput)
        
        self.findButton = QPushButton('Find Twin Primes')
        self.findButton.clicked.connect(self.on_find_click)
        layout.addWidget(self.findButton)
        
        self.resultTextEdit = QTextEdit()
        self.resultTextEdit.setReadOnly(True)
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setWidget(self.resultTextEdit)
        layout.addWidget(scroll)
        
        self.saveButton = QPushButton('Save Results')
        self.saveButton.clicked.connect(self.on_save_click)
        layout.addWidget(self.saveButton)
        
        self.setLayout(layout)
    
    def on_find_click(self):
        try:
            start = int(self.fromInput.text())
            end = int(self.toInput.text())
            twin_primes = find_twin_primes(start, end)
            results = 'Twin Primes and Digital Root Check:\n'
            for prime1, prime2 in twin_primes:
                product = prime1 * prime2
                root = digital_root(product)
                results += f"({prime1}, {prime2}), Product: {product}, Digital Root: {root}\n"
            self.resultTextEdit.setText(results)
        except ValueError:
            self.resultTextEdit.setText('Please enter valid numbers.')
    
    def on_save_click(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(self,"Save Results","","Text Files (*.txt);;All Files (*)", options=options)
        if fileName:
            with open(fileName, 'w') as file:
                file.write(self.resultTextEdit.toPlainText())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TwinPrimeFinder()
    ex.show()
    sys.exit(app.exec_())
