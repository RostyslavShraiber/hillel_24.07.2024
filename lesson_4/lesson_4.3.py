import random

# Створюємо список з випадкових чисел
original_list = [random.randint(1,10) for i in range(random.randint(3, 10))]
print("Оригінальний список:", original_list)

# Створюємо новий список з 3 елементів: першого, третього і другого з кінця
if len(original_list) >= 3:
    new_list = [original_list[0], original_list[2], original_list[-2]]
else:
    new_list = []

#Виводимо новий список
print("Новий список:", new_list)