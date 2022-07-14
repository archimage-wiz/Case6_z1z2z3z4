
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
        avg_sum = calc_avg_score(self.grades)
        text = F"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {avg_sum}.\n"
        text = text + F"Курсы в процессе изучения: " + ", ".join(self.courses_in_progress) + "\n"
        text = text + F"Завершенные курсы:" + ", ".join(self.finished_courses)
        return text
    def __gt__(self, other_student):
        if isinstance(other_student, Student):
            return True if calc_avg_score(self.grades) > calc_avg_score(other_student.grades) else False
        else:
            return None

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
        avg_sum = calc_avg_score(self.grades)
        text = F"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {avg_sum}."
        return text
    def __gt__(self, other_lector):
        if isinstance(other_lector, Lecturer):
            return True if calc_avg_score(self.grades) > calc_avg_score(other_lector.grades) else False
        else:
            return None

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

def calc_avg_score(grades_dict):
        avg_sum = 0
        lect_counter = 0
        for grade_name, grade_val in grades_dict.items():
            avg_sum += sum(grade_val)
            lect_counter += len(grade_val)
        return round(avg_sum / lect_counter if lect_counter > 0 else 0, 1)


best_student = Student('Ruoy', 'Eman', 'Gomunkul')
best_student.courses_in_progress += ['Python']

worst_student = Student('Igor', 'Potakhin', 'Male')
worst_student.courses_in_progress += ['Python']
worst_student.finished_courses += ["C++"]

some_reviewer1 = Reviewer("Ivan", "Pupkin")
some_reviewer1.courses_attached += ['Python']
some_reviewer1.rate_hw(best_student, "Python", 9)
some_reviewer1.rate_hw(worst_student, "Python", 5)

some_reviewer2 = Reviewer("Пetr", "Petrov")
some_reviewer2.courses_attached += ['Python']
some_reviewer2.rate_hw(best_student, "Python", 10)
some_reviewer2.rate_hw(worst_student, "Python", 4)

some_lector1 = Lecturer("Oleg", "Buligin")
some_lector1.courses_attached += ['Python']
some_lector1.courses_attached += ['DataScience']

some_lector2 = Lecturer("Evgeniy", "Shmargunov")
some_lector2.courses_attached += ['Python']

best_student.rate_hw(some_lector1, "Python", 9)
best_student.rate_hw(some_lector2, "Python", 7)
worst_student.rate_hw(some_lector1, "Python", 7)
worst_student.rate_hw(some_lector2, "Python", 6)


print("Студенты:")
print(best_student)
print(worst_student, "\n")

print("Ревьюеры:")
print(some_reviewer1)
print(some_reviewer2, "\n")

print("Лекторы:")
print(some_lector1)
print(some_lector2, "\n")

print("Сравнение лекторов 1 и 2:")
print(some_lector1 > some_lector2, "\n")

print("Сравнение студентов 1 и 2:")
print(best_student < worst_student, "\n")

# Задание 4

def calculate_overall_scores_by_couse(estimated_list, course_name):
    average_sum = 0
    total_estimation_counter = 0
    for evaluated_obj in estimated_list:
        if isinstance(evaluated_obj, Student) or isinstance(evaluated_obj, Lecturer):
            if course_name in evaluated_obj.grades:
                average_sum += sum(evaluated_obj.grades[course_name])
                total_estimation_counter += len(evaluated_obj.grades[course_name])
    return round(average_sum / total_estimation_counter if total_estimation_counter > 0 else 0, 1)
            

some_students_array = [best_student, worst_student]
print("Средняя оценка по курсу Python среди всех студентов: ", end="")
print(calculate_overall_scores_by_couse(some_students_array, "Python"), "\n")

some_lectors_array = [some_lector1, some_lector2]
print("Средняя оценка по курсу Python среди всех лекторов: ", end="")
print(calculate_overall_scores_by_couse(some_lectors_array, "Python"), "\n")

