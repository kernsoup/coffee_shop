# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class MainScreen(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.table = QtWidgets.QTableView(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(30, 10, 741, 291))
        self.table.setObjectName("table")
        self.newbtn = QtWidgets.QPushButton(self.centralwidget)
        self.newbtn.setGeometry(QtCore.QRect(260, 310, 81, 31))
        self.newbtn.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.newbtn.setObjectName("newbtn")
        self.upd = QtWidgets.QPushButton(self.centralwidget)
        self.upd.setGeometry(QtCore.QRect(460, 310, 121, 31))
        self.upd.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.upd.setObjectName("upd")
        self.add = QtWidgets.QPushButton(self.centralwidget)
        self.add.setGeometry(QtCore.QRect(360, 310, 81, 31))
        self.add.setStyleSheet("background-color: rgb(255, 170, 127);\n"
"background-color: rgb(255, 255, 127);")
        self.add.setObjectName("add")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuor_not_yay = QtWidgets.QMenu(self.menubar)
        self.menuor_not_yay.setObjectName("menuor_not_yay")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuor_not_yay.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "COFFEE YAY"))
        self.newbtn.setText(_translate("MainWindow", "New"))
        self.upd.setText(_translate("MainWindow", "Update the database"))
        self.add.setText(_translate("MainWindow", "Update a line"))
        self.menuor_not_yay.setTitle(_translate("MainWindow", "or not yay..."))
