## List has tasks

## List is empty

# todo_list = ["Do Homework", "Mow Lawn", "Take out trash"]
todo_list = []



# for i in range(1,4):
#     print(i)
    
# disney_trips = [1,2,5]

# for trip in disney_trips:
#     print(f"The number of disney trips is: {trip}")
    

    

def view_tasks():
    if todo_list:
        print("This is the to do list")
        for task in todo_list:
            print(f"Task: {task}")
    else:
        print("It is empty")

view_tasks()