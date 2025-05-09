from typing import List, Iterator
from person import Person
from enrollment import Enrollment


class Student(Person):
    def __init__(self, name: str, id_number: str) -> None:
        super().__init__(name, id_number)
        self.enrollments: List[Enrollment] = []

    def enroll(self, enrollment: Enrollment) -> None:
        self.enrollments.append(enrollment)

    def get_courses(self) -> Iterator:
        for enrollment in self.enrollments:
            yield enrollment.course

    def get_role(self) -> str:
        return "Student"

    def __add__(self, other: "Student") -> List:
        return list({course for course in self.get_courses()}.union({course for course in other.get_courses()}))
