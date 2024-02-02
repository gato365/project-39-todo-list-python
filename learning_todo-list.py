# Define the to-do list
todo_list = []

def add_task(task):
    todo_list.append(task)
    print(f"\nTask '{task}' added to the list!")

def delete_task(task):
    try:
        todo_list.remove(task)
        print(f"\nTask '{task}' removed from the list!")
    except ValueError:
        print(f"\nTask '{task}' not found in the list.")

def view_tasks():
    if todo_list:
        print("\nTasks in your To-Do List:")
        for task in todo_list:
            print(f"- {task}")
    else:
        print("\nYour To-Do List is empty.")

while True:
    print("\nTo Do List Application")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. View all Tasks")
    print("4. Exit")
    
    choice = input("\nChoose an option: ")
    
    if choice == '1':
        task_to_add = input("\nEnter new task:")
        add_task(task_to_add)
    elif choice == '2':
        task_to_delete = input("\nEnter task to delete:")
        delete_task(task_to_delete)
    elif choice == '3':
        view_tasks()
    elif choice == '4':
        print("Leaving application")
        break
    else:
        print("Please adhere to the application guidelines")