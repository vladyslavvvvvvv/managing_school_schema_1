from django.db import models # type: ignore

class Subject(models.Model):
    name = models.CharField(max_length=747)

class Teacher(models.Model):
    name = models.CharField(max_length=747)
    id = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)