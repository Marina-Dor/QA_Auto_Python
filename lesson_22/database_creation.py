import random
from models import Session, Student, Course

session = Session()

# Adding courses
course_names = ["Mathematics", "Computer Science", "History", "Physics", "Literature"]
courses = [Course(name=name) for name in course_names]
session.add_all(courses)
session.commit()

# Adding students
students_data = [
    {"first_name": "Alice", "last_name": "Wonderland", "age": 19},
    {"first_name": "Bob", "last_name": "Marley", "age": 20},
    {"first_name": "Charlie", "last_name": "Sheen", "age": 18},
    {"first_name": "Diana", "last_name": "Spenser", "age": 21},
    {"first_name": "Edward", "last_name": "Scissorhands", "age": 22},
    {"first_name": "Fiona", "last_name": "Brown", "age": 19},
    {"first_name": "George", "last_name": "Michael", "age": 20},
    {"first_name": "Hannah", "last_name": "Montana", "age": 18},
    {"first_name": "Ian", "last_name": "Somerhalder", "age": 21},
    {"first_name": "Jane", "last_name": "Air", "age": 22},
    {"first_name": "Kevin", "last_name": "Mccalister", "age": 19},
    {"first_name": "Laura", "last_name": "Dern", "age": 20},
    {"first_name": "Michael", "last_name": "Jackson", "age": 18},
    {"first_name": "Nancy", "last_name": "Wheeler", "age": 21},
    {"first_name": "Oscar", "last_name": "Wilde", "age": 22},
    {"first_name": "Paula", "last_name": "Mitchell", "age": 19},
    {"first_name": "Joanne", "last_name": "Cooper", "age": 20},
    {"first_name": "Rachel", "last_name": "Green", "age": 18},
    {"first_name": "Steve", "last_name": "Wright", "age": 21},
    {"first_name": "Tina", "last_name": "Turner", "age": 22}
]

students = [Student(first_name=data["first_name"], last_name=data["last_name"], age=data["age"])
            for data in students_data]
session.add_all(students)
session.commit()

# Random course distribution of students (1 student can be assigned to 1 and up to 3 courses)
all_courses = session.query(Course).all()
for student in session.query(Student).all():
    selected_courses = random.sample(all_courses, k=random.randint(1, 3))
    student.courses.extend(selected_courses)

# Saving to DB
session.commit()
session.close()

print("Data base was initialised with course names and list of 20 students")
