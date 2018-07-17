#!/usr/bin/env python3

from commandbutton import CommandButton

import os
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QIcon

class Ninekey(QApplication):
    def __init__(self, args):
        super().__init__(args)
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
            label = conf_file.readline()
            command = conf_file.readline()
            newButton = CommandButton(self.window, label, command)
            buttons.append(newButton)

        for y in range(0, 3):
            for x in range(0, 3):
                buttons[x + y*3].move(100 * x, 100 * y)
                buttons[x + y*3].show()
