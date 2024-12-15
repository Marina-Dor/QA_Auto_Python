from models import Session, Student, Course

"""
Write a program that adds a new student to a database and adds him to a specific course.
"""


def add_student_to_course(first_name, last_name, age, course_name):
    session = Session()

    # Get the course by name
    course = session.query(Course).filter_by(name=course_name).first()
    if not course:
        print(f"Error: Course '{course_name}' does not exist.")
        session.close()
        return

    # Creating a new student
    new_student = Student(first_name=first_name, last_name=last_name, age=age)

    # Adding a student to the course
    new_student.courses.append(course)

    # Saving new student in DB
    session.add(new_student)
    session.commit()

    print(f"Student {first_name} {last_name} added to the course {course_name}.")
    session.close()


add_student_to_course("John", "Doe", 22, "Mathematics")
