import random
import string

def coding(word):
    if len(word) >= 3:
       new_word = word[1:] + word[0]
       start_letters = (random.choice(string.ascii_lowercase) for _ in range(3))
       end_letters = (random.choice(string.ascii_lowercase) for _ in range(3))
       return ''.join(''.join(start_letters) + new_word + ''.join(end_letters))
    else:
        return ''.join(reversed(word))


def decoding(word):
    if len(word) <3 :
        return ''.join(reversed(word))
    else:
        cleaned_word = word[3:-3]
        return cleaned_word[-1] + cleaned_word[:-1]

word = str(input("Enter your word : "))

User_choice = str(input("Do you want to code or decode the word? \n If you want to decode your word must      contain more than 8 letters (Enter 'code' or 'decode'): ")).lower()

if User_choice == 'code':
    print("Your coded word is: ",coding(word))
else:
    print("Your decoded word is: ",decoding(word))
