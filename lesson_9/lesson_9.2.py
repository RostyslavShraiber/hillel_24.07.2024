def difference(*args: int | float) -> int | float:
    """
    Обчислюємо різницю між найбільшим та найменшим аргументами (як числами) набору. Функція приймає будь-яку к-сть
    числових аргументів, дані аргументи можуть бути або цілими числами (int), або числами з плаваючою комою (float).

    :param args: Змінна кількість аргументів як числа (int, float)
    :return: Різниця між максимумом і мінімумом як число (int, float).
    """
    if args:
        # Обчислюємо різницю і повертаємо результат
        return round(max(args) - min(args), 2)
    else:
        #Якщо аргументів немає, повертаємо 0
        return 0


assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')
