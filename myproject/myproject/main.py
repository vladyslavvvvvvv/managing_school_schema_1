#import django_setup

from venv import student

from myproject.myproject.models import Student

student = Student(
    name = 'Scott Carson',
    id = 101
)

