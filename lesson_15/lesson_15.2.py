import math

class Fraction:
    def __init__(self, a: int, b: int):
        if b == 0:
            raise ValueError("Знаменник не може бути рівним нулю")
        self.a = a
        self.b = b

    def reduce(self):
        """Скорочує дріб."""
        gcd = math.gcd(self.a, self.b)
        return Fraction(self.a // gcd, self.b // gcd)

    def __mul__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return Fraction(self.a * other.a, self.b * other.b)

    def __add__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        new_a = self.a * other.b + other.a * self.b
        new_b = self.b * other.b
        return Fraction(new_a, new_b)

    def __sub__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        # Використовуємо віднімання чисельників
        new_a = self.a * other.b - other.a * self.b
        new_b = self.b * other.b
        return Fraction(new_a, new_b)

    def __eq__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        # Порівнюємо скорочені значення
        self_reduced = self.reduce()
        other_reduced = other.reduce()
        return self_reduced.a == other_reduced.a and self_reduced.b == other_reduced.b

    def __gt__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.a * other.b > other.a * self.b

    def __lt__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.a * other.b < other.a * self.b

    def __str__(self):
        return f"Fraction: {self.a}, {self.b}"


# Тестування
f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
assert str(f_c) == 'Fraction: 21, 18', f"Отримано: {str(f_c)}"
f_d = f_b * f_a
assert str(f_d) == 'Fraction: 6, 18', f"Отримано: {str(f_d)}"
f_e = f_a - f_b
assert str(f_e) == 'Fraction: 3, 18', f"Отримано: {str(f_e)}"

assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True
f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2  # True
print('OK')
