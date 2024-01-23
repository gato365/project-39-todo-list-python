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

# Main program starts here
while True:
    print("\nTo-Do List Application")
    print("1. Add a task")
    print("2. Delete a task")
    print("3. View all tasks")
    print("4. Exit")

    choice = input("\nChoose an option: ")

    if choice == '1':
        task_to_add = input("\nEnter the task you want to add: ")
        add_task(task_to_add)
    elif choice == '2':
        task_to_delete = input("Enter the task you want to delete: ")
        delete_task(task_to_delete)
    elif choice == '3':
        view_tasks()
    elif choice == '4':
        print("Exiting the To-Do List Application. Have a great day!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
