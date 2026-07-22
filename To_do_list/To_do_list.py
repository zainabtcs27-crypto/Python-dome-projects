import os
file = 'To_do_list/to_do_list.txt'
task_list = []
def add_task():
    new_task = input("Enter your new task: ")
    if new_task in  task_list:
        print("That task is already exist in your To-Do List.")
    else:
        task_list.append(new_task + "\n")
        print("Your task is successfully added.")
def search_task():
    u_index = int(input("Please enter the index of the task that you want to search: "))
    if u_index > 0 and u_index <= len(task_list):
        l_index = u_index - 1
        print(f"The task for whom you are looking is : {task_list[l_index]}")
    else: 
        print("----Index Not Found---")
def view_tasks():
    for index , task in enumerate(task_list):
        print(index ,task)
   
def remove_task():
    u_index = int(input("Please enter the index of the task that you want to remove: "))
    if u_index > 0 and u_index <= len(task_list):
        l_index = u_index - 1
        task_list.pop(l_index)
        print("Your Defined task is successfully removed from your To-Do List")
    else: 
        print("----Index Not Found---")

def mark():
    u_index = int(input("Please enter the index of the task that you want to mark done: "))
    if u_index > 0 and u_index <= len(task_list):
        l_index = u_index - 1
        task_list[l_index] = task_list[l_index] + "Done" + "\n"
        print("Your Defined task is successfully marked Done.")
    else: 
        print("----Index Not Found---")


if os.path.exists(file):
    with open("To_do_list/to_do_list.txt", "r") as f:
        print("---File Found----")
        tasks = f.readlines()
        
        for task in tasks:
            if task not in task_list:
              if not task.endswith("\n"):
                 task = task + "\n"
            task_list.append(task)
else:
    print("File not found")


while True:
    print("---Menu List---")
    print("1. Add New Task \n 2. View Task\n 3. Remove Task \n 4. Mark Completed\n 5. Search Spefific Task \n 6. Exit")
    user_choice = input("Enter your choice: ")

    if user_choice == '1':
        add_task()
    elif user_choice == '2':
        view_tasks()
    elif user_choice == '3':
        remove_task()
    elif user_choice == '4':
        mark()
    elif user_choice == '5':
        search_task()
    elif user_choice == '6':
        with open("To_do_list/to_do_list.txt", "w") as f:
            for task in task_list:
               f.write(task) 
            print("Your file is updated successfully.")
            break