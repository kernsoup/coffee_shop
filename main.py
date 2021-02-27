import sys

from PyQt5.QtSql import QSqlTableModel, QSqlDatabase
import sqlite3
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets, uic


class MyWidget(QMainWindow):
    def __init__(self):
        super(MyWidget, self).__init__()
        uic.loadUi('main.ui', self)
        self.newbtn.clicked.connect(self.redacting)
        self.add.clicked.connect(self.redacting)
        self.upd.clicked.connect(self.initUI)
        self.initUI()

    def initUI(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('coffee.db')
        db.open()
        self.model = QSqlTableModel(self, db)
        self.model.setTable('coffee')
        self.model.select()
        self.table.setModel(self.model)
        
    def redacting(self):
        self.r = Redacting()
        self.r.show()
        if self.sender().text() == 'New':
            self.r.new()
        

class Redacting(QMainWindow):
    def __init__(self):
        super(Redacting, self).__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.pushButton.clicked.connect(self.update_result)
        self.tableWidget.itemChanged.connect(self.item_changed)
        self.pushButton_2.clicked.connect(self.save_results)
        x = cur.execute("SELECT id FROM coffee").fetchall()
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(max(x)[0])
        self.modified = {}
        self.titles = None

    def update_result(self, *args):
        item_id = self.spinBox.text()
        if args[0]:
            item_id = args[0][0][0]
        cur = con.cursor()
        self.result = cur.execute("SELECT * FROM coffee WHERE id=?",
                             (item_id,)).fetchall()
        if not self.result:
            self.statusBar().showMessage('Ничего не нашлось')
            return
        else:
            self.statusBar().showMessage(f"Нашлась запись с id = {item_id}")
        self.tableWidget.setRowCount(len(self.result))
        self.tableWidget.setColumnCount(len(self.result[0]))
        self.titles = [description[0] for description in cur.description]
        for i, elem in enumerate(self.result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
        self.modified = {}

    def item_changed(self, item):
        self.modified[self.titles[item.column()]] = item.text()

    def save_results(self):
        if self.modified:
            cur = con.cursor()
            que = "UPDATE coffee SET\n"
            for key in self.modified.keys():
                que += "{}='{}'\n".format(key, self.modified.get(key))
            que += "WHERE id = ?"
            cur.execute(que, (self.spinBox.text(),))
            con.commit()
            self.modified.clear()
    
    def new(self):
        item, ok_pressed = QInputDialog.getText(self, "", "Введите название кофе")
        if item == '':
            return
        cur.execute("""INSERT INTO coffee(title) VALUES(?)""", (item,))
        con.commit()
        result = cur.execute("""SELECT id FROM coffee WHERE title == ?""", (item,)).fetchall()
        x = cur.execute("SELECT id FROM coffee").fetchall()
        self.spinBox.setMaximum(max(x)[0])
        self.update_result(result)
        self.save_results()        
        
        
con = sqlite3.connect('coffee.db')
cur = con.cursor()

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())