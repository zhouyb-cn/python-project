# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_kq.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_kq(object):
    def setupUi(self, kq):
        kq.setObjectName("kq")
        kq.resize(868, 761)
        self.centralWidget = QtWidgets.QWidget(kq)
        self.centralWidget.setObjectName("centralWidget")
        self.labelpath = QtWidgets.QLabel(self.centralWidget)
        self.labelpath.setGeometry(QtCore.QRect(20, 40, 41, 31))
        self.labelpath.setObjectName("labelpath")
        self.pushButton_import = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_import.setGeometry(QtCore.QRect(320, 40, 71, 31))
        self.pushButton_import.setObjectName("pushButton_import")
        self.pushButton_merge_data = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_merge_data.setGeometry(QtCore.QRect(20, 100, 80, 24))
        self.pushButton_merge_data.setObjectName("pushButton_merge_data")
        self.pushButton_over_time = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_over_time.setGeometry(QtCore.QRect(130, 100, 101, 31))
        self.pushButton_over_time.setObjectName("pushButton_over_time")
        self.label_result = QtWidgets.QLabel(self.centralWidget)
        self.label_result.setGeometry(QtCore.QRect(20, 150, 59, 16))
        self.label_result.setObjectName("label_result")
        self.pushButton_exception = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_exception.setGeometry(QtCore.QRect(270, 100, 101, 31))
        self.pushButton_exception.setObjectName("pushButton_exception")
        self.tableWidget_result = QtWidgets.QTableWidget(self.centralWidget)
        self.tableWidget_result.setGeometry(QtCore.QRect(10, 180, 850, 500))
        self.tableWidget_result.setColumnCount(0)
        self.tableWidget_result.setObjectName("tableWidget_result")
        self.tableWidget_result.setRowCount(0)
        self.label_file_name = QtWidgets.QLabel(self.centralWidget)
        self.label_file_name.setGeometry(QtCore.QRect(70, 45, 221, 21))
        self.label_file_name.setObjectName("label_file_name")
        self.pushButton_export = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_export.setGeometry(QtCore.QRect(750, 143, 80, 31))
        self.pushButton_export.setObjectName("pushButton_export")
        kq.setCentralWidget(self.centralWidget)
        self.statusBar = QtWidgets.QStatusBar(kq)
        self.statusBar.setObjectName("statusBar")
        kq.setStatusBar(self.statusBar)
        self.toolBar = QtWidgets.QToolBar(kq)
        self.toolBar.setObjectName("toolBar")
        kq.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(kq)
        QtCore.QMetaObject.connectSlotsByName(kq)

    def retranslateUi(self, kq):
        _translate = QtCore.QCoreApplication.translate
        kq.setWindowTitle(_translate("kq", "kq"))
        self.labelpath.setText(_translate("kq", "文件："))
        self.pushButton_import.setText(_translate("kq", "导入"))
        self.pushButton_merge_data.setText(_translate("kq", "合并数据"))
        self.pushButton_over_time.setText(_translate("kq", "统计加班时间"))
        self.label_result.setText(_translate("kq", "结果"))
        self.pushButton_exception.setText(_translate("kq", "统计异常"))
        self.label_file_name.setText(_translate("kq", "点击右侧导入按钮导入文件"))
        self.pushButton_export.setText(_translate("kq", "导出"))
        self.toolBar.setWindowTitle(_translate("kq", "toolBar"))

