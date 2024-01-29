## Step 1: You create a list called todo_list with two items: “work” and “play”. You print the list to the console.
todo_list = ["work","play"]
print(todo_list)
## Step 2: You use the append() method to add another item, “study”, to the end of the todo_list. You print the updated list to the console.
todo_list.append("study")
print(todo_list)
## Step 3: You use the input() function to prompt the user to enter a new task. You store the user’s input in a variable called store_info. You use the append() method again to add the store_info to the todo_list. You print the final list to the console.
store_info = input("Add new task: " )
todo_list.append(store_info)
print(todo_list)
## Step 4: You define a function called add_task that takes one parameter, task. The function adds the task to the todo_list using the append() method. Then, it uses the print() function to display a message to the user. The message uses an f-string, which is a way to embed expressions inside string literals. The f-string has an f before the opening quotation mark and a curly brace {} around the expression. The expression is replaced with its value when the f-string is evaluated. In this case, the expression is task, which is the parameter of the function. The f-string prints the task that was added to the list. 
def add_task(task):
    todo_list.append(task)
    print(f"\n Task '{task}' added to the list!")


store_info = input("Add new task: " )
add_task(store_info)

