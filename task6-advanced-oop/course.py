from typing import List, Iterator
from enrollment import Enrollment
from abc import ABC


class Course(ABC):
    def __init__(self, title: str, code: str) -> None:
        self.title = title
        self.code = code
        self.enrollments: List[Enrollment] = []

    def enroll_student(self, enrollment: Enrollment) -> None:
        self.enrollments.append(enrollment)

    def get_students(self) -> Iterator:
        for enrollment in self.enrollments:
            yield enrollment.student

    def __str__(self) -> str:
        return f"{self.code}: {self.title}"

    @classmethod
    def create_course(cls, title: str, code: str) -> "Course":
        return cls(title, code)
