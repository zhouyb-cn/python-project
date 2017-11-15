# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_calculator.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Calculator(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(239, 361)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {\n"
"  qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"background-color : white;")
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.pushButton_clear = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_clear.setGeometry(QtCore.QRect(0, 60, 61, 61))
        self.pushButton_clear.setStyleSheet("QPushButton {\n"
"  background-color: rgb(215, 215, 215);\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
"}")
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.pushButton_plus_mins = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_plus_mins.setGeometry(QtCore.QRect(60, 60, 61, 61))
        self.pushButton_plus_mins.setStyleSheet("QPushButton {\n"
"  background-color: rgb(215, 215, 215);\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
"}")
        self.pushButton_plus_mins.setObjectName("pushButton_plus_mins")
        self.pushButton_percent = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_percent.setEnabled(True)
        self.pushButton_percent.setGeometry(QtCore.QRect(120, 60, 61, 61))
        self.pushButton_percent.setStyleSheet("QPushButton {\n"
"  background-color: rgb(215, 215, 215);\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
"}")
        self.pushButton_percent.setObjectName("pushButton_percent")
        self.pushButton_divide = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_divide.setGeometry(QtCore.QRect(180, 60, 61, 61))
        self.pushButton_divide.setStyleSheet("QPushButton {\n"
"  background-color: rgb(255, 151, 57);\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FF7832, stop: 1 #FF9739);\n"
"}")
        self.pushButton_divide.setObjectName("pushButton_divide")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_9.setGeometry(QtCore.QRect(120, 120, 61, 61))
        self.pushButton_9.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_ride = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_ride.setGeometry(QtCore.QRect(180, 120, 61, 61))
        self.pushButton_ride.setStyleSheet("QPushButton {\n"
"  background-color: rgb(255, 151, 57);\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FF7832, stop: 1 #FF9739);\n"
"}")
        self.pushButton_ride.setObjectName("pushButton_ride")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_7.setGeometry(QtCore.QRect(0, 120, 61, 61))
        self.pushButton_7.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_8.setGeometry(QtCore.QRect(60, 120, 61, 61))
        self.pushButton_8.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_6.setGeometry(QtCore.QRect(120, 180, 61, 61))
        self.pushButton_6.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_reduce = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_reduce.setGeometry(QtCore.QRect(180, 180, 61, 61))
        self.pushButton_reduce.setStyleSheet("QPushButton {\n"
"  background-color: rgb(255, 151, 57);\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FF7832, stop: 1 #FF9739);\n"
"}")
        self.pushButton_reduce.setObjectName("pushButton_reduce")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 180, 61, 61))
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_5.setGeometry(QtCore.QRect(60, 180, 61, 61))
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_3.setGeometry(QtCore.QRect(120, 240, 61, 61))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_plus = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_plus.setGeometry(QtCore.QRect(180, 240, 61, 61))
        self.pushButton_plus.setStyleSheet("QPushButton {\n"
"  background-color: rgb(255, 151, 57);\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FF7832, stop: 1 #FF9739);\n"
"}")
        self.pushButton_plus.setObjectName("pushButton_plus")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_1.setGeometry(QtCore.QRect(0, 240, 61, 61))
        self.pushButton_1.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 240, 61, 61))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_dot = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_dot.setGeometry(QtCore.QRect(120, 300, 61, 61))
        self.pushButton_dot.setStyleSheet("QPushButton {\n"
"  background-color: rgb(215, 215, 215);\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
"}")
        self.pushButton_dot.setObjectName("pushButton_dot")
        self.pushButton_0 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_0.setGeometry(QtCore.QRect(0, 300, 121, 61))
        self.pushButton_0.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.pushButton_0.setObjectName("pushButton_0")
        self.pushButton_equal = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_equal.setGeometry(QtCore.QRect(180, 300, 61, 61))
        self.pushButton_equal.setStyleSheet("QPushButton {\n"
"  background-color: rgb(255, 151, 57);\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FF7832, stop: 1 #FF9739);\n"
"}")
        self.pushButton_equal.setObjectName("pushButton_equal")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "0"))
        self.pushButton_clear.setText(_translate("MainWindow", "C"))
        self.pushButton_plus_mins.setText(_translate("MainWindow", "+/-"))
        self.pushButton_percent.setText(_translate("MainWindow", "%"))
        self.pushButton_divide.setText(_translate("MainWindow", "/"))
        self.pushButton_9.setText(_translate("MainWindow", "9"))
        self.pushButton_ride.setText(_translate("MainWindow", "x"))
        self.pushButton_7.setText(_translate("MainWindow", "7"))
        self.pushButton_8.setText(_translate("MainWindow", "8"))
        self.pushButton_6.setText(_translate("MainWindow", "6"))
        self.pushButton_reduce.setText(_translate("MainWindow", "-"))
        self.pushButton_4.setText(_translate("MainWindow", "4"))
        self.pushButton_5.setText(_translate("MainWindow", "5"))
        self.pushButton_3.setText(_translate("MainWindow", "3"))
        self.pushButton_plus.setText(_translate("MainWindow", "+"))
        self.pushButton_1.setText(_translate("MainWindow", "1"))
        self.pushButton_2.setText(_translate("MainWindow", "2"))
        self.pushButton_dot.setText(_translate("MainWindow", "."))
        self.pushButton_0.setText(_translate("MainWindow", "0"))
        self.pushButton_equal.setText(_translate("MainWindow", "="))

