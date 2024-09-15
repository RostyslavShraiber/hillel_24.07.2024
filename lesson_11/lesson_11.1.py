from inspect import isgenerator
from typing import Generator


def prime_generator(end: int) -> Generator[int, None, None]:
    """
    Генератор простих чисел.

    Параметри:
    end (int): Верхня межа діапазону, до якого потрібно знайти прості числа (включно).

    Повертає:
    Generator[int, None, None]: Генератор, який послідовно повертає прості числа.
    """
    def is_prime(n: int) -> bool:
        """
        Перевіряє, чи є число простим.

        Параметри:
        n (int): Число для перевірки на простоту.

        Повертає:
        bool: True, якщо число просте, False в іншому випадку.
        """
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    for num in range(2, end + 1):
        if is_prime(num):
            yield num


gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')
