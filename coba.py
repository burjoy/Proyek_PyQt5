import sys
import os
from json import load
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import gspread
import numpy as np

hitung = 0


class UI(QMainWindow):
    def __init__(self, state=False):
        super(UI, self).__init__()
        loadUi("Design_Trial.ui", self)

        self.deterstate(state)
        self.show()
        global hitung

        open = gspread.service_account(filename="creds.json")
        sheets = open.open_by_key(
            "1gVmaW9uDWLIy7-B90HDruVZSlTZnTSGv_mGj-BmWRTo")

        worksheetsSatu = sheets.worksheet("MODUL 6")
        worksheetsDua = sheets.worksheet("MODUL 7")
        worksheetsTiga = sheets.worksheet("MODUL 8")
        wsarr = np.array([worksheetsSatu, worksheetsDua, worksheetsTiga])

        self.showData(wsarr)

        clear = self.findChild(QPushButton, "clear")
        clear.clicked.connect(lambda: self.clearData(
            self.tabWidget_2.currentIndex(), wsarr, state))

        saveButton = self.tabWidget.findChild(QPushButton)
        saveButton.clicked.connect(lambda: self.saveJadwal(wsarr))

        saveBtnAslab = self.findChild(QPushButton, "saveaslab")
        saveBtnAslab.clicked.connect(lambda: self.saveJadwalAslab(wsarr))
        # allval =

        # counter
        nambah = self.findChild(QPushButton, "incButton")
        kurang = self.findChild(QPushButton, "decButton")
        kelompok = self.findChild(QLabel, "layarHitung")
        kelompok.setNum(0)

        nambah.clicked.connect(self.counterUp)
        kurang.clicked.connect(self.counterDown)

        simpan = self.findChild(QPushButton, "simpan")
        simpan.clicked.connect(lambda: self.saveJadwal(wsarr))

    def deterstate(self, state):
        statelabel = self.findChild(QLabel, "label_5")
        statelabel.setStyleSheet("background-color: yellow; font: 12pt;")
        if state == True:
            statelabel.setText("Aslab")
            self.tabWidget.removeTab(0)
        else:
            statelabel.setText("Praktikan")
            self.tabWidget.removeTab(1)

    def saveJadwal(self, sheetp):

        modul6Sesi = self.findChild(QComboBox, "modul6_sesi")
        modul6Tanggal = self.findChild(QComboBox, "modul6_tanggal")
        modul7Sesi = self.findChild(QComboBox, "modul7_sesi")
        modul7Tanggal = self.findChild(QComboBox, "modul7_tanggal")
        modul8Sesi = self.findChild(QComboBox, "modul8_sesi")
        modul8Tanggal = self.findChild(QComboBox, "modul8_tanggal")
        prakarr = np.array([modul6Sesi,modul6Tanggal,modul7Sesi,modul7Tanggal,modul8Sesi,modul8Tanggal])

        # print('\n\nNo Kelompok :' + str(str(hitung)))
        # print('\nModul 6 :')
        # print("Tanggal :" + modul6Tanggal.currentText())
        # print("Sesi ke-" + modul6Sesi.currentText())

        # print('\nModul 7 :')
        # print("Tanggal :" + modul7Tanggal.currentText())
        # print("Sesi ke-" + modul7Sesi.currentText())

        # print('\nModul 8 :')
        # print("Tanggal :" + modul8Tanggal.currentText())
        # print("Sesi ke-" + modul8Sesi.currentText())

        #sesiPrak = np.array([int(modul6Sesi.currentText()), int(modul7Sesi.currentText()), int(modul8Sesi.currentText())])
        #hariPrak = np.array([modul6Tanggal.currentText(), modul7Tanggal.currentText(), modul8Tanggal.currentText()])

        self.pilihModul6(sheetp[0], int(modul6Sesi.currentText()),
                         modul6Tanggal.currentText())
        self.pilihModul7(sheetp[1], int(modul7Sesi.currentText()),
                         modul7Tanggal.currentText())
        self.pilihModul8(sheetp[2], int(modul8Sesi.currentText()),
                         modul8Tanggal.currentText())

        self.clearPrak(prakarr)
        self.showData(sheetp)

    def clearPrak(self,arr):
        self.counterUp()
        for i in range(len(arr)):
            arr[i].setCurrentIndex(0)


    def pilihModul6(self, sheetP, sesiPraktikum, hariPraktikum):
        if hariPraktikum == 'Senin (31/10)':
            hariP = 1
            if sesiPraktikum == 1:
                #curr = str(sheetP.cell(3, 2+hariP).value)+" "
                sheetP.update_cell(3, 2+hariP, str(hitung))
            elif sesiPraktikum == 2:
                sheetP.update_cell(5, 2+hariP, str(hitung))
            elif sesiPraktikum == 3:
                sheetP.update_cell(7, 2+hariP, str(hitung))
            elif sesiPraktikum == 4:
                sheetP.update_cell(9, 2+hariP, str(hitung))
        elif hariPraktikum == 'Selasa (1/11)':
            hariP = 2
            if sesiPraktikum == 1:
                sheetP.update_cell(3, 2+hariP, str(hitung))
            elif sesiPraktikum == 2:
                sheetP.update_cell(5, 2+hariP, str(hitung))
            elif sesiPraktikum == 3:
                sheetP.update_cell(7, 2+hariP, str(hitung))
            elif sesiPraktikum == 4:
                sheetP.update_cell(9, 2+hariP, str(hitung))
        elif hariPraktikum == 'Rabu (2/11)':
            hariP = 3
            if sesiPraktikum == 1:
                sheetP.update_cell(3, 2+hariP, str(hitung))
            elif sesiPraktikum == 2:
                sheetP.update_cell(5, 2+hariP, str(hitung))
            elif sesiPraktikum == 3:
                sheetP.update_cell(7, 2+hariP, str(hitung))
            elif sesiPraktikum == 4:
                sheetP.update_cell(9, 2+hariP, str(hitung))
        elif hariPraktikum == 'Kamis (3/11)':
            hariP = 4
            if sesiPraktikum == 1:
                sheetP.update_cell(3, 2+hariP, str(hitung))
            elif sesiPraktikum == 2:
                sheetP.update_cell(5, 2+hariP, str(hitung))
            elif sesiPraktikum == 3:
                sheetP.update_cell(7, 2+hariP, str(hitung))
            elif sesiPraktikum == 4:
                sheetP.update_cell(9, 2+hariP, str(hitung))
        elif hariPraktikum == 'Jumat (4/11)':
            hariP = 5
            if sesiPraktikum == 1:
                sheetP.update_cell(3, 2+hariP, str(hitung))
            elif sesiPraktikum == 2:
                sheetP.update_cell(5, 2+hariP, str(hitung))
            elif sesiPraktikum == 3:
                sheetP.update_cell(7, 2+hariP, str(hitung))
            elif sesiPraktikum == 4:
                sheetP.update_cell(9, 2+hariP, str(hitung))

    def pilihModul7(self, sheetP, sesiPraktikum, hariPraktikum):
        if hariPraktikum == 'Senin (7/11)':
            hariP = 1
            if sesiPraktikum == 1:
                sheetP.update_cell(3, 2+hariP, str(hitung))
            elif sesiPraktikum == 2:
                sheetP.update_cell(5, 2+hariP, str(hitung))
            elif sesiPraktikum == 3:
                sheetP.update_cell(7, 2+hariP, str(hitung))
            elif sesiPraktikum == 4:
                sheetP.update_cell(9, 2+hariP, str(hitung))
        elif hariPraktikum == 'Selasa (8/11)':
            hariP = 2
            if sesiPraktikum == 1:
                sheetP.update_cell(3, 2+hariP, str(hitung))
            elif sesiPraktikum == 2:
                sheetP.update_cell(5, 2+hariP, str(hitung))
            elif sesiPraktikum == 3:
                sheetP.update_cell(7, 2+hariP, str(hitung))
            elif sesiPraktikum == 4:
                sheetP.update_cell(9, 2+hariP, str(hitung))
        elif hariPraktikum == 'Rabu (9/11)':
            hariP = 3
            if sesiPraktikum == 1:
                sheetP.update_cell(3, 2+hariP, str(hitung))
            elif sesiPraktikum == 2:
                sheetP.update_cell(5, 2+hariP, str(hitung))
            elif sesiPraktikum == 3:
                sheetP.update_cell(7, 2+hariP, str(hitung))
            elif sesiPraktikum == 4:
                sheetP.update_cell(9, 2+hariP, str(hitung))
        elif hariPraktikum == 'Kamis (10/11)':
            hariP = 4
            if sesiPraktikum == 1:
                sheetP.update_cell(3, 2+hariP, str(hitung))
            elif sesiPraktikum == 2:
                sheetP.update_cell(5, 2+hariP, str(hitung))
            elif sesiPraktikum == 3:
                sheetP.update_cell(7, 2+hariP, str(hitung))
            elif sesiPraktikum == 4:
                sheetP.update_cell(9, 2+hariP, str(hitung))
        elif hariPraktikum == 'Jumat (11/11)':
            hariP = 5
            if sesiPraktikum == 1:
                sheetP.update_cell(3, 2+hariP, str(hitung))
            elif sesiPraktikum == 2:
                sheetP.update_cell(5, 2+hariP, str(hitung))
            elif sesiPraktikum == 3:
                sheetP.update_cell(7, 2+hariP, str(hitung))
            elif sesiPraktikum == 4:
                sheetP.update_cell(9, 2+hariP, str(hitung))

    def pilihModul8(self, sheetP, sesiPraktikum, hariPraktikum):
        if hariPraktikum == 'Senin (14/11)':
            hariP = 1
            if sesiPraktikum == 1:
                sheetP.update_cell(3, 2+hariP, str(hitung))
            elif sesiPraktikum == 2:
                sheetP.update_cell(5, 2+hariP, str(hitung))
            elif sesiPraktikum == 3:
                sheetP.update_cell(7, 2+hariP, str(hitung))
            elif sesiPraktikum == 4:
                sheetP.update_cell(9, 2+hariP, str(hitung))
        elif hariPraktikum == 'Selasa (15/11)':
            hariP = 2
            if sesiPraktikum == 1:
                sheetP.update_cell(3, 2+hariP, str(hitung))
            elif sesiPraktikum == 2:
                sheetP.update_cell(5, 2+hariP, str(hitung))
            elif sesiPraktikum == 3:
                sheetP.update_cell(7, 2+hariP, str(hitung))
            elif sesiPraktikum == 4:
                sheetP.update_cell(9, 2+hariP, str(hitung))
        elif hariPraktikum == 'Rabu (16/11)':
            hariP = 3
            if sesiPraktikum == 1:
                sheetP.update_cell(3, 2+hariP, str(hitung))
            elif sesiPraktikum == 2:
                sheetP.update_cell(5, 2+hariP, str(hitung))
            elif sesiPraktikum == 3:
                sheetP.update_cell(7, 2+hariP, str(hitung))
            elif sesiPraktikum == 4:
                sheetP.update_cell(9, 2+hariP, str(hitung))
        elif hariPraktikum == 'Kamis (17/11)':
            hariP = 4
            if sesiPraktikum == 1:
                sheetP.update_cell(3, 2+hariP, str(hitung))
            elif sesiPraktikum == 2:
                sheetP.update_cell(5, 2+hariP, str(hitung))
            elif sesiPraktikum == 3:
                sheetP.update_cell(7, 2+hariP, str(hitung))
            elif sesiPraktikum == 4:
                sheetP.update_cell(9, 2+hariP, str(hitung))
        elif hariPraktikum == 'Jumat (18/11)':
            hariP = 5
            if sesiPraktikum == 1:
                sheetP.update_cell(3, 2+hariP, str(hitung))
            elif sesiPraktikum == 2:
                sheetP.update_cell(5, 2+hariP, str(hitung))
            elif sesiPraktikum == 3:
                sheetP.update_cell(7, 2+hariP, str(hitung))
            elif sesiPraktikum == 4:
                sheetP.update_cell(9, 2+hariP, str(hitung))

    def saveJadwalAslab(self, sheetar):
        kodeAslab = self.findChild(QLineEdit, "kodeaslab")
        modulAslab = self.findChild(QComboBox, "modulaslab")
        hariAslab = self.findChild(QComboBox, "hariaslab")
        sesi1aslab = self.findChild(QCheckBox, "sesi1aslab")
        sesi2aslab = self.findChild(QCheckBox, "sesi2aslab")
        sesi3aslab = self.findChild(QCheckBox, "sesi3aslab")
        sesi4aslab = self.findChild(QCheckBox, "sesi4aslab")
        sesiArray = np.array([sesi1aslab, sesi2aslab, sesi3aslab, sesi4aslab])
        sesiaslab = np.array([sesi1aslab.isChecked(), sesi2aslab.isChecked(
        ), sesi3aslab.isChecked(), sesi4aslab.isChecked()])
        #print(kodeAslab.text(), modulAslab.currentText(), hariAslab.currentText())
        # print(sesiaslab)

        if kodeAslab.text() == '':
            self.error("Tidak ada Kode Aslab")
            return
        else:
            if modulAslab.currentText() == "Modul 6":
                self.aslabUpdate(
                    sheetar[0], hariAslab.currentText(), sesiaslab, kodeAslab.text())
            elif modulAslab.currentText() == "Modul 7":
                self.aslabUpdate(
                    sheetar[1], hariAslab.currentText(), sesiaslab, kodeAslab.text())
            elif modulAslab.currentText() == "Modul 8":
                self.aslabUpdate(
                    sheetar[2], hariAslab.currentText(), sesiaslab, kodeAslab.text())

            self.aslabclear(hariAslab, modulAslab, sesiArray)

        self.showData(sheetar)

    def aslabUpdate(self, sheet, hari, sesiarr, kode):
        if hari == 'Senin':
            inthari = 1
            for i in range(len(sesiarr)):
                if sesiarr[i] == True:
                    sheet.update_cell(2+2*i, 2+inthari, kode)

        elif hari == 'Selasa':
            inthari = 2
            for i in range(len(sesiarr)):
                if sesiarr[i] == True:
                    sheet.update_cell(2+2*i, 2+inthari, kode)

        elif hari == 'Rabu':
            inthari = 3
            for i in range(len(sesiarr)):
                if sesiarr[i] == True:
                    sheet.update_cell(2+2*i, 2+inthari, kode)

        elif hari == 'Kamis':
            inthari = 4
            for i in range(len(sesiarr)):
                if sesiarr[i] == True:
                    sheet.update_cell(2+2*i, 2+inthari, kode)

        elif hari == 'Jumat':
            inthari = 5
            for i in range(len(sesiarr)):
                if sesiarr[i] == True:
                    sheet.update_cell(2+2*i, 2+inthari, kode)

    def aslabclear(self, hariAslab, modulAslab, sesiarr):
        hariAslab.setCurrentIndex(hariAslab.currentIndex()+1)
        if hariAslab.currentIndex() == -1:
            modulAslab.setCurrentIndex(modulAslab.currentIndex()+1)
            hariAslab.setCurrentIndex(0)
        sesiarr[0].setCheckState(False)
        sesiarr[1].setCheckState(False)
        sesiarr[2].setCheckState(False)
        sesiarr[3].setCheckState(False)

    def counterUp(self):
        global hitung
        hitung += 1
        kelompok = self.findChild(QLabel, "layarHitung")
        kelompok.setNum(hitung)

    def counterDown(self):
        global hitung
        hitung -= 1
        kelompok = self.findChild(QLabel, "layarHitung")
        kelompok.setNum(hitung)

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

    def showData(self, sheetarr):
        self.Modul_6.clear()
        self.Modul_7.clear()
        self.Modul_8.clear()

        self.Modul_6.setRowCount(0)
        self.Modul_7.setRowCount(0)
        self.Modul_8.setRowCount(0)

        jadwalSatu = sheetarr[0].get_all_values()
        for x in range(len(jadwalSatu)):
            self.insertRowSatu(jadwalSatu[x])

        jadwalDua = sheetarr[1].get_all_values()
        for x in range(len(jadwalDua)):
            self.insertRowDua(jadwalDua[x])

        jadwalTiga = sheetarr[2].get_all_values()
        for x in range(len(jadwalTiga)):
            self.insertRowTiga(jadwalTiga[x])

    def clearData(self, tabnum, wsarr, state):
        rangeaslab = ["C2:G2", "C4:G4", "C6:G6", "C8:G8"]
        rangepraktikan = ["C3:G3", "C5:G5", "C7:G7", "C9:G9"]
        if state == True:
            wsarr[tabnum].batch_clear(rangeaslab)
        elif state == False:
            wsarr[tabnum].batch_clear(rangepraktikan)
        self.showData(wsarr)

    def error(self, errormsg):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Error")
        msg.setInformativeText(errormsg)
        msg.setWindowTitle("Error")
        msg.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UI()
    window.show()
    sys.exit(app.exec())
