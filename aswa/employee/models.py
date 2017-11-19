from django.db import models
# from unittest.util import _MAX_LENGTH

class Employee(models.Model):
    name = models.CharField(max_length = 140, unique=True, primary_key=True)
    password = models.CharField(max_length = 140)
    
    def __str__(self):
        return self.name
'''
class AppointmentTypes(models.Model):
    employee = models.OneToOneField(
        Employee.name, 
        on_delete=models.CASCADE, 
        primary_key=True,)
    type = models.CharField(max_length = 140)
    duration = models.DurationField()
    
class Availability(models.Model):
    employee = models.OneToOneField(
        Employee.name, 
        on_delete=models.CASCADE, 
        primary_key=True,)
    starttime = models.TimeField(default='8:00')
    endtime = models.TimeField(default='17:00')
    sun = models.BooleanField(default=True)
    mon = models.BooleanField(default=True)
    tue = models.BooleanField(default=True)
    wed = models.BooleanField(default=True)
    thur = models.BooleanField(default=True)
    fri = models.BooleanField(default=True)
    sat = models.BooleanField(default=True)
    
class DailyUnavailable(models.Model):
    employee = models.OneToOneField(
        Employee.name, 
        on_delete=models.CASCADE, 
        primary_key=True,)
    weekday = models.CharField(max_length = 11)
    dailystarttime = models.TimeField()
    dailyendtime = models.TimeField()
    
class CustomUnavailable(models.Model):
    employee = models.OneToOneField(
        Employee.name, 
        on_delete=models.CASCADE, 
        primary_key=True,)
    day = models.DateField()
    customstarttime = models.TimeField()
    customendtime = models.TimeField()
'''  
