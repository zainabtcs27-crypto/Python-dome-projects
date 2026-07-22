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

sentence = str(input("Please Enter your sentence : "))
word_list = sentence.split()

User_choice = str(input("Do you want to code or decode the sentence? (Enter 'code' or 'decode'): ")).lower()
new_word_list = []
for word in word_list:
    if User_choice == 'code':
        new_word_list.append(coding(word))
        # print("Your coded word is: ",coding(word))
    else:
        new_word_list.append(decoding(word))
        # print("Your decoded word is: ",decoding(word))
print("Your resulted sentence is: ", ' '.join(new_word_list))

