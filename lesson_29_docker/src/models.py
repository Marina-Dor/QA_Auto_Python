from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from src.db_manager import engine

Base = declarative_base()


# Association Table for Many-to-Many Relationship
student_course_relationships = Table(
     'student_course_relationships', Base.metadata,
     Column('student_id', Integer, ForeignKey('students.id')),
     Column('course_id', Integer, ForeignKey('courses.id'))
 )


# Student Model
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    age = Column(Integer)
    courses = relationship('Course', secondary=student_course_relationships, back_populates='students')

    def __repr__(self):
        return f"Student(id={self.id}, first_name={self.first_name}, last_name={self.last_name}, age={self.age})"


# Course Model
class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    students = relationship('Student', secondary=student_course_relationships, back_populates='courses')

    def __repr__(self):
        return f"Course(id={self.id}, name={self.name})"
