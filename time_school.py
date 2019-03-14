import sqlite3
import time

conn = sqlite3.connect("School.db")
cursor_time = conn.cursor()

try:
    cursor_time.execute("""CREATE TABLE time
                  (time integer)
                   """)
except sqlite3.OperationalError:
    pass


def one_minute():
    sql = f"UPDATE time SET time={check_time_s()+60}"
    cursor_time.execute(sql)
    conn.commit()


def check_time_s():
    sql = "SELECT * FROM time"
    cursor_time.execute(sql)
    check_time = cursor_time.fetchone()
    if check_time is None:
        cursor_time.execute("INSERT INTO time VALUES (1188793800)")
        conn.commit()
        sql = "SELECT * FROM time"
        cursor_time.execute(sql)
        check_time = cursor_time.fetchone()
    return check_time[0]


def ctime_time():
    return time.ctime(check_time_s())


def day_week(now_time):
    day_of_week = {"Mon": 1, "Tue": 2, "Wed": 3, "Thu": 4, "Fri": 5, "Sat": 6, "Sun": 7}
    now_time = now_time.split()
    now_day_week = day_of_week[now_time[0]]
    return now_day_week


def time_test(year_start=None, year_finish=None, month_start=None, month_finish=None, day_month_start=None,
              day_month_finish=None, day_week_start=None, day_week_finish=None, hour_start=None, hour_finish=None,
              minute_start=None, minute_finish=None):
    day_of_week = {"Mon": 1, "Tue": 2, "Wed": 3, "Thu": 4, "Fri": 5, "Sat": 6, "Sun": 7}
    month = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6,
             "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12}
    now_time = ctime_time()
    now_time = now_time.split()
    now_day_week = day_of_week[now_time[0]]
    now_month = month[now_time[1]]
    now_day_month = int(now_time[2])
    now_hour = int(now_time[3].split(":")[0])
    now_minute = int(now_time[3].split(":")[1])
    now_year = int(now_time[4])
    if year_start is None and not (year_finish is None):
        year_start = now_year
    elif year_finish is None:
        now_year = "None"
        year_start = "None"
        year_finish = "None"
    if day_month_start is None and not (day_month_finish is None):
        day_month_start = now_day_month
    elif day_month_finish is None:
        now_day_month = "None"
        day_month_start = "None"
        day_month_finish = "None"
    if day_week_start is None and not (day_week_finish is None):
        day_week_start = now_day_week
    elif day_week_finish is None:
        now_day_week = "None"
        day_week_start = "None"
        day_week_finish = "None"
    if month_start is None and not (month_finish is None):
        month_start = now_month
    elif month_finish is None:
        now_month = "None"
        month_start = "None"
        month_finish = "None"
    if hour_start is None and not (hour_finish is None):
        hour_start = now_hour
    elif hour_finish is None:
        now_hour = "None"
        hour_start = "None"
        hour_finish = "None"
    if minute_start is None and not (minute_finish is None):
        minute_start = now_minute
    elif minute_finish is None:
        now_minute = "None"
        minute_start = "None"
        minute_finish = "None"
    if year_start <= now_year <= year_finish and month_start <= now_month <= month_finish and \
            day_month_start <= now_day_month <= day_month_finish and day_week_start <= now_day_week <= day_week_finish \
            and hour_start <= now_hour <= hour_finish and minute_start <= now_minute <= minute_finish:
        return True
    else:
        return False
