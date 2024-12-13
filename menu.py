from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5 import QtCore, QtGui
from snake_game import Snake_game


class Menu(QWidget):  # Код для меню на PyQt5
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Меню - Змейка")
        self.setGeometry(800, 380, 400, 300)

        self.layout = QVBoxLayout()

        # Заголовок игры
        self.title_label = QLabel("Змейка", self)
        self.title_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.title_label)

        # Максимальный результат
        self.max_score = self.load_max_score()
        self.score_label = QLabel(f"Максимальный результат: {self.max_score}", self)
        self.score_label.setStyleSheet("font-size: 14px")
        self.score_label.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.score_label)

        # Кнопка "Запустить игру"
        self.start_button = QPushButton("Запустить игру", self)
        self.start_button.clicked.connect(self.start_game)
        self.layout.addWidget(self.start_button)

        # Кнопка "Выход"
        self.exit_button = QPushButton("Выход", self)
        self.exit_button.clicked.connect(self.exit_game)
        self.layout.addWidget(self.exit_button)

        self.setLayout(self.layout)

    def load_max_score(self):
        try:
            with open("highscore.txt", "r") as file:
                max_score = file.readline().strip()
                return max_score if max_score else "0"
        except FileNotFoundError:
            return "0"

    def start_game(self):
        game_result = Snake_game()
        self.close()

    def exit_game(self):
        print("Выход из игры.")
        self.close()
