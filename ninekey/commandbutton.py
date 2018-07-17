from PyQt5.QtWidgets import QPushButton
from multiprocessing import Process
import shlex
import subprocess

class CommandButton(QPushButton):
    def __init__(self, parent, label, command):
        super().__init__(parent)
        self.resize(100, 100)
        self.setText(label)
        self.setCommand(command)
        self.clicked.connect(self.startProcess)

    def setCommand(self, command):
        """Parse a string into tokens that make up a command."""
        self.command = shlex.split(command)

        if self.command:
            self.setToolTip(' '.join(self.command))
        else:
            self.setToolTip('')
            self.setDisabled(True)

    def startProcess(self):
        """Spawn a new process that will run the command."""
        commandProcess = Process(target=subprocess.run, args=(self.command,))
        commandProcess.start()
        return commandProcess
