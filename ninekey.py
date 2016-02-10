#!/usr/bin/env python3

import sys
import os
from multiprocessing import Process
import subprocess
import shlex
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

        if os.path.exists(os.path.expanduser("~/.config/ninekey/ninekey.conf")):
            conf_file = open(os.path.expanduser("~/.config/ninekey/ninekey.conf"),"r")
        elif os.path.exists(os.path.expanduser("~/.config/ninekey")):
            conf_file = open(os.path.expanduser("~/.config/ninekey/ninekey.conf"),"w+")
        else:
            os.mkdir(os.path.expanduser("~/.config/ninekey/"))
            conf_file = open(os.path.expanduser("~/.config/ninekey/ninekey.conf"),"w+")

        buttons = []
        for i in range(9):
            newButton = QPushButton(self.window)
            newButton.resize(100, 100)
            newButton.setText(conf_file.readline())
            newButton.command = conf_file.readline()
            if newButton.command:
                newButton.clicked.connect(self.startProcess)
                newButton.setToolTip(newButton.command)
            else:
                newButton.setDisabled(True)

            buttons.append(newButton)

        for y in range(0, 3):
            for x in range(0, 3):
                buttons[x + y*3].move(100 * x, 100 * y)
                buttons[x + y*3].show()

    def startProcess(self):
        sender = self.sender()
        commandProcess = Process(target=self.runCommand, args=(sender.command,))
        commandProcess.start()

    def runCommand(self, command):
        subprocess.run(shlex.split(command))
        

if __name__ == "__main__":
    app = Ninekey(sys.argv)
