from student import Student
from instructor import Instructor
from teaching_assistant import TeachingAssistant
from course import Course
from enrollment import Enrollment


class StandardCourse(Course):
    pass


def main() -> None:
    # Create Courses
    math101 = StandardCourse.create_course("Calculus I", "MATH101")
    AI     = StandardCourse.create_course("Intro to AI", "Advanced AI")

    # Create Students
    Eric = Student("Eric Smith", "S001")
    Cyiza = Student("Cyiza Jones", "S002")

    # Create Instructor
    dr_brown = Instructor("Dr. Brown", "I001")

    # Create Teaching Assistant
    ALEXIS = TeachingAssistant("ALEXIS Green", "TA001")

    # Enroll Students
    enrollment1 = Enrollment(Eric, math101)
    enrollment2 = Enrollment(Cyiza, AI)
    enrollment3 = Enrollment(ALEXIS, AI)

    Eric.enroll(enrollment1)
    Cyiza.enroll(enrollment2)
    ALEXIS.enroll(enrollment3)

    math101.enroll_student(enrollment1)
    AI.enroll_student(enrollment2)
    AI.enroll_student(enrollment3)

    # Demo
    print(Eric)
    print("Courses enrolled:")
    for course in Eric.get_courses():
        print(f"- {course}")

    print()
    print(f"Students in {AI.title}:")
    for student in AI.get_students():
        print(f"- {student.name}")

    print()
    print(f"Combined course load of Alice and Bob:")
    combined_courses = Eric + Cyiza
    for course in combined_courses:
        print(f"- {course}")

if __name__ == "__main__":
    main()
