user_number = int(input("Введіть число: "))

while user_number > 9:
    result = 1
    for digit in str(user_number):
        result *= int(digit)
    user_number = result
print(f"Кінцевий результат: {user_number}")