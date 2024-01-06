import sys

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5 import uic

from widgets.infoConsts import *


class InfoEl(QWidget):
    def __init__(self, num, pos_x, pos_y):
        super().__init__()
        self.num = num
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.args = open_csv_file(self.num)
        uic.loadUi(ui_path, self)
        self.loadInfo()

    def loadInfo(self):
        self.setFixedSize(525, 850)
        self.setWindowTitle(window_name_convert(self.args["name"]))
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
        self.ch_mass.setText(weight_convert(self.args["weight"]))
        self.ch_group.setText(str(self.pos_y))
        self.ch_period.setText(str(group_convert(self.pos_x)))

    # вносим данные в line4 и line5
        self.line45_background.setStyleSheet(island_style)
        self.text_electron_config.setText(self.args["expandedconfig"])
        self.text_electron_string.setText(self.args["electronstring"])
        self.text_oxidation.setText(oxidation_convert(self.args["oxidation"]))

    # вносим данные в line6
        self.line6_background.setStyleSheet(island_style)
        self.date_discover.setText(date_covert(self.args["discover"]))
        self.ch_melt.setText(temperature_convert(self.args["melt"]))
        self.ch_boil.setText(temperature_convert(self.args["boil"]))
        self.ch_density_stp.setText(density_convert(self.args["density_stp"]))
        self.ch_density_liquid.setText(density_convert(self.args["density_liquid"]))
        self.ch_isotopes.setText(self.args["isotopes"])

    def cntNeutron(self):
        return str(round(float(self.args["weight"])) - self.num)


def main():
    app = QApplication(sys.argv)
    ex = InfoEl(17, 3, 17)
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
