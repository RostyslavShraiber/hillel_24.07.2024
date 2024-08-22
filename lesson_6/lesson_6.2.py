user_time = int(input("Введіть число (від 0 до 8640000): "))

if 0 <= user_time <= 8640000:

    div, mod = divmod(user_time, (24*60*60))
    days = str(div)

    last_digit = div % 10
    last_two_digits = div % 100

    if last_two_digits in range(11, 20):
        name_days = "днів"
    elif last_digit in [2, 3, 4]:
        name_days = "дні"
    elif last_digit == 1:
        name_days = "день"
    else:
        name_days = "днів"

    div, mod = divmod(mod, (60*60))
    hours = str(div).zfill(2)

    div, mod = divmod(mod, 60)
    minutes = str(div).zfill(2)
    seconds = str(mod).zfill(2)

    print(f'{days} {name_days}, {hours}:{minutes}:{seconds}')

else:
    print("Будь ласка, введіть число в діапазоні від 0 до 8640000 (див. підказку при введенні)")
