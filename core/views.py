
from cal.models import Event
from cal.views import event
from student.models import Student
from django.shortcuts import render
from courses.models import Courses
from trainer.models import Trainer
# Create your views here.
def home(request):
    students=Student.objects.count()
    courses=Courses.objects.count()
    trainers=Trainer.objects.count()
    event=Event.objects.count()
    data={"students":students,"courses":courses,"trainers":trainers,event:"event"}
    return render(request,"home.html",data)