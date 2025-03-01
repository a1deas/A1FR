import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QWidget, QApplication, QMainWindow, QLabel, QToolBar, QStatusBar, QLineEdit, QVBoxLayout, QPushButton
from PyQt6.QtGui import QAction, QIcon

# Project Modules
from interface.main_window import MainWindow


app = QApplication(sys.argv)

window = MainWindow()
window.show()


app.exec()
