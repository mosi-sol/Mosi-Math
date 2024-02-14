import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QFileDialog
from PyQt5.QtCore import Qt

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    p = 3
    while p * p <= n:
        if n % p == 0:
            return False
        p += 2
    return True

def find_primes(start, end):
    """Find all prime numbers in a given range using an optimized check approach."""
    primes = []
    for number in range(start, end + 1):
        if is_prime(number):
            primes.append(number)
    return primes

class PrimeFinderUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Prime Number Finder')
        self.setGeometry(100, 100, 600, 400)

        # Range inputs
        self.labelFrom = QLabel('From:', self)
        self.labelFrom.move(20, 20)
        self.inputFrom = QLineEdit(self)
        self.inputFrom.move(70, 20)
        
        self.labelTo = QLabel('To:', self)
        self.labelTo.move(250, 20)
        self.inputTo = QLineEdit(self)
        self.inputTo.move(280, 20)

        # Find button
        self.btnFind = QPushButton('Find Primes', self)
        self.btnFind.move(470, 20)
        self.btnFind.clicked.connect(self.findPrimes)

        # Results table
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setHorizontalHeaderLabels(['Prime Numbers'])
        self.tableWidget.move(20, 60)
        self.tableWidget.resize(560, 280)

        # Save functionality
        self.btnSave = QPushButton('Save Results', self)
        self.btnSave.move(440, 350)
        self.btnSave.clicked.connect(self.saveResults)

    def findPrimes(self):
        start = int(self.inputFrom.text())
        end = int(self.inputTo.text())
        primes = find_primes(start, end)
        self.displayResults(primes)

    def displayResults(self, primes):
        self.tableWidget.setRowCount(len(primes))
        for i, prime in enumerate(primes):
            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(prime)))

    def saveResults(self):
        options = QFileDialog.Options()
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File", "", "All Files (*);;Text Files (*.txt);;CSV Files (*.csv)", options=options)
        if filePath:
            content = "\n".join([self.tableWidget.item(row, 0).text() for row in range(self.tableWidget.rowCount())])
            with open(filePath, 'w') as file:
                file.write(content)

def main():
    app = QApplication(sys.argv)
    ex = PrimeFinderUI()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
