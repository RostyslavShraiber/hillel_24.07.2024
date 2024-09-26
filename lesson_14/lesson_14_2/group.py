from student import Student


class GroupFullError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


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
