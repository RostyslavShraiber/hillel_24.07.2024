def common_elements():

    #Створюємо першу множину (числа кратні 3)
    set_1 = set(range(0, 100, 3))

    #Створюємо другу множину (числа кратні 5)
    set_2 = set(range(0, 100, 5))

    #Знаходимо перетин чисел у двох списках
    intersection_set = set_1.intersection(set_2)

    return intersection_set


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print("OK")
