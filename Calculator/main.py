import sys
from calculator import CalculatorWindow
from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)

calculator = CalculatorWindow()

sys.exit(app.exec_())




