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

        self.showData()

        refresh = self.findChild(QPushButton, "refresh")
        saveButton = self.tabWidget.findChild(QPushButton)
        infoBox = self.tabWidget.findChild(QTextEdit)
        data = infoBox.toPlainText()
        saveButton.clicked.connect(self.insertData)
        refresh.clicked.connect(self.showData)

    def insertRowSatu(self, items):
        rowPosition = self.Modul_6.rowCount()
        self.Modul_6.insertRow(rowPosition)
        for x in range(len(items)):
            qtablewidgetitem = QTableWidgetItem()
            self.Modul_6.setItem(rowPosition, x, qtablewidgetitem)
            qtablewidgetitem = self.Modul_6.item(rowPosition, x)
            qtablewidgetitem.setText(items[x])

    def insertRowDua(self, items):
        rowPosition = self.Modul_7.rowCount()
        self.Modul_7.insertRow(rowPosition)
        for x in range(len(items)):
            qtablewidgetitem = QTableWidgetItem()
            self.Modul_7.setItem(rowPosition, x, qtablewidgetitem)
            qtablewidgetitem = self.Modul_7.item(rowPosition, x)
            qtablewidgetitem.setText(items[x])

    def insertRowTiga(self, items):
        rowPosition = self.Modul_8.rowCount()
        self.Modul_8.insertRow(rowPosition)
        for x in range(len(items)):
            qtablewidgetitem = QTableWidgetItem()
            self.Modul_8.setItem(rowPosition, x, qtablewidgetitem)
            qtablewidgetitem = self.Modul_8.item(rowPosition, x)
            qtablewidgetitem.setText(items[x])

    def insertData(self):
        open = gspread.service_account(
            filename="creds.json")
        sheets = open.open_by_key(
            "1gVmaW9uDWLIy7-B90HDruVZSlTZnTSGv_mGj-BmWRTo")
        worksheet = sheets.worksheet("MODUL 8")
        infoBox = self.tabWidget.findChild(QTextEdit)
        peserta = infoBox.toPlainText()
        worksheet.update_cell(2, 3, peserta)

    def showData(self):
        self.Modul_6.clear()
        self.Modul_7.clear()
        self.Modul_8.clear()

        self.Modul_6.setRowCount(0)
        self.Modul_7.setRowCount(0)
        self.Modul_8.setRowCount(0)
        open = gspread.service_account(filename="creds.json")
        sheets = open.open_by_key(
            "1gVmaW9uDWLIy7-B90HDruVZSlTZnTSGv_mGj-BmWRTo")

        worksheetsSatu = sheets.worksheet("MODUL 6")
        jadwalSatu = worksheetsSatu.get_all_values()
        for x in range(len(jadwalSatu)):
            self.insertRowSatu(jadwalSatu[x])

        worksheetsDua = sheets.worksheet("MODUL 7")
        jadwalDua = worksheetsDua.get_all_values()
        for x in range(len(jadwalDua)):
            self.insertRowDua(jadwalDua[x])

        worksheetsTiga = sheets.worksheet("MODUL 8")
        jadwalTiga = worksheetsTiga.get_all_values()
        for x in range(len(jadwalTiga)):
            self.insertRowTiga(jadwalTiga[x])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UI()
    window.show()
    sys.exit(app.exec())
