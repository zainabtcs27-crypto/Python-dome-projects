import os
import json
file_name = 'contacts.json'
if os.path.exists(file_name):
    with open ("contacts.json" , "r" ) as file:
        print("----File Found----")
        contacts = json.load(file)
else:
    print("----File not found----")
    contacts = {}

def add():
    name = input("Please enter your name: ")
    number = input("Please enter your number: ")
    contacts[name] = number
    print(f"Information about {name} is succsessfully added.")


def show():
    print(contacts)

def remove():
    name = input("Please enter the name that you want to remove from the dictionary: ")
    if name in contacts:
        contacts.pop(name)
        print("----Contact Removed---- ")
    else:
        print(f"Information about {name} is not found.")

def search():
    name = input("Please enter the name that you want to search from the dictionary: ")
    if name in contacts:
        print("----Contact Found---- ")
        filtered_data = contacts[name]
        print(f"Name: {name} ")
        print(f"Number: {filtered_data} ")
    else:
        print(f"Information about {name} is not found.")

while True:
    print("1. Add\n 2. Remove\n 3. Search\n 4. Show\n 5. Exit")
    user_choice = input("Enter your choice: ")

    if user_choice == '1':
        add()
    elif user_choice == '2':
        remove()
    elif user_choice == '3':
        search()
    elif user_choice == '4':
        show()
    elif user_choice == '5':
        with open("contacts.json", "w") as file:
            json.dump(contacts, file)
        print("Your file is updated successfully.")
        break