import string

#отримуємо значення рядка
input_string = input("Введіть рядок: ")
clean_string = ""

#визначаємо значення очищеного рядка від символів та пробілів на основі отриманого рядка з поля вводу
for char in input_string:
    if char not in string.punctuation:
        clean_string += char

#перетворення рядка на список зі словами
array_string = clean_string.split(' ')
hashtag = ""

for word in array_string:
    hashtag += word.capitalize()

#створюємо хештег (додаємо # на початок)
hashtag = "#" + hashtag

#проводимо перевірку на довжину хештегу (довжина не повинна перевищувати 140 символів) та друкуємо його
if len(hashtag) <= 140:
    print(hashtag)
else:
    print(hashtag[:140])
