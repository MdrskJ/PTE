from math import ceil
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit
from PyQt5.QtGui import QFont
from PyQt5 import QtCore
from PyQt5.QtCore import Qt

from widgets.elementInfo import InfoEl
from widgets.slotConsts import *


class SlotEl(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.args = args
        self.initUI()

    def initUI(self):
        self.setStyleSheet(
            "color: rgb(255, 255, 255);"
            "border: 0px solid;"
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
            self.arr_of_counts = list(self.args[5].split())
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

        (indent_left, indent_left_orb, indent_top_num,
         indent_top_sym, indent_top_name, indent_top_mass) = get_indents(a)

        self.num.setFixedSize(*size_b_base)
        self.num.setFont(font_base)
        self.num.move(indent_left, indent_top_num)

        self.sym.setFixedSize(*size_b_sym)
        self.sym.setFont(font_sym)
        self.sym.move(indent_left, indent_top_sym)

        self.name.setFixedSize(*size_b_base)
        self.name.setFont(font_base)
        self.name.move(indent_left, indent_top_name)

        self.mass.setFixedSize(*size_b_base)
        self.mass.setFont(font_base)
        self.mass.move(indent_left, indent_top_mass)

        for i, orb in enumerate(self.arr_of_orbs):
            orb.setFixedSize(a // 8 + a // 16, a // 8)
            orb.setFont(font_base)
            orb.move(indent_left_orb, (a // 16) + a // 8 * i)

        square_size = QtCore.QSize(a, a)
        self.resize(square_size)

        return super().resizeEvent(event)

    def showInfo(self):
        self.info = InfoEl(self.args[0], self.args[6], self.args[7])
        self.info.show()
