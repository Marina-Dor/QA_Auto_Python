from src.models import Course
from src.db_manager import Session


# Reading the list of students assigned to a particular course
# SELECT students.first_name, students.last_name, students.age
# FROM students
# JOIN student_course_relationships
# ON students.id = student_course_relationships.student_id
# JOIN courses
# ON student_course_relationships.course_id = courses.id
# WHERE courses.name = 'Computer Science'
# ORDER BY students.last_name, students.first_name;
def get_students_by_course(course_name, session):
    if not session:
        raise ValueError("Session is invalid")

    course = session.query(Course).filter_by(name=course_name).first()
    print(f"The list of students assigned to a course {course_name}:\n")
    if course and course.students:
        for student in course.students:
            print(f"Student {student.first_name} {student.last_name}, Age: {student.age}")
        print(f"Total number of students attending {course_name} - {len(course.students)}")
    else:
        print("No students found")
