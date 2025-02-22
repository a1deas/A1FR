import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QWidget, QApplication, QMainWindow, QLabel, QToolBar, QStatusBar, QLineEdit, QVBoxLayout, QPushButton
from PyQt6.QtGui import QAction, QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create Window
        self.setWindowTitle("Your AI Friend")
        self.setGeometry(100, 100, 1280, 800)

        # Create Layout
        layout = QVBoxLayout()

        # Chat
        self.chat_area = QLabel("I am Ready to answer", self)
        self.chat_area.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(self.chat_area)

        self.input_field = QLineEdit(self)
        layout.addWidget(self.input_field)

        self.ask_button = QPushButton("Ask AI", self)
        layout.addWidget(self.ask_button)

        self.ask_button.clicked.connect(self.get_answer)

        # Main layout

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Toolbar
        # toolbar = QToolBar("MyMain toolbar")
        # self.addToolBar(toolbar)

        button_action = QAction("Option 1", self)
        # toolbar.addAction(button_action)

        button_action2 = QAction("Option 2", self)
        # toolbar.addAction(button_action2)

        # Menu
        menu = self.menuBar()
        file_menu = menu.addMenu("&File")
        file_menu.addAction(button_action)
        file_menu.addAction(button_action2)

    def get_answer(self):
        user_input = self.input_field.text()
        self.output_label.setText(f"AI Answer: {user_input}")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
