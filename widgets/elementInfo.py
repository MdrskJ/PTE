import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPixmap
from PyQt5 import uic

from infoConsts import *
from data import arr_of_elements


class InfoEl(QWidget):
    def __init__(self, num):
        super().__init__()
        self.num = num
        self.args = arr_of_elements[num]
        uic.loadUi(ui_path, self)
        self.loadInfo()

    def loadInfo(self):
        self.setFixedSize(525, 850)
        self.setStyleSheet(
            "background-color: rgb(50, 50, 50);"
            "color: rgb(255, 255, 255);"
            "border: 0px solid #094065;"
        )

    # вносим данные в line1
        self.line1_background.setStyleSheet(island_style)
        self.sym.setText(self.args["symbol"])
        self.name.setText(self.args["name"])
        pixmap = QPixmap(f'{picture_dir_path}/{self.num}.jpg')
        pixmap = pixmap.scaled(150, 150)
        self.picture_of_element.setPixmap(pixmap)

    # вносим данные в line2
        self.line2_background.setStyleSheet(island_style)
        self.ch_electron.setText(self.args["atomic"])
        self.ch_proton.setText(self.args["atomic"])
        self.ch_neutron.setText(self.cntNeutron())

    # вносим данные в line3
        self.line3_background.setStyleSheet(island_style)
        self.ch_atomic_num.setText(self.args["atomic"])
        self.ch_mass.setText(self.args["weight"])

    # вносим данные в line4 и line5
        self.line45_background.setStyleSheet(island_style)
        self.text_electron_config.setText(self.args["expandedconfig"])
        self.text_electron_string.setText(self.args["electronstring"])

        if "valence" in self.args:
            self.text_valence.setText("0")
        else:
            self.text_valence.setText(self.args["oxidation"])

    # вносим данные в line6
        self.line6_background.setStyleSheet(island_style)
        self.date_discover.setText(self.args["discover"])
        self.ch_melt.setText(self.args["melt"])
        self.ch_boil.setText(self.args["boil"])
        self.ch_density.setText(self.args["density"]["stp"])
        self.ch_isotopes.setText(str(self.args["isotopes"]))

    def cntNeutron(self):
        return str(round(float(self.args["weight"])) - self.num)


def main():
    app = QApplication(sys.argv)
    ex = InfoEl(90)
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
