import sys
from PyQt5.QtWidgets import QApplication, QSizePolicy
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
from infoConsts import *


class InfoEl(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.args = args
        uic.loadUi(ui_path, self)
        self.loadInfo()

    def loadInfo(self):
        self.setFixedSize(525, 850)
        self.setStyleSheet(
            "background-color: rgb(50, 50, 50);"
            "color: rgb(255, 255, 255);"
            "border: 0px solid #094065;"
        )

        self.line1_background.setStyleSheet(
            "background-color: rgb(100, 100, 100);"
            "border-radius: 20px;"
        )
        self.sym.setText(self.args[1])
        self.name.setText(self.args[2])
        pixmap = QPixmap(f'pictures_of_elements/{self.args[0]}.jpg')
        pixmap = pixmap.scaled(150, 150)
        self.picture_of_element.setPixmap(pixmap)




def main():
    app = QApplication(sys.argv)
    ex = InfoEl(10, 'Ne', 'Неон', '20.1797', '66AAFF', 8, 2, 19)
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
