
from rest_framework import serializers
from student.models import Student
from trainer.models import Trainer
from courses.models import Courses
from cal.models import Event

class StudentSerializer(serializers.ModelSerializer):
      class Meta:
            model= Student
            fields=("first_name","last_name","age","nationality","gender","date_of_birth","big_sister")


class TrainerSerializer(serializers.ModelSerializer):
      class Meta:
            model= Trainer
            fields=("first_name","last_name","image","email","gender","courses_taught")


class CoursesSerializer(serializers.ModelSerializer):
      class Meta:
            model= Courses
            fields=("course_name","course_code","syllabus","course_duration")
     

class EventSerializer(serializers.ModelSerializer):
      class Meta:
            model= Event
            fields=("title","description","start_time","end_time")
     