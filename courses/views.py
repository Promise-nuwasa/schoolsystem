from .models import Courses
from django.shortcuts import render

# Create your views here.
from django.forms.forms import Form
from django.http import request
from django.shortcuts import redirect, render
# Create your views here.
from .forms import CoursesRegistrationForm
def register_courses(request):
    if request.method=="POST":
         form=CoursesRegistrationForm(request.POST)
         if form.is_valid():
           form.save()
           return redirect(register_courses)

    else:
        print("form.errors")
        form=CoursesRegistrationForm()
    return render(request,"register_courses.html",{"form":form})
def course_list(request):
    courses=Courses.objects.all()
    return render(request,"course_list.html",{"courses":courses})
def edit_courses(request,id):
    courses= Courses.objects.get(id=id)
    if request.method=='POST':
        form= CoursesRegistrationForm(request.POST,instance=courses)
        if form.is_valid:
            form.save()
    else:
            form=CoursesRegistrationForm(instance=courses)
            return render(request,'edit_course.html',{'form':form})
    return redirect("register_courses")
   
def courses_profile(request,id):
    courses=Courses.objects.get(id=id)
    return render(request,"course_profile.html",{"courses":courses})

def delete_courses(request,id):
    courses=Courses.objects.get(id=id)
    courses.delete()
    return redirect("course_list")

