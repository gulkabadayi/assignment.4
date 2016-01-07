from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from assignment3.forms import *
from assignment3.models import *


def Teacher_Adding(request):

    if request.method == "GET":
        return "Please choose post"
    else:
        template = TForm(request.POST)
        if template.is_valid():
            modeling = teachermodel(teachername=template.cleaned_data["teachername"],
                        surname=template.cleaned_data["surname"],
                        odetails=template.cleaned_data["odetails"],
                        number=template.cleaned_data["number"],
                        emailaddress=template.cleaned_data["emailaddress"])
            modeling.save()
            return HttpResponseRedirect('/all-teachers/')
        else:
            template = TForm()
        return render_to_response('Teacher_Adding.html', {'form': template},
                              RequestContext(request))


def Course_Adding(request):
    if request.method == 'GET':
        print "Please choose post"
    else:
        template2 = CForm(request.POST)
        if template2.is_valid():
            modeling2 = coursemodel(coursename=template2.cleaned_data["coursename"],
                       coursecode=template2.cleaned_data["coursecode"],
                       courseclass=template2.cleaned_data["courseclass"],
                       date=template2.cleaned_data["date"],
                       oneteacher=template2.cleaned_data["oneteacher"])
            modeling2.save()
            return HttpResponseRedirect('/all-courses/')
        else:
            template2 = CForm()
        return render_to_response('Course_Adding.html', {'form': template2},
                                  RequestContext(request))


def Student_Adding(request):
    if request.method == 'GET':
        print "Please choose post "
    else:

        form = SForm(request.POST)
        form2 = Student_Course_Form(request.POST)
        if form.is_valid():
            if form2.is_valid():
                modeling3 = studentmodel(studentname=form.cleaned_data["studentname"],
                            surname=form.cleaned_data["surname"],
                            emailaddress=form.cleaned_data["emailaddress"])
                modeling3.save()
                c = coursemodel.objects.get(id=form2.cleaned_data["enrolledcourses"])
                modeling3.enrolledcourses.add(c)
                return HttpResponseRedirect('/all-students/')
            else:
                form = SForm()
                form2 = Student_Course_Form()
            return render_to_response('Student_Adding.html', {'form': form, 'form2': form2},
                              RequestContext(request))


def All_courses(request):
    c = coursemodel.objects.all()
    return render_to_response('All_courses.html', {'c':c}, RequestContext(request))


def All_teachers(request):
    t = teachermodel.objects.all()
    return render_to_response('All_teachers.html', {'t':t}, RequestContext(request))



def All_students(request):
    s = studentmodel.objects.all()
    return render_to_response('All_students.html', {'s':s}, RequestContext(request))


# Create your views here.
