def add_one(some_list: list) -> list:
    # Перетворюємо список цілих чисел у стрічку
    some_string = "".join(map(str, some_list))

    # Перетворюємо стрічку у число та збільчуємо число на 1
    new_number = int(some_string) + 1

    # Перетворюємо число (збільшене на 1) назад у стрічку
    new_string = str(new_number)

    # Створюємо пустий список
    new_some_list = []

    # Наповнюємо пустий список елемантами стрічки та перетворюємо їх у цифри
    for elem in new_string:
        new_some_list.append(int(elem))
    return new_some_list


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")
