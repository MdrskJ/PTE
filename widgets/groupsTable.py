import sys
import sqlite3
from math import ceil

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QFont
from PyQt5 import uic

from widgets.groupsConsts import *


class GTW(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(ui_path, self)
        self.initUI()

    def initUI(self):
        self.setStyleSheet(
            "background-color: rgb(100, 100, 100);"
            "color: rgb(255, 255, 255);"
            "border: 0px;"
        )

        self.alkali_metals.setStyleSheet('text-align:left;')
        self.alkaline_earth_metals.setStyleSheet('text-align:left;')
        self.transitionmetals.setStyleSheet('text-align:left;')
        self.posttransition_metals.setStyleSheet('text-align:left;')
        self.semimetals.setStyleSheet('text-align:left;')
        self.nonmetals.setStyleSheet('text-align:left;')
        self.halogens.setStyleSheet('text-align:left;')
        self.inert_gases.setStyleSheet('text-align:left;')
        self.lanthanides.setStyleSheet('text-align:left;')
        self.actinoids.setStyleSheet('text-align:left;')

        con = sqlite3.connect("elements_db.sqlite")

        cur = con.cursor()

        result = cur.execute("""
                        SELECT types.color
                        FROM types""").fetchall()

        self.alkali_metals_pict.setStyleSheet(f'background-color: #{get_color(result, 0)};')
        self.alkaline_earth_metals_pict.setStyleSheet(f'background-color: #{get_color(result, 1)};')
        self.transitionmetals_pict.setStyleSheet(f'background-color: #{get_color(result, 2)};')
        self.posttransition_metals_pict.setStyleSheet(f'background-color: #{get_color(result, 3)};')
        self.semimetals_pict.setStyleSheet(f'background-color: #{get_color(result, 4)};')
        self.nonmetals_pict.setStyleSheet(f'background-color: #{get_color(result, 5)};')
        self.halogens_pict.setStyleSheet(f'background-color: #{get_color(result, 6)};')
        self.inert_gases_pict.setStyleSheet(f'background-color: #{get_color(result, 7)};')
        self.lanthanides_pict.setStyleSheet(f'background-color: #{get_color(result, 8)};')
        self.actinoids_pict.setStyleSheet(f'background-color: #{get_color(result, 9)};')

    def resizeEvent(self, event):
        cur_size = self.size()
        cur_w = cur_size.width()
        cur_h = cur_size.height()
        a = min(cur_w, cur_h)
        a_icon = a // 6

        self.alkali_metals_pict.setFixedSize(a_icon, a_icon)
        self.alkaline_earth_metals_pict.setFixedSize(a_icon, a_icon)
        self.transitionmetals_pict.setFixedSize(a_icon, a_icon)
        self.posttransition_metals_pict.setFixedSize(a_icon, a_icon)
        self.semimetals_pict.setFixedSize(a_icon, a_icon)
        self.nonmetals_pict.setFixedSize(a_icon, a_icon)
        self.halogens_pict.setFixedSize(a_icon, a_icon)
        self.inert_gases_pict.setFixedSize(a_icon, a_icon)
        self.lanthanides_pict.setFixedSize(a_icon, a_icon)
        self.actinoids_pict.setFixedSize(a_icon, a_icon)

        size_base = a // 9
        font_base = QFont()
        font_base.setPixelSize(size_base)

        size_b_base = (ceil(a * 1.5), ceil(size_base * 1.2))

        self.alkali_metals.setFont(font_base)
        self.alkali_metals.setFixedSize(*size_b_base)

        self.alkaline_earth_metals.setFont(font_base)
        self.alkaline_earth_metals.setFixedSize(*size_b_base)

        self.transitionmetals.setFont(font_base)
        self.transitionmetals.setFixedSize(*size_b_base)

        self.posttransition_metals.setFont(font_base)
        self.posttransition_metals.setFixedSize(*size_b_base)

        self.semimetals.setFont(font_base)
        self.semimetals.setFixedSize(*size_b_base)

        self.nonmetals.setFont(font_base)
        self.nonmetals.setFixedSize(*size_b_base)

        self.halogens.setFont(font_base)
        self.halogens.setFixedSize(*size_b_base)

        self.inert_gases.setFont(font_base)
        self.inert_gases.setFixedSize(*size_b_base)

        self.lanthanides.setFont(font_base)
        self.lanthanides.setFixedSize(*size_b_base)

        self.actinoids.setFont(font_base)
        self.actinoids.setFixedSize(*size_b_base)


def main():
    app = QApplication(sys.argv)
    ex = GTW()
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
