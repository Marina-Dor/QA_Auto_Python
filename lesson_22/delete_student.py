from models import Session, Student


def delete_student(first_name, last_name):
    session = Session()

    # Finding the student
    student = session.query(Student).filter_by(first_name=first_name, last_name=last_name).first()

    if not student:
        print(f"No student found with the name {first_name} {last_name}.")
    else:
        session.delete(student)
        session.commit()
        print(f"Student {first_name} {last_name} has been deleted from the database.")

    session.close()


delete_student("John", "Doe")
