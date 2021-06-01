# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtWidgets
from PyQt5.QtCore import QRect, QSize, Qt, QMetaObject, QCoreApplication
from PyQt5.QtGui import QIcon, QPixmap, QFont, QCursor


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(405, 519)
        icon = QIcon()
        icon.addPixmap(QPixmap("res/icon.ico"), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.play = QtWidgets.QPushButton(self.centralwidget)
        self.play.setGeometry(QRect(240, 30, 101, 81))
        font = QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.play.setFont(font)
        self.play.setAutoFillBackground(False)
        self.play.setText("")
        icon1 = QIcon()
        icon1.addPixmap(QPixmap("res/play.png"), QIcon.Normal, QIcon.Off)
        self.play.setIcon(icon1)
        self.play.setIconSize(QSize(75, 75))
        self.play.setFlat(True)
        self.play.setObjectName("play")
        self.pause = QtWidgets.QPushButton(self.centralwidget)
        self.pause.setGeometry(QRect(240, 130, 101, 81))
        font = QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.pause.setFont(font)
        self.pause.setText("")
        icon2 = QIcon()
        icon2.addPixmap(QPixmap("res/pause.png"), QIcon.Normal, QIcon.Off)
        self.pause.setIcon(icon2)
        self.pause.setIconSize(QSize(75, 75))
        self.pause.setFlat(True)
        self.pause.setObjectName("pause")
        self.stop = QtWidgets.QPushButton(self.centralwidget)
        self.stop.setGeometry(QRect(240, 220, 101, 81))
        font = QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.stop.setFont(font)
        self.stop.setText("")
        icon3 = QIcon()
        icon3.addPixmap(QPixmap("res/stop.png"), QIcon.Normal, QIcon.Off)
        self.stop.setIcon(icon3)
        self.stop.setIconSize(QSize(75, 75))
        self.stop.setFlat(True)
        self.stop.setObjectName("stop")
        self.change_dir = QtWidgets.QPushButton(self.centralwidget)
        self.change_dir.setGeometry(QRect(240, 310, 141, 81))
        font = QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.change_dir.setFont(font)
        icon4 = QIcon()
        icon4.addPixmap(QPixmap("res/find.png"), QIcon.Normal, QIcon.Off)
        self.change_dir.setIcon(icon4)
        self.change_dir.setIconSize(QSize(50, 50))
        self.change_dir.setDefault(False)
        self.change_dir.setFlat(True)
        self.change_dir.setObjectName("change_dir")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QRect(0, 10, 231, 491))
        self.listWidget.setObjectName("listWidget")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QRect(240, 460, 160, 22))
        self.horizontalSlider.setCursor(QCursor(Qt.CrossCursor))
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QRect(300, 450, 47, 13))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Music Box"))
        self.change_dir.setText(_translate("MainWindow", "Change Folder"))
        self.label.setText(_translate("MainWindow", "Volume"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
