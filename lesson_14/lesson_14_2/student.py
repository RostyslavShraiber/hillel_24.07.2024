from human import Human


class Student(Human):
    def __init__(self, gender: str, age: int, first_name: str, last_name: str, record_book: str):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self) -> str:
        return f'Student: {self.first_name} {self.last_name}, {self.gender}, {self.age} years old, Record Book: {self.record_book}'

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        else:
            return str(self) == str(other)

    def __hash__(self):
        return hash(str(self))
