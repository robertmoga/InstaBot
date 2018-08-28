from datetime import datetime


gloabl_hours= [0, 6, 12, 18]


def string_to_datetime(param_date):
    cur_date, cur_time = param_date.split(" ")
    cur_date = cur_date.split("-")
    cur_time = cur_time.split(":")

    # d = date(int(cur_date[0]), int(cur_date[1]), int(cur_date[2]))
    # t = time(int(cur_time[0]), int(cur_time[1]), int(cur_time[2]))
    # print(d)
    # print(t)
    res = datetime(int(cur_date[0]), int(cur_date[1]), int(cur_date[2]), int(cur_time[0]), int(cur_time[1]), int(cur_time[2]))
    return res


def datetime_to_string(para_date):
    str_date = para_date.strftime("%Y-%m-%d %H:%M:%S")
    return str_date


def get_next_time(day_delay, hour_delay):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    date, time = now.split(" ")
    year, month, day = date.split("-")
    hour, minute, second = time.split(":")
    minute, second = 0,  0

    if hour_delay is True:
        next_hour = -1
        for item in gloabl_hours:
            if item > int(hour):
                next_hour = item
                break
        hour = next_hour

    if day_delay is True:
        day = int(day)+2 #treat the cases where we are at the endof the month

    return_time = str(str(day)+"-"+month+"-"+year+" "+str(hour)+":"+str(minute)+":"+str(second))
    return return_time

#
# def compare_date():
#     str = "2018-08-28 11:38:50"
#     d = string_to_datetime(str)
#     now = datetime.now()
#
#     print(d)
#
#     if d > now:
#         print(True)
#     else:
#         print(False)

# compare_date()

