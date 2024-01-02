import sys

from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QLineEdit
from PyQt5.QtGui import QFont

from PyQt5 import QtCore
from PyQt5.QtCore import Qt

from math import ceil
from data import arr_of_elements
from widgets.elementInfo import InfoEl


class SlotEl(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.args = args
        self.initUI()

    def initUI(self):
        self.setGeometry(600, 400, 200, 200)
        self.setStyleSheet(
            "color: rgb(255, 255, 255);"
            "border: 0px solid #094065;"
            f"background-color: #{self.args[4]};"
        )

        self.num = QLineEdit(str(self.args[0]), self)
        self.num.setReadOnly(True)

        self.sym = QPushButton(self.args[1], self)
        if self.num.text() != '':
            self.sym.clicked.connect(self.showInfo)
        self.sym.setStyleSheet('text-align:left;')

        self.name = QLineEdit(self.args[2], self)
        self.name.setReadOnly(True)

        self.mass = QLineEdit(self)
        if self.args[3] != 0:
            self.mass.setText(str("{:.3f}".format(float(self.args[3]))))
        self.mass.setReadOnly(True)

        if self.args[0] != '':
            self.arr_of_counts = arr_of_elements[int(self.args[0])]["electrons"]
        else:
            self.arr_of_counts = []

        self.arr_of_orbs = []
        for cnt in self.arr_of_counts:
            orb = QLineEdit(str(cnt), self)
            orb.setReadOnly(True)
            orb.setAlignment(Qt.AlignRight)
            self.arr_of_orbs.append(orb)

    def resizeEvent(self, event):
        cur_size = self.size()
        cur_w = cur_size.width()
        cur_h = cur_size.height()
        a = min(cur_w, cur_h)

        size_base = a // 8
        font_base = QFont()
        font_base.setFamily('Arial')
        font_base.setPixelSize(size_base)

        size_sym = a // 4
        font_sym = QFont()
        font_sym.setFamily('Arial')
        font_sym.setPixelSize(size_sym)

        size_b_base = (a, ceil(size_base * 1.2))
        size_b_sym = (a, ceil(size_sym * 1.2))

        self.num.setFixedSize(*size_b_base)
        self.num.setFont(font_base)
        self.num.move(a // 16, a // 16)

        self.sym.setFixedSize(*size_b_sym)
        self.sym.setFont(font_sym)
        self.sym.move(a // 16, a // 4)

        self.name.setFixedSize(*size_b_base)
        self.name.setFont(font_base)
        self.name.move(a // 16, a // 2 + a // 16)

        self.mass.setFixedSize(*size_b_base)
        self.mass.setFont(font_base)
        self.mass.move(a // 16, a // 4 * 3)

        for i, orb in enumerate(self.arr_of_orbs):
            orb.setFixedSize(a // 8 + a // 16, a // 8)
            orb.setFont(font_base)
            orb.move(a // 4 * 3 + a // 16, (a // 16) + a // 8 * i)

        square_size = QtCore.QSize(a, a)
        self.resize(square_size)

        return super().resizeEvent(event)

    def showInfo(self):
        self.info = InfoEl(*self.args)
        self.info.show()


def main():
    app = QApplication(sys.argv)
    ex = SlotEl(118, 'Og', 'Оганесон', 294, '66AAFF', 8)
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
