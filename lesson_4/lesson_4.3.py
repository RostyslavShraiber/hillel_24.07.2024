import string

#отримуємо значення рядка
input_string = input("Введіть рядок: ")

#перетворюємо першу літеру кожного слова на велику
input_string = input_string.title()

#визначаємо значення очищеного рядка від символів та пробілів (за замовчуванням)
clean_string = ""

#визначаємо значення очищеного рядка від символів та пробілів на основі отриманого рядка з поля вводу
for char in input_string:
    if char not in string.punctuation and char != " ":
        clean_string += char

#створюємо хештег (додаємо # на початок)
hashtag = "#" + clean_string

#проводимо перевірку на довжину хештегу (довжина не повинна перевищувати 140 символів) та друкуємо його
if len(hashtag) <= 140:
    print(hashtag)
else:
    print(hashtag[:140])
