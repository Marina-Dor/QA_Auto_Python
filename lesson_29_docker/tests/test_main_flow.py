import pytest
import builtins
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from src.models import Base, Student, Course
from src.reading_from_db import get_students_by_course
from src.student_manager import StudentManager
from src.course_manager import CourseManager


# Fixture for creating temp database
@pytest.fixture(scope="function")
def test_session():
    TEST_DATABASE_URL = "postgresql://postgres:123456aA!@postgres_container:5432/test_student_management"
    engine = create_engine(TEST_DATABASE_URL)

    # Create the test database if it doesn't exist
    if not database_exists(engine.url):
        create_database(engine.url)

    Session = sessionmaker(bind=engine)

    # Create tables before each test
    Base.metadata.create_all(engine)
    session = Session()

    yield session

    # Drop tables after each test
    session.close()
    Base.metadata.drop_all(engine)
    engine.dispose()


@pytest.fixture(scope="function")
def student_manager(test_session):
    class TestStudentManager(StudentManager):
        def __init__(self):
            self.session = test_session

    return TestStudentManager()


@pytest.fixture(scope="function")
def course_manager(test_session):
    class TestCourseManager(CourseManager):
        def __init__(self):
            self.session = test_session

    return TestCourseManager()


# Testing features
def test_add_student(student_manager, test_session):
    # Adding course
    test_session.add(Course(name="Mathematics"))
    test_session.commit()

    # Adding student
    student_manager.add_student("John", "Doe", 22, "Mathematics")

    # Checking that student was added
    student = test_session.query(Student).filter_by(first_name="John", last_name="Doe").first()
    assert student is not None
    assert student.age == 22
    assert len(student.courses) == 1
    assert student.courses[0].name == "Mathematics"


def test_delete_student(student_manager, test_session):
    # Adding student
    student = Student(first_name="John", last_name="Doe", age=22)
    test_session.add(student)
    test_session.commit()

    # Deleting student
    student_manager.delete_student("John", "Doe")

    # Checking that student was deleted
    student = test_session.query(Student).filter_by(first_name="John", last_name="Doe").first()
    assert student is None


def test_update_student(student_manager, test_session):
    # Adding new student
    student = Student(first_name="John", last_name="Doe", age=22)
    test_session.add(student)
    test_session.commit()

    # Updating student data
    student_manager.update_student("John", "Doe", new_first_name="Johnny", new_age=23)

    # checking that data was updated
    student = test_session.query(Student).filter_by(first_name="Johnny", last_name="Doe").first()
    assert student is not None
    assert student.age == 23


def test_get_students_by_course(test_session):
    # Adding course and students for test
    course = Course(name="Mathematics")
    student1 = Student(first_name="Alice", last_name="Smith", age=20)
    student2 = Student(first_name="Bob", last_name="Brown", age=22)
    course.students.extend([student1, student2])
    test_session.add(course)
    test_session.commit()

    result = []

    def mock_print(*args):
        result.append(" ".join(map(str, args)))

    original_print = builtins.print
    builtins.print = mock_print
    try:
        get_students_by_course("Mathematics", test_session)
    finally:
        builtins.print = original_print

    # Checking the results
    assert "Alice Smith" in " ".join(result)
    assert "Bob Brown" in " ".join(result)
    assert "Total number of students attending Mathematics - 2" in " ".join(result)
