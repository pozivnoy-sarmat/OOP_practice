# Код требует доработки (и я прошу его туда отправить): перегрузка метода __str__ пока не реализована;
# не реализованы методы сравнения и средних оценок (задание 4).
#
# Была проблема со словарём оценок для лекторов: если словарь объявлять внутри класса Lecturer (без self),
# то у лекторов будет один словарь на двоих. Можно ли было реализовать решение как-то иначе, без вынесения
# атрибута grades в материнский класс?
#

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}


class Lecturer(Mentor):
    pass


class Reviewer(Mentor):
    # def __init__(self, name):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def grade_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


best_student_1 = Student('Иван', 'Иванов', 'мужской')
best_student_1.courses_in_progress += ['Python']
best_student_1.courses_in_progress += ['C++']
best_student_1.courses_in_progress += ['JS']

cool_reviewer = Reviewer('Ещё', 'Доцент')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['C++']
cool_reviewer.courses_attached += ['JS']

cool_lecturer_1 = Lecturer('Уже', 'Профессор')
cool_lecturer_1.courses_attached += ['Python']
cool_lecturer_1.courses_attached += ['C++']
cool_lecturer_1.courses_attached += ['JS']

cool_reviewer.rate_hw(best_student_1, 'Python', 10)
cool_reviewer.rate_hw(best_student_1, 'C++', 8)
cool_reviewer.rate_hw(best_student_1, 'JS', 7)

best_student_1.grade_lecturer(cool_lecturer_1, 'Python', 9)
best_student_1.grade_lecturer(cool_lecturer_1, 'C++', 5)
best_student_1.grade_lecturer(cool_lecturer_1, 'JS', 0)

best_student_2 = Student('Пётр', 'Петров', 'мужской')
best_student_2.courses_in_progress += ['Python']
best_student_2.courses_in_progress += ['C++']
best_student_2.courses_in_progress += ['JS']

# cool_reviewer = Reviewer('Кандидат', 'Наук')
# cool_reviewer.courses_attached += ['Python']

cool_lecturer_2 = Lecturer('Доктор', 'Наук')
cool_lecturer_2.courses_attached += ['Python']
cool_lecturer_2.courses_attached += ['C++']
cool_lecturer_2.courses_attached += ['JS']

cool_reviewer.rate_hw(best_student_2, 'Python', 10)
cool_reviewer.rate_hw(best_student_2, 'C++', 7)
cool_reviewer.rate_hw(best_student_2, 'JS', 2)

best_student_2.grade_lecturer(cool_lecturer_2, 'Python', 10)
best_student_2.grade_lecturer(cool_lecturer_2, 'C++', 4)
best_student_2.grade_lecturer(cool_lecturer_2, 'JS', 6)

# print(best_student_1.grades)
# print(cool_lecturer_1.grades)
# print(cool_lecturer_1.courses_attached)
# print(best_student_2.grades)
# print(cool_lecturer_2.grades)
# print(cool_lecturer_2.courses_attached)
print(
    f'Проверяющий: {cool_reviewer.name} {cool_reviewer.surname}'
    f'\nпроверяет курсы: {" ".join(cool_reviewer.courses_attached)}\n')
print(f'Оценки студента: {best_student_1.name} {best_student_1.surname}\n{best_student_1.grades}')
print(f'Оценки студента: {best_student_2.name} {best_student_2.surname}\n{best_student_2.grades}')
print(f'Оценки лектору: {cool_lecturer_1.name} {cool_lecturer_1.surname}\n{cool_lecturer_1.grades}')
print(f'Оценки лектору: {cool_lecturer_2.name} {cool_lecturer_2.surname}\n{cool_lecturer_2.grades}')
