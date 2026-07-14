contacts = {}

def add():
    name = input("Please enter yoour name: ")
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
    filtered_data = contacts(name)
    if name in contacts:
        print("----Contact Found---- ")
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
        break