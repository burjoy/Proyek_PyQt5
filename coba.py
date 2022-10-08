import sys
import os
from json import load
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import gspread


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        loadUi("Design_Trial.ui", self)

        self.show()

        open = gspread.service_account(filename="creds.json")
        sheets = open.open_by_key(
            "1gVmaW9uDWLIy7-B90HDruVZSlTZnTSGv_mGj-BmWRTo")
        worksheet = sheets.sheet1

        jadwal = worksheet.get_all_values()
        for x in range(len(jadwal)):
            if x > 0:
                self.insertRow(jadwal[x])

    def insertRow(self, items):
        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)
        for x in range(len(items)):
            qtablewidgetitem = QTableWidgetItem()
            self.tableWidget.setItem(rowPosition, x, qtablewidgetitem)
            qtablewidgetitem = self.tableWidget.item(rowPosition, x)
            qtablewidgetitem.setText(items[x])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UI()
    window.show()
    sys.exit(app.exec())
