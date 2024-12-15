from src.db_manager import DatabaseManager
from src.models import Student, Course


class StudentManager(DatabaseManager):
    def add_student(self, first_name, last_name, age, course_name):
        course = self.session.query(Course).filter_by(name=course_name).first()
        if not course:
            print(f"Error: Course '{course_name}' does not exist.")
            return
        new_student = Student(first_name=first_name, last_name=last_name, age=age)
        new_student.courses.append(course)
        self.session.add(new_student)
        self.session.commit()
        print(f"Student {first_name} {last_name} added to the course {course_name}.")

    def delete_student(self, first_name, last_name):
        student = self.session.query(Student).filter_by(first_name=first_name, last_name=last_name).first()
        if not student:
            print(f"No student found with the name {first_name} {last_name}.")
        else:
            self.session.delete(student)
            self.session.commit()
            print(f"Student {first_name} {last_name} has been deleted.")

    # UPDATE students
    # SET first_name = 'Alice',
    #     last_name = 'Wonderland',
    # 	  age = 19
    # WHERE id = 1
    def update_student(self, first_name, last_name, new_first_name=None, new_last_name=None, new_age=None):
        student = self.session.query(Student).filter_by(first_name=first_name, last_name=last_name).first()
        if not student:
            print(f"Student {first_name} {last_name} not found.")
            return

        # Updating fields
        if new_first_name:
            student.first_name = new_first_name
        if new_last_name:
            student.last_name = new_last_name
        if new_age is not None:
            student.age = new_age

        self.session.commit()
        print("Student info was updated")
