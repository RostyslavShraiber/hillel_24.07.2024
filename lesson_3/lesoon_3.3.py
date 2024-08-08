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
