from student.models import Student
from trainer.models import Trainer
from courses.models import Courses, Courses
from django import urls
from django.urls import path
from django.urls.resolvers import URLPattern
from.views import home
urlpatterns=[
    path('',home, name="home_page"),
    path('course/', Courses, name='Course'),
    path('trainer/',Trainer, name='Trainer'),
    path('student/', Student, name='Student'),
]