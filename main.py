print("Привет, GitHub! Это моя лабораторная работа №7.")

# main.py — учебный файл
power = 999
print(f"Сила: {power}")
# черновик новой функции


class Student:
    def __init__(self, name, group):
        self.name = name
        self.group = group
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

def main():
    student = Student("Иван Иванов", "ИВТ-101")
    student.add_grade(5)
    student.add_grade(4)
    print(f"Студент: {student.name}, средний балл: {student.get_average()}")

if __name__ == "__main__":
    main()
