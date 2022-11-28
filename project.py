import math
import sys
from functools import partial
from math import sqrt
from random import randint

from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton


def my_split(x):
    answer = ['']
    if '-' not in x and '+' not in x and '=' not in x:
        return [x]

    for dfghjk in x:
        if dfghjk not in '+-=':
            answer[-1] += dfghjk
        elif dfghjk in '+-=':
            answer.append('')

    return answer


def my_isdigit(num: str):
    num = num.strip()

    if not num:
        return False

    if num[0] == '-':
        if num[1:].isdigit():
            return True

    if num.isdigit():
        return True

    return False


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # главный экран
        self.setGeometry(200, 200, 700, 700)
        self.setWindowTitle('Решатор')
        self.setWindowIcon(QIcon('ICON.png'))

        self.btn_change_colours = QPushButton('обновить', self)
        self.btn_change_colours.setGeometry(620, 10, 70, 30)
        self.btn_change_colours.setFont(QFont('Times', 10))
        self.btn_change_colours.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.btn_change_colours.clicked.connect(self.change_colours)
        self.btn_change_colours.show()

        self.simple_equation = QPushButton('Обычные уравнения', self)
        self.simple_equation.setGeometry(50, 50, 160, 160)
        self.simple_equation.setFont(QFont('Times', 11))
        self.simple_equation.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.simple_equation.clicked.connect(self.equation)

        self.square_equation = QPushButton('Квадратные уранения', self)
        self.square_equation.setGeometry(260, 50, 160, 160)
        self.square_equation.setFont(QFont('Times', 11))
        self.square_equation.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.square_equation.clicked.connect(self.square_equation_)

        self.btn_not_equation = QPushButton('Неравенства', self)
        self.btn_not_equation.setGeometry(470, 50, 160, 160)
        self.btn_not_equation.setFont(QFont('Times', 11))
        self.btn_not_equation.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.btn_not_equation.clicked.connect(self.not_equation_)

        self.square_table = QPushButton('Таблица квадратов', self)
        self.square_table.setGeometry(50, 260, 160, 160)
        self.square_table.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.square_table.clicked.connect(self.show_square_table)
        self.square_table.setFont(QFont('Times', 11))

        self.block_table = QPushButton('Таблица кубов', self)
        self.block_table.setGeometry(260, 260, 160, 160)
        self.block_table.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.block_table.clicked.connect(self.show_block_table)
        self.block_table.setFont(QFont('Times', 11))

        self.sin_cos_tg = QPushButton('Син, кос, танг', self)
        self.sin_cos_tg.setGeometry(470, 260, 160, 160)
        self.sin_cos_tg.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.sin_cos_tg.clicked.connect(self.show_sin_cos_tg)
        self.sin_cos_tg.setFont(QFont('Times', 11))

        self.calculator = QPushButton('Калькулятор', self)
        self.calculator.setGeometry(50, 470, 160, 160)
        self.calculator.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.calculator.clicked.connect(self.simple_calculator)
        self.calculator.setFont(QFont('Times', 11))

        self.sum_of_fractions = QPushButton('Сложение дробей', self)
        self.sum_of_fractions.setGeometry(260, 470, 160, 160)
        self.sum_of_fractions.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.sum_of_fractions.clicked.connect(self.show_sum_fractions)
        self.sum_of_fractions.setFont(QFont('Times', 11))

        self.proportions = QPushButton('Решение пропорций', self)
        self.proportions.setGeometry(470, 470, 160, 160)
        self.proportions.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.proportions.clicked.connect(self.show_proportions)
        self.proportions.setFont(QFont('Times', 11))

    def hiding_main(self):
        self.simple_equation.hide()
        self.square_equation.hide()
        self.btn_not_equation.hide()
        self.square_table.hide()
        self.block_table.hide()
        self.sin_cos_tg.hide()
        self.calculator.hide()
        self.sum_of_fractions.hide()
        self.proportions.hide()
        self.btn_change_colours.hide()

    def eq_work(self, eq_data):
        if eq_data.isdigit() and \
                (not self.line_of_eq.text() or self.line_of_eq.text()[-1] != 'x'):
            self.line_of_eq.setText(self.line_of_eq.text() + eq_data)

        elif eq_data == 'x' and (not self.line_of_eq.text() or self.line_of_eq.text()[-1] != 'x'):
            self.line_of_eq.setText(self.line_of_eq.text() + eq_data)

        elif (eq_data == '+' or eq_data == '-') and \
                (self.line_of_eq.text()[-1] == '+' or self.line_of_eq.text()[-1] == '-') and \
                self.line_of_eq.text()[-1] != '.' and self.line_of_eq.text()[-1] != '=':
            self.line_of_eq.setText(self.line_of_eq.text()[:-1] + eq_data)

        elif (eq_data == '+' or eq_data == '-') and self.line_of_eq.text()[-1] != '.' and \
                self.line_of_eq.text()[-1] != '=':
            self.line_of_eq.setText(self.line_of_eq.text() + eq_data)

        elif eq_data == '=' and '=' not in self.line_of_eq.text():
            self.line_of_eq.setText(self.line_of_eq.text() + eq_data)

        elif eq_data == '.' and self.line_of_eq.text() and \
                '.' not in my_split(self.line_of_eq.text())[-1] and \
                'x' not in self.line_of_eq.text()[-1]:
            self.line_of_eq.setText(self.line_of_eq.text() + eq_data)

        elif eq_data == 'del':
            self.line_of_eq.setText(self.line_of_eq.text()[:-1])

        elif eq_data == 'del_all':
            self.line_of_eq.setText('')

    def eq_solve_answer(self):
        if not self.line_of_eq.text():
            self.eq_answer.setText('Уравнение отсутствует')
            return

        if '=' not in self.line_of_eq.text() or not self.line_of_eq.text().split('=')[-1]:
            self.eq_answer.setText('это не уравнение')
            return

        if 'x' not in self.line_of_eq.text():
            eq_lines_tr_fl = self.line_of_eq.text().split('=')
            if eval(eq_lines_tr_fl[0]) == eval(eq_lines_tr_fl[1]):
                self.eq_answer.setText('Правда')
                return
            self.eq_answer.setText('Ложь')
            return

        eq_x = []
        eq_num = []
        eq_info = ''
        n = -1

        for eq_eq in self.line_of_eq.text().split('='):
            n += 1

            for eqq in eq_eq:
                if eqq == '+' and eq_info != '':
                    if n == 0:
                        eq_num.append(str(-1 * float(eq_info)))

                    if n == 1:
                        eq_num.append(eq_info)

                    eq_info = ''

                elif eqq == '-':
                    if eq_info:
                        if n == 0:
                            eq_num.append(str(-1 * float(eq_info)))

                        if n == 1:
                            eq_num.append(eq_info)

                        eq_info = ''

                        continue

                    eq_info = '-'

                elif eqq == 'x' and eq_info != '':
                    if n == 0 and eq_info != '-':
                        eq_x.append(eq_info)

                    if n == 0 and eq_info == '-':
                        eq_x.append('-1')

                    elif n == 1 and eq_info != '-':
                        eq_x.append(str(-1 * float(eq_info)))

                    elif n == 1 and eq_info == '-':
                        eq_x.append('1')

                    eq_info = ''

                elif eqq == 'x' and eq_info == '':
                    if n == 0:
                        eq_x.append('1')

                    elif n == 1:
                        eq_x.append('-1')
                    eq_info = ''

                elif eqq.isdigit() or eqq == '.':
                    eq_info += eqq

            if eq_info:
                if n == 0:
                    eq_num.append(str(-1 * float(eq_info)))

                elif n == 1:
                    eq_num.append(eq_info)

                eq_info = ''

        if not eq_num:
            self.eq_answer.setText('x = любое число')
            return

        eqq_num = sum([float(eqq) for eqq in eq_num])
        eqq_x = sum([float(eqqq) for eqqq in eq_x])

        if eqq_x != 0:
            answer = eqq_num / eqq_x

            self.eq_answer.setText(f'x = {str(answer)}')

        elif eqq_x == 0:
            if eqq_num == 0:
                self.eq_answer.setText('Правда')

            elif eqq_num != 0:
                self.eq_answer.setText('Ложь')

    def equation(self):
        self.hiding_main()

        self.setGeometry(100, 100, 1000, 900)

        self.equation_back = QPushButton('На главный экран', self)
        self.equation_back.setGeometry(770, 10, 200, 50)
        self.equation_back.setFont(QFont('Times', 12))
        self.equation_back.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.equation_back.show()
        self.equation_back.clicked.connect(partial(self.back_to_main, 'eq'))

        self.line_of_eq = QLineEdit(self)
        self.line_of_eq.setReadOnly(True)
        self.line_of_eq.setGeometry(10, 10, 750, 136)
        self.line_of_eq.setFont(QFont('Times', 20))
        self.line_of_eq.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.line_of_eq.show()

        self.eq_answer = QLineEdit(self)
        self.eq_answer.setReadOnly(True)
        self.eq_answer.setGeometry(10, 198, 750, 136)
        self.eq_answer.setFont(QFont('Times', 20))
        self.eq_answer.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.eq_answer.show()

        self.eq_btn_del = QPushButton('del', self)
        self.eq_btn_del.setFont(QFont('Times', 50))
        self.eq_btn_del.setGeometry(770, 65, 100, 100)
        self.eq_btn_del.clicked.connect(partial(self.eq_work, 'del'))
        self.eq_btn_del.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.eq_btn_del.show()

        self.eq_btn_del_all = QPushButton('del all', self)
        self.eq_btn_del_all.setFont(QFont('Times', 30))
        self.eq_btn_del_all.setGeometry(880, 65, 115, 100)
        self.eq_btn_del_all.clicked.connect(partial(self.eq_work, 'del_all'))
        self.eq_btn_del_all.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.eq_btn_del_all.show()

        self.eq_btn_solve = QPushButton('решить', self)
        self.eq_btn_solve.setGeometry(770, 196, 200, 136)
        self.eq_btn_solve.setFont(QFont('Times', 40))
        self.eq_btn_solve.clicked.connect(self.eq_solve_answer)
        self.eq_btn_solve.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.eq_btn_solve.show()

        self.eq_btn_1 = QPushButton('1', self)
        self.eq_btn_1.setFont(QFont('Times', 100))
        self.eq_btn_1.setGeometry(10, 382, 136, 136)
        self.eq_btn_1.clicked.connect(partial(self.eq_work, '1'))
        self.eq_btn_1.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.eq_btn_1.show()

        self.eq_btn_2 = QPushButton('2', self)
        self.eq_btn_2.setFont(QFont('Times', 100))
        self.eq_btn_2.setGeometry(196, 382, 136, 136)
        self.eq_btn_2.clicked.connect(partial(self.eq_work, '2'))
        self.eq_btn_2.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.eq_btn_2.show()

        self.eq_btn_3 = QPushButton('3', self)
        self.eq_btn_3.setFont(QFont('Times', 100))
        self.eq_btn_3.setGeometry(382, 382, 136, 136)
        self.eq_btn_3.clicked.connect(partial(self.eq_work, '3'))
        self.eq_btn_3.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.eq_btn_3.show()

        self.eq_btn_0 = QPushButton('0', self)
        self.eq_btn_0.setFont(QFont('Times', 100))
        self.eq_btn_0.setGeometry(568, 382, 136, 136)
        self.eq_btn_0.clicked.connect(partial(self.eq_work, '0'))
        self.eq_btn_0.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.eq_btn_0.show()

        self.eq_btn_4 = QPushButton('4', self)
        self.eq_btn_4.setFont(QFont('Times', 100))
        self.eq_btn_4.setGeometry(10, 568, 136, 136)
        self.eq_btn_4.clicked.connect(partial(self.eq_work, '4'))
        self.eq_btn_4.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.eq_btn_4.show()

        self.eq_btn_5 = QPushButton('5', self)
        self.eq_btn_5.setFont(QFont('Times', 100))
        self.eq_btn_5.setGeometry(196, 568, 136, 136)
        self.eq_btn_5.clicked.connect(partial(self.eq_work, '5'))
        self.eq_btn_5.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.eq_btn_5.show()

        self.eq_btn_6 = QPushButton('6', self)
        self.eq_btn_6.setFont(QFont('Times', 100))
        self.eq_btn_6.setGeometry(382, 568, 136, 136)
        self.eq_btn_6.clicked.connect(partial(self.eq_work, '6'))
        self.eq_btn_6.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.eq_btn_6.show()

        self.eq_btn_7 = QPushButton('7', self)
        self.eq_btn_7.setFont(QFont('Times', 100))
        self.eq_btn_7.setGeometry(10, 754, 136, 136)
        self.eq_btn_7.clicked.connect(partial(self.eq_work, '7'))
        self.eq_btn_7.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.eq_btn_7.show()

        self.eq_btn_8 = QPushButton('8', self)
        self.eq_btn_8.setFont(QFont('Times', 100))
        self.eq_btn_8.setGeometry(196, 754, 136, 136)
        self.eq_btn_8.clicked.connect(partial(self.eq_work, '8'))
        self.eq_btn_8.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.eq_btn_8.show()

        self.eq_btn_9 = QPushButton('9', self)
        self.eq_btn_9.setFont(QFont('Times', 100))
        self.eq_btn_9.setGeometry(382, 754, 136, 136)
        self.eq_btn_9.clicked.connect(partial(self.eq_work, '9'))
        self.eq_btn_9.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.eq_btn_9.show()

        self.eq_btn_plus = QPushButton('+', self)
        self.eq_btn_plus.setFont(QFont('Times', 100))
        self.eq_btn_plus.setGeometry(568, 568, 136, 136)
        self.eq_btn_plus.clicked.connect(partial(self.eq_work, '+'))
        self.eq_btn_plus.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.eq_btn_plus.show()

        self.eq_btn_minus = QPushButton('-', self)
        self.eq_btn_minus.setFont(QFont('Times', 100))
        self.eq_btn_minus.setGeometry(568, 754, 136, 136)
        self.eq_btn_minus.clicked.connect(partial(self.eq_work, '-'))
        self.eq_btn_minus.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.eq_btn_minus.show()

        self.eq_btn_dot = QPushButton('●', self)
        self.eq_btn_dot.setFont(QFont('Times', 100))
        self.eq_btn_dot.setGeometry(754, 382, 136, 136)
        self.eq_btn_dot.clicked.connect(partial(self.eq_work, '.'))
        self.eq_btn_dot.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.eq_btn_dot.show()

        self.eq_btn_x = QPushButton('x', self)
        self.eq_btn_x.setFont(QFont('Times', 100))
        self.eq_btn_x.setGeometry(754, 568, 136, 136)
        self.eq_btn_x.clicked.connect(partial(self.eq_work, 'x'))
        self.eq_btn_x.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.eq_btn_x.show()

        self.eq_btn_eq = QPushButton('=', self)
        self.eq_btn_eq.setFont(QFont('Times', 100))
        self.eq_btn_eq.setGeometry(754, 754, 136, 136)
        self.eq_btn_eq.clicked.connect(partial(self.eq_work, '='))
        self.eq_btn_eq.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.eq_btn_eq.show()

    def square_coeff(self, sq_coeff_info):
        self.sq_coeff = sq_coeff_info

    def square_nums_work(self, sq_num):
        if self.sq_coeff == 'a':
            self.sq_line_a.setText(self.sq_line_a.text() + sq_num)

        elif self.sq_coeff == 'b':
            self.sq_line_b.setText(self.sq_line_b.text() + sq_num)

        elif self.sq_coeff == 'c':
            self.sq_line_c.setText(self.sq_line_c.text() + sq_num)

    def sq_del(self):
        if self.sq_coeff == 'a':
            self.sq_line_a.setText(self.sq_line_a.text()[:-1])

        elif self.sq_coeff == 'b':
            self.sq_line_b.setText(self.sq_line_b.text()[:-1])

        elif self.sq_coeff == 'c':
            self.sq_line_c.setText(self.sq_line_c.text()[:-1])

    def sq_del_all(self):
        self.sq_line_a.setText('')
        self.sq_line_b.setText('')
        self.sq_line_c.setText('')

    def sq_work(self):
        if not self.sq_line_a.text():
            self.sq_line_d.setText('нет "a"')
            self.sq_line_sqrt_d.setText('нет "a"')
            self.sq_x1.setText('нет "a"')
            self.sq_x2.setText('нет "a"')

        elif not self.sq_line_b.text():
            self.sq_line_d.setText('нет "b"')
            self.sq_line_sqrt_d.setText('нет "b"')
            self.sq_x1.setText('нет "b"')
            self.sq_x2.setText('нет "b"')

        elif not self.sq_line_c.text():
            self.sq_line_d.setText('нет "c"')
            self.sq_line_sqrt_d.setText('нет "c"')
            self.sq_x1.setText('нет "c"')
            self.sq_x2.setText('нет "c"')

        else:
            a = int(self.sq_line_a.text())
            b = int(self.sq_line_b.text())
            c = int(self.sq_line_c.text())

            if a != 0:
                d = b ** 2 - 4 * a * c
                self.sq_line_d.setText('D = ' + str(d))

                if d < 0:
                    self.sq_line_sqrt_d.setText('D < 0')
                    self.sq_x1.setText('нет корней')
                    self.sq_x2.setText('нет корней')

                elif d >= 0:
                    self.sq_line_sqrt_d.setText('√D = ' + str(round(sqrt(d), 4)))
                    self.sq_x1.setText(f'x1 = {round((-1 * b + sqrt(d)) / (2 * a), 4)}')
                    self.sq_x2.setText(f'x2 = {round((-1 * b - sqrt(d)) / (2 * a), 4)}')

            elif a == 0 and c != 0:
                self.sq_x1.setText(f'x1 = {b / (-1 * c)}')
                self.sq_x2.setText(f'x2 = {b / (-1 * c)}')
            elif a == 0:
                self.sq_x1.setText(f'x1 = {b / (-1 * c)}')
                self.sq_x2.setText(f'x2 = {b / (-1 * c)}')

            elif a == 0 and c == 0:
                self.sq_x1.setText('нет корней')
                self.sq_x2.setText('нет корней')

    def sq_plus_minus(self):
        if self.sq_coeff == 'a' and self.sq_line_a.text() and self.sq_line_a.text()[0] != '-':
            self.sq_line_a.setText('-' + self.sq_line_a.text())

        elif self.sq_coeff == 'a' and self.sq_line_a.text() and self.sq_line_a.text()[0] == '-':
            self.sq_line_a.setText(self.sq_line_a.text()[1:])

        elif self.sq_coeff == 'b' and self.sq_line_b.text() and self.sq_line_b.text()[0] != '-':
            self.sq_line_b.setText('-' + self.sq_line_b.text())

        elif self.sq_coeff == 'b' and self.sq_line_b.text() and self.sq_line_b.text()[0] == '-':
            self.sq_line_b.setText(self.sq_line_b.text()[1:])

        elif self.sq_coeff == 'c' and self.sq_line_c.text() and self.sq_line_c.text()[0] != '-':
            self.sq_line_c.setText('-' + self.sq_line_c.text())

        elif self.sq_coeff == 'c' and self.sq_line_c.text() and self.sq_line_c.text()[0] == '-':
            self.sq_line_c.setText(self.sq_line_c.text()[1:])

    def square_equation_(self):
        self.hiding_main()

        self.sq_coeff = 'a'

        self.setGeometry(90, 90, 1020, 940)

        self.sq_example = QLineEdit(self)
        self.sq_example.setReadOnly(True)
        self.sq_example.setGeometry(10, 10, 630, 100)
        self.sq_example.setText('ax² + bx + c = 0')
        self.sq_example.setFont(QFont('Times', 60))
        self.sq_example.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.sq_example.show()

        self.sq_btn_back = QPushButton('на главный экран', self)
        self.sq_btn_back.setGeometry(680, 10, 330, 100)
        self.sq_btn_back.setFont(QFont('Times', 27))
        self.sq_btn_back.clicked.connect(partial(self.back_to_main, 'sq_eq'))
        self.sq_btn_back.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.sq_btn_back.show()

        self.sq_line_a = QLineEdit(self)
        self.sq_line_a.setReadOnly(True)
        self.sq_line_a.setGeometry(10, 130, 300, 100)
        self.sq_line_a.setFont(QFont('Times', 50))
        self.sq_line_a.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.sq_line_a.show()

        self.sq_line_b = QLineEdit(self)
        self.sq_line_b.setReadOnly(True)
        self.sq_line_b.setGeometry(360, 130, 300, 100)
        self.sq_line_b.setFont(QFont('Times', 50))
        self.sq_line_b.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.sq_line_b.show()

        self.sq_line_c = QLineEdit(self)
        self.sq_line_c.setReadOnly(True)
        self.sq_line_c.setGeometry(710, 130, 300, 100)
        self.sq_line_c.setFont(QFont('Times', 50))
        self.sq_line_c.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.sq_line_c.show()

        self.sq_txt_a = QPushButton('a', self)
        self.sq_txt_a.setFont(QFont('Times', 35))
        self.sq_txt_a.setGeometry(10, 230, 300, 50)
        self.sq_txt_a.clicked.connect(partial(self.square_coeff, 'a'))
        self.sq_txt_a.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.sq_txt_a.show()

        self.sq_txt_b = QPushButton('b', self)
        self.sq_txt_b.setFont(QFont('Times', 35))
        self.sq_txt_b.setGeometry(360, 230, 300, 50)
        self.sq_txt_b.clicked.connect(partial(self.square_coeff, 'b'))
        self.sq_txt_b.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.sq_txt_b.show()

        self.sq_txt_c = QPushButton('c', self)
        self.sq_txt_c.setFont(QFont('Times', 35))
        self.sq_txt_c.setGeometry(710, 230, 300, 50)
        self.sq_txt_c.clicked.connect(partial(self.square_coeff, 'c'))
        self.sq_txt_c.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.sq_txt_c.show()

        self.sq_btn_1 = QPushButton('1', self)
        self.sq_btn_1.setFont(QFont('Times', 90))
        self.sq_btn_1.setGeometry(10, 310, 125, 100)
        self.sq_btn_1.clicked.connect(partial(self.square_nums_work, '1'))
        self.sq_btn_1.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.sq_btn_1.show()

        self.sq_btn_2 = QPushButton('2', self)
        self.sq_btn_2.setFont(QFont('Times', 80))
        self.sq_btn_2.setGeometry(185, 310, 125, 100)
        self.sq_btn_2.clicked.connect(partial(self.square_nums_work, '2'))
        self.sq_btn_2.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.sq_btn_2.show()

        self.sq_btn_3 = QPushButton('3', self)
        self.sq_btn_3.setFont(QFont('Times', 80))
        self.sq_btn_3.setGeometry(360, 310, 125, 100)
        self.sq_btn_3.clicked.connect(partial(self.square_nums_work, '3'))
        self.sq_btn_3.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.sq_btn_3.show()

        self.sq_btn_4 = QPushButton('4', self)
        self.sq_btn_4.setFont(QFont('Times', 80))
        self.sq_btn_4.setGeometry(535, 310, 125, 100)
        self.sq_btn_4.clicked.connect(partial(self.square_nums_work, '4'))
        self.sq_btn_4.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.sq_btn_4.show()

        self.sq_btn_5 = QPushButton('5', self)
        self.sq_btn_5.setFont(QFont('Times', 80))
        self.sq_btn_5.setGeometry(710, 310, 125, 100)
        self.sq_btn_5.clicked.connect(partial(self.square_nums_work, '5'))
        self.sq_btn_5.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.sq_btn_5.show()

        self.sq_btn_del = QPushButton('del', self)
        self.sq_btn_del.setFont(QFont('Times', 60))
        self.sq_btn_del.setGeometry(885, 310, 125, 100)
        self.sq_btn_del.clicked.connect(self.sq_del)
        self.sq_btn_del.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.sq_btn_del.show()

        self.sq_btn_6 = QPushButton('6', self)
        self.sq_btn_6.setFont(QFont('Times', 80))
        self.sq_btn_6.setGeometry(10, 440, 125, 100)
        self.sq_btn_6.clicked.connect(partial(self.square_nums_work, '6'))
        self.sq_btn_6.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.sq_btn_6.show()

        self.sq_btn_7 = QPushButton('7', self)
        self.sq_btn_7.setFont(QFont('Times', 80))
        self.sq_btn_7.setGeometry(185, 440, 125, 100)
        self.sq_btn_7.clicked.connect(partial(self.square_nums_work, '7'))
        self.sq_btn_7.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.sq_btn_7.show()

        self.sq_btn_8 = QPushButton('8', self)
        self.sq_btn_8.setFont(QFont('Times', 80))
        self.sq_btn_8.setGeometry(360, 440, 125, 100)
        self.sq_btn_8.clicked.connect(partial(self.square_nums_work, '8'))
        self.sq_btn_8.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.sq_btn_8.show()

        self.sq_btn_9 = QPushButton('9', self)
        self.sq_btn_9.setFont(QFont('Times', 80))
        self.sq_btn_9.setGeometry(535, 440, 125, 100)
        self.sq_btn_9.clicked.connect(partial(self.square_nums_work, '9'))
        self.sq_btn_9.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.sq_btn_9.show()

        self.sq_btn_0 = QPushButton('0', self)
        self.sq_btn_0.setFont(QFont('Times', 80))
        self.sq_btn_0.setGeometry(710, 440, 125, 100)
        self.sq_btn_0.clicked.connect(partial(self.square_nums_work, '0'))
        self.sq_btn_0.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.sq_btn_0.show()

        self.sq_btn_del_all = QPushButton('del all', self)
        self.sq_btn_del_all.setFont(QFont('Times', 30))
        self.sq_btn_del_all.setGeometry(885, 440, 125, 100)
        self.sq_btn_del_all.clicked.connect(self.sq_del_all)
        self.sq_btn_del_all.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.sq_btn_del_all.show()

        self.sq_btn_solve = QPushButton('решить', self)
        self.sq_btn_solve.setFont(QFont('Times', 60))
        self.sq_btn_solve.setGeometry(10, 570, 825, 100)
        self.sq_btn_solve.clicked.connect(self.sq_work)
        self.sq_btn_solve.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.sq_btn_solve.show()

        self.sq_btn_plus_minus = QPushButton('±', self)
        self.sq_btn_plus_minus.setFont(QFont('Times', 80))
        self.sq_btn_plus_minus.setGeometry(885, 570, 125, 100)
        self.sq_btn_plus_minus.clicked.connect(self.sq_plus_minus)
        self.sq_btn_plus_minus.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.sq_btn_plus_minus.show()

        self.sq_line_d = QLineEdit(self)
        self.sq_line_d.setReadOnly(True)
        self.sq_line_d.setGeometry(10, 700, 475, 100)
        self.sq_line_d.setText('D = ')
        self.sq_line_d.setFont(QFont('Times', 50))
        self.sq_line_d.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.sq_line_d.show()

        self.sq_line_sqrt_d = QLineEdit(self)
        self.sq_line_sqrt_d.setReadOnly(True)
        self.sq_line_sqrt_d.setGeometry(535, 700, 475, 100)
        self.sq_line_sqrt_d.setText('√D = ')
        self.sq_line_sqrt_d.setFont(QFont('Times', 50))
        self.sq_line_sqrt_d.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.sq_line_sqrt_d.show()

        self.sq_x1 = QLineEdit(self)
        self.sq_x1.setReadOnly(True)
        self.sq_x1.setGeometry(10, 830, 475, 100)
        self.sq_x1.setText('x1 = ')
        self.sq_x1.setFont(QFont('Times', 50))
        self.sq_x1.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.sq_x1.show()

        self.sq_x2 = QLineEdit(self)
        self.sq_x2.setReadOnly(True)
        self.sq_x2.setGeometry(535, 830, 475, 100)
        self.sq_x2.setText('x2 = ')
        self.sq_x2.setFont(QFont('Times', 50))
        self.sq_x2.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.sq_x2.show()

    def neq_work(self, neq_data):
        if neq_data.isdigit() and \
                (not self.neq_line_of_neq.text() or self.neq_line_of_neq.text()[-1] != 'x'):
            self.neq_line_of_neq.setText(self.neq_line_of_neq.text() + neq_data)

        elif neq_data == 'del' and self.neq_line_of_neq.text():
            self.neq_line_of_neq.setText(self.neq_line_of_neq.text()[:-1])

        elif neq_data == 'del all':
            self.neq_line_of_neq.setText('')

        elif neq_data == 'x' and (not self.neq_line_of_neq.text() or self.neq_line_of_neq.text()[-1] != 'x'):
            self.neq_line_of_neq.setText(self.neq_line_of_neq.text() + neq_data)

        elif (neq_data == '+' or neq_data == '-') and \
                (self.neq_line_of_neq.text()[-1] == '+' or self.neq_line_of_neq.text()[-1] == '-') and \
                self.neq_line_of_neq.text()[-1] not in ['.', '>', '<', '=']:
            self.neq_line_of_neq.setText(self.neq_line_of_neq.text()[:-1] + neq_data)

        elif (neq_data == '+' or neq_data == '-') and self.neq_line_of_neq.text()[-1] not in ['.', '>', '<', '=']:
            self.neq_line_of_neq.setText(self.neq_line_of_neq.text() + neq_data)

        elif neq_data in ['>', '<', '>=', '<='] and \
                '>' not in self.neq_line_of_neq.text() and \
                '<' not in self.neq_line_of_neq.text() and \
                '⩾' not in self.neq_line_of_neq.text() and \
                '⩽' not in self.neq_line_of_neq.text():
            if neq_data in ['<', '>']:
                self.neq_line_of_neq.setText(self.neq_line_of_neq.text() + neq_data)

            elif neq_data == '>=':
                self.neq_line_of_neq.setText(self.neq_line_of_neq.text() + '⩾')

            elif neq_data == '<=':
                self.neq_line_of_neq.setText(self.neq_line_of_neq.text() + '⩽')

        elif neq_data == '.' and self.neq_line_of_neq.text() and \
                '.' not in my_split(self.neq_line_of_neq.text())[-1] and \
                'x' not in self.neq_line_of_neq.text()[-1]:
            self.neq_line_of_neq.setText(self.neq_line_of_neq.text() + neq_data)

    def neq_solve(self):
        if not '>' in self.neq_line_of_neq.text() and not '<' in self.neq_line_of_neq.text() and not \
                '⩾' in self.neq_line_of_neq.text() and not '⩽' in self.neq_line_of_neq.text():
            self.neq_line_answer.setText('это не неравенство')
            return
        neq_symbol = list(filter(lambda x: x in ['>', '<', '⩾', '⩽'], self.neq_line_of_neq.text()))[0]

        neq_x = []
        neq_num = []
        neq_info = ''

        n = -1

        for neq in self.neq_line_of_neq.text().split(neq_symbol):
            n += 1

            for neqq in neq:
                if neqq == '+' and neq_info != '':
                    if n == 0:
                        neq_num.append(str(-1 * float(neq_info)))

                    if n == 1:
                        neq_num.append(neq_info)

                    neq_info = ''

                elif neqq == '-':
                    if neq_info:
                        if n == 0:
                            neq_num.append(str(-1 * float(neq_info)))

                        if n == 1:
                            neq_num.append(neq_info)

                        neq_info = '-'

                        continue

                    neq_info = '-'

                elif neqq == 'x' and neq_info != '':
                    if n == 0 and neq_info != '-':
                        neq_x.append(neq_info)

                    if n == 0 and neq_info == '-':
                        neq_x.append('-1')

                    elif n == 1 and neq_info != '-':
                        neq_x.append(str(-1 * float(neq_info)))

                    elif n == 1 and neq_info == '-':
                        neq_x.append('1')

                    neq_info = ''

                elif neqq == 'x' and neq_info == '':
                    if n == 0:
                        neq_x.append('1')

                    elif n == 1:
                        neq_x.append('-1')

                    neq_info = ''

                elif neqq.isdigit() or neqq == '.':
                    neq_info += neqq

            if neq_info:
                if n == 0:
                    neq_num.append(str(-1 * float(neq_info)))

                elif n == 1:
                    neq_num.append(neq_info)

                neq_info = ''

        if not neq_num:
            self.neq_line_answer.setText('x = нет корней')
            return

        neq_sum_x = sum([float(x) for x in neq_x])
        neq_sum_num = sum([float(x) for x in neq_num])

        if neq_sum_x == 0:
            if neq_symbol == '>':
                if neq_sum_num < 0:
                    self.neq_line_answer.setText('Правда')

                elif neq_sum_num >= 0:
                    self.neq_line_answer.setText('Ложь')

            elif neq_symbol == '<':
                if neq_sum_num > 0:
                    self.neq_line_answer.setText('Правда')

                elif neq_sum_num <= 0:
                    self.neq_line_answer.setText('Ложь')

            elif neq_symbol == '⩾':
                if neq_sum_num <= 0:
                    self.neq_line_answer.setText('Правда')

                elif neq_sum_num > 0:
                    self.neq_line_answer.setText('Ложь')

            elif neq_symbol == '⩽':
                if neq_sum_num >= 0:
                    self.neq_line_answer.setText('Правда')

                elif neq_sum_num < 0:
                    self.neq_line_answer.setText('Ложь')

            return

        elif neq_sum_x < 0:
            if neq_symbol == '>':
                neq_symbol = '<'

            elif neq_symbol == '<':
                neq_symbol = '>'

            elif neq_symbol == '⩾':
                neq_symbol = '⩽'

            elif neq_symbol == '⩽':
                neq_symbol = '⩾'

        self.neq_line_answer.setText(f'x {neq_symbol} {round(neq_sum_num / neq_sum_x, 4)}')

    def not_equation_(self):
        self.hiding_main()

        self.setGeometry(100, 100, 1020, 900)

        self.neq_line_of_neq = QLineEdit(self)
        self.neq_line_of_neq.setReadOnly(True)
        self.neq_line_of_neq.setFont(QFont('Times', 20))
        self.neq_line_of_neq.setGeometry(10, 10, 765, 136)
        self.neq_line_of_neq.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.neq_line_of_neq.show()

        self.neq_btn_back_to_main = QPushButton('на главный экран', self)
        self.neq_btn_back_to_main.setGeometry(785, 10, 225, 53)
        self.neq_btn_back_to_main.setFont(QFont('Times', 20))
        self.neq_btn_back_to_main.clicked.connect(partial(self.back_to_main, 'neq'))
        self.neq_btn_back_to_main.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.neq_btn_back_to_main.show()

        self.neq_btn_del = QPushButton('del', self)
        self.neq_btn_del.setGeometry(785, 83, 105, 63)
        self.neq_btn_del.setFont(QFont('Times', 40))
        self.neq_btn_del.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.neq_btn_del.clicked.connect(partial(self.neq_work, 'del'))
        self.neq_btn_del.show()

        self.neq_btn_del_all = QPushButton('del all', self)
        self.neq_btn_del_all.setFont(QFont('Times', 27))
        self.neq_btn_del_all.setGeometry(910, 83, 100, 63)
        self.neq_btn_del_all.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.neq_btn_del_all.clicked.connect(partial(self.neq_work, 'del all'))
        self.neq_btn_del_all.show()

        self.neq_line_answer = QLineEdit(self)
        self.neq_line_answer.setReadOnly(True)
        self.neq_line_answer.setGeometry(10, 196, 765, 136)
        self.neq_line_answer.setFont(QFont('Times', 50))
        self.neq_line_answer.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.neq_line_answer.show()

        self.neq_btn_solve = QPushButton('решить', self)
        self.neq_btn_solve.setFont(QFont('Times', 48))
        self.neq_btn_solve.setGeometry(785, 196, 225, 136)
        self.neq_btn_solve.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.neq_btn_solve.clicked.connect(self.neq_solve)
        self.neq_btn_solve.show()

        self.neq_btn_1 = QPushButton('1', self)
        self.neq_btn_1.setFont(QFont('Times', 100))
        self.neq_btn_1.setGeometry(10, 382, 125, 136)
        self.neq_btn_1.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.neq_btn_1.clicked.connect(partial(self.neq_work, '1'))
        self.neq_btn_1.show()

        self.neq_btn_2 = QPushButton('2', self)
        self.neq_btn_2.setFont(QFont('Times', 100))
        self.neq_btn_2.setGeometry(185, 382, 125, 136)
        self.neq_btn_2.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.neq_btn_2.clicked.connect(partial(self.neq_work, '2'))
        self.neq_btn_2.show()

        self.neq_btn_3 = QPushButton('3', self)
        self.neq_btn_3.setFont(QFont('Times', 100))
        self.neq_btn_3.setGeometry(360, 382, 125, 136)
        self.neq_btn_3.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.neq_btn_3.clicked.connect(partial(self.neq_work, '3'))
        self.neq_btn_3.show()

        self.neq_btn_0 = QPushButton('0', self)
        self.neq_btn_0.setFont(QFont('Times', 100))
        self.neq_btn_0.setGeometry(535, 382, 125, 136)
        self.neq_btn_0.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.neq_btn_0.clicked.connect(partial(self.neq_work, '0'))
        self.neq_btn_0.show()

        self.neq_btn_dot = QPushButton('●', self)
        self.neq_btn_dot.setFont(QFont('Times', 100))
        self.neq_btn_dot.setGeometry(710, 382, 125, 136)
        self.neq_btn_dot.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.neq_btn_dot.clicked.connect(partial(self.neq_work, '.'))
        self.neq_btn_dot.show()

        self.neq_btn_less = QPushButton('<', self)
        self.neq_btn_less.setFont(QFont('Times', 100))
        self.neq_btn_less.setGeometry(885, 382, 125, 136)
        self.neq_btn_less.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.neq_btn_less.clicked.connect(partial(self.neq_work, '<'))
        self.neq_btn_less.show()

        self.neq_btn_4 = QPushButton('4', self)
        self.neq_btn_4.setFont(QFont('Times', 100))
        self.neq_btn_4.setGeometry(10, 568, 125, 136)
        self.neq_btn_4.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.neq_btn_4.clicked.connect(partial(self.neq_work, '4'))
        self.neq_btn_4.show()

        self.neq_btn_5 = QPushButton('5', self)
        self.neq_btn_5.setFont(QFont('Times', 100))
        self.neq_btn_5.setGeometry(185, 568, 125, 136)
        self.neq_btn_5.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.neq_btn_5.clicked.connect(partial(self.neq_work, '5'))
        self.neq_btn_5.show()

        self.neq_btn_6 = QPushButton('6', self)
        self.neq_btn_6.setFont(QFont('Times', 100))
        self.neq_btn_6.setGeometry(360, 568, 125, 136)
        self.neq_btn_6.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.neq_btn_6.clicked.connect(partial(self.neq_work, '6'))
        self.neq_btn_6.show()

        self.neq_btn_plus = QPushButton('+', self)
        self.neq_btn_plus.setFont(QFont('Times', 100))
        self.neq_btn_plus.setGeometry(535, 568, 125, 136)
        self.neq_btn_plus.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.neq_btn_plus.clicked.connect(partial(self.neq_work, '+'))
        self.neq_btn_plus.show()

        self.neq_btn_x = QPushButton('x', self)
        self.neq_btn_x.setFont(QFont('Times', 100))
        self.neq_btn_x.setGeometry(710, 568, 125, 136)
        self.neq_btn_x.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.neq_btn_x.clicked.connect(partial(self.neq_work, 'x'))
        self.neq_btn_x.show()

        self.neq_btn_more_eq = QPushButton('⩾', self)
        self.neq_btn_more_eq.setFont(QFont('Times', 100))
        self.neq_btn_more_eq.setGeometry(885, 568, 125, 136)
        self.neq_btn_more_eq.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.neq_btn_more_eq.clicked.connect(partial(self.neq_work, '>='))
        self.neq_btn_more_eq.show()

        self.neq_btn_7 = QPushButton('7', self)
        self.neq_btn_7.setFont(QFont('Times', 100))
        self.neq_btn_7.setGeometry(10, 754, 125, 136)
        self.neq_btn_7.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.neq_btn_7.clicked.connect(partial(self.neq_work, '7'))
        self.neq_btn_7.show()

        self.neq_btn_8 = QPushButton('8', self)
        self.neq_btn_8.setFont(QFont('Times', 100))
        self.neq_btn_8.setGeometry(185, 754, 125, 136)
        self.neq_btn_8.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.neq_btn_8.clicked.connect(partial(self.neq_work, '8'))
        self.neq_btn_8.show()

        self.neq_btn_9 = QPushButton('9', self)
        self.neq_btn_9.setFont(QFont('Times', 100))
        self.neq_btn_9.setGeometry(360, 754, 125, 136)
        self.neq_btn_9.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.neq_btn_9.clicked.connect(partial(self.neq_work, '9'))
        self.neq_btn_9.show()

        self.neq_btn_minus = QPushButton('-', self)
        self.neq_btn_minus.setFont(QFont('Times', 100))
        self.neq_btn_minus.setGeometry(535, 754, 125, 136)
        self.neq_btn_minus.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.neq_btn_minus.clicked.connect(partial(self.neq_work, '-'))
        self.neq_btn_minus.show()

        self.neq_btn_more = QPushButton('>', self)
        self.neq_btn_more.setFont(QFont('Times', 100))
        self.neq_btn_more.setGeometry(710, 754, 125, 136)
        self.neq_btn_more.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.neq_btn_more.clicked.connect(partial(self.neq_work, '>'))
        self.neq_btn_more.show()

        self.neq_btn_less_eq = QPushButton('⩽', self)
        self.neq_btn_less_eq.setFont(QFont('Times', 100))
        self.neq_btn_less_eq.setGeometry(885, 754, 125, 136)
        self.neq_btn_less_eq.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.neq_btn_less_eq.clicked.connect(partial(self.neq_work, '<='))
        self.neq_btn_less_eq.show()

    def show_square_table(self):
        self.hiding_main()

        self.setGeometry(200, 200, 920, 650)

        self.sq_table = QPixmap('square_table.png')

        self.sq_table_image = QLabel(self)
        self.sq_table_image.setGeometry(10, 120, 900, 500)
        self.sq_table_image.setPixmap(self.sq_table)
        self.sq_table_image.show()

        self.sq_table_btn_back_to_main = QPushButton('На главный экран', self)
        self.sq_table_btn_back_to_main.setGeometry(400, 10, 510, 100)
        self.sq_table_btn_back_to_main.setFont(QFont('Times', 40))
        self.sq_table_btn_back_to_main.clicked.connect(partial(self.back_to_main, 'sq_tb'))
        self.sq_table_btn_back_to_main.setStyleSheet(
            f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.sq_table_btn_back_to_main.show()

    def show_block_table(self):
        self.hiding_main()

        self.setGeometry(200, 100, 1620, 1000)

        self.bl_table = QPixmap('block_table.png')

        self.bl_table_image = QLabel(self)
        self.bl_table_image.setGeometry(10, 80, 1600, 880)
        self.bl_table_image.setPixmap(self.bl_table)
        self.bl_table_image.show()

        self.bl_btn_back_to_main = QPushButton('На главный экран', self)
        self.bl_btn_back_to_main.setGeometry(800, 10, 710, 90)
        self.bl_btn_back_to_main.setFont(QFont('Times', 60))
        self.bl_btn_back_to_main.clicked.connect(partial(self.back_to_main, 'bl_tb'))
        self.bl_btn_back_to_main.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.bl_btn_back_to_main.show()

    def sct_work(self, data):
        if data.isdigit() or (data == '.' and '.' not in self.sct_line_angle.text()):
            self.sct_line_angle.setText(self.sct_line_angle.text() + data)

        elif data == '±':
            if self.sct_line_angle.text()[0] != '-':
                self.sct_line_angle.setText('-' + self.sct_line_angle.text())

            elif self.sct_line_angle.text()[0] == '-':
                self.sct_line_angle.setText(self.sct_line_angle.text()[1:])

        elif data == 'del' and self.sct_line_angle.text():
            self.sct_line_angle.setText(self.sct_line_angle.text()[:-1])

        elif data == 'del all':
            self.sct_line_angle.setText('')

    def sct_solve(self):
        if self.sct_line_angle.text():
            angle = float(self.sct_line_angle.text())

            self.sct_line_sin.setText(str(round(math.sin(math.radians(angle)), 4)))
            self.sct_line_sin.setFont(QFont('Times', 60))

            self.sct_line_cos.setText(str(round(math.cos(math.radians(angle)), 4)))
            self.sct_line_cos.setFont(QFont('Times', 60))

            self.sct_line_tg.setText(str(round(math.tan(math.radians(angle)), 4)))
            self.sct_line_tg.setFont(QFont('Times', 60))

        else:
            self.sct_line_sin.setText('нет угла')
            self.sct_line_sin.setFont(QFont('Times', 50))

            self.sct_line_cos.setText('нет угла')
            self.sct_line_cos.setFont(QFont('Times', 50))

            self.sct_line_tg.setText('нет угла')
            self.sct_line_tg.setFont(QFont('Times', 50))

    def show_sin_cos_tg(self):
        self.hiding_main()

        self.setGeometry(200, 200, 1020, 830)

        self.sct_line_angle = QLineEdit(self)
        self.sct_line_angle.setReadOnly(True)
        self.sct_line_angle.setGeometry(10, 10, 700, 100)
        self.sct_line_angle.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.sct_line_angle.setFont(QFont('Times', 40))
        self.sct_line_angle.show()

        self.sct_btn_back_to_main = QPushButton('На главный экран', self)
        self.sct_btn_back_to_main.setGeometry(760, 10, 250, 100)
        self.sct_btn_back_to_main.setFont(QFont('Times', 20))
        self.sct_btn_back_to_main.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.sct_btn_back_to_main.clicked.connect(partial(self.back_to_main, 'sct'))
        self.sct_btn_back_to_main.show()

        self.sct_btn_1 = QPushButton('1', self)
        self.sct_btn_1.setGeometry(10, 160, 125, 100)
        self.sct_btn_1.setFont(QFont('Times', 80))
        self.sct_btn_1.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.sct_btn_1.clicked.connect(partial(self.sct_work, '1'))
        self.sct_btn_1.show()

        self.sct_btn_2 = QPushButton('2', self)
        self.sct_btn_2.setGeometry(185, 160, 125, 100)
        self.sct_btn_2.setFont(QFont('Times', 80))
        self.sct_btn_2.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.sct_btn_2.clicked.connect(partial(self.sct_work, '2'))
        self.sct_btn_2.show()

        self.sct_btn_3 = QPushButton('3', self)
        self.sct_btn_3.setGeometry(360, 160, 125, 100)
        self.sct_btn_3.setFont(QFont('Times', 80))
        self.sct_btn_3.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.sct_btn_3.clicked.connect(partial(self.sct_work, '3'))
        self.sct_btn_3.show()

        self.sct_btn_4 = QPushButton('4', self)
        self.sct_btn_4.setGeometry(535, 160, 125, 100)
        self.sct_btn_4.setFont(QFont('Times', 80))
        self.sct_btn_4.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.sct_btn_4.clicked.connect(partial(self.sct_work, '4'))
        self.sct_btn_4.show()

        self.sct_btn_5 = QPushButton('5', self)
        self.sct_btn_5.setGeometry(710, 160, 125, 100)
        self.sct_btn_5.setFont(QFont('Times', 80))
        self.sct_btn_5.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.sct_btn_5.clicked.connect(partial(self.sct_work, '5'))
        self.sct_btn_5.show()

        self.sct_btn_del = QPushButton('del', self)
        self.sct_btn_del.setGeometry(885, 160, 125, 100)
        self.sct_btn_del.setFont(QFont('Times', 60))
        self.sct_btn_del.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.sct_btn_del.clicked.connect(partial(self.sct_work, 'del'))
        self.sct_btn_del.show()

        self.sct_btn_6 = QPushButton('6', self)
        self.sct_btn_6.setGeometry(10, 310, 125, 100)
        self.sct_btn_6.setFont(QFont('Times', 80))
        self.sct_btn_6.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.sct_btn_6.clicked.connect(partial(self.sct_work, '6'))
        self.sct_btn_6.show()

        self.sct_btn_7 = QPushButton('7', self)
        self.sct_btn_7.setGeometry(185, 310, 125, 100)
        self.sct_btn_7.setFont(QFont('Times', 80))
        self.sct_btn_7.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.sct_btn_7.clicked.connect(partial(self.sct_work, '7'))
        self.sct_btn_7.show()

        self.sct_btn_8 = QPushButton('8', self)
        self.sct_btn_8.setGeometry(360, 310, 125, 100)
        self.sct_btn_8.setFont(QFont('Times', 80))
        self.sct_btn_8.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.sct_btn_8.clicked.connect(partial(self.sct_work, '8'))
        self.sct_btn_8.show()

        self.sct_btn_9 = QPushButton('9', self)
        self.sct_btn_9.setGeometry(535, 310, 125, 100)
        self.sct_btn_9.setFont(QFont('Times', 80))
        self.sct_btn_9.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.sct_btn_9.clicked.connect(partial(self.sct_work, '9'))
        self.sct_btn_9.show()

        self.sct_btn_0 = QPushButton('0', self)
        self.sct_btn_0.setGeometry(710, 310, 125, 100)
        self.sct_btn_0.setFont(QFont('Times', 80))
        self.sct_btn_0.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.sct_btn_0.clicked.connect(partial(self.sct_work, '0'))
        self.sct_btn_0.show()

        self.sct_btn_del_all = QPushButton('del all', self)
        self.sct_btn_del_all.setGeometry(885, 310, 125, 100)
        self.sct_btn_del_all.setFont(QFont('Times', 32))
        self.sct_btn_del_all.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.sct_btn_del_all.clicked.connect(partial(self.sct_work, 'del all'))
        self.sct_btn_del_all.show()

        self.sct_btn_dot = QPushButton('●', self)
        self.sct_btn_dot.setGeometry(10, 460, 125, 100)
        self.sct_btn_dot.setFont(QFont('Times', 80))
        self.sct_btn_dot.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.sct_btn_dot.clicked.connect(partial(self.sct_work, '.'))
        self.sct_btn_dot.show()

        self.sct_btn_solve = QPushButton('найти', self)
        self.sct_btn_solve.setGeometry(185, 460, 650, 100)
        self.sct_btn_solve.setFont(QFont('Times', 83))
        self.sct_btn_solve.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.sct_btn_solve.clicked.connect(self.sct_solve)
        self.sct_btn_solve.show()

        self.sct_btn_plus_minus = QPushButton('±', self)
        self.sct_btn_plus_minus.setGeometry(885, 460, 125, 100)
        self.sct_btn_plus_minus.setFont(QFont('Times', 80))
        self.sct_btn_plus_minus.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.sct_btn_plus_minus.clicked.connect(partial(self.sct_work, '±'))
        self.sct_btn_plus_minus.show()

        self.sct_line_sin = QLineEdit(self)
        self.sct_line_sin.setReadOnly(True)
        self.sct_line_sin.setGeometry(10, 610, 300, 100)
        self.sct_line_sin.setFont(QFont('Times', 60))
        self.sct_line_sin.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.sct_line_sin.show()

        self.sct_line_cos = QLineEdit(self)
        self.sct_line_cos.setReadOnly(True)
        self.sct_line_cos.setGeometry(360, 610, 300, 100)
        self.sct_line_cos.setFont(QFont('Times', 60))
        self.sct_line_cos.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.sct_line_cos.show()

        self.sct_line_tg = QLineEdit(self)
        self.sct_line_tg.setReadOnly(True)
        self.sct_line_tg.setGeometry(710, 610, 300, 100)
        self.sct_line_tg.setFont(QFont('Times', 60))
        self.sct_line_tg.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.sct_line_tg.show()

        self.sct_txt_sin = QLabel(self)
        self.sct_txt_sin.setGeometry(20, 700, 300, 100)
        self.sct_txt_sin.setText('синус')
        self.sct_txt_sin.setFont(QFont('Times', 60))
        self.sct_txt_sin.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.sct_txt_sin.show()

        self.sct_txt_cos = QLabel(self)
        self.sct_txt_cos.setGeometry(360, 700, 300, 100)
        self.sct_txt_cos.setText('косинус')
        self.sct_txt_cos.setFont(QFont('Times', 60))
        self.sct_txt_cos.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.sct_txt_cos.show()

        self.sct_txt_tg = QLabel(self)
        self.sct_txt_tg.setGeometry(710, 700, 300, 100)
        self.sct_txt_tg.setText('тангенс')
        self.sct_txt_tg.setFont(QFont('Times', 60))
        self.sct_txt_tg.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.sct_txt_tg.show()

    def ca_solve(self):
        if self.ca_line_answer.text() == '':
            return

        if '/0' in self.ca_line_answer.text() or '/' == self.ca_line_answer.text()[-1]:
            self.ca_line_answer.setText('Error')
            return

        elif not self.ca_line_answer.text():
            return

        else:
            self.ca_line_answer.setText(str(eval(self.ca_line_answer.text().replace('^', '**'))))

    def ca_work(self, ca_data):
        b = '=' in self.ca_line_answer.text()

        if self.ca_line_answer.text() == 'Error' or '=' in self.ca_line_answer.text():
            self.ca_line_answer.setText('')
            return

        if self.ca_line_answer.text() and \
                ca_data == '0' and self.ca_line_answer.text()[-1] in '+-*/^':
            return

        elif ca_data == '0' and not self.ca_line_answer.text():
            return

        elif ca_data.isdigit():
            self.ca_line_answer.setText(self.ca_line_answer.text() + ca_data)

        elif self.ca_line_answer.text() and \
                ca_data in '+-*/^' and self.ca_line_answer.text()[-1] in '+-*/^':
            self.ca_line_answer.setText(self.ca_line_answer.text()[:-1] + ca_data)

        elif self.ca_line_answer.text() and \
                ca_data in '+-*/^' and self.ca_line_answer.text()[-1] not in '+-*/^.':
            self.ca_line_answer.setText(self.ca_line_answer.text() + ca_data)

        elif ca_data == 'c':
            self.ca_line_answer.setText(self.ca_line_answer.text()[:-1])

        elif ca_data == 'ce':
            self.ca_line_answer.setText('')

        elif ca_data == '.' and self.ca_line_answer.text() and \
                '.' not in my_split(self.ca_line_answer.text())[-1] and \
                self.ca_line_answer.text()[-1] not in '+-*/^':
            self.ca_line_answer.setText(self.ca_line_answer.text() + ca_data)

        elif ca_data == '√' or ca_data == '!':
            self.ca_solve()

            if self.ca_line_answer.text() == 'Error' or not self.ca_line_answer.text():
                self.ca_line_answer.setText('')
                return

            if ca_data == '√' and float(self.ca_line_answer.text()) >= 0:
                self.ca_line_answer.setText(f'√{self.ca_line_answer.text()} ='
                                            f' {round(sqrt(float(self.ca_line_answer.text())), 4)}')

            elif ca_data == '!' and self.ca_line_answer.text().isdigit() and \
                    int(self.ca_line_answer.text()) >= 0:
                self.ca_line_answer.setText(f'!{self.ca_line_answer.text()} = '
                                            f'{math.factorial(int(self.ca_line_answer.text()))}')

            elif float(self.ca_line_answer.text()) < 0:
                self.ca_line_answer.setText('Error')

    def simple_calculator(self):
        self.hiding_main()

        self.setGeometry(200, 100, 960, 930)

        self.ca_btn_back = QPushButton('на главный экран', self)
        self.ca_btn_back.setGeometry(485, 10, 425, 100)
        self.ca_btn_back.setFont(QFont('Times', 35))
        self.ca_btn_back.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.ca_btn_back.clicked.connect(partial(self.back_to_main, 'ca'))
        self.ca_btn_back.show()

        self.ca_line_answer = QLineEdit(self)
        self.ca_line_answer.setGeometry(10, 160, 750, 100)
        self.ca_line_answer.setFont(QFont('Times', 50))
        self.ca_line_answer.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.ca_line_answer.setText('')
        self.ca_line_answer.setReadOnly(True)
        self.ca_line_answer.show()

        self.ca_btn_eq = QPushButton('=', self)
        self.ca_btn_eq.setGeometry(810, 160, 100, 100)
        self.ca_btn_eq.setFont(QFont('Times', 90))
        self.ca_btn_eq.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.ca_btn_eq.clicked.connect(self.ca_solve)
        self.ca_btn_eq.show()

        self.ca_btn_1 = QPushButton('1', self)
        self.ca_btn_1.setGeometry(10, 310, 140, 100)
        self.ca_btn_1.setFont(QFont('Times', 80))
        self.ca_btn_1.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.ca_btn_1.clicked.connect(partial(self.ca_work, '1'))
        self.ca_btn_1.show()

        self.ca_btn_2 = QPushButton('2', self)
        self.ca_btn_2.setGeometry(200, 310, 140, 100)
        self.ca_btn_2.setFont(QFont('Times', 80))
        self.ca_btn_2.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.ca_btn_2.clicked.connect(partial(self.ca_work, '2'))
        self.ca_btn_2.show()

        self.ca_btn_3 = QPushButton('3', self)
        self.ca_btn_3.setGeometry(390, 310, 140, 100)
        self.ca_btn_3.setFont(QFont('Times', 80))
        self.ca_btn_3.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.ca_btn_3.clicked.connect(partial(self.ca_work, '3'))
        self.ca_btn_3.show()

        self.ca_btn_4 = QPushButton('4', self)
        self.ca_btn_4.setGeometry(580, 310, 140, 100)
        self.ca_btn_4.setFont(QFont('Times', 80))
        self.ca_btn_4.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.ca_btn_4.clicked.connect(partial(self.ca_work, '4'))
        self.ca_btn_4.show()

        self.ca_btn_5 = QPushButton('5', self)
        self.ca_btn_5.setGeometry(770, 310, 140, 100)
        self.ca_btn_5.setFont(QFont('Times', 80))
        self.ca_btn_5.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.ca_btn_5.clicked.connect(partial(self.ca_work, '5'))
        self.ca_btn_5.show()

        self.ca_btn_6 = QPushButton('6', self)
        self.ca_btn_6.setGeometry(10, 460, 140, 100)
        self.ca_btn_6.setFont(QFont('Times', 80))
        self.ca_btn_6.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.ca_btn_6.clicked.connect(partial(self.ca_work, '6'))
        self.ca_btn_6.show()

        self.ca_btn_7 = QPushButton('7', self)
        self.ca_btn_7.setGeometry(200, 460, 140, 100)
        self.ca_btn_7.setFont(QFont('Times', 80))
        self.ca_btn_7.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.ca_btn_7.clicked.connect(partial(self.ca_work, '7'))
        self.ca_btn_7.show()

        self.ca_btn_8 = QPushButton('8', self)
        self.ca_btn_8.setGeometry(390, 460, 140, 100)
        self.ca_btn_8.setFont(QFont('Times', 80))
        self.ca_btn_8.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.ca_btn_8.clicked.connect(partial(self.ca_work, '8'))
        self.ca_btn_8.show()

        self.ca_btn_9 = QPushButton('9', self)
        self.ca_btn_9.setGeometry(580, 460, 140, 100)
        self.ca_btn_9.setFont(QFont('Times', 80))
        self.ca_btn_9.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.ca_btn_9.clicked.connect(partial(self.ca_work, '9'))
        self.ca_btn_9.show()

        self.ca_btn_0 = QPushButton('0', self)
        self.ca_btn_0.setGeometry(770, 460, 140, 100)
        self.ca_btn_0.setFont(QFont('Times', 80))
        self.ca_btn_0.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.ca_btn_0.clicked.connect(partial(self.ca_work, '0'))
        self.ca_btn_0.show()

        self.ca_btn_plus = QPushButton('+', self)
        self.ca_btn_plus.setGeometry(10, 610, 140, 100)
        self.ca_btn_plus.setFont(QFont('Times', 80))
        self.ca_btn_plus.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.ca_btn_plus.clicked.connect(partial(self.ca_work, '+'))
        self.ca_btn_plus.show()

        self.ca_btn_minus = QPushButton('-', self)
        self.ca_btn_minus.setGeometry(200, 610, 140, 100)
        self.ca_btn_minus.setFont(QFont('Times', 80))
        self.ca_btn_minus.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.ca_btn_minus.clicked.connect(partial(self.ca_work, '-'))
        self.ca_btn_minus.show()

        self.ca_btn_dot = QPushButton('●', self)
        self.ca_btn_dot.setGeometry(390, 610, 140, 100)
        self.ca_btn_dot.setFont(QFont('Times', 80))
        self.ca_btn_dot.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.ca_btn_dot.clicked.connect(partial(self.ca_work, '.'))
        self.ca_btn_dot.show()

        self.ca_btn_comp = QPushButton('*', self)
        self.ca_btn_comp.setGeometry(580, 610, 140, 100)
        self.ca_btn_comp.setFont(QFont('Times', 80))
        self.ca_btn_comp.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.ca_btn_comp.clicked.connect(partial(self.ca_work, '*'))
        self.ca_btn_comp.show()

        self.ca_btn_div = QPushButton('/', self)
        self.ca_btn_div.setGeometry(770, 610, 140, 100)
        self.ca_btn_div.setFont(QFont('Times', 80))
        self.ca_btn_div.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.ca_btn_div.clicked.connect(partial(self.ca_work, '/'))
        self.ca_btn_div.show()

        self.ca_btn_c = QPushButton('c', self)
        self.ca_btn_c.setGeometry(10, 760, 140, 100)
        self.ca_btn_c.setFont(QFont('Times', 80))
        self.ca_btn_c.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.ca_btn_c.clicked.connect(partial(self.ca_work, 'c'))
        self.ca_btn_c.show()

        self.ca_btn_sqrt = QPushButton('√', self)
        self.ca_btn_sqrt.setGeometry(200, 760, 140, 100)
        self.ca_btn_sqrt.setFont(QFont('Times', 80))
        self.ca_btn_sqrt.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.ca_btn_sqrt.clicked.connect(partial(self.ca_work, '√'))
        self.ca_btn_sqrt.show()

        self.ca_btn_fact = QPushButton('!', self)
        self.ca_btn_fact.setGeometry(390, 760, 140, 100)
        self.ca_btn_fact.setFont(QFont('Times', 80))
        self.ca_btn_fact.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.ca_btn_fact.clicked.connect(partial(self.ca_work, '!'))
        self.ca_btn_fact.show()

        self.ca_btn_deg = QPushButton('^', self)
        self.ca_btn_deg.setGeometry(580, 760, 140, 100)
        self.ca_btn_deg.setFont(QFont('Times', 80))
        self.ca_btn_deg.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.ca_btn_deg.clicked.connect(partial(self.ca_work, '^'))
        self.ca_btn_deg.show()

        self.ca_btn_ce = QPushButton('ce', self)
        self.ca_btn_ce.setGeometry(770, 760, 140, 100)
        self.ca_btn_ce.setFont(QFont('Times', 80))
        self.ca_btn_ce.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.ca_btn_ce.clicked.connect(partial(self.ca_work, 'ce'))
        self.ca_btn_ce.show()

    def ssf_work(self):

        self.ssf_whole_num_answer.setText('')
        self.ssf_numerator_answer.setText('')
        self.ssf_denominator_answer.setText('')

        # input errors
        if self.ssf_whole_num_1.text() and not my_isdigit(self.ssf_whole_num_1.text()):
            self.ssf_line_wrong.setText('неправильный ввод: целое 1')
            return

        elif not my_isdigit(self.ssf_numerator_1.text()):
            self.ssf_line_wrong.setText('неправильный ввод: числитель 1')
            return

        elif not my_isdigit(self.ssf_denominator_1.text()):
            self.ssf_line_wrong.setText('неправильный ввод: знаменатель 1')
            return

        elif self.ssf_whole_num_2.text() and not my_isdigit(self.ssf_whole_num_2.text()):
            self.ssf_line_wrong.setText('неправильный ввод: целое 2')
            return

        elif not my_isdigit(self.ssf_numerator_2.text()):
            self.ssf_line_wrong.setText('неправильный ввод: числитель 2')
            return

        elif not my_isdigit(self.ssf_denominator_2.text()):
            self.ssf_line_wrong.setText('неправильный ввод: знаменатель 2')
            return

        elif self.ssf_symbol.text() not in ['+', '-', '*', '/']:
            self.ssf_line_wrong.setText('неправильный ввод: знак')
            return

        self.ssf_line_wrong.setText('')

        den1 = int(self.ssf_denominator_1.text())
        den2 = int(self.ssf_denominator_2.text())

        num1, num2 = 0, 0

        if self.ssf_whole_num_1.text():
            num1 = int(self.ssf_whole_num_1.text()) * den1 + int(self.ssf_numerator_1.text())

        elif not self.ssf_whole_num_1.text():
            num1 = int(self.ssf_numerator_1.text())

        if self.ssf_whole_num_2.text():
            num2 = int(self.ssf_whole_num_2.text()) * den2 + int(self.ssf_numerator_2.text())

        elif not self.ssf_whole_num_2.text():
            num2 = int(self.ssf_numerator_2.text())

        num_answer, nok = 0, 0

        if self.ssf_symbol.text() in '+-':
            nok = den1 * den2 // math.gcd(den1, den2)

            num1 = num1 * (nok // den1)

            num2 = num2 * (nok // den2)

            num_answer = num1 + num2 if self.ssf_symbol.text() == '+' else num1 - num2

        elif self.ssf_symbol.text() == '*':
            num_answer = num1 * num2

            nok = den1 * den2

        elif self.ssf_symbol.text() == '/':
            num_answer = num1 * den2

            nok = den1 * num2

        if num_answer == nok:
            self.ssf_whole_num_answer.setText('1')
            self.ssf_numerator_answer.setText('')
            self.ssf_denominator_answer.setText('')
            return

        num_answer, nok, whole_num = num_answer // math.gcd(num_answer, nok), nok // math.gcd(num_answer, nok), 0

        if abs(num_answer) > nok:
            whole_num = abs(num_answer) // nok

            num_answer = num_answer % nok

            self.ssf_whole_num_answer.setText(str(whole_num))

        if num_answer < 0:
            if self.ssf_whole_num_answer.text():
                self.ssf_whole_num_answer.setText('-' + str(whole_num))

            elif not self.ssf_whole_num_answer.text():
                self.ssf_whole_num_answer.setText('-')

            self.ssf_numerator_answer.setText(str(abs(num_answer)))
            self.ssf_denominator_answer.setText(str(nok))

        elif num_answer != 0 and num_answer:
            self.ssf_numerator_answer.setText(str(num_answer))
            self.ssf_denominator_answer.setText(str(nok))

        elif num_answer == 0:
            self.ssf_numerator_answer.setText('')
            self.ssf_denominator_answer.setText('')
            self.ssf_whole_num_answer.setText('0' if not whole_num else str(whole_num))

    def show_sum_fractions(self):
        self.hiding_main()

        self.setGeometry(200, 200, 1060, 520)

        self.ssf_line_wrong = QLineEdit(self)
        self.ssf_line_wrong.setReadOnly(True)
        self.ssf_line_wrong.setGeometry(10, 10, 650, 100)
        self.ssf_line_wrong.setFont(QFont('Times', 26))
        self.ssf_line_wrong.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.ssf_line_wrong.setText('текст ошибки')
        self.ssf_line_wrong.show()

        self.ssf_btn_back_to_main = QPushButton('на главный экран', self)
        self.ssf_btn_back_to_main.setGeometry(710, 10, 280, 100)
        self.ssf_btn_back_to_main.setFont(QFont('Times', 25))
        self.ssf_btn_back_to_main.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.ssf_btn_back_to_main.clicked.connect(partial(self.back_to_main, 'ssf'))
        self.ssf_btn_back_to_main.show()

        self.ssf_whole_num_1 = QLineEdit(self)
        self.ssf_whole_num_1.setGeometry(10, 270, 100, 100)
        self.ssf_whole_num_1.setFont(QFont('Times', 30))
        self.ssf_whole_num_1.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.ssf_whole_num_1.show()

        self.ssf_numerator_1 = QLineEdit(self)
        self.ssf_numerator_1.setGeometry(130, 160, 100, 100)
        self.ssf_numerator_1.setFont(QFont('Times', 30))
        self.ssf_numerator_1.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.ssf_numerator_1.show()

        self.ssf_denominator_1 = QLineEdit(self)
        self.ssf_denominator_1.setGeometry(130, 380, 100, 100)
        self.ssf_denominator_1.setFont(QFont('Times', 30))
        self.ssf_denominator_1.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.ssf_denominator_1.show()

        self.ssf_label_1 = QLabel(self)
        self.ssf_label_1.setGeometry(50, 470, 100, 50)
        self.ssf_label_1.setFont(QFont('Times', 14))
        self.ssf_label_1.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.ssf_label_1.setText('дробь №1')
        self.ssf_label_1.show()

        self.ssf_symbol = QLineEdit(self)
        self.ssf_symbol.setGeometry(280, 270, 150, 100)
        self.ssf_symbol.setFont(QFont('Times', 40))
        self.ssf_symbol.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.ssf_symbol.show()

        self.ssf_whole_num_2 = QLineEdit(self)
        self.ssf_whole_num_2.setGeometry(460, 270, 100, 100)
        self.ssf_whole_num_2.setFont(QFont('Times', 30))
        self.ssf_whole_num_2.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.ssf_whole_num_2.show()

        self.ssf_numerator_2 = QLineEdit(self)
        self.ssf_numerator_2.setGeometry(570, 160, 100, 100)
        self.ssf_numerator_2.setFont(QFont('Times', 30))
        self.ssf_numerator_2.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.ssf_numerator_2.show()

        self.ssf_denominator_2 = QLineEdit(self)
        self.ssf_denominator_2.setGeometry(570, 380, 100, 100)
        self.ssf_denominator_2.setFont(QFont('Times', 30))
        self.ssf_denominator_2.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.ssf_denominator_2.show()

        self.ssf_btn_eq = QPushButton('=', self)
        self.ssf_btn_eq.setGeometry(700, 270, 100, 100)
        self.ssf_btn_eq.setFont(QFont('Times', 50))
        self.ssf_btn_eq.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.ssf_btn_eq.clicked.connect(self.ssf_work)
        self.ssf_btn_eq.show()

        self.ssf_whole_num_answer = QLineEdit(self)
        self.ssf_whole_num_answer.setGeometry(830, 270, 100, 100)
        self.ssf_whole_num_answer.setFont(QFont('Times', 30))
        self.ssf_whole_num_answer.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.ssf_whole_num_answer.setReadOnly(True)
        self.ssf_whole_num_answer.show()

        self.ssf_numerator_answer = QLineEdit(self)
        self.ssf_numerator_answer.setGeometry(950, 160, 100, 100)
        self.ssf_numerator_answer.setFont(QFont('Times', 30))
        self.ssf_numerator_answer.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.ssf_numerator_answer.setReadOnly(True)
        self.ssf_numerator_answer.show()

        self.ssf_denominator_answer = QLineEdit(self)
        self.ssf_denominator_answer.setGeometry(950, 380, 100, 100)
        self.ssf_denominator_answer.setFont(QFont('Times', 30))
        self.ssf_denominator_answer.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.ssf_denominator_answer.setReadOnly(True)
        self.ssf_denominator_answer.show()

    def pr_solve(self):
        if not my_isdigit(self.pr_left_high.text()):
            self.pr_line.setFont(QFont('Times', 20))
            self.pr_line.setText('ошибка ввода - левый верх')
            return

        if not my_isdigit(self.pr_left_low.text()):
            self.pr_line.setFont(QFont('Times', 20))
            self.pr_line.setText('ошибка ввода - левый низ')
            return

        if not my_isdigit(self.pr_right_high.text()):
            self.pr_line.setFont(QFont('Times', 20))
            self.pr_line.setText('ошибка ввода - правый верх')
            return

        if not my_isdigit(self.pr_right_low.text()):
            self.pr_line.setFont(QFont('Times', 20))
            self.pr_line.setText('ошибка ввода - правый низ')
            return

        if int(self.pr_left_low.text()) == 0 or int(self.pr_right_low.text()) == 0:
            self.pr_line.setFont(QFont('Times', 20))
            self.pr_line.setText('ответ не определен')
            return

        self.pr_line.setFont(QFont('Times', 35))
        self.pr_line.setText('')

        self.pr_line.setText('x = ' + str(round(
            int(self.pr_left_high.text()) * int(self.pr_right_low.text()) /
            (int(self.pr_left_low.text()) * int(self.pr_right_high.text())), 3)))

    def show_proportions(self):
        self.hiding_main()

        self.setGeometry(200, 200, 630, 520)

        self.pr_line = QLineEdit(self)
        self.pr_line.setReadOnly(True)
        self.pr_line.setGeometry(10, 10, 430, 100)
        self.pr_line.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.pr_line.setFont(QFont('Times', 35))
        self.pr_line.show()

        self.pr_btn_back = QPushButton('на главный экран', self)
        self.pr_btn_back.setGeometry(470, 10, 150, 100)
        self.pr_btn_back.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.pr_btn_back.setFont(QFont('Times', 12))
        self.pr_btn_back.clicked.connect(partial(self.back_to_main, 'pr'))
        self.pr_btn_back.show()

        self.pr_left_high = QLineEdit(self)
        self.pr_left_high.setGeometry(10, 160, 200, 100)
        self.pr_left_high.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.pr_left_high.setFont(QFont('Times', 30))
        self.pr_left_high.setMaxLength(6)
        self.pr_left_high.show()

        self.pr_left_low = QLineEdit(self)
        self.pr_left_low.setGeometry(10, 380, 200, 100)
        self.pr_left_low.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.pr_left_low.setFont(QFont('Times', 30))
        self.pr_left_low.setMaxLength(6)
        self.pr_left_low.show()

        self.pr_btn_eq = QPushButton('=', self)
        self.pr_btn_eq.setGeometry(240, 270, 100, 100)
        self.pr_btn_eq.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.pr_btn_eq.setFont(QFont('Times', 30))
        self.pr_btn_eq.clicked.connect(self.pr_solve)
        self.pr_btn_eq.show()

        self.pr_right_high = QLineEdit(self)
        self.pr_right_high.setGeometry(370, 160, 200, 100)
        self.pr_right_high.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.pr_right_high.setFont(QFont('Times', 30))
        self.pr_right_high.setMaxLength(6)
        self.pr_right_high.show()

        self.pr_right_low = QLineEdit(self)
        self.pr_right_low.setGeometry(370, 380, 200, 100)
        self.pr_right_low.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')
        self.pr_right_low.setFont(QFont('Times', 30))
        self.pr_right_low.setMaxLength(6)
        self.pr_right_low.show()

        self.pr_symb_x = QLabel(self)
        self.pr_symb_x.setText('x')
        self.pr_symb_x.setGeometry(505, 155, 100, 100)
        self.pr_symb_x.setFont(QFont('Times', 40))
        self.pr_symb_x.show()

    def back_to_main(self, data):
        if data == 'eq':
            self.equation_back.hide()
            self.line_of_eq.hide()
            self.eq_answer.hide()
            self.eq_btn_solve.hide()
            self.eq_btn_del.hide()
            self.eq_btn_1.hide()
            self.eq_btn_2.hide()
            self.eq_btn_3.hide()
            self.eq_btn_4.hide()
            self.eq_btn_5.hide()
            self.eq_btn_6.hide()
            self.eq_btn_7.hide()
            self.eq_btn_8.hide()
            self.eq_btn_9.hide()
            self.eq_btn_0.hide()
            self.eq_btn_plus.hide()
            self.eq_btn_minus.hide()
            self.eq_btn_dot.hide()
            self.eq_btn_x.hide()
            self.eq_btn_eq.hide()
            self.eq_btn_del_all.hide()

        elif data == 'sq_eq':
            self.sq_example.hide()
            self.sq_btn_back.hide()
            self.sq_line_b.hide()
            self.sq_line_a.hide()
            self.sq_line_c.hide()
            self.sq_txt_a.hide()
            self.sq_txt_b.hide()
            self.sq_txt_c.hide()
            self.sq_btn_1.hide()
            self.sq_btn_2.hide()
            self.sq_btn_3.hide()
            self.sq_btn_4.hide()
            self.sq_btn_5.hide()
            self.sq_btn_6.hide()
            self.sq_btn_7.hide()
            self.sq_btn_8.hide()
            self.sq_btn_9.hide()
            self.sq_btn_0.hide()
            self.sq_btn_solve.hide()
            self.sq_line_d.hide()
            self.sq_line_sqrt_d.hide()
            self.sq_x1.hide()
            self.sq_x2.hide()
            self.sq_btn_del.hide()
            self.sq_btn_del_all.hide()
            self.sq_btn_plus_minus.hide()

        elif data == 'neq':
            self.neq_line_of_neq.hide()
            self.neq_btn_back_to_main.hide()
            self.neq_btn_del.hide()
            self.neq_btn_del_all.hide()
            self.neq_line_answer.hide()
            self.neq_btn_solve.hide()
            self.neq_btn_1.hide()
            self.neq_btn_2.hide()
            self.neq_btn_3.hide()
            self.neq_btn_0.hide()
            self.neq_btn_dot.hide()
            self.neq_btn_less.hide()
            self.neq_btn_4.hide()
            self.neq_btn_5.hide()
            self.neq_btn_6.hide()
            self.neq_btn_plus.hide()
            self.neq_btn_x.hide()
            self.neq_btn_more_eq.hide()
            self.neq_btn_7.hide()
            self.neq_btn_8.hide()
            self.neq_btn_9.hide()
            self.neq_btn_minus.hide()
            self.neq_btn_more.hide()
            self.neq_btn_less_eq.hide()

        elif data == 'sq_tb':
            self.sq_table_image.hide()
            self.sq_table_btn_back_to_main.hide()

        elif data == 'bl_tb':
            self.bl_table_image.hide()
            self.bl_btn_back_to_main.hide()

        elif data == 'sct':
            self.sct_line_angle.hide()
            self.sct_btn_back_to_main.hide()
            self.sct_btn_1.hide()
            self.sct_btn_2.hide()
            self.sct_btn_3.hide()
            self.sct_btn_4.hide()
            self.sct_btn_5.hide()
            self.sct_btn_del.hide()
            self.sct_btn_6.hide()
            self.sct_btn_7.hide()
            self.sct_btn_8.hide()
            self.sct_btn_9.hide()
            self.sct_btn_0.hide()
            self.sct_btn_del_all.hide()
            self.sct_btn_dot.hide()
            self.sct_btn_solve.hide()
            self.sct_btn_plus_minus.hide()
            self.sct_line_sin.hide()
            self.sct_line_cos.hide()
            self.sct_line_tg.hide()
            self.sct_txt_sin.hide()
            self.sct_txt_cos.hide()
            self.sct_txt_tg.hide()

        elif data == 'ca':
            self.ca_line_answer.hide()
            self.ca_btn_back.hide()
            self.ca_btn_eq.hide()
            self.ca_btn_1.hide()
            self.ca_btn_2.hide()
            self.ca_btn_3.hide()
            self.ca_btn_4.hide()
            self.ca_btn_5.hide()
            self.ca_btn_6.hide()
            self.ca_btn_7.hide()
            self.ca_btn_8.hide()
            self.ca_btn_9.hide()
            self.ca_btn_0.hide()
            self.ca_btn_plus.hide()
            self.ca_btn_minus.hide()
            self.ca_btn_comp.hide()
            self.ca_btn_dot.hide()
            self.ca_btn_div.hide()
            self.ca_btn_ce.hide()
            self.ca_btn_deg.hide()
            self.ca_btn_fact.hide()
            self.ca_btn_c.hide()
            self.ca_btn_sqrt.hide()

        elif data == 'ssf':
            self.ssf_line_wrong.hide()
            self.ssf_btn_back_to_main.hide()
            self.ssf_whole_num_1.hide()
            self.ssf_numerator_1.hide()
            self.ssf_denominator_1.hide()
            self.ssf_label_1.hide()
            self.ssf_symbol.hide()
            self.ssf_whole_num_2.hide()
            self.ssf_numerator_2.hide()
            self.ssf_denominator_2.hide()
            self.ssf_btn_eq.hide()
            self.ssf_whole_num_answer.hide()
            self.ssf_numerator_answer.hide()
            self.ssf_denominator_answer.hide()

        elif data == 'pr':
            self.pr_line.hide()
            self.pr_btn_back.hide()
            self.pr_left_high.hide()
            self.pr_left_low.hide()
            self.pr_btn_eq.hide()
            self.pr_right_high.hide()
            self.pr_right_low.hide()
            self.pr_symb_x.hide()

        self.setGeometry(200, 200, 700, 700)
        self.change_colours()

    def change_colours(self):
        self.simple_equation.show()
        self.simple_equation.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')

        self.square_equation.show()
        self.square_equation.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')

        self.btn_not_equation.show()
        self.btn_not_equation.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')

        self.square_table.show()
        self.square_table.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')

        self.block_table.show()
        self.block_table.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')

        self.sin_cos_tg.show()
        self.sin_cos_tg.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')

        self.calculator.show()
        self.calculator.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')

        self.sum_of_fractions.show()
        self.sum_of_fractions.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')

        self.proportions.show()
        self.proportions.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')

        self.btn_change_colours.show()
        self.btn_change_colours.setStyleSheet(f'color: rgb{(randint(1, 256), randint(1, 256), randint(1, 256))}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
