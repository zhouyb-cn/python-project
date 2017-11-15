import PyQt5
from ui_calculator import Ui_Calculator

class CalculatorWindow(PyQt5.QtWidgets.QMainWindow, Ui_Calculator):

    firstNum = None
    userIsTypingSecondNumber = False

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.pushButton_0.clicked.connect(self.digit_pressed)
        self.pushButton_1.clicked.connect(self.digit_pressed)
        self.pushButton_2.clicked.connect(self.digit_pressed)
        self.pushButton_3.clicked.connect(self.digit_pressed)
        self.pushButton_4.clicked.connect(self.digit_pressed)
        self.pushButton_5.clicked.connect(self.digit_pressed)
        self.pushButton_6.clicked.connect(self.digit_pressed)
        self.pushButton_7.clicked.connect(self.digit_pressed)
        self.pushButton_8.clicked.connect(self.digit_pressed)
        self.pushButton_9.clicked.connect(self.digit_pressed)

        """
            :type: PyQt5.QtWidgets.QPushButton
        """

        self.pushButton_dot.clicked.connect(self.dot_pressed)

        self.pushButton_plus_mins.clicked.connect(self.unary_operation_pressed)
        self.pushButton_percent.clicked.connect(self.unary_operation_pressed)

        self.pushButton_plus.clicked.connect(self.operation)
        self.pushButton_reduce.clicked.connect(self.operation)
        self.pushButton_ride.clicked.connect(self.operation)
        self.pushButton_divide.clicked.connect(self.operation)

        self.pushButton_plus.setCheckable(True)
        self.pushButton_reduce.setCheckable(True)
        self.pushButton_ride.setCheckable(True)
        self.pushButton_divide.setCheckable(True)

        self.pushButton_equal.setCheckable(True)

        self.pushButton_equal.clicked.connect(self.equal_oreration)

        self.pushButton_clear.clicked.connect(self.clear_pressed)

    def digit_pressed(self):
        button = self.sender()

        if (self.pushButton_plus.isChecked() or self.pushButton_reduce.isChecked() \
                or self.pushButton_ride.isChecked() or self.pushButton_divide.isChecked()) and (not self.userIsTypingSecondNumber):
            newLabel = format(float(button.text()), ".15g")
            self.userIsTypingSecondNumber = True
        elif self.pushButton_equal.isChecked():
            newLabel = format(float(button.text()), ".15g")
            self.pushButton_equal.setChecked(False)
        else:
            if "." in self.label.text() and button.text() == "0":
                newLabel = format(self.label.text() + button.text(), ".15")
            else:
                newLabel = format(float(self.label.text() + button.text()), ".15g")

        self.label.setText(newLabel)

    def dot_pressed(self):

        laberNumber = self.label.text()
        if laberNumber.find(".") == -1:
            self.label.setText(self.label.text() + ".")

    def unary_operation_pressed(self):
        button = self.sender()
        laberNumber = float(self.label.text())

        if button.text() == "+/-":
            laberNumber = laberNumber * -1
        else:
            laberNumber = laberNumber * 0.01

        newLabel = format(laberNumber, ".15g")

        self.label.setText(newLabel)

    def operation(self):
        button  = self.sender()
        self.firstNum = float(self.label.text())
        button.setChecked(True)

    def equal_oreration(self):
        button = self.sender()
        secondNum = float(self.label.text())

        if self.pushButton_plus.isChecked():
            labelNumber = self.firstNum + secondNum
            newLabel = format(labelNumber, ".15g")
            self.label.setText(newLabel)
            self.pushButton_plus.setChecked(False)
        elif self.pushButton_reduce.isChecked():
            labelNumber = self.firstNum - secondNum
            newLabel = format(labelNumber, ".15g")
            self.label.setText(newLabel)
            self.pushButton_reduce.setChecked(False)
        elif self.pushButton_ride.isChecked():
            labelNumber = self.firstNum * secondNum
            newLabel = format(labelNumber, ".15g")
            self.label.setText(newLabel)
            self.pushButton_ride.setChecked(False)
        elif self.pushButton_divide.isChecked():
            labelNumber = self.firstNum / secondNum
            newLabel = format(labelNumber, ".15g")
            self.label.setText(newLabel)
            self.pushButton_divide.setChecked(False)
        self.userIsTypingSecondNumber = False
        self.pushButton_equal.setChecked(True)


    def clear_pressed(self):
        button = self.sender()

        self.userIsTypingSecondNumber = False
        self.pushButton_plus.setChecked(False)
        self.pushButton_ride.setChecked(False)
        self.pushButton_reduce.setChecked(False)
        self.pushButton_divide.setChecked(False)

        self.label.setText("0")