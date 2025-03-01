from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QWidget, QApplication, QMainWindow, QLabel, QToolBar, QStatusBar, QLineEdit, QVBoxLayout, QPushButton
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
        layout = QVBoxLayout()

        # Chat
        self.chat_area = QLabel("I am Ready to analyse your input", self)
        self.chat_area.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(self.chat_area)

        # self.output_label = QLabel("Sentiment: None", self)
        # self.output_label.setAlignment(Qt.AlignmentFlag.AlignBottom)

        self.input_field = QLineEdit(self)
        layout.addWidget(self.input_field)

        self.ask_button = QPushButton("Ask AI", self)
        layout.addWidget(self.ask_button)

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

    def get_answer(self):
        user_input = self.input_field.text()
        sentiment_result = self.analyser.analyze(user_input)
        self.chat_area.setText(
            f"{user_input}... Sentiment analysis: {sentiment_result}")
