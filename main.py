class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):      #Оценка лектора от студента
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_rate(self):          #Средняя оценка студента по всем курсам
        raiting = 0
        length = 0
        for course in self.grades:
            length += len(self.grades[course])
            for rate in self.grades[course]:
                raiting += rate
        res = raiting / length
        return res

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rate()}\nКурсы в процессе изучения: {",".join(self.courses_in_progress)}\nЗвершённые курсы: {",".join(self.finished_courses)}'
        return res

    def __gt__(self, other):
        return self.average_rate() > other.average_rate()

    def __lt__(self, other):
        return self.average_rate() < other.average_rate()

    def __ge__(self, other):
        return self.average_rate() >= other.average_rate()

    def __le__(self, other):
        return self.average_rate() <= other.average_rate()

    def __eq__(self, other):
        return self.average_rate() == other.average_rate()

    def __ne__(self, other):
        return self.average_rate() != other.average_rate()


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}


class Lecturer(Mentor):

    def average_rate(self):        #Средняя оценка лекторов по всем курсам
        raiting = 0
        length = 0
        for course in self.grades:
            length += len(self.grades[course])
            for rate in self.grades[course]:
                raiting += rate
        res = raiting / length
        return res

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rate()}'
        return res

    def __gt__(self, other):
        return self.average_rate() > other.average_rate()

    def __lt__(self, other):
        return self.average_rate() < other.average_rate()

    def __ge__(self, other):
        return self.average_rate() >= other.average_rate()

    def __le__(self, other):
        return self.average_rate() <= other.average_rate()

    def __eq__(self, other):
        return self.average_rate() == other.average_rate()

    def __ne__(self, other):
        return self.average_rate() != other.average_rate()


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):          #Оценка студента от лектора
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res

students = {}
lectors = {}

# Добавляем студентов
ruoy = Student('Ruoy', 'Eman', 'male')
ruoy.courses_in_progress += ['Python']
ruoy.courses_in_progress += ['Git']
emma = Student('Emma', 'Watson', 'female')
emma.courses_in_progress += ['Python']

# Добавляем лекторов
obi = Lecturer('Obi-van', 'Kenobi')
obi.courses_attached += ['Python']
indiana = Lecturer('Indiana', 'Jones')
indiana.courses_attached += ['Python']

# Добавляем проверяющих
james = Reviewer('James', 'Bond')
james.courses_attached += ['Python']
ostin = Reviewer('Ostin', 'Powers')
ostin.courses_attached += ['Python']
ostin.courses_attached += ['Git']

ruoy.rate_lecturer(obi, 'Python', 10)
ruoy.rate_lecturer(indiana, 'Python', 10)
emma.rate_lecturer(obi, 'Python', 9)
james.rate_hw(ruoy, 'Python', 9)
james.rate_hw(emma, 'Python', 7)
ostin.rate_hw(ruoy, 'Python', 8)
ostin.rate_hw(ruoy, 'Git', 8)
students['ruoy'] = ruoy.grades
students['emma'] = emma.grades
lectors['obi'] = obi.grades
lectors['indiana'] = indiana.grades


def student_average(student, item):     #Средняя оценка у всех студентов по определённому курсу
    sum_rates = 0
    length_rates = 0
    items_list = list(student.values())
    for items_dict in items_list:
        for items_name in items_dict:
            if items_name == 'Python':
                items_rate = list(items_dict.values())
                for rates in items_rate:
                    for rate in rates:
                        sum_rates += rate
                        length_rates += 1
    res = sum_rates / length_rates
    return res


def lectors_average(lector, item):              #Средняя оценка лекторов по определённому курсу
    sum_rates = 0
    length_rates = 0
    items_list = list(lector.values())
    for items_dict in items_list:
        for items_name in items_dict:
            if items_name == 'Python':
                items_rate = list(items_dict.values())
                for rates in items_rate:
                    for rate in rates:
                        sum_rates += rate
                        length_rates += 1
    res = sum_rates / length_rates
    return res

print(ruoy)             #Задание 3(__str__) + Задание 2 + Задание 1
print(emma)
print(obi)
print(indiana)
print(james)
print(ostin)
print(emma < obi)          # Задание 3 пункт 2
print(emma > obi)
print(indiana <= ruoy)
print(indiana >= ruoy)
print(indiana == emma)
print(obi != ruoy)
print(student_average(students, 'Python')) # Задание 4 пункт 1
print(lectors_average(lectors, 'Python')) # Задание 4 пункт 2
