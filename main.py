import time
from father_classes import Classroom_teacher_Junior, Me
import sqlite3
from time_school import time_test, day_week, one_minute, ctime_time


schedule = {1: ["ОРКСЭ", "Математика", "Музыка", "Русский язык", "Физкультура"],
            2: ["Математика", "Труд", "Русский язык", "Чтение", "Физкультура"],
            3: ["Русский язык", "Математика", "Физкультура", "Английский язык", "Чтение"],
            4: ["Окружающий мир", "Математика", "Русский язык", "ИЗО", "Речь"],
            5: ["Русский язык", "Чтение", "Английский язык", "Окружающий мир", "Азбука здоровья"],
            6: [],
            7: []}

skills = {"Русский язык": "soth_ekonom",
          "Математика": "fiz_math",
          "Чтение": "soth_ekonom",
          "Окружающий мир": "him_bio",
          "Физкультура": "fiz_math",
          "Труд": "fiz_math",
          "ОРКСЭ": "soth_ekonom",
          "Музыка": "soth_ekonom",
          "Английский язык": "soth_ekonom",
          "ИЗО": "soth_ekonom",
          "Речь": "soth_ekonom",
          "Азбука здоровья": "him_bio"}


conn = sqlite3.connect("School.db")

if __name__ == "__main__":
    Classroom_teacher_Junior = Classroom_teacher_Junior()
    Me = Me()
    while True:
        if ctime_time().split()[3] == "00:00:00":
            Me.loss_one_skill()
            one_minute()
        elif Me.hod != 0:
            print(f"Вам осталось ждать {Me.hod} минут")
            Me.none_hod()
            one_minute()
            time.sleep(0.4)
        else:
            wwod = input(
                "Что вы хотите?\n1. Узнать отношение с учителем\n2. Заработать денег\n3. Информация\n4. Учиться\n5. Подождать x минут\n6. Выйти\nВведите цифру: ")
            if not wwod.isdecimal():
                print("\nЯ же просил, введи число\n")
            else:
                wwod = int(wwod)
                if wwod == 1:
                    Classroom_teacher_Junior.respect_with_teacher()
                elif wwod == 2:
                    Me.take_money()
                elif wwod == 3:
                    Me.info()
                elif wwod == 4:
                    schedule_now = schedule[day_week(ctime_time())]
                    if not time_test(day_week_start=6, day_week_finish=7):
                        if time_test(hour_start=8, hour_finish=8, minute_start=30,
                                     minute_finish=30):
                            Me.study(schedule_now[0])
                        elif time_test(hour_start=9, hour_finish=9, minute_start=25,
                                       minute_finish=25):
                            Me.study(schedule_now[1])
                        elif time_test(hour_start=10, hour_finish=10, minute_start=25,
                                       minute_finish=25):
                            Me.study(schedule_now[2])
                        elif time_test(hour_start=11, hour_finish=11, minute_start=20,
                                       minute_finish=20):
                            Me.study(schedule_now[3])
                        elif time_test(hour_start=12, hour_finish=12, minute_start=15,
                                       minute_finish=15):
                            Me.study(schedule_now[4])
                        else:
                            print("Не то время для учёбы")
                    else:
                        print("Не тот день для учёбы")
                elif wwod == 5:
                    minute = input("Сколько минут хочешь подождать? ")
                    if minute.isdigit():
                        Me.some_hod(int(minute))
                    else:
                        print("Введи число")
                elif wwod == 6:
                    print("\nПока")
                    conn.close()
                    break
                else:
                    print("\nВведи ту цифру, что я просил\n")
