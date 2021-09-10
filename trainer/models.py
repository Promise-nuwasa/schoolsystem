from django.db import models

# Create your models here.
class Trainer(models.Model):
    GENDER_CHOICES = (
        (u'M', u'Male'),
        (u'F', u'Female'),
    )
    first_name=models.CharField(max_length=10,default="jane")
    last_name=models.CharField(max_length=10,default="Sincere")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
    image=models.ImageField(upload_to="images",default=".jpeg") 
    email=models.EmailField(max_length = 254,default="estherayebaza@gmail.com")
    cv=models.FileField(upload_to='images',default='cv.png')
    courses_taught=models.CharField(max_length=30,default='python')
    trainer_Id=models.CharField(max_length=20,default='2376889999')
    lessons_attended=models.PositiveSmallIntegerField(default='4')
    bank_account=models.CharField(max_length=30,default='34526677789')
    contract=models.CharField(max_length=30,default='seven_month')
    profession=models.CharField(max_length=200,default='backend_developer')
    def __str__(self):
        return self.first_name
    def full_name(self):
            return f"{self.first_name}{self.last_name}"
