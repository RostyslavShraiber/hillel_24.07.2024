import string
import keyword

my_string = input("Вкажіть текст: ")

if my_string in keyword.kwlist:
    print(False)
else:
    if my_string[0].isdigit():
        print(False)
    elif any(char.isupper() for char in my_string):
        print(False)
    elif any(char in string.punctuation.replace('_', '') for char in my_string):
        print(False)
    elif my_string.count('_') > 1:
        print(False)
    else:
        print(True)
