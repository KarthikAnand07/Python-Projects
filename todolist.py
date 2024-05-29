def add_task(task_list):
    task = input("Enter a task: ")
    task_list.append(task)
    print(f"'{task}' has been added to the list.")

def view_tasks(task_list):
    if not task_list:
        print("Your to-do list is empty.")
    else:
        print("Your to-do list:")
        for i, task in enumerate(task_list, 1):
            print(f"{i}. {task}")

def remove_task(task_list):
    view_tasks(task_list)
    if task_list:
        try:
            task_num = int(input("Enter the task number to remove: "))
            if 1 <= task_num <= len(task_list):
                removed_task = task_list.pop(task_num - 1)
                print(f"'{removed_task}' has been removed from the list.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def save_tasks(task_list, filename="tasks.txt"):
    with open(filename, "w") as file:
        for task in task_list:
            file.write(task + "\n")
    print("Tasks have been saved.")

def load_tasks(filename="tasks.txt"):
    try:
        with open(filename, "r") as file:
            task_list = [line.strip() for line in file]
        print("Tasks have been loaded.")
    except FileNotFoundError:
        print("No saved tasks found.")
        task_list = []
    return task_list

def get_user_choice():
    print("\n Choose an action:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Save a tasks")
    print("5. Load tasks")
    print("6. Exit")
    choice = input("Enter the number of your choice: ")
    return choice

def perform_action(choice, task_list):
    if choice == '1':
        add_task(task_list)
    elif choice == '2':
        view_tasks(task_list)
    elif choice == '3':
        remove_task(task_list)
    elif choice == '4':
        save_tasks(task_list)
    elif choice == '5':
        task_list = load_tasks()
    elif choice == '6':
        print("Exiting the to-do list application.")
        return False
    else:
        print("Invalid choice. Please enter a number from 1 to 6.")
    return True

def main():
    task_list = []
    running = True
    while running:
        choice = get_user_choice()
        running = perform_action(choice, task_list)

if __name__ == "__main__":
    main()
