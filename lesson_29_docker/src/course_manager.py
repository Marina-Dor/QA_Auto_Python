from src.db_manager import DatabaseManager
from src.models import Course


class CourseManager(DatabaseManager):
    def update_course(self, course_name, new_course_name):
        course = self.session.query(Course).filter_by(name=course_name).first()
        if not course:
            print(f"No course found with the name {course_name}.")
        else:
            course.name = new_course_name
            self.session.commit()
            print(f"Course name updated to {new_course_name}.")
