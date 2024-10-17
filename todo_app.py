# todo_app.py
def display_menu():
    print("To-Do List App")
    print("----------------")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as completed")
    print("4. Delete task")
    print("5. Quit")
def add_task():
    task_description = input("Enter a task description: ")
    with open("tasks.txt", "a") as file:
        file.write(task_description + "\n")

def view_tasks():
    with open("tasks.txt", "r") as file:
        tasks = file.read().splitlines()
    if tasks:
        print("Your tasks:")
        for task in tasks:
            print(task)
    else:
        print("No tasks to display.")
def mark_task_as_completed():
    with open("tasks.txt", "r") as file:
        tasks = file.read().splitlines()
    if tasks:
        print("Your tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        task_number = int(input("Enter the task number to mark as completed: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1] = tasks[task_number - 1].replace("[ ]", "[X]")
            with open("tasks.txt", "w") as file:
                file.write("\n".join(tasks))
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
    else:
        print("No tasks to display.")
def delete_task():
    with open("tasks.txt", "r") as file:
        tasks = file.read().splitlines()
    if tasks:
        print("Your tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        task_number = int(input("Enter the task number to delete: "))
        if 1 <= task_number <= len(tasks):
            del tasks[task_number - 1]
            with open("tasks.txt", "w") as file:
                file.write("\n".join(tasks))
            print("Task deleted!")
        else:
            print("Invalid task number.")
    else:
        print("No tasks to display.")
def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
           add_task() 
                # Add task logic will go here
        elif choice == "2":
           view_tasks()     # View tasks logic will go here
      
        elif choice == "3":
            mark_task_as_completed() 
             # Mark task as completed logic will go here
        elif choice == "4":
            delete_task()  
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()