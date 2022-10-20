import sys
import os
from json import load
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import gspread


class UI(QMainWindow):
    def __init__(self, state='False'):
        super(UI, self).__init__()
        loadUi("Design_Trial.ui", self)

        print(state)
        self.show()

        open = gspread.service_account(filename="creds.json")
        sheets = open.open_by_key(
            "1gVmaW9uDWLIy7-B90HDruVZSlTZnTSGv_mGj-BmWRTo")
        worksheets = sheets.worksheet("MODUL 8")

        jadwal = worksheets.get_all_values()
        for x in range(len(jadwal)):
            self.insertRow(jadwal[x])

        saveButton = self.tabWidget.findChild(QPushButton)
        infoBox = self.tabWidget.findChild(QTextEdit)
        data = infoBox.toPlainText()
        saveButton.clicked.connect(self.insertData)

    def insertRow(self, items):
        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)
        for x in range(len(items)):
            qtablewidgetitem = QTableWidgetItem()
            self.tableWidget.setItem(rowPosition, x, qtablewidgetitem)
            qtablewidgetitem = self.tableWidget.item(rowPosition, x)
            qtablewidgetitem.setText(items[x])

    def insertData(self):
        open = gspread.service_account(filename="creds.json")
        sheets = open.open_by_key(
            "1gVmaW9uDWLIy7-B90HDruVZSlTZnTSGv_mGj-BmWRTo")
        worksheet = sheets.worksheet("MODUL 8")
        infoBox = self.tabWidget.findChild(QTextEdit)
        peserta = infoBox.toPlainText()
        worksheet.update_cell(2, 3, peserta)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UI()
    window.show()
    sys.exit(app.exec())
