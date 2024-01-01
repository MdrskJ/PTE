import sys
from PyQt5.QtWidgets import QLabel, QApplication
from PyQt5.QtWidgets import QWidget


class InfoEl(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.args = args
        self.initUI()

    def initUI(self):
        # self.setWindowFlags(Qt.FramelessWindowHint)
        self.setGeometry(80, 80, 500, 800)
        self.setWindowTitle(self.args[0])

        self.name = QLabel(self.args[0], self)
        self.name.adjustSize()
        self.name.move(70, 70)


def main():
    app = QApplication(sys.argv)
    ex = InfoEl('123')
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
