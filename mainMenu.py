from json import load
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import sys


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        loadUi("DesignAwal.ui", self)
        self.calendar = self.findChild(QCalendarWidget, "calendar")
        self.DateLabel = self.findChild(QLabel, "labelDate")
        self.calendar.selectionChanged.connect(self.launchCalendar)

        self.show()

    def launchCalendar(self):
        selectedDate = self.calendar.selectedDate()
        self.DateLabel.setText(selectedDate.toString())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UI()
    window.show()
    sys.exit(app.exec())
