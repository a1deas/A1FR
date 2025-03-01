from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QWidget, QApplication, QMainWindow, QLabel, QToolBar, QStatusBar, QLineEdit, QGridLayout, QPushButton
from PyQt6.QtGui import QAction, QIcon

from model.sentiment import SentimentAnalyzer


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create Window
        self.setWindowTitle("Your AI Friend")
        self.setGeometry(100, 100, 1280, 800)

        if not hasattr(self, 'analyser'):
            self.analyser = SentimentAnalyzer()

        # Create Layout
        layout = QGridLayout()

        # Chat
        self.analyse_label = QLabel("I am Ready to analyse your input", self)
        self.analyse_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        # self.output_label = QLabel("Sentiment: None", self)
        # self.output_label.setAlignment(Qt.AlignmentFlag.AlignBottom)

        self.input_field = QLineEdit(self)

        self.ask_button = QPushButton("Ask AI", self)

        # Button Logic
        self.ask_button.clicked.connect(self.get_answer)

        # Main layout
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        button_action = QAction("Option 1", self)
        button_action2 = QAction("Option 2", self)

        # Menu
        menu = self.menuBar()
        file_menu = menu.addMenu("&File")
        file_menu.addAction(button_action)
        file_menu.addAction(button_action2)

        # Layout setup
        layout.addWidget(self.input_field,     4, 0)
        layout.addWidget(self.ask_button,      4, 1)
        layout.addWidget(self.analyse_label,   2, 0)

    def get_answer(self):
        user_input = self.input_field.text()
        sentiment_result = self.analyser.analyze(user_input)
        self.analyse_label.setText(
            f"{user_input}... Sentiment analysis: {sentiment_result}")
