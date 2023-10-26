path_to_file = "books/frankenstein.txt"

def word_nb(text):
    word_list = text.split()
    return len(word_list)

def count_letters(text):
    letter_dict = {}
    lower_text = text.lower()
    word_list = lower_text.split()
    for word in word_list:
        if word.isalpha():
            for letter in word:
                if letter in letter_dict:
                    letter_dict[letter] = letter_dict[letter]+1
                else:
                    letter_dict[letter] = 1
    return letter_dict

with open(path_to_file) as f:
    file_contents = f.read()
    print ("--- Begin report of books/frankenstein.txt ---")
    print (f"{word_nb(file_contents)} words found in the document")
    letter_list = list(count_letters(file_contents).items())
    for letter in letter_list:
        print(f"The '{letter[0]}' character was found {letter[1]} times")
    
