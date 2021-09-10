from django.forms import Form
from django.http import request
from django.shortcuts import redirect, render
from.models import Student
# Create your views here.
from .forms import StudentRegistrationForm
def register_student(request):
    if request.method=="POST":
         form=StudentRegistrationForm(request.POST)
         if form.is_valid():
           form.save()
           return redirect(register_student)
    else:
        print("form.errors")
        form=StudentRegistrationForm()
    return render(request,"register_student.html",{"form":form})


def student_list(request):
    students=Student.objects.all()
    return render(request,"student_list.html",{"students":students})

def edit_student(request,id):
    student= Student.objects.get(id=id)
    if request.method=='POST':
        form= StudentRegistrationForm(request.POST,instance=student)
        if form.is_valid:
            form.save()
    else:
            form=StudentRegistrationForm(instance=student)
            return render(request,'edit_student.html',{'form':form})
    return redirect("register_student")
    
def student_profile(request,id):
    student=Student.objects.get(id=id)
    return render(request,"student_profile.html",{"student":student})

def delete_student(request,id):
    student=Student.objects.get(id=id)
    student.delete()
    return redirect("student_list")
            








    
