from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=747)

class Teacher(models.Model):
    name = models.CharField(max_length=747)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL,null=True)

class Clas(models.Model):
    title = models.TextField(max_length=747)

class Student(models.Model):
    name = models.CharField(max_length=747)
    clas = models.ForeignKey(Clas,on_delete=models.CASCADE)

class Schedule(models.Model):
    time = models.TimeField()
    clas = models.ForeignKey(Clas, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)

class Grade():
    grade_choices = {
        'a': 'Perfect',
        'b': 'Extradionary',
        'c': 'Very good',
        'd': 'Good',
        'f': 'Failed',
    }
    value = models.CharField(max_length=1, choices=grade_choices)

    student = models.CharField(Student, on_delete=models.CASCADE)
    subject = models.CharField(Subject, on_delete=models.CASCADE)