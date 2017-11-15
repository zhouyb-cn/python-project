from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from ui_kq import Ui_kq
import os
from attendance import handle
import codecs
from Common.common import *

class KqMainWindow(QMainWindow, Ui_kq):
    filename = None
    export_path = None
    merge_data = []
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.pushButton_import.clicked.connect(self.import_pressed)
        self.pushButton_merge_data.clicked.connect(self.merge_data_pressed)
        # self.pushButton_exception
        self.pushButton_over_time.clicked.connect(self.over_time_pressed)

        self.pushButton_export.clicked.connect(self.export_pressed)


    def import_pressed(self):
        filenames = QFileDialog.getOpenFileName(self, 'save file', '/')
        self.filename = filenames[0]
        self.label_file_name.setText(self.filename.split('/')[-1])
        self.statusBar.showMessage('导入文件 {} 成功!'.format(self.filename))

    def merge_data_pressed(self):
        if self.filename == None:
            QMessageBox.information(self, "提示", "请先导入文件!", QMessageBox.Ok)
            return
        self.merge_data = handle(self.filename)

        self.tableWidget_result.setRowCount(len(self.merge_data))
        self.tableWidget_result.setColumnCount(8)
        self.tableWidget_result.setHorizontalHeaderLabels(['时间', '姓名', '账号', '部门', '早上打卡时间', '晚上打卡时间', \
                                                           '早上打卡地点', '晚上打卡地点'])
        for index in range(0, len(self.merge_data)):
            items = self.merge_data[index].split('|')
            for item in range(0, len(items)):
                self.tableWidget_result.setItem(index, item, QTableWidgetItem(items[item]))

        print(self.merge_data)

    # def exception_pressed(self):
    #     return
    def over_time_pressed(self):
        time = init_over_time(self.merge_data)
        for i in range(0, len(self.merge_data)):
            explode = self.merge_data[i].split("|")
            date = explode[0].split("-")
            weekday = datetime(int(date[0]), int(date[1]), int(date[2])).weekday()
            after_format = time_format(str(time_diff(explode[4].strip(), explode[5].strip())))
            if after_format == 0.00:
                continue
            elif int(explode[4].split(":")[0]) > 11 or int(explode[5].split(":")[0]) < 15:
                over = "%.2f" % (after_format - init_weekday(weekday, 2))
            else:
                over = "%.2f" % (after_format - init_weekday(weekday, 1))
            time[explode[1].strip()] = round(time[explode[1].strip()] + float(over), 2)

        # self.tableWidget_result.clear()

        self.tableWidget_result.setRowCount(len(time))
        self.tableWidget_result.setColumnCount(1)

        self.tableWidget_result.setHorizontalHeaderLabels(['加班总时长'])
        v_labels = []
        v_values = []
        for key in time.keys():
            v_labels.append(key)
            v_values.append(time[key])
        self.tableWidget_result.setVerticalHeaderLabels(v_labels)
        # self.tableWidget_result.
        for k in range(0, len(time)):
            self.tableWidget_result.item(k, 0).setText(str(v_values[k]))
        print(v_values)


    def export_pressed(self):
        path = QFileDialog.getExistingDirectory()
        self.export_path = path + '/data.md'
        self.statusBar.showMessage('文件成功导出到 {} '.format(self.export_path))

        row_count = self.tableWidget_result.rowCount()
        column_count = self.tableWidget_result.columnCount()

        file = codecs.open(self.export_path, "w", "utf-8")
        header = []
        second = []
        for i in range(0, column_count):
            header.append(self.tableWidget_result.horizontalHeaderItem(i).text())
            second.append('------------')
        file.writelines(u' | '.join(header) + u"\n")
        file.writelines(u' | '.join(second) + u"\n")

        line = []
        for j in range(0, row_count):
            for k in range(0, column_count):
                line.append(self.tableWidget_result.item(j, k).text())
            file.writelines(u' | '.join(line) + u"\n")
            line = []

        file.close()
