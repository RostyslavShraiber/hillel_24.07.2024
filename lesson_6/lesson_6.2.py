user_time = int(input("Введіть число (від 0 до 8640000): "))

if 0 <= user_time <= 8640000:

    days, mod = divmod(user_time, (24*60*60))
    hours, mod = divmod(mod, (60 * 60))
    minutes, seconds = divmod(mod, 60)

    last_two_digits = days % 100
    last_digit = days % 10

    if last_two_digits in range(11, 20):
        name_days = "днів"
    elif last_digit in [2, 3, 4]:
        name_days = "дні"
    elif last_digit == 1:
        name_days = "день"
    else:
        name_days = "днів"
    print(f'{days} {name_days}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}')
else:
    print("Будь ласка, введіть число в діапазоні від 0 до 8640000 (див. підказку при введенні)")
