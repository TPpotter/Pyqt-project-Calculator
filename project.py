import sys
from functools import partial

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # главный экран
        self.setGeometry(200, 200, 700, 700)
        self.setWindowTitle('Решатор')
        self.setWindowIcon(QIcon('SIO.png'))

        self.simple_equation = QPushButton('Обычные уравнения', self)
        self.simple_equation.setGeometry(50, 50, 160, 160)
        self.simple_equation.setFont(QFont('Times', 11))

        self.square_equation = QPushButton('Квадратные уранения', self)
        self.square_equation.setGeometry(260, 50, 160, 160)
        self.square_equation.setFont(QFont('Times', 11))

        self.not_equation = QPushButton('Неравенства', self)
        self.not_equation.setGeometry(470, 50, 160, 160)
        self.not_equation.setFont(QFont('Times', 11))

        self.square_table = QPushButton('Таблица квадратов', self)
        self.square_table.setGeometry(50, 260, 160, 160)
        self.square_table.setFont(QFont('Times', 11))

        self.block_table = QPushButton('Таблица кубов', self)
        self.block_table.setGeometry(260, 260, 160, 160)
        self.block_table.setFont(QFont('Times', 11))

        self.sin_cos_tg = QPushButton('Син, кос, танг', self)
        self.sin_cos_tg.setGeometry(470, 260, 160, 160)
        self.sin_cos_tg.setFont(QFont('Times', 11))

        self.calculator = QPushButton('Калькулятор', self)
        self.calculator.setGeometry(50, 470, 160, 160)
        self.calculator.setFont(QFont('Times', 11))

        self.sum_of_fractions = QPushButton('Сложение дробей', self)
        self.sum_of_fractions.setGeometry(260, 470, 160, 160)
        self.sum_of_fractions.setFont(QFont('Times', 11))

        self.proportions = QPushButton('Решение пропорций', self)
        self.proportions.setGeometry(470, 470, 160, 160)
        self.proportions.setFont(QFont('Times', 11))
        #g

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
