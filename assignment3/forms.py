from django import forms
from assignment3.models import teachermodel, coursemodel




class TForm(forms.Form):
    teachername=forms.CharField(max_length=50)
    surname=forms.CharField(max_length=40)
    odetails=forms.CharField(max_length=140)
    number=forms.IntegerField()
    emailaddress=forms.EmailField(max_length=130)



class CForm(forms.Form):
    coursename=forms.CharField(max_length=50)
    coursecode=forms.CharField(max_length=40)
    courseclass=forms.CharField(max_length=20)
    date=forms.TimeField(widget=forms.TimeInput(attrs={'type':'time'}))
    oneteacher=forms.ModelChoiceField(teachermodel.objects.all())


class SForm(forms.Form):
    studentname=forms.CharField(max_length=50)
    surname=forms.CharField(max_length=40)
    emailaddress=forms.EmailField(max_length=140)

class Student_Course_Form(forms.Form):
    enrolledcourses=forms.ModelMultipleChoiceField(coursemodel.objects.all())