todo_list = ["Have Fun", "Run"]




def delete_task(task):
    try:
        todo_list.remove(task)
        print(f"The task {task} has been deleted")
    except ValueError:
        print(f"Task {task} not in list")

print(todo_list)       
delete_task("Have Fun")
print(todo_list)
delete_task("run")
print(todo_list)