from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from student import Student
    from course import Course


class Enrollment:
    def __init__(self, student: "Student", course: "Course") -> None:
        self.student = student
        self.course = course
