import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *

import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def smCal(a,b,c):

    ans = a+b+c

    return ans

form = resource_path("simple.ui")
form_class = uic.loadUiType(form)[0]

#화면을 띄우는데 사용되는 Class 선언


class Worker1(QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

    def run(self):
        self.parent.label.setText('%f' %smCal(float(self.parent.lineEdit.text()),float(self.parent.lineEdit_2.text())
                                     ,float(self.parent.lineEdit_3.text())))

class Worker2(QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

    def run(self):
        self.parent.label.setText('%f' %smCal(float(self.parent.lineEdit.text()),float(self.parent.lineEdit_2.text())
                                     ,float(self.parent.lineEdit_3.text())))

class Worker3(QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

    def run(self):
        self.parent.label.setText('%f' %smCal(float(self.parent.lineEdit.text()),float(self.parent.lineEdit_2.text())
                                     ,float(self.parent.lineEdit_3.text())))

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.lineEdit.textChanged.connect(self.actionFunction1)
        self.lineEdit_2.textChanged.connect(self.actionFunction2)
        self.lineEdit_3.textChanged.connect(self.actionFunction3)

    def actionFunction1(self):
        h1 = Worker1(self)
        h1.start()

    def actionFunction2(self):
        h2 = Worker2(self)
        h2.start()

    def actionFunction3(self):
        h3 = Worker3(self)
        h3.start()


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()