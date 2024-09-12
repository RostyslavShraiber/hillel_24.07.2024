from inspect import isgenerator
from typing import Generator


def generate_cube_numbers(end: int) -> Generator[int, None, None]:
    """
    Генератор кубів чисел, починаючи з числа 2 і до заданої верхньої межі.

    Параметри:
    end (int): Верхня межа діапазону для генерації кубів чисел. Генерація завершується, коли куб перевищує це значення.

    Повертає:
    Generator[int, None, None]: Генератор, який послідовно повертає куби чисел, починаючи з 2 і до числа, яке в кубі не
    перевищує `end`.
    """
    n = 2 # починаємо з 2, так як 1 ** 3 поверне 1
    while True:
        cube = n ** 3
        if cube > end:
            return  # Завершує генерацію, якщо куб більше зазначеного значення
        yield cube
        n += 1


gen = generate_cube_numbers(1)
assert isgenerator(gen) == True, 'Test0'
assert list(generate_cube_numbers(10)) == [8], 'оскільки воно менше 10.'
assert list(generate_cube_numbers(100)) == [8, 27, 64], '5 у кубі це 125, а воно вже більше 100'
assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000], '10 у кубі це 1000'
print('Ok')
