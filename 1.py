
def calc_avg(vals_dict):
        avg_sum = 0
        lect_counter = 0
        for grade_name, grade_val in vals_dict.items():
            avg_sum += sum(grade_val)
            lect_counter += len(grade_val)
        return round(avg_sum / lect_counter if lect_counter > 0 else 0, 1)


class Student():
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def rate_hw(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in lector.courses_attached and course in self.courses_in_progress:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        avg_sum = calc_avg(self.grades)
        text = F"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {avg_sum}.\n"
        text = text + F"Курсы в процессе изучения: " + ", ".join(self.courses_in_progress) + "\n"
        text = text + F"Завершенные курсы:" + ", ".join(self.finished_courses)
        return text


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    def __str__(self):
        avg_sum = calc_avg(self.grades)
        text = F"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {avg_sum}."
        return text


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        text = F"Имя: {self.name}\nФамилия: {self.surname}"
        return text





best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
 
some_reviewer = Reviewer("Ivan", "Pupkin")
some_reviewer.courses_attached += ['Python']
some_reviewer.rate_hw(best_student, "Python", 9)

print(best_student.grades)

some_lector = Lecturer("Oleg", "Buligin")
some_lector.courses_attached += ['Python']
some_lector.courses_attached += ['DataScience']


best_student.rate_hw(some_lector, "Python", 5)
best_student.rate_hw(some_lector, "Python", 8)

print(some_lector.grades)

print(some_reviewer)
print(some_lector)
print(best_student)
