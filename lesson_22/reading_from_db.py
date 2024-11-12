from models import Session, Student, Course
from utils import print_separator


# Reading info about the students and their courses. Counting the number of students
# SELECT students.first_name, students.last_name, students.age, courses.name AS course_name
# FROM students
# JOIN student_course_relationships ON students.id = student_course_relationships.student_id
# JOIN courses ON student_course_relationships.course_id = courses.id
# ORDER BY students.last_name, students.first_name;
def reading_all_students_and_courses():
    session = Session()
    students = session.query(Student).all()
    number_of_students = 0
    for student in students:
        course_names = ", ".join(course.name for course in student.courses)
        print(f"Student {student.first_name} {student.last_name}, Age: {student.age}, "
              f"attending course: {course_names}")
        number_of_students += 1
    print(f"Total number of students - {number_of_students}")
    session.close()


reading_all_students_and_courses()

print_separator()

"""
Write database queries that return information about students assigned to a particular course 
or courses to which a particular student is assigned.
"""


# Reading the list of students assigned to a particular course
# SELECT students.first_name, students.last_name, students.age
# FROM students
# JOIN student_course_relationships
# ON students.id = student_course_relationships.student_id
# JOIN courses
# ON student_course_relationships.course_id = courses.id
# WHERE courses.name = 'Computer Science'
# ORDER BY students.last_name, students.first_name;
def get_students_by_course(course_name):
    session = Session()
    number_of_students = 0
    # Finding the course
    course = session.query(Course).filter_by(name=course_name).first()
    print(f"The list of students assigned to a course {course_name}:\n")
    if course:
        for student in course.students:
            print(f"Student {student.first_name} {student.last_name}, Age: {student.age}")
            number_of_students += 1
        print(f"Total number of students attending {course_name} - {number_of_students}")
    else:
        print("No students found")

    session.close()


get_students_by_course("Computer Science")

print_separator()


# Reading the list of courses to which a particular student is assigned
# SELECT courses.name AS course_name
# FROM courses
# JOIN student_course_relationships
# ON courses.id = student_course_relationships.course_id
# JOIN students
# ON student_course_relationships.student_id = students.id
# WHERE students.first_name = 'Kevin' AND students.last_name = 'Mccalister';
def get_courses_by_student(first_name, last_name):
    session = Session()

    # Finding the student
    student = session.query(Student).filter_by(first_name=first_name, last_name=last_name).first()

    if not student:
        print(f"No student found")
    else:
        print(f"The list of courses assigned to student {first_name} {last_name}:\n")
        if student and student.courses:
            for course in student.courses:
                print(f"Course {course.name}")
        else:
            print("No courses found")

    session.close()


get_courses_by_student("Kevin", "McAllister")
print_separator()


# Get info about particular student
# SELECT students.first_name, students.last_name, students.age, courses.name AS course_name
# FROM students
# JOIN student_course_relationships
# ON students.id = student_course_relationships.student_id
# JOIN courses
# ON student_course_relationships.course_id = courses.id
# WHERE students.first_name = 'Kevin' AND students.last_name = 'McAllister';
def get_student_info(first_name, last_name):
    session = Session()

    # Finding the student
    student = session.query(Student).filter_by(first_name=first_name, last_name=last_name).first()
    if not student:
        print(f"No student found")
    else:
        print(f"Student {student.first_name} {student.last_name}, Age: {student.age} ")
        if student.courses:
            print(f"attending course:")
            for course in student.courses:
                print(course.name)
        else:
            print("isn't assigned to any course")


get_student_info("Kevin", "McAllister")
