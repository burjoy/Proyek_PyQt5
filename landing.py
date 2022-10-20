import sys
import os
from json import load
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
import gspread
from coba import UI

class landingUI(QtWidgets.QMainWindow):
    def openmain(self, state):
        self.window = UI(state)
        #print (state)

    def __init__(self):
        super(landingUI, self).__init__()
        loadUi("landing.ui", self)
        self.show()

        LoginBtn = self.findChild(QtWidgets.QPushButton, "LoginBtn")
        LoginBtn.autoDefault()
        LoginBtn.clicked.connect(self.loginAtt)

        PrakBtn = self.findChild(QtWidgets.QPushButton, "PrakBtn")
        #PrakBtn.clicked.connect(self.prakAtt)
        PrakBtn.clicked.connect(lambda : self.openmain(False))
    
    def loginAtt(self):
        pw = self.lineEdit.text()
        if (pw == 'password123'):
            self.aslab = True
            self.close()
            self.openmain(True)
        else :
            self.error('Password Salah!')
            self.lineEdit.clear()
            return

    def prakAtt(self):
        self.aslab = False
        self.close()
        self.openmain(False)
            
    def error(self,errormsg):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText("Error")
        msg.setInformativeText(errormsg)
        msg.setWindowTitle("Error")
        msg.exec_()
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = landingUI()
    window.show()
    sys.exit(app.exec())