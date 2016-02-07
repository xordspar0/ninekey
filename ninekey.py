#!/usr/bin/env python3

import sys
import os
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QIcon

class Ninekey(QApplication):
    def __init__(self, args):
        QApplication.__init__(self, args)
        self.addWidgets()
        self.exec_()

    def addWidgets(self):
        self.window = QWidget()
        self.window.setFixedSize(300, 300)
        self.window.setWindowTitle("Ninekey")
        self.window.setWindowIcon(QIcon("ninekey.png"))
        self.window.show()

        buttons = []
        if os.path.exists(os.path.expanduser("~/.config/ninekey/ninekey.conf")):
            conf_file = open(os.path.expanduser("~/.config/ninekey/ninekey.conf"),"r")
        elif os.path.exists(os.path.expanduser("~/.config/ninekey")):
            conf_file = open(os.path.expanduser("~/.config/ninekey/ninekey.conf"),"w+")
        else:
            os.mkdir(os.path.expanduser("~/.config/ninekey/"))
            conf_file = open(os.path.expanduser("~/.config/ninekey/ninekey.conf"),"w+")

        for i in range(0, 9):
            name = conf_file.readline()
            buttons.append(QPushButton(name, self.window))
            buttons[i].command = conf_file.readline()
            buttons[i].clicked.connect(self.runCommand)
            buttons[i].setToolTip(buttons[i].command)
            buttons[i].resize(100, 100)

        for y in range(0, 3):
            for x in range(0, 3):
                buttons[x + y*3].move(100 * x, 100 * y)
                buttons[x + y*3].show()

    def runCommand(self):
        sender = self.sender()
        os.system(sender.command)

if __name__ == "__main__":
    app = Ninekey(sys.argv)
