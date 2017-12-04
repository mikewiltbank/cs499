from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Employees(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.TextField(max_length=200)
    email = models.EmailField(max_length=200)
    starttime = models.TimeField(default='8:00')
    endtime = models.TimeField(default='17:00')
    sun = models.BooleanField(default=True)
    mon = models.BooleanField(default=True)
    tue = models.BooleanField(default=True)
    wed = models.BooleanField(default=True)
    thur = models.BooleanField(default=True)
    fri = models.BooleanField(default=True)
    sat = models.BooleanField(default=True)
    
    def __str__(self):
        return self.full_name

@receiver(post_save, sender=User)
def update_employees_profile(sender, instance, created, **kwargs):
    if created:
        Employees.objects.create(user=instance)
    instance.employees.save()
    
'''    
class AppointmentTypes(models.Model):
    employee = models.ForeignKey(Employees)
    name = models.TextField(max_length=128)
    duration = models.IntegerField()
    
    def __str__(self):
        return self.name

'''
'''
    
class Practice(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class Business(models.Model):
    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name

class Employee(models.Model):
    business = models.ForeignKey(Business)
    name = models.CharField(max_length = 128, unique=True, primary_key=True)
    password = models.CharField(max_length = 128)
    
    def __str__(self):
        return self.name


class AppointmentTypes(models.Model):
    employee = models.OneToOneField(
        Employee.name, 
        on_delete=models.CASCADE, 
        primary_key=True,)
    type = models.CharField(max_length = 140)
    duration = models.DurationField()
    
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
