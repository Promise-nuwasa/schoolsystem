
# Create your models here.

from django.db import models
from django.db.models.fields import CharField
 
class Event(models.Model):
   title=models.CharField(max_length=20,null='true',blank="true")
   event_date=models.DateTimeField()
   event_agenda=models.CharField(max_length=20)
   event_duration=models.DateTimeField()
   event_planner=models.CharField(max_length=20, default='Samantha')
   event_venue=models.CharField(max_length=20, help_text='eg Bool')
   number_of_attendees=models.PositiveSmallIntegerField()
   event_activity=CharField(max_length=20, default='Cultural day')
   signed_by=models.CharField(max_length=20, default='Samantha')
   start_time = models.DateTimeField()
   end_time = models.DateTimeField()
 
   def __str__(self):
       return self.event_activity
