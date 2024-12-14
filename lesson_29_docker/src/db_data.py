from src.models import Course, Student
from src.db_manager import DatabaseManager


class DataInitialization(DatabaseManager):
    def db_data(self):
        # Adding Courses
        course_names = ["Mathematics", "Computer Science", "History", "Physics", "Literature"]
        courses = [Course(name=name) for name in course_names]
        self.session.add_all(courses)
        self.session.commit()

        # Adding Students
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
        students = [Student(**data) for data in students_data]
        self.session.add_all(students)
        self.session.commit()

        print("Data base was initialised with course names and list of students")
