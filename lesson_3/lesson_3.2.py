list_1 = [12, 3, 4, 10]

if len(list_1) > 1:
    #отримуємо останній елемент списку
    last_element = list_1.pop()
    #підставляємо останній елемент на початок списку
    first_element = list_1.insert(0, last_element)
    print(list_1) #відображаємо оновлений список
else:
    print(list_1) #відображаємо список без змін
