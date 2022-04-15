from django.db import models

# Create your models here.
class Main(models.Model): 
   title = models.CharField(max_length=255) 
   event = models.ForeignKey('Event', null=True, on_delete=models.CASCADE)

class Event(models.Model):
   day = models.DateField(u'Day of the event', help_text=u'Day of the event', null=True)