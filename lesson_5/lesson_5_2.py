while True:
    number_1 = int(input("Введіть перше число: "))
    type_operation = (input("Вкажіть тип арифметичної операції (+, -, *, /): "))
    number_2 = int(input("Введіть друге число: "))

    #обчислення результату
    if type_operation == "/": #перевірка на дію ділення
        if number_2 == 0: #перевірка ділення на 0
            print("Ви не можете здійснити операцію ділення на 0")
        else:
            print("Ваш результат:", number_1 / number_2)
    elif type_operation == "*": #перевірка на дію множення
        print("Ваш результат:", number_1 * number_2)
    elif type_operation == "-": #перевірка на дію віднімання
        print("Ваш результат:", number_1 - number_2)
    elif type_operation == "+": #перевірка на дію додавання
        print("Ваш результат:", number_1 + number_2)
    else: #перевірка на некоректну арифметичну дію
        print("Дана операція зараз не підтримується. Зверніться у підтримку.")

    continue_to_count = input("Ви бажаєте продовжити? (для продовження напишіть 'yes' or 'y'): ")

    if "y" not in continue_to_count.lower():
        print ("Приходьте ще :)")
        break
