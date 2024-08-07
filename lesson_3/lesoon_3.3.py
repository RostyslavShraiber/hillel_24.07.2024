#Приклад №1 - список містить парну кількість елементів
list_1 = [1, 2, 3, 4, 5, 6]

#Визначення довжини списку
len_list_1 = len(list_1)

#Визначення довжини першої частини списку
if len_list_1 % 2 == 0: #Якщо кількість елементів у списку парна
    first_list_len = len_list_1 // 2
else: #Якщо кількість елементів у списку не парна
    first_list_len = len_list_1 // 2 + 1

#визначення вмісту першої частини списку
first_list = list_1[0:first_list_len]

#визначення вмісту другої частини списку
second_list = list_1[first_list_len:]

#створення списку з двома списками всередині
new_list_1 = [first_list, second_list]
print(new_list_1)



#Приклад №2 - список містить непарну кількість елементів
list_2 = [1, 2, 3]

len_list_2 = len(list_2)

if len_list_2 % 2 == 0: #Якщо кількість елементів у списку парна
    first_list_len_2 = len_list_2 // 2
else: #Якщо кількість елементів у списку не парна
    first_list_len_2 = len_list_2 // 2 + 1

first_list_2 = list_2[0:first_list_len_2]
second_list_2 = list_2[first_list_len_2:]
list_2 = [first_list_2, second_list_2]

print(list_2)



#Приклад №3 - список містить непарну кількість елементів
list_3 = [1, 2, 3, 4, 5]

len_list_3 = len(list_3)

if len_list_3 % 2 == 0: #Якщо кількість елементів у списку парна
    first_list_len_3 = len_list_3 // 2
else: #Якщо кількість елементів у списку не парна
    first_list_len_3 = len_list_3 // 2 + 1

first_list_3 = list_3[0:first_list_len_3]
second_list_3 = list_3[first_list_len_3:]
new_list_3 = [first_list_3, second_list_3]

print(new_list_3)



#Приклад №4 - список містить 1 елемент
list_4 = [1]

len_list_4 = len(list_4)

if len_list_4 % 2 == 0: #Якщо кількість елементів у списку парна
    first_list_len_4 = len_list_4 // 2
else: #Якщо кількість елементів у списку не парна
    first_list_len_4 = len_list_4 // 2 + 1

first_list_4 = list_4[0:first_list_len_4]
second_list_4 = list_4[first_list_len_4:]
new_list_4 = [first_list_4, second_list_4]

print(new_list_4)



#Приклад №5 - пустий список
list_5 = []

len_list_5 = len(list_5)

if len_list_5 % 2 == 0: #Якщо кількість елементів у списку парна
    first_list_len_5 = len_list_5 // 2
else: #Якщо кількість елементів у списку не парна
    first_list_len_5 = len_list_5 // 2 + 1

first_list_5 = list_5[0:first_list_len_5]
second_list_5 = list_5[first_list_len_5:]
new_list_5 = [first_list_5, second_list_5]

print(new_list_5)
