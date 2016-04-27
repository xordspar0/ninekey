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
        appname = "ninekey"
        apptitle = "Ninekey"

        self.window = QWidget()
        self.window.setFixedSize(300, 300)
        self.window.setWindowTitle(apptitle)
        self.window.setWindowIcon(QIcon(appname + ".png"))
        self.window.show()

        # Set up the config file.
        if os.name == "posix":
            conf_dir_path = "/".join([os.environ["HOME"], ".config", appname])
            conf_file_path = "/".join([conf_dir_path, appname + ".conf"])
        elif os.name == "nt":
            conf_dir = "\\".join(["%APPDATA%", appname])
            conf_file_path = "\\".join([conf_dir_path, appname + ".conf"])
        else:
            conf_dir = ""
            conf_file_path = appname + ".conf"
        
        if not os.path.exists(conf_dir_path):
            os.mkdir(conf_dir_path)

        if os.path.exists(conf_file_path):
            conf_file = open(conf_file_path,"r")
        else:
            conf_file = open(conf_file_path,"w+")

        # Add the buttons.
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

    # Spawn a new process that will run the command.
    def startProcess(self):
        sender = self.sender()
        commandProcess = Process(target=self.runCommand, args=(sender.command,))
        commandProcess.start()

    def runCommand(self, command):
        subprocess.run(shlex.split(command))
        

if __name__ == "__main__":
    app = Ninekey(sys.argv)
