todo_list = ["work","play"]
print(todo_list)

todo_list.append("study")
print(todo_list)

# store_info = input("Add new task: ")
# todo_list.append(store_info)
# print(todo_list)

def add_task(task):
    todo_list.append(task)
    print(f"\n Task {task} added to the list!")

store_info = input("Add task this time: ")
add_task(store_info)