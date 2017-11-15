from PyQt5.QtWidgets import QApplication
import sys
from kq import KqMainWindow

app = QApplication(sys.argv)

kq = KqMainWindow()

sys.exit(app.exec_())