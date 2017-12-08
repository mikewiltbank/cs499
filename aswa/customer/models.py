from __future__ import unicode_literals

from django.db import models
from employee.models import Employees
# Create your models here.

class Appointments(models.Model):
    employee = models.ForeignKey(Employees)
    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=11)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=128)
    details = models.TextField()
    date = models.DateField()
    starttime = models.TimeField()
    endtime = models.TimeField()
    duration = models.IntegerField()
    
    def __str__(self):
        return self.name
    

        
#@receiver(post_save, sender=Appointments)
#def update_appointments(sender, instance, created, **kwargs):
    #if created:
        #Appointments.objects.create(employee=instance)
    #instance.appointments.save()