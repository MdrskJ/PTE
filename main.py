import sys
from math import ceil
import sqlite3

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QScrollArea
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QGridLayout
from PyQt5.QtCore import Qt

import widgets
from mainConsts import *


class PTE(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(QApplication.desktop().geometry())
        self.setWindowTitle('The Periodic Table of the Elements')
        self.setStyleSheet(
            "background-color: rgb(50, 50, 50);"
        )

        self.surfaceMain = QWidget()
        self.setCentralWidget(self.surfaceMain)

        self.scrollVLayout = QVBoxLayout()
        self.surfaceMain.setLayout(self.scrollVLayout)
        self.scrollHLayout = QHBoxLayout()
        self.scrollVLayout.addLayout(self.scrollHLayout)

        self.scrollArea = QScrollArea()
        self.scrollHLayout.addWidget(self.scrollArea)

        self.surfacePTE = QWidget()

        W, H = ceil(self.size().width() * k_for_task_bar), ceil(self.size().height() * k_for_task_bar)
        k = cnt_columns / cnt_strings
        if W / H > k:
            self.surfacePTE.resize(ceil(H * k), H)
        else:
            self.surfacePTE.resize(W, ceil(W / k))

        self.scrollArea.setWidget(self.surfacePTE)

        self.surfacePTEVLayout = QVBoxLayout()
        self.surfacePTE.setLayout(self.surfacePTEVLayout)

        self.mainElLayout = QGridLayout()
        self.mainElLayout.setSpacing(1)
        self.surfacePTEVLayout.addLayout(self.mainElLayout)

        con = sqlite3.connect("elements_db.sqlite")
        cur = con.cursor()

    # создание и расположение слотов элементов
        result = cur.execute("""
                SELECT elements.num, elements.sym, elements.name, elements.mass, types.color, elements.electrons,
                elements.pos_x, elements.pos_y
                FROM elements INNER JOIN types
                    ON elements.type = types.id""").fetchall()

        for info in result:
            slotLayout = QHBoxLayout()
            slot = widgets.SlotEl(*info)
            slotLayout.addWidget(slot)

            item = QWidget()
            item.setLayout(slotLayout)
            item.setStyleSheet(
                "color: rgb(255, 255, 255);"
                f"background-color: #{info[4]};"
            )

            self.mainElLayout.addWidget(item, info[6], info[7])

    # создание подписей групп и высших оксидов
        result = cur.execute("""
                SELECT groups.convert, groups.oxid, groups.pos_x, groups.pos_y
                FROM groups""").fetchall()

        for info in result:
            groupLayout = QHBoxLayout()
            groupLayout.addWidget(widgets.SlotEl('', info[0], '', 0, None, '00ffffff'))

            item = QWidget()
            item.setLayout(groupLayout)
            item.setStyleSheet(sign_style)
            self.mainElLayout.addWidget(item, info[2], info[3])

            oxidLayout = QHBoxLayout()
            oxidLayout.addWidget(widgets.SlotEl('', info[1], '', 0, None, '00ffffff'))

            item = QWidget()
            item.setLayout(oxidLayout)
            item.setStyleSheet(sign_style)
            self.mainElLayout.addWidget(item, 8, info[3])

        con.close()

    # создание подписей периодов
        for i in range(1, 8):
            periodLayout = QHBoxLayout()
            periodLayout.addWidget(widgets.SlotEl('', f'          {i}', '', 0, None, '00ffffff'))

            item = QWidget()
            item.setLayout(periodLayout)
            item.setStyleSheet(sign_style)
            self.mainElLayout.addWidget(item, i, 0)

    # создание слота лантаноидов
        lanSlotLayout = QHBoxLayout()
        lanSlotLayout.addWidget(widgets.SlotEl('', '57-71', 'Лантаноиды', 0, 'DDAACB', 8))

        lan = QWidget()
        lan.setLayout(lanSlotLayout)
        lan.setStyleSheet(sign_lan_style)
        self.mainElLayout.addWidget(lan, 6, 3)

     # создание слота актиноидов
        actSlotLayout = QHBoxLayout()
        actSlotLayout.addWidget(widgets.SlotEl('', '89-103', 'Актиноиды', 0, 'BBAADE', 8))

        act = QWidget()
        act.setLayout(actSlotLayout)
        act.setStyleSheet(sign_act_style)
        self.mainElLayout.addWidget(act, 7, 3)

        self.surfaceGroups = QWidget(self.surfacePTE)
        self.surfaceGroups.setStyleSheet(
            "background-color: rgb(100, 100, 100);"
            "border-radius: 20px"
            )

    #создаём таблицу с подписями групп элементов
        self.groupsLayout = QHBoxLayout()
        self.groupsLayout.addWidget(widgets.GTW())
        self.surfaceGroups.setLayout(self.groupsLayout)
        self.surfaceGroups.resize(int(self.surfacePTE.size().width() // 2.3),
                                  int(self.surfacePTE.size().height() // 4.6))
        self.surfaceGroups.move(int(self.surfacePTE.size().width() // 4.8),
                                int(self.surfacePTE.size().height() // 13.1))

    def keyPressEvent(self, event):
        if int(event.modifiers()) == Qt.CTRL:
            x, y = self.surfacePTE.x(), self.surfacePTE.y()
            k = cnt_columns / cnt_strings
            if event.key() == Qt.Key_P:
                d = v
                h = self.surfacePTE.size().height() + d
                self.surfacePTE.resize(ceil(h * k), h)

                self.surfaceGroups.resize(int(self.surfacePTE.size().width() // 2.3),
                                          int(self.surfacePTE.size().height() // 4.6))
                self.surfaceGroups.move(int(self.surfacePTE.size().width() // 4.8),
                                        int(self.surfacePTE.size().height() // 13.1))

                self.surfacePTE.move(int(x - (d * k) // 2), int(y - d // 2))
            if event.key() == Qt.Key_M:
                d = -v
                h = self.surfacePTE.size().height() + d
                self.surfacePTE.resize(ceil(h * k), h)

                self.surfaceGroups.resize(int(self.surfacePTE.size().width() // 2.3),
                                          int(self.surfacePTE.size().height() // 4.6))
                self.surfaceGroups.move(int(self.surfacePTE.size().width() // 4.8),
                                        int(self.surfacePTE.size().height() // 13.1))

                self.surfacePTE.move(int(x - (d * k) // 2), int(y - d // 2))


def main():
    app = QApplication(sys.argv)
    ex = PTE()
    ex.showMaximized()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
