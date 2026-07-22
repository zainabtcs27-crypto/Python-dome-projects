import os
file_name = 'Word-character/Text_file.txt'
if os.path.exists(file_name):
    with open("Word-character/Text_file.txt", "r") as file:
        print("----File Found----")
        text_data = file.read()
        words = text_data.split()
        word_count = {}
        
        for word in words:
            if word in word_count:
                word_count[word]+=1
            else:
                word_count[word] = 1
        max_freq_word = ""
        max_count = 0
        for word, count in word_count.items():
            if count > max_count:
                max_count = count
                max_freq_word = word
            
        print(f"'{max_freq_word}' is your most repeated word in your file\n Its word count is {max_count}.")

else:
    print("----File Not Found---")