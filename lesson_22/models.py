from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

# Connection to DB PostgreSQL with user data
DATABASE_URL = "postgresql://postgres:123456aA!@localhost/students_management"
engine = create_engine(DATABASE_URL)

# Creating a base class for models
Base = declarative_base()

# Setting session
Session = sessionmaker(bind=engine)


"""
Creating a data model: Create a simple data model for a student management system. 
The model can contain tables for students, courses, and their relationships. 
Each student can be registered for several courses. 
For example, create 5 courses and randomly assign 20 students.
"""

# Course student relationships table
student_course_relationships = Table(
    'student_course_relationships', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('course_id', Integer, ForeignKey('courses.id'))
)


# MODEL STUDENT
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    age = Column(Integer)
    courses = relationship('Course', secondary=student_course_relationships, back_populates='students')


# MODEL COURSE
class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    students = relationship("Student", secondary=student_course_relationships, back_populates="courses")


# Creating tables
Base.metadata.create_all(engine)
