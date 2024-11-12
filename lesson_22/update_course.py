from models import Session, Course


# UPDATE courses
# SET name = 'Advanced Computer Science'
# where id = 1
def update_course(course_name, new_course_name):
    session = Session()

    course = session.query(Course).filter_by(name=course_name).first()

    if not course:
        print(f"No course found with the name {course_name}")
    else:
        course.name = new_course_name

    session.commit()
    print(f"Course name was updated")
    session.close()


update_course('Computer Science', 'Advanced Computer Science')
