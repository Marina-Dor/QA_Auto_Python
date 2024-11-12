from models import Session, Student

"""
Implement the ability to update student or course data
"""


# UPDATE students
# SET first_name = 'Alice',
#     last_name = 'Wonderland',
# 	  age = 19
# WHERE id = 1
def update_student(first_name, last_name, new_first_name=None, new_last_name=None, new_age=None):
    session = Session()

    # Finding the student
    student = session.query(Student).filter_by(first_name=first_name, last_name=last_name).first()

    # Updating fields
    if new_first_name:
        student.first_name = new_first_name
    if new_last_name:
        student.last_name = new_last_name
    if new_age is not None:
        student.age = new_age

    session.commit()
    print(f"Student info was updated")

    session.close()


update_student("Kevin", "Mccalister", new_first_name="Kevin", new_last_name="McAllister", new_age=20)


