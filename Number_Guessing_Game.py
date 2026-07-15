import random

random_number = (random.randint(1,100))
count = 0

while True:   
   num = int(input("Please enter your input to guess a num: ")) 
   count +=1
   if random_number==num:
      print(f"You have guessed a correct number {num}")
      break
   elif count==7:
      print(f"You have used up all your attempts.\nYou had to guess the number {random_number}.")
      break
   if random_number < num:
      print(f"Your guessed number {num} is too high.")
   elif random_number > num:
      print(f"Your guessed number {num} is too low.")
   elif random_number==num:
      print(f"You have guessed a correct number {num}")
      break

print(f"You have done {count} attempts to guess a number.")


