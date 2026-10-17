TASKS_FILE = "tasks.txt"

def handle_file_error(error, action):
    if isinstance(error, FileNotFoundError):
        print("No saved task list found yet. One will be created when you add a task.")
    elif isinstance(error, PermissionError):
        print(f"Error: you don't have permission to {action} the tasks file.")
    else:
        print(f"Error: could not {action} the tasks file ({error}).")

def save_tasks(tasks, file_name):
    try:
        with open(file_name, "w", encoding="utf-8") as file:
            for task in tasks:
                file.write(task + "\n")
        return True
    except OSError as error:
        handle_file_error(error, "write to")
        return False

def load_tasks(file_name):
    tasks = []
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if line != "":
                    tasks.append(line)
    except OSError as error:
        handle_file_error(error, "read from")
    return tasks

def add_task(tasks, task):
    task = task.strip()
    if task == "":
        print("The task can't be empty.")
        return
    tasks.append(task)
    if save_tasks(tasks, TASKS_FILE):
        print("Task added.")

def remove_task(tasks, number):
    if number < 1 or number > len(tasks):
        print(f"Invalid number: choose between 1 and {len(tasks)}.")
        return
    removed = tasks.pop(number - 1)
    if save_tasks(tasks, TASKS_FILE):
        print(f"Removed: {removed}")

def view_tasks(tasks):
    if len(tasks) == 0:
        print("Your task list is empty.")
        return
    print("\n--- Your tasks ---")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def main():
    tasks = load_tasks(TASKS_FILE)

    while True:
        print("\n1. Add a task")
        print("2. Remove a completed task")
        print("3. View tasks")
        print("4. Quit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_task(tasks, input("Enter the task: "))
        elif choice == "2":
            view_tasks(tasks)
            if len(tasks) > 0:
                try:
                    number = int(input("Enter the number of the task to remove: "))
                    remove_task(tasks, number)
                except ValueError:
                    print("Invalid input: please enter a whole number.")
        elif choice == "3":
            view_tasks(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please enter 1, 2, 3 or 4.")

main()