import string

user_letters = input("Введіть два числа (наприклад: a-Z): ")

first_letter = user_letters[0]
separator = user_letters[1]
last_letter = user_letters[2]

if separator != "-" or len(user_letters) > 3:
    print("Вкажіть правильний формат тексту (див. підказку у прикладі при введенні).")
elif first_letter and last_letter not in string.ascii_letters:
    print("Вкажіть літери, що знаходяться в межах a-z або A-Z.")
else:
    all_letters = string.ascii_letters
    first_index = string.ascii_letters.index(first_letter)
    last_index = string.ascii_letters.index(last_letter)

    if first_index <= last_index:
        result = all_letters[first_index:last_index + 1]
    else:
        result = all_letters[last_index:first_index + 1][::-1]
    print(result)
