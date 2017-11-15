# -*- coding: utf-8 -*-
import codecs

def initmd():
    file = codecs.open("detail.md", "w", "utf-8")
    file.writelines(u"时间 | 姓名 | 账号 | 部门 | 早上打卡时间 | 晚上打卡时间 | 早上打卡地点 | 晚上打卡地点\n")
    file.writelines("------------ | ------------- | ------------ | ------------ | ------------- | \
        ------------ | ------------ | -------------\n")
    file.close()

def convert2md(data):
    file = codecs.open("detail.md", "a", "utf-8")
    file.write(data)
    file.close()
    return

def init_exception_md():
    file = codecs.open("exception.md", "w", "utf-8")
    file.writelines(u"姓名 | 时间 | 早上未打卡 | 晚上未打卡 | 早上打卡地点异常 | 晚上打卡地点异常\n")
    file.writelines("------------ | ------------- | ------------ | ------------ | ------------- | \
        ------------\n")
    file.close()

def write2md(data):
    file = codecs.open("exception.md", "a", "utf-8")
    file.write(data)
    file.close()
    return