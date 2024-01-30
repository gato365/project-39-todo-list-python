## Part 1: View Tasks - Two things:
1) if it empty
2) if it has items

1) if it is empty tell user that it is empty
2) display the list
    but we want to add some paszazz to this view

```
def view_task():
    if todo_list:
        print("\nThis is your to do list: ")
        print(todo_list)
    else:
        print("\nYour To-Do List is empty.")
```

## Part 2: For Loop

- This is when we can introduce a for loop for paszazz
- A for loop is similar to a while loop in that it repeast an action
- The only difference is that a for loop knows when it is going to stop and a while loop does not

for example

a for loop looks like this in python
```
for i in range(1, 4):
    print(i)
```
Note that python starts with 0 rather than 1


lets create a small list
```
disney_trips = [1,2,3]
```
if I run 
```
for trip in disney_trips:
    print(trip)
```

Lets add some paszazz
```
for trip in disney_trips:
    print(f"The number of trips is - {trip}")
```

Now if our list is of `todo_list`` is
```
todo_list = ["Have Fun", "Look at Birds", "Run"]
```

We can add paszazz with our
```
for task in todo_list:
    print(f"Task: {task}")
```

soooooo we can finally develop a view_task function

```
def view_task():
    if todo_list:
        print("\n This is your to do list: ")
        for task in todo_list:
            print(f"Task: {task}")
    else:
        print("\nYour To-Do List is empty.")
```




    