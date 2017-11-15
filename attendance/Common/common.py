from datetime import datetime

def table_data_list(table):
    data = []
    nrows = table.nrows
    for i in range(0, nrows):
        if i < 3:
            continue
        data.append(table.row_values(i))
    return data

def time_diff(date1, date2):
    date1 = datetime.strptime(date1, "%H:%M")
    date2 = datetime.strptime(date2, "%H:%M")
    return date2 - date1

def time_format(time):
    time = time.split(":")
    hour = time[0]
    minutes = "%.2f" % (int(time[1]) / 60)
    return int(hour) + float(minutes)

def init_weekday(day, flag):
    return {
        0: float("%.1f" % (9/flag)),
        1: float("%.1f" % (9/flag)),
        2: float("%.1f" % (9/flag)),
        3: float("%.1f" % (9/flag)),
        4: float("%.1f" % (9/flag)),
        5: 0,
        6: 0
    }.get(day)

def init_people(data):
    peoples = []
    for i in range(0, len(data)):
        name = data[i].split("|")[1].strip()
        if name not in peoples:
            peoples.append(name)
    return peoples

def init_over_time(data):
    peoples = {
        "周彦博": 0,
        "王亚楠": 0,
        "张宁": 0,
        "赵晓彤": 0,
        "侯明珠": 0
    }

    for people in list(peoples):
        for i in range(0, len(data)):
            name = data[i].split("|")[1].strip()
            day = data[i].split("|")[0].strip().split("-")[2]
            if name not in peoples.keys():
                peoples[name] = 0
            if name == people and (int(day) == 8 or int(day) == 22) and time_format(str(time_diff(data[i].split("|")[4].strip(), data[i].split("|")[5].strip()))) >= 8:
                peoples[name] -= 8

    # for i in range(0, len(data)):
    #     name = data[i].split("|")[1].strip()
    #     if name not in peoples.keys():
    #         peoples[name] = 0
    return peoples