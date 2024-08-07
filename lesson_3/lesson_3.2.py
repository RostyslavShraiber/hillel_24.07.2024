#Приклад №1 - список містить > 1 елемента
list_1 = [12, 3, 4, 10]

if len(list_1) > 1:
    #отримуємо останній елемент списку
    last_element = list_1.pop()
    #підставляємо останній елемент на початок списку
    first_element = list_1.insert(0, last_element)
    print(list_1) #відображаємо оновлений список
else:
    print(list_1) #відображаємо список без змін


#Приклад №2 - список містить = 1 елемент
list_2 = [1]

if len(list_2) > 1:
    last_element = list_2.pop()
    first_element = list_2.insert(0, last_element)
    print(list_2)
else:
    print(list_2)


#Приклад №3 - список не містить елементів = 0
list_3 = []
if len(list_3) > 1:
    last_element = list_3.pop()
    first_element = list_3.insert(0, last_element)
    print(list_3)
else:
    print(list_3)


#Приклад №4 - список містить > 1 елемента
list_4 = [12, 3, 4, 10, 8]
if len(list_4) > 1:
    last_element = list_4.pop()
    first_element = list_4.insert(0, last_element)
    print(list_4)
else:
    print(list_4)
