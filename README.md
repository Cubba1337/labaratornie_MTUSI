# labaratornie_MTUSI 4
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton, QMessageBox


class Calculator(QWidget):
    def __init__(self):
        super(Calculator, self).__init__()
        self.vbox = QVBoxLayout(self)
        self.hbox_input = QHBoxLayout()
        self.hbox_first = QHBoxLayout()
        self.hbox_result = QHBoxLayout()

        self.vbox.addLayout(self.hbox_input)
        self.vbox.addLayout(self.hbox_first)
        self.vbox.addLayout(self.hbox_result)

        self.input = QLineEdit(self)
        self.hbox_input.addWidget(self.input)
        self.b_1 = QPushButton("0", self)
        self.hbox_first.addWidget(self.b_1)
        self.b_2 = QPushButton("1", self)
        self.hbox_first.addWidget(self.b_2)
        self.b_3 = QPushButton("2", self)
        self.hbox_first.addWidget(self.b_3)
        self.b_4 = QPushButton("3", self)
        self.hbox_first.addWidget(self.b_4)
        self.b_5 = QPushButton("4", self)
        self.hbox_first.addWidget(self.b_5)
        self.b_6 = QPushButton("5", self)
        self.hbox_first.addWidget(self.b_6)
        self.b_7 = QPushButton("6", self)
        self.hbox_first.addWidget(self.b_7)
        self.b_8 = QPushButton("7", self)
        self.hbox_first.addWidget(self.b_8)
        self.b_9 = QPushButton("8", self)
        self.hbox_first.addWidget(self.b_9)
        self.b_10 = QPushButton("9", self)
        self.hbox_first.addWidget(self.b_10)
        self.b_11 = QPushButton("C", self)
        self.hbox_first.addWidget(self.b_11)
        self.b_plus = QPushButton("+", self)
        self.hbox_first.addWidget(self.b_plus)
        self.b_minus = QPushButton("-", self)
        self.hbox_first.addWidget(self.b_minus)
        self.b_multiply = QPushButton("*", self)
        self.hbox_first.addWidget(self.b_multiply)
        self.b_divide = QPushButton("/", self)
        self.hbox_first.addWidget(self.b_divide)
        self.b_float = QPushButton(".", self)
        self.hbox_first.addWidget(self.b_float)
        self.b_result = QPushButton("=", self)
        self.hbox_result.addWidget(self.b_result)

        self.b_plus.clicked.connect(lambda: self._operation("+"))
        self.b_minus.clicked.connect(lambda: self._operation("-"))
        self.b_multiply.clicked.connect(lambda: self._operation("*"))
        self.b_divide.clicked.connect(lambda: self._operation("/"))
        self.b_float.clicked.connect(lambda: self._button("."))
        self.b_result.clicked.connect(self._result)
        self.b_1.clicked.connect(lambda: self._button("0"))
        self.b_2.clicked.connect(lambda: self._button("1"))
        self.b_3.clicked.connect(lambda: self._button("2"))
        self.b_4.clicked.connect(lambda: self._button("3"))
        self.b_5.clicked.connect(lambda: self._button("4"))
        self.b_6.clicked.connect(lambda: self._button("5"))
        self.b_7.clicked.connect(lambda: self._button("6"))
        self.b_8.clicked.connect(lambda: self._button("7"))
        self.b_9.clicked.connect(lambda: self._button("8"))
        self.b_10.clicked.connect(lambda: self._button("9"))
        self.b_11.clicked.connect(lambda: self._operation('C'))

    def _button(self, param):
        line = self.input.text()
        self.input.setText(line + param)

    def _operation(self, op):
        if "." in self.input.text() and ".." not in self.input.text():
            self.num_1 = float(self.input.text())
        else:
            self.num_1 = int(self.input.text())
        self.op = op
        self.input.setText("")

    def _result(self):
        if self.input.text().isnumeric() == False and (
                '?' or '!' or ';' or ':' or ',') not in self.input.text() and ".." not in self.input.text():
            QMessageBox.about(self, "ОШИБКА", "Вы не можете вводить буквенные значения")
            self.input.setText("")
        elif self.input.text().isnumeric() == False and ('?' or '!' or ';' or ':' or ',') in self.input.text():
            QMessageBox.about(self, "ОШИБКА", "Вы не можете вводить знаки пунктуации")
            self.input.setText("")
        elif self.input.text().isnumeric() == False and (
                '?' or '!' or ';' or ':' or ',') not in self.input.text() and ".." in self.input.text():
            QMessageBox.about(self, "ОШИБКА", "Вы не можете ввести 2 плавающие точки в одном числе")
            self.input.setText("")
        else:
            if "." in self.input.text() and ".." not in self.input.text():
                self.num_2 = float(self.input.text())
            elif "." in self.input.text() and ".." in self.input.text():
                QMessageBox.about(self, "ОШИБКА", "Вы не можете поставить 2 плавающие точки в одном числе")
                self.input.setText("")
            else:
                self.num_2 = int(self.input.text())
                if self.op == "+":
                    self.input.setText(str(self.num_1 + self.num_2))
                elif self.op == '-':
                    self.input.setText(str(self.num_1 - self.num_2))
                elif self.op == '*':
                    if type(self.num_1 * self.num_2) == int:
                        self.input.setText(str((self.num_1 * self.num_2)))
                    elif type(self.num_1 * self.num_2) == float and (self.num_1 * self.num_2) == int(
                            self.num_1 * self.num_2):
                        self.input.setText(str(int(self.num_1 * self.num_2)))
                    elif type(self.num_1 * self.num_2) == float and (self.num_1 * self.num_2) != int(
                            self.num_1 * self.num_2):
                        self.input.setText(str(self.num_1 * self.num_2))
                elif self.op == '/' and self.num_2 != 0:
                    if self.num_1 % self.num_2 == 0:
                        self.input.setText(str(self.num_1 // self.num_2))
                    elif self.num_1 % self.num_2 != 0:
                        self.input.setText(str(self.num_1 / self.num_2))
                elif self.op == '/' and self.num_2 == 0:
                    QMessageBox.about(self, "ОШИБКА", "Вы не можете разделить на ноль")
                    self.input.setText("")

                elif self.op == 'C':
                    self.input.setText("")


app = QApplication(sys.argv)

win = Calculator()
win.show()

sys.exit(app.exec_())
