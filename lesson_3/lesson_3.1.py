#ввід першого числа
number_1 = int(input("Введіть перше число: "))

#вибір математичної дії (підтримуються: +, -, *, /)
type_operation = (input("Вкажіть тип арифметичної операції (+, -, *, /): "))

#ввід другого числа
number_2 = int(input("Введіть друге число: "))

#обчислення результату
if type_operation == "/":
    #перевірка ділення на 0
    if number_2 == 0 and type_operation == "/":
        print("Ви не зможете здійснити операцію ділення на 0")
    else:
        print("Ваш результат:", number_1 / number_2)
elif type_operation == "*":
    print("Ваш результат:", number_1 * number_2)
elif type_operation == "-":
    print("Ваш результат:", number_1 - number_2)
elif type_operation == "+":
    print("Ваш результат:", number_1 + number_2)
else:
    print("Дана операція зараз не підтримується. Зверніться у підтримку.")
