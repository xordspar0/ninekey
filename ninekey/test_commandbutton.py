from ninekey.commandbutton import CommandButton

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget

import unittest

class TestCommandButton(unittest.TestCase):
    class TestApplication(QApplication):
        def __init__(self):
            QApplication.__init__(self, [])
            self.window = QWidget()

    def setUp(self):
        self.app = self.TestApplication()

    def test_set_command(self):
        button = CommandButton(self.app.window, 'test', '')
        button.setCommand('echo hello')
        self.assertEqual(button.command, ['echo', 'hello'])

    def test_start_process(self):
        button = CommandButton(self.app.window, 'test', 'true')
        process = button.startProcess()
        process.join(0.1)
        self.assertEqual(process.exitcode, 0)
