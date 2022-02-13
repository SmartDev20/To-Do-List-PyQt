from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from main_window import Ui_MainWindow
from dialog import Ui_Dialog
from stylesheets import main_style_sheet
from stylesheets import dialog_style_sheet


class Dialog(QDialog):
      def __init__(self , parent=None) :
          super(Dialog,self).__init__(parent)
          self.ui = Ui_Dialog()
          self.ui.setupUi(self)
          self.setStyleSheet(dialog_style_sheet)



class MainWindow(QMainWindow , Ui_MainWindow):
     def __init__(self , parent=None):
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)
        self.btn_new.clicked.connect(self.add_stuff)
        self.btn_done.clicked.connect(self.do_task)
        self.btn_notDone.clicked.connect(self.not_done)
        self.setStyleSheet(main_style_sheet)


     def add_task(self , task):
        if bool(task) != False :
           self.new_tasks.addItem(task)



     def add_stuff(self):
       dig = Dialog()
       dig.ui.buttonBox.accepted.connect(lambda: self.add_task(dig.ui.lineEdit.text()))
       dig.exec()


     def do_task(self) :
        task = self.new_tasks.takeItem(self.new_tasks.currentRow())
        if bool(task) :
           self.finished_list.addItem(task.text())


     def not_done(self) :
        task = self.finished_list.takeItem(self.finished_list.currentRow())
        if bool(task) :
           self.new_tasks.addItem(task.text())


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
