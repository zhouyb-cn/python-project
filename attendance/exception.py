import calendar
import codecs
from datetime import datetime

from Common.common import init_people
from Common.convert2md import init_exception_md
from Common.convert2md import write2md
from Const.const import *

# 初始化异常md文件
init_exception_md()

data = []

with codecs.open("./detail.md", "r", "utf-8") as f:
    read = f.read().splitlines()
    for i in range(2, len(read)):
        data.append(read[i])

peoples = init_people(data)

print(peoples)

date = data[0].split("|")[0].strip().split("-")
month = calendar.monthrange(int(date[0]), int(date[1]))

i = month[1]
while i > 0:
    weekday = datetime(int(date[0]), int(date[1]), i).weekday()
    if weekday == SATURDAY or weekday == SUNDAY:
        i -= 1
        continue
    else:
        for people in peoples:
            flag = 0
            details = ""
            for item in data:
                riqi = int(item.split("|")[0].strip().split("-")[2])
                name = item.split("|")[1].strip()
                if riqi == i and name == people:
                    flag = 1
                    details = item
                    data.remove(item)
                    break
            if flag == 0:
                content = [people, "{}月{}日".format(date[1], i), "异常", "异常", "未打卡", "未打卡"]
                write2md(u" | ".join(content) + "\n")
            else:
                detail = details.split("|")
                content = [people, "{}月{}日".format(date[1], i)]
                has_content = 0
                if int(detail[4].strip().split(":")[0]) > 10:
                    has_content = 1
                    content.append(detail[4])
                else:
                    content.append("")
                if int(detail[5].strip().split(":")[0]) < 18:
                    has_content = 1
                    content.append(detail[4])
                else:
                    content.append("")
                if detail[-1].find("望京SOHO") == -1:
                    has_content = 1
                    content.append(detail[-1])
                else:
                    content.append("")
                if detail[-2].find("望京SOHO") == -1:
                    has_content = 1
                    content.append(detail[-2])
                else:
                    content.append("")
                if has_content == 1:
                    write2md(u" | ".join(content) + "\n")
    i -= 1


