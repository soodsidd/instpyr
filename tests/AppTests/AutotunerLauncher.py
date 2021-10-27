from PyQt5.QtWidgets import *
import sys
from src.InstPyr.Apps.Autotuner import MainWindow


app=QApplication(sys.argv)
window=MainWindow()
window.show()
app.exec_()