class Student:
    def __init__(self, name, age, grades=None):
        self.name = name
        self.age = age
        self.grades = grades if grades is not None else []

    def add_grade(self, grade):
        self.grades.append(grade)

    def calculate_average(self):
        if len(self.grades) == 0:
            return None
        return sum(self.grades) / len(self.grades)

    def display_info(self):
        average = self.calculate_average()
        average_text = "N/A" if average is None else f"{average:.2f}"
        print(f"Name: {self.name} | Age: {self.age} | Grades: {self.grades} | Average: {average_text}")


class StudentDatabase:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"Added student: {student.name}")

    def find_student(self, name):
        for student in self.students:
            if student.name.lower() == name.lower():
                return student
        return None

    def display_all(self):
        if len(self.students) == 0:
            print("The database is empty.")
            return
        for student in self.students:
            student.display_info()


def main():
    database = StudentDatabase()

    print("--- Adding students ---")
    database.add_student(Student("Alice", 20, [85, 90, 78]))
    database.add_student(Student("Bob", 22, [70, 65, 88, 92]))

    print("\n--- All students ---")
    database.display_all()

    print("\n--- Adding a new student ---")
    database.add_student(Student("Carol", 19))

    print("\n--- Adding grades for Carol ---")
    carol = database.find_student("Carol")
    carol.add_grade(95)
    carol.add_grade(100)
    carol.display_info()

    print("\n--- Final database ---")
    database.display_all()

main()