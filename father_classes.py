from random import randint
from time import ctime
from time_school import check_time_s, day_week
from teacher import check_teacher
from learner import money_learner, None_hod, check_learner, learner_study, loss_of_skill, schedule_on_day

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

list_of_name = [["Ева", "Валерия", "Софья", "Алина", "Виктория", "Дарья", "Эвелина"],
                ["Роман", "Артём", "Герман", "Максим", "Денис", "Андрей", "Даниил"]]

lesson_time = ["8:30-9:10", "9:25-10:05", "10:25-11:05", "11:20-12:00", "12:15-12:55", "13:10-13:50", "14:00-14:40"]


def respect(respect):
    if respect <= 10:
        return 1
    elif 10 < respect < 90:
        return 2
    elif respect >= 90:
        return 3


class Me:
    def __init__(self):
        self.id = 0
        check = check_learner(self.id, list_of_name)
        self.name = check[1]
        self.is_man = check[2]
        self.money = check[3]
        self.him_bio = check[4]
        self.fiz_math = check[5]
        self.soth_ekonom = check[6]
        self.hod = check[7]

    def info(self):
        print(f"\n{ctime(check_time_s())}\n"
              f"Тебя зовут {self.name}\n"
              f"{self.money} - у тебя денег\n"
              f"Расписание: {schedule_on_day(schedule[day_week(ctime(check_time_s()))], lesson_time)}\n"
              f"{self.him_bio} - у тебя способностей в хим.био.\n"
              f"{self.fiz_math} - у тебя способностей в физ.мате\n"
              f"{self.soth_ekonom} - у тебя способностей в соц.экономе\n")

    def none_hod(self):
        self.hod -= 1
        None_hod(self.name, self.hod)

    def loss_one_skill(self):
        if self.soth_ekonom > 0:
            self.soth_ekonom -= 1
        if self.fiz_math > 0:
            self.fiz_math -= 1
        if self.him_bio > 0:
            self.him_bio -= 1
        loss_of_skill(self.name)

    def one_hod(self):
        self.hod = 1
        Me().none_hod()

    def some_hod(self, hod):
        self.hod = hod

    def study(self, lessen):
        self.hod = 40
        exec(f"self.{skills[lessen]} = {learner_study(self.name, skills[lessen])}")

    def take_money(self):
        self.hod = 30
        money = randint(10, 100)
        print(f"Ты выпросил у родителей {money} рублей")
        self.money = money + self.money
        money_learner(self.name, self.money)


class Classroom_teacher_Junior():

    def __init__(self):
        check = check_teacher()
        self.name = check[0]
        self.respect = check[-1]

    def respect_with_teacher(self):
        if respect(self.respect) == 1:
            print(f"\nТвои дела плохи, у тебя {self.respect} отношений с классным руководителем,"
                  " а это значит, что тебе не отвертеться от сдачи "
                  "денег на шторы и у тебя будет всё довольно плохо"
                  "(сочувствую, тебе банально не повезло)\n")
        elif respect(self.respect) == 2:
            print(f"\nТы похож на 80% учеников, у тебя {self.respect} отношений с классным руководителем,"
                  " тут нечем гордиться. Тебе надо сдавать на шторы, но жить ты будешь\n")
        elif respect(self.respect) == 3:
            print(f"\nТы счастливчик, у тебя целых {self.respect} отношений"
                  " с классным руководителем, скажу по секрету, тебе не надо беспокоиться даже"
                  " о шторах не говоря уж об оценках и драках\n")

