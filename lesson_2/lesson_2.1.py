#ввід 4-значного числа
number = int(input("Введіть 4-значне число (Наприклад: 1234): "))

#отримання окремих цифр
number_1 = (number // 1000)
number_2 = (number // 100) % 10
number_3 = (number // 10) % 10
number_4 = (number % 10)


#вивід цифр у стовпчик
print(number_1)
print(number_2)
print(number_3)
print(number_4)
