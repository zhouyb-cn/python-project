import PyQt5
from ui_kq import Ui_kq
import os
from attendance import handle

class KqMainWindow(PyQt5.QtWidgets.QMainWindow, Ui_kq):
    filename = None
    merge_data = []
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.pushButton_import.clicked.connect(self.import_pressed)
        self.pushButton_merge_data.clicked.connect(self.merge_data_pressed)
        # self.pushButton_exception


    def import_pressed(self):
        print("test")
        filenames = PyQt5.QtWidgets.QFileDialog.getOpenFileName(self, 'save file', '/')
        self.filename = filenames[0]
        self.textEdit_file_path.setText(self.filename)
        self.statusBar.showMessage('导入文件 {} 成功!'.format(self.filename))

    def merge_data_pressed(self):
        print('merge')
        self.merge_data = handle(self.filename)

        self.tableWidget_result.setRowCount(len(self.merge_data))
        self.tableWidget_result.setColumnCount(8)
        self.tableWidget_result.setHorizontalHeaderLabels(['时间', '姓名', '账号', '部门', '早上打卡时间', '晚上打卡时间', \
                                                           '早上打卡地点', '晚上打卡地点'])
        for index in range(0, len(self.merge_data)):
            items = self.merge_data[index].split('|')
            for item in range(0, len(items)):
                self.tableWidget_result.setItem(index, item, PyQt5.QtWidgets.QTableWidgetItem(items[item]))

        print(self.merge_data)

    def exception_pressed(self):
        return