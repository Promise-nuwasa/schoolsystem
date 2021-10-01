from django.db import models

# Create your models here.
class Trainer(models.Model):
    GENDER_CHOICES = (
        (u'M', u'Male'),
        (u'F', u'Female'),
    )
    first_name=models.CharField(max_length=10,null='true',blank="true")
    last_name=models.CharField(max_length=10,null='true',blank="true")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
    image=models.ImageField(upload_to="images",null='true',blank="true") 
    email=models.EmailField(max_length = 254,null='true',blank="true")
    cv=models.FileField(upload_to='images',null='true',blank="true")
    courses_taught=models.CharField(max_length=30,null='true',blank="true")
    trainer_Id=models.CharField(max_length=20,null='true',blank="true")
    lessons_attended=models.PositiveSmallIntegerField(null='true',blank="true")
    bank_account=models.CharField(max_length=30,null='true',blank="true")
    contract=models.CharField(max_length=30,null='true',blank="true")
    profession=models.CharField(max_length=200,null='true',blank="true")
    def __str__(self):
        return self.first_name
    def full_name(self):
            return f"{self.first_name}   {self.last_name}"
    def full_name(self):
            return f"{self.first_name}  {self.last_name}"
    # def year_of_birth(self):
    #     year=datetime.datetime.now().year
    #     return year-self.age