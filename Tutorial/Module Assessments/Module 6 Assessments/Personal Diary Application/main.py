from datetime import datetime

DIARY_FILE = "diary.txt"

def add_entry(file_name, text, use_timestamp=True):
    try:
        with open(file_name, "a", encoding="utf-8") as file:
            if use_timestamp:
                stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.write(f"[{stamp}] {text}\n")
            else:
                file.write(text + "\n")
        print("Entry saved.")
    except PermissionError:
        print("Error: you don't have permission to write to the diary file.")
    except OSError as error:
        print(f"Error: could not save the entry ({error}).")

def view_entries(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            entries = file.read()
        if entries.strip() == "":
            print("Your diary is empty.")
        else:
            print("\n--- Your diary entries ---")
            print(entries)
    except FileNotFoundError:
        print("No diary found yet. Write your first entry to create one.")
    except PermissionError:
        print("Error: you don't have permission to read the diary file.")
    except OSError as error:
        print(f"Error: could not read the diary ({error}).")

def main():
    while True:
        print("\n1. Write a new entry")
        print("2. View previous entries")
        print("3. Quit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            text = input("Write your entry: ")
            answer = input("Add a timestamp? (y/n): ").strip().lower()
            add_entry(DIARY_FILE, text, use_timestamp=(answer == "y"))
        elif choice == "2":
            view_entries(DIARY_FILE)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please enter 1, 2 or 3.")

main()