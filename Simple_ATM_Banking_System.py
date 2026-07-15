Balance = 0

def deposit():
    global Balance
    deposit_amount = int(input("Enter the amount that you want to deposit: "))
    print("----Successfuly Deposit----")
    Balance = Balance + deposit_amount
    print(f"Your current balance is {Balance}")

def withdraw():
    global Balance
    withdraw_amount = int(input("Enter the amount that you want to withdraw: "))
    if withdraw_amount < Balance:
        print("----Successfuly Withdrawn----")
        Balance = Balance - withdraw_amount
        print(f"Your remaining balance is {Balance}")
    else:
        print("----Withdraw Failed----")
        print(f"Your withdraw amount {withdraw_amount} is larger than your current balance:")

def balance():
    print(f"Your current balance is: {Balance}")

while True:
    print("1. Deposit \n 2. Withdraw \n 3. Balance \n 4. Exit")
    user_choice = input("Enter your choice: ")

    if user_choice == '1':
        deposit()
    elif user_choice == '2':
        withdraw()
    elif user_choice == '3':
        balance()
    elif user_choice == '4':
        break
