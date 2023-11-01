import os
from datetime import datetime

import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Student


def add_students():
    Student.objects.create(
        student_id='FC5204',
        first_name='John',
        last_name='Doe',
        birth_date=datetime.strptime("15/05/1995", "%d/%m/%Y").strftime("%Y-%m-%d"),
        email='john.doe@university.com'
    )

    student_2 = Student(
        student_id='FE0054',
        first_name='Jane',
        last_name='Smith',
        email='jane.smith@university.com'
    )

    student_2.save()

    Student.objects.create(
        student_id='FH2014',
        first_name='Alice',
        last_name='Johnson',
        birth_date=datetime.strptime("10/02/1998", "%d/%m/%Y").strftime("%Y-%m-%d"),
        email='alice.johnson@university.com'
    )

    Student.objects.create(
        student_id='FH2015',
        first_name='Bob',
        last_name='Wilson',
        birth_date=datetime.strptime("25/11/1996", "%d/%m/%Y").strftime("%Y-%m-%d"),
        email='bob.wilson@university.com'
    )


# add_students()
# print(Student.objects.all())

def get_students_info():
    students = Student.objects.all()
    student_info = [f"Student №{student.student_id}: {student.first_name} "
                    f"{student.last_name}; Email: {student.email}" for student in students]

    return "\n".join(student_info)


# print(get_students_info())


def update_students_emails():
    students = Student.objects.all()

    for student in students:
        new_email = student.email.replace('university.com', 'uni-students.com')

        student.email = new_email

        student.save()


# update_students_emails()
# for student in Student.objects.all():
#     print(student.email)


def truncate_students():

    Student.objects.all().delete()


# truncate_students()
# print(Student.objects.all())
# print(f"Number of students: {Student.objects.count()}")
