#ввід 5-значного числа
number = int(input("Введіть 5-значне число (Наприклад: 12345): "))

#отримання окремих цифр
number_1 = (number // 10000)
number_2 = (number // 1000) % 10
number_3 = (number // 100) % 10
number_4 = (number // 10) % 10
number_5 = (number % 10)

#вивід цифр у зворотньому порядку
print(number_5,number_4,number_3,number_2,number_1)