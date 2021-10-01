from django.db import models
import datetime
# Create your models here.
class Student(models.Model):
    GENDER_CHOICES = (
        (u'M', u'Male'),
        (u'F', u'Female'),
    )
    first_name=models.CharField(max_length=18,null='true',blank="true")
    last_name=models.CharField(max_length=18,null="true",blank="true")
    age=models.PositiveSmallIntegerField(null="true",blank="true")
    date_of_birth=models.DateField(null="True",blank="True")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null="True",blank="True")
    mentor=models.CharField(max_length=29,null="True",blank="True")
    medical_form=models.FileField(upload_to="images",null="True",blank="True")
    id_number=models.CharField(max_length=20,null="True",blank="True")
    passport_number=models.CharField(max_length=20,null="True",blank="True")
    image=models.ImageField(upload_to="images",null="true",blank="true") 

    nationality=models.CharField(max_length=15,null="True",blank="True")
    class_name=models.CharField(max_length=10,null="True",blank="True")
    room_number=models.CharField(max_length=5,null="True",blank="True")
    email=models.EmailField(max_length = 254,null="True",blank="True")
    county_or_district=models.CharField(max_length=15,null="True",blank="True")
    big_sister=models.CharField(max_length=20,null="True",blank="True")
    def __str__(self):
        return self.first_name
    def full_name(self):
        return f"{self.first_name}  {self.last_name}"
    def year_of_birth(self):
        year=datetime.datetime.now().year
        return year-self.age
