from .models import Trainer
from django.forms.forms import Form
from django.http import request
from django.shortcuts import redirect,render
# Create your views here.
from .forms import TrainerRegistrationForm
def register_trainer(request):
    if request.method=="POST":
         form=TrainerRegistrationForm(request.POST)
         if form.is_valid():
           form.save()
           return redirect(register_trainer)

    else:
        print("form.errors")
        form=TrainerRegistrationForm()
    return render(request,"register_trainer.html",{"form":form})
def trainer_list(request):
    trainers=Trainer.objects.all()
    return render(request,"trainer_list.html",{"trainers":trainers})
def edit_trainer(request,id):
    trainer= Trainer.objects.get(id=id)
    if request.method=='POST':
        form= TrainerRegistrationForm(request.POST,instance=trainer)
        if form.is_valid:
            form.save()
    else:
            form=TrainerRegistrationForm(instance=trainer)
            return render(request,'edit_trainer.html',{'form':form})
    return redirect("register_trainer")
   
def trainer_profile(request,id):
    trainer=Trainer.objects.get(id=id)
    return render(request,"trainer_profile.html",{"trainer":trainer})

def delete_trainer(request,id):
    trainer=Trainer.objects.get(id=id)
    trainer.delete()
    return redirect("trainer_list")
