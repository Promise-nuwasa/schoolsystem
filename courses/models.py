from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Courses(models.Model):
  
    course_name=models.CharField(max_length=30,default="jane")
    syllabus=models.CharField(max_length=100,default="Sincere")
    course_code=models.CharField(max_length=10)
    course_description=models.CharField(max_length=200)
    course_material=models.CharField(max_length=400)
    course_duration=models.CharField(max_length=20)
    course_units=models.CharField(max_length=100)
    def __str__(self):
        return self.course_name
    
