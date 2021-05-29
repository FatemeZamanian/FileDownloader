# This Python file uses the following encoding: utf-8
import sys
import os
import urllib.request

from PySide6.QtWidgets import QApplication, QWidget,QMessageBox,QFileDialog
from PySide6 import *
from PyQt5.QtCore import QDir
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader


class FileDownloader(QWidget):
    def __init__(self):
        super(FileDownloader, self).__init__()
        loader = QUiLoader()
        self.ui = loader.load('form.ui')
        self.ui.show()
        self.setFocus()
        self.ui.btn_download.clicked.connect(self.download)
        self.ui.btn_browse.clicked.connect(self.browse)

    def browse(self):
        save=QFileDialog.getSaveFileName(self,caption="Save file as",dir=".",filter="All Files (*.*)")
        self.ui.txt_location.setText(QDir.toNativeSeparators(save[0]))

    def download(self):
        url=self.ui.txt_url.text()
        location=self.ui.txt_location.text()
        while True:
            if location=="":
                QMessageBox.warning(self, "Warning!", "please select file location and name")
                self.browse()
                location = self.ui.txt_location.text()
            else:
                break
        try:
            urllib.request.urlretrieve(url,location,self.report)
            QMessageBox.information(self, "Information", "The download is complete")
            self.ui.progress.setValue(0)
            self.ui.txt_url.setText("")
            self.ui.txt_location.setText("")
        except Exception:
            QMessageBox.warning(self,"Warning!","The download failed")
            return




    def report(self,blockNum,blockSize,totalSize):
        rs=blockNum*blockSize
        if totalSize>0:
            percent=rs*100/totalSize
            self.ui.progress.setValue(int(percent))


if __name__ == "__main__":
    app = QApplication([])
    widget = FileDownloader()
    sys.exit(app.exec_())
