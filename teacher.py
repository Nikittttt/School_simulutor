import sqlite3
from random import randint

conn = sqlite3.connect("School.db")
cursor_teacher = conn.cursor()
try:
    cursor_teacher.execute("""CREATE TABLE teacher
                  (lesson text, name text, respect_me integer)
                   """)
except sqlite3.OperationalError:
    pass


def new_teacher(lesson, name):
    cursor_teacher.execute(f"INSERT INTO teacher VALUES ('{lesson}','{name}',{randint(1, 100)})")
    conn.commit()


def check_teacher():
    sql = "SELECT * FROM teacher WHERE lesson=?"
    cursor_teacher.execute(sql, ["Classroom"])
    check = cursor_teacher.fetchone()
    if check is None:
        new_teacher("Classroom", "Инна Иванова")
        sql = "SELECT * FROM teacher WHERE lesson=?"
        cursor_teacher.execute(sql, ["Classroom"])
        check = cursor_teacher.fetchone()
    return check

