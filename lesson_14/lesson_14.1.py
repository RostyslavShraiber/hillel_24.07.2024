class GroupFullError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class Human:
    def __init__(self, gender: str, age: int, first_name: str, last_name: str):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}, {self.gender}, {self.age} years old'


class Student(Human):
    def __init__(self, gender: str, age: int, first_name: str, last_name: str, record_book: str):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self) -> str:
        return f'Student: {self.first_name} {self.last_name}, {self.gender}, {self.age} years old, Record Book: {self.record_book}'


class Group:
    def __init__(self, number: str):
        self.number = number
        self.group = set()

    def add_student(self, student: Student, group_limit: int = 10) -> None:
        """Додає студента в групу."""
        if len(self.group) >= group_limit:
            raise GroupFullError(f"Cannot add more than {group_limit} students to the group.")
        self.group.add(student)


    def delete_student(self, last_name: str) -> None:
        """Видаляє студента з групи за прізвищем."""
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name: str) -> Student | None:
        """Шукає студента за прізвищем і повертає об'єкт класу Student або None."""
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self) -> str:
        """Повертає список студентів у вигляді рядка."""
        all_students = "\n".join([str(student) for student in self.group])
        return f'Group: {self.number}\n{all_students}'


#тестування
try:
    gr = Group('PD1')
    st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
    st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
    st3 = Student('Male', 30, 'Lena', 'Jobs', 'AN142')
    st4 = Student('Female', 25, 'Luiza', 'Taylor', 'AN145')
    st5 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
    st6 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
    st7 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
    st8 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
    st9 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
    st10 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
    st11 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
    # Додаємо 10 різних студентів (до ліміту)
    for student in [st1, st2, st3, st4, st5, st6, st7, st8, st9, st10]:
        gr.add_student(student)
    # Спроба додати 11-го студента, що має викликати виняток
    gr.add_student(st11)  # Новий студент
except Exception as e:
    print(f'Error: {e}')
