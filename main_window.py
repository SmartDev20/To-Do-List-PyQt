# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(380, 50, 344, 271))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_done_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_done_2.setObjectName("label_done_2")
        self.gridLayout.addWidget(self.label_done_2, 0, 0, 1, 1)
        self.btn_new = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_new.setObjectName("btn_new")
        self.gridLayout.addWidget(self.btn_new, 0, 1, 1, 1)
        self.new_tasks = QtWidgets.QListWidget(self.layoutWidget)
        self.new_tasks.setObjectName("new_tasks")
        self.gridLayout.addWidget(self.new_tasks, 1, 0, 1, 2)
        self.btn_done = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_done.setObjectName("btn_done")
        self.gridLayout.addWidget(self.btn_done, 2, 0, 1, 2)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 50, 344, 271))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.finished_list = QtWidgets.QListWidget(self.layoutWidget1)
        self.finished_list.setObjectName("finished_list")
        self.gridLayout_2.addWidget(self.finished_list, 3, 0, 1, 1)
        self.label_done = QtWidgets.QLabel(self.layoutWidget1)
        self.label_done.setObjectName("label_done")
        self.gridLayout_2.addWidget(self.label_done, 0, 0, 1, 1)
        self.btn_notDone = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn_notDone.setObjectName("btn_notDone")
        self.gridLayout_2.addWidget(self.btn_notDone, 4, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "To Do List"))
        self.label_done_2.setText(_translate("MainWindow", "To be Finish"))
        self.btn_new.setText(_translate("MainWindow", "New Task"))
        self.btn_done.setText(_translate("MainWindow", "Done"))
        self.label_done.setText(_translate("MainWindow", "Finished List"))
        self.btn_notDone.setText(_translate("MainWindow", "Not Done"))
