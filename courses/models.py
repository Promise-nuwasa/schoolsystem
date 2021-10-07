from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Courses(models.Model):
  
    course_name=models.TextField(max_length=30,null='true',blank="true")
    syllabus=models.TextField(max_length=100,null='true',blank="true")
    course_code=models.TextField(max_length=10)
    course_description=models.TextField(max_length=200)
    course_material=models.TextField(max_length=400)
    course_duration=models.TextField(max_length=20)
    course_units=models.TextField(max_length=100)
    def __str__(self):
        return self.course_name
    
