#!/usr/bin/python3

import sys
import os
from PyQt4 import Qt
from PyQt4 import QtGui

class Ninekey(Qt.QApplication):
    def __init__(self, args):
        Qt.QApplication.__init__(self, args)
        self.addWidgets()
        self.exec_()

    def addWidgets(self):
        self.window = QtGui.QWidget()
        self.window.setFixedSize(300, 300)
        self.window.setWindowTitle("Ninekey")
        self.window.setWindowIcon(QtGui.QIcon("ninekey.png"))
        self.window.show()

        buttons = []
        conf_file = open(os.path.expanduser("~/.config/ninekey/ninekey.conf"),"r")

        for i in range(0, 9):
            name = conf_file.readline()
            buttons.append(QtGui.QPushButton(name, self.window))
            buttons[i].command = conf_file.readline()
            self.connect(buttons[i], Qt.SIGNAL("clicked()"), self.run_command)
            buttons[i].setToolTip(buttons[i].command)
            buttons[i].resize(100, 100)

        for x in range(0, 3):
            for y in range(0, 3):
                buttons[x*3 + y].move(100 * x, 100 * y)
                buttons[x*3 + y].show()

    def run_command(self):
        sender = self.sender()
        os.system(sender.command)

if __name__ == "__main__":
    app = Ninekey(sys.argv)
