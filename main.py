class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def mark_for_lect(self, lecturer, course, grade_lect):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.finished_courses:
            if course in lecturer.grade_lect:
                lecturer.grade_lect[course] += [grade_lect]
            else:
                lecturer.grade_lect[course] = [grade_lect]
        else:
            return 'Ошибка'

    def __str__(self):
        res = (f'Имя: {self.name}\nФамилия: {self.surname}\n'
               f'Средняя оценка за домашние задания: '
               f'{self.avg_grade_stud}\n'
               f'Курсы в процессе изучения: '
               f'{", ".join(self.courses_in_progress)}\n'
               f'Завершенные курсы: {", ".join(self.finished_courses)}')
        return res

    def __lt__(self, other):
        if not isinstance(other, Student) and isinstance(other, Lecturer):
            print('Сравнение невозможно')
            return
        if (Student.avg_grade_stud(self) < Student.avg_grade_stud(other)):
            return 'Оценка студента выше оценки лектора'
        elif (Student.avg_grade_stud(self) >
              Student.avg_grade_stud(other)):
            return 'Оценка лектора выше оценки студента'
        else:
            return 'Оценки равны'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grade_lect = {}
        self.courses_attached = []

    def avg_grade_lect(self):

        global avg_grade_l
        sum_grades = 0

        for grades in self.grade_lect.values():
            len_grades = len(grades)
            for list_grades in grades:
                sum_grades += list_grades
                avg_grade_l = sum_grades/len_grades
            return avg_grade_l

    def __str__(self):
        res = (f'Имя: {self.name}\nФамилия: {self.surname}\n'
               f'Средняя оценка за лекции: {self.avg_grade_lect()}')
        return res


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
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

def avg_grade_stud(self):
    sum_grades_s = 0
    if len(self.grades.values()) == 0:
        return "Ошибка"
    else:
        for grades_s in self.grades.values():
            for list_grades in grades_s:
                sum_grades_s += list_grades
                avg_grade_s = sum_grades_s/len(grades_s)
            return avg_grade_s


def avg_grade_lect(self):

    global avg_grade_l
    sum_grades = 0

    for grades in self.grade_lect.values():
        len_grades = len(grades)
        for list_grades in grades:
            sum_grades += list_grades
            avg_grade_l = sum_grades/len_grades
        return avg_grade_l


student_1 = Student('Sergei', 'Serii ', 'men')
student_1.courses_in_progress += ['Data Science']
student_1.finished_courses += ['Опытный опыт']
student_1.finished_courses += ['Ленивая лень']


student_2 = Student('Vitalii', 'Ivanov', 'man')
student_2.courses_in_progress += ['Data Science']
student_2.finished_courses += ['Опытный опыт']
student_2.finished_courses += ['Ленивая лень']

lecturer_1 = Lecturer('Ibragim', 'Maga')
lecturer_1.courses_attached += ['Опытный опыт']

lecturer_2 = Lecturer('Oleg', 'Olegko')
lecturer_2.courses_attached += ['Ленивая лень']

reviewer_1 = Reviewer('Сам', 'Бади')
reviewer_1.courses_attached += ['Опытный опыт']
reviewer_1.courses_attached += ['Ленивая лень']

reviewer_2 = Reviewer('Вкус', 'Вкусный')
reviewer_2.courses_attached += ['Data Science']
reviewer_2.courses_attached += ['Data Science']

reviewer_1.rate_hw(student_1, 'Data Science', 10)
reviewer_2.rate_hw(student_2, 'Data Science', 10)

reviewer_1.rate_hw(student_1, 'Data Science', 10)
reviewer_2.rate_hw(student_2, 'Ленивая лень', 10)

student_1.mark_for_lect(lecturer_1, 'Опытный опыт', 10)
student_1.mark_for_lect(lecturer_2, 'Ленивая лень', 10)

student_1.mark_for_lect(lecturer_1, 'Опытный опыт', 10)
student_1.mark_for_lect(lecturer_2, 'Ленивая лень', 10)


print(student_1)
print(student_2)
print(lecturer_1)
print(lecturer_2)
print(reviewer_1)
print(reviewer_2)
