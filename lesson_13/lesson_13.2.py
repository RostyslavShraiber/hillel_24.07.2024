class Counter:
    def __init__(self, current: int = 1, min_value: int = 0, max_value: int = 10):
        self.current: int = current
        self.min_value: int = min_value
        self.max_value: int = max_value

    def set_current(self, start: int) -> None:
        if start < self.min_value or start > self.max_value:
            raise ValueError(f"Current value must be between {self.min_value} and {self.max_value}.")
        self.current = start

    def set_max(self, max_max: int) -> None:
        if max_max < self.min_value:
            raise ValueError("Maximum value must be greater than or equal to the minimum value.")
        self.max_value = max_max
        if self.current > self.max_value:
            self.current = self.max_value

    def set_min(self, min_min: int) -> None:
        if min_min > self.max_value:
            raise ValueError("Minimum value must be less than or equal to the maximum value.")
        self.min_value = min_min
        if self.current < self.min_value:
            self.current = self.min_value

    def step_up(self) -> None:
        if self.current >= self.max_value:
            raise ValueError("Reached the maximum value!")
        self.current += 1

    def step_down(self) -> None:
        if self.current <= self.min_value:
            raise ValueError("Reached the minimum value!")
        self.current -= 1

    def get_current(self) -> int:
        return self.current


# Тестування
counter = Counter()
counter.set_current(7)
counter.step_up()
counter.step_up()
counter.step_up()
assert counter.get_current() == 10, 'Test1'
try:
    counter.step_up()
except ValueError as e:
    print(e)
assert counter.get_current() == 10, 'Test2'

counter.set_min(7)
counter.step_down()
counter.step_down()
counter.step_down()
assert counter.get_current() == 7, 'Test3'
try:
    counter.step_down()
except ValueError as e:
    print(e)
assert counter.get_current() == 7, 'Test4'
