from django.db import models
import datetime
# Create your models here.
class Student(models.Model):
    first_name=models.TextField(max_length=10,blank=True, null=True )
    last_name=models.TextField(max_length=10, blank=True, null=True)
    age=models.PositiveSmallIntegerField(blank=True, null=True)
    date_of_birth=models.DateField( blank=True, null=True)
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'), ('U', 'Unisex/Parody'))
    gender = models.TextField(max_length=1, choices=GENDER_CHOICES, default='female' , blank=True, null=True)
    mentor=models.TextField(max_length=29, null=True, blank=True)
    medical_form=models.FileField(default='default.jpg', blank=True, null=True)
    id_number=models.TextField(max_length=20, default=5343, blank=True, null=True)
    passport_number=models.TextField(max_length=20,default=3445, blank=True, null=True)
    image=models.ImageField(upload_to='images',default='default.jpg', blank=True, null=True)
    countries=(('Uganda'),("Kenya"),('Tanzania'),('Rwanda'),('Sudan'),('South Sudan'))
    nationality=models.TextField(max_length=15, default='Ugandan', blank=True, null=True)
    class_name=models.TextField(max_length=10, null=True, blank=True)
    room_number=models.TextField(max_length=5, null=True, blank=True)
    email=models.EmailField(default='anyijukirjanett@gmail.com', blank=True, null=True)
    county_or_district=models.TextField(max_length=15, blank=True, null=True)
    big_sister=models.TextField(max_length=20, null=True, blank=True)
    """How django stores files"""
    def __str__(self):
       return self.first_name
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    def year_of_birth(self):
        return  datetime.datetime.now().year -self.age