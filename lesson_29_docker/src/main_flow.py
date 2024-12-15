from src.student_manager import StudentManager
from src.course_manager import CourseManager
from src.db_data import DataInitialization

if __name__ == "__main__":
    student_manager = StudentManager()
    course_manager = CourseManager()
    data_init = DataInitialization()

    try:
        data_init.db_data()
        student_manager.add_student("John", "Doe", 22, "Mathematics")
        student_manager.delete_student("John", "Doe")
        course_manager.update_course("Mathematics", "Advanced Mathematics")
    finally:
        student_manager.close()
        course_manager.close()
