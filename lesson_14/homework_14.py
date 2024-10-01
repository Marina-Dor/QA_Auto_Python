"""Create a class Student with attributes firstname, lastname, age, and GPA.
Create an object of this class representing a student.
Then add a method to the Student class that allows you to change the student's GPA.
Display student information and change their GPA."""


class Student:
    def __init__(self, firstname, lastname, age, gpa):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.gpa = gpa

    def student_presentation(self):
        return f"Hello! My name is {self.firstname} {self.lastname}. I am {self.age} years old. My GPA is {self.gpa}."

    def change_student_gpa(self):
        self.gpa = input("Enter new GPA: ")
        return f"GPA was changed. New GPA is {self.gpa}"


new_student = Student("Maryna", "Doroshenko", 36, 86.3)
print(new_student.student_presentation())
print(new_student.change_student_gpa())
print(new_student.student_presentation())
