from __future__ import unicode_literals
from __future__ import unicode_literals
from django.db import models


class teachermodel(models.Model):
    teachername=models.CharField(max_length=50)
    surname=models.CharField(max_length=40)
    odetail=models.CharField(max_length=140)
    number=models.PositiveIntegerField()
    emailaddress=models.EmailField(max_length=130)



class coursemodel(models.Model):
    coursename=models.CharField(max_length=120)
    coursecode=models.CharField(max_length=120)
    courseclass=models.CharField(max_length=120)
    date=models.TimeField()
    oneteacher=models.OneToOneField(teachermodel)



class studentmodel(models.Model):
    studentname=models.CharField(max_length=50)
    surname=models.CharField(max_length=40)
    emailaddress=models.EmailField(max_length=140)
    enrolledcourses=models.ManyToManyField(coursemodel)

from django.db import models

# Create your models here.
