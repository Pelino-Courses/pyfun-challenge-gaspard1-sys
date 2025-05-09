from student import Student
from instructor import Instructor


class TeachingAssistant(Student, Instructor):
    def __init__(self, name: str, id_number: str) -> None:
        super().__init__(name, id_number)

    def get_role(self) -> str:
        return "Teaching Assistant"
