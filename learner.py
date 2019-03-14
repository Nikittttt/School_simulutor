import sqlite3
from random import randint

conn = sqlite3.connect("School.db")
cursor_learner = conn.cursor()

try:
    cursor_learner.execute("""CREATE TABLE learner
                          (id_player integer, name text, is_man integer, money integer, him_bio integer, fiz_math integer, soth_ekonom integer, hod integer)
                           """)
except sqlite3.OperationalError:
    pass


def new_learner(id_player, name, is_man):
    cursor_learner.execute(f"INSERT INTO learner VALUES ({id_player},'{name}',{is_man},{randint(-100, 100)},{randint(0, 10)},{randint(0, 10)},{randint(0, 10)},0)")
    conn.commit()


def money_learner(name, money):
    sql = f"UPDATE learner SET money={money} WHERE name='{name}'"
    cursor_learner.execute(sql)
    conn.commit()


def learner_study(name, lessen):
    sql = f"SELECT {lessen} FROM learner WHERE name='{name}'"
    cursor_learner.execute(sql)
    check = cursor_learner.fetchone()
    if check[0] <= 30:
        sql = f"UPDATE learner SET {lessen}={check[0]+randint(0,2)} WHERE name='{name}'"
        cursor_learner.execute(sql)
        conn.commit()
        sql = f"SELECT {lessen} FROM learner WHERE name='{name}'"
        cursor_learner.execute(sql)
        check = cursor_learner.fetchone()
    return check[0]


def schedule_on_day(schedule, lesson_time):
    schedules = ""
    for i in range(len(schedule)):
        schedules += f"\n{i+1} урок - {schedule[i]}  {lesson_time[i]}"
    return schedules


def loss_of_skill(name):
    for lessen in ["him_bio", "fiz_math", "soth_ekonom"]:
        sql = f"SELECT {lessen} FROM learner WHERE name='{name}'"
        cursor_learner.execute(sql)
        check = cursor_learner.fetchone()
        if check[0] != 0:
            sql = f"UPDATE learner SET {lessen}={check[0] - 1} WHERE name='{name}'"
            cursor_learner.execute(sql)
            conn.commit()


def None_hod(name, hod):
    sql = f"UPDATE learner SET hod={hod} WHERE name='{name}'"
    cursor_learner.execute(sql)
    conn.commit()


def new_name(list_of_name, gender):
    return list_of_name[gender].pop(randint(0, len(list_of_name[gender])-1))


def check_learner(id_player, list_of_name):
    sql = f"SELECT * FROM learner WHERE id_player={id_player}"
    cursor_learner.execute(sql)
    check = cursor_learner.fetchone()
    if check is None:
        gender = randint(0, 1)
        new_learner(id_player, new_name(list_of_name, gender), gender)
        sql = f"SELECT * FROM learner WHERE id_player={id_player}"
        cursor_learner.execute(sql)
        check = cursor_learner.fetchone()
    return check
