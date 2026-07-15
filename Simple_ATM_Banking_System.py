Balance = 0
pin_code = "1234"
login_attempts = 0
withdraw_attempts = 0
def deposit():
    global Balance
    deposit_amount = int(input("Enter the amount that you want to deposit: "))
    print("----Successfuly Deposit----")
    Balance = Balance + deposit_amount
    print(f"Your current balance is {Balance}")

def withdraw():
    global Balance , withdraw_attempts
    while True: 
       verification = input("Please enter your PIN Code: ")
       withdraw_attempts +=1
       if verification == pin_code:
           withdraw_amount = int(input("Enter the amount that you want to withdraw: "))
           if withdraw_amount < Balance:
              print("----Successfuly Withdrawn----")
              Balance = Balance - withdraw_amount
              print(f"Your remaining balance is {Balance}")
              break
           else:
              print("----Withdraw Failed----")
              print(f"Your withdraw amount {withdraw_amount} is larger than your current balance:")
              break
       elif verification != pin_code:
           print("---Incorrect PIN---")
           if withdraw_attempts == 3:
               print("You have used all of your attempts.")
               print("Your account is LOCKED.")
               break
           else:
               r_withdraw_attempts = 3-withdraw_attempts
               print(f"You have {r_withdraw_attempts} more attempts.")
   
def balance():
    print(f"Your current balance is: {Balance}")

while True:
    verification = input("Please enter your PIN Code: ")
    login_attempts +=1
    if verification == pin_code:
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
              print("Thank You..")
              break
        break
    elif verification != pin_code:
        print("---Incorrect PIN---")
        if login_attempts == 3:
            print("You have used all of your attempts.")
            print("Your account is LOCKED.")
            break
        else:
            r_attempts = 3-login_attempts
            print(f"You have {r_attempts} more attempts.")
    



    
