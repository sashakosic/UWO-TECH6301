GRADES_FILE = "grades.txt"

def get_grade_input():
    while True:
        text = input("Enter the grade (0-100): ").strip()
        try:
            grade = float(text)
        except ValueError:
            print("Invalid input: please enter a number, like 85 or 92.5.")
            continue
        if 0 <= grade <= 100:
            return grade
        print("Invalid input: the grade must be between 0 and 100.")

def add_grade(file_name, subject, grade):
    try:
        with open(file_name, "a", encoding="utf-8") as file:
            file.write(f"{subject},{grade}\n")
        print("Grade saved.")
    except PermissionError:
        print("Error: you don't have permission to write to the grades file.")
    except OSError as error:
        print(f"Error: could not save the grade ({error}).")

def load_grades(file_name):
    grades = []
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if line == "":
                    continue
                try:
                    subject, grade = line.rsplit(",", 1)
                    grades.append((subject, float(grade)))
                except ValueError:
                    print(f"Skipping a damaged line in the file: {line!r}")
    except FileNotFoundError:
        print("No grades saved yet. Add a grade to create the file.")
    except PermissionError:
        print("Error: you don't have permission to read the grades file.")
    except OSError as error:
        print(f"Error: could not read the grades file ({error}).")
    return grades

def calculate_average(grades):
    if len(grades) == 0:
        return None
    total = sum(grade for subject, grade in grades)
    return total / len(grades)

def show_grades(file_name):
    grades = load_grades(file_name)
    if len(grades) == 0:
        print("There are no grades to show.")
        return
    print("\n--- Your grades ---")
    for subject, grade in grades:
        print(f"{subject}: {grade}")
    print(f"Average grade: {calculate_average(grades):.2f}")

def main():
    while True:
        print("\n1. Add a grade")
        print("2. View grades and average")
        print("3. Quit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            subject = input("Enter the subject: ").strip()
            if subject == "":
                print("The subject can't be empty.")
                continue
            grade = get_grade_input()
            add_grade(GRADES_FILE, subject, grade)
        elif choice == "2":
            show_grades(GRADES_FILE)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please enter 1, 2 or 3.")

main()