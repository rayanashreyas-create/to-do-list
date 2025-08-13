def load_tasks():
    tasks = []
    try:
        with open("tasks.txt", "r") as file:
             tasks = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
            open("tasks.txt", "w").close()
    return tasks
    
def save_tasks(tasks):
    with open("tasks.txt", "w") as file:

        for task in tasks:
            file.write(task + "/n")

def view_tasks(tasks):
    if not tasks:
        print("No tasks yet!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}.{task}")

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{task}' added successfully!")

def main(tasks):
    tasks = load_tasks()

    while True:
        print("\n--- To-Do List Menu---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
             add_task(tasks)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1,2, or 3.")

if __name__ == "__main__":
    tasks = load_tasks()
    main(tasks)
    
        




      
