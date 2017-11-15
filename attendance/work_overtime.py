import codecs
from datetime import datetime
from Common.common import time_diff
from Common.common import time_format
from Common.common import init_weekday
from Common.common import init_over_time

data = []

with codecs.open("./detail.md", "r", "utf-8") as f:
    read = f.read().splitlines()
    for i in range(2, len(read)):
        data.append(read[i])

time = init_over_time(data)

with codecs.open("./detail.md", "r", "utf-8") as f:
    read = f.read().splitlines()
    for i in range(2, len(read)):
        explode = read[i].split("|")
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

print(time)