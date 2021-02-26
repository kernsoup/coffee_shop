import sys

from PyQt5.QtSql import *
import sqlite3
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets, uic


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.initUI()

    def initUI(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('coffee.db')
        db.open()
        self.model = QSqlTableModel(self, db)
        self.model.setTable('coffee')
        self.model.select()
        self.table.setModel(self.model)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())