from django.db import models


# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=40)


class Student(models.Model):
    student_name = models.CharField(max_length=30)
    student_adm = models.CharField(max_length=30)
    student_date_of_admission = models.DateField()
    std_fk = models.ForeignKey(Course, on_delete=models.CASCADE)
