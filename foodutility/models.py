from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('volunteer', 'Volunteer'),
        ('donator', 'Donator'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='donator')
    phone = models.CharField(max_length=15, blank=True, null=True)
    def __str__(self):
        return self.username

class Volunteer_Detail(models.Model):
    username = models.CharField(max_length=122, blank=True, null=True)
    phone = models.BigIntegerField(max_length=15, blank=True, null=True)
    email = models.CharField(max_length=122, blank=True, null=True)
    city =  models.CharField(max_length=122, blank=True, null=True)
    foodName =  models.CharField(max_length=122, blank=True, null=True)
    quantity =  models.CharField(max_length=122, blank=True, null=True)
    duedate = models.DateField(default = "2003-12-11")
    def __str__(self):
        return self.username
    
class Donor_Detail(models.Model):
    username = models.CharField(max_length=122, blank=True, null=True)
    phone = models.BigIntegerField(max_length=15, blank=True, null=True)
    email = models.CharField(max_length=122, blank=True, null=True)
    city =  models.CharField(max_length=122, blank=True, null=True)
    def __str__(self):
        return self.username
    
class Donate_Money(models.Model):
    donor = models.CharField(max_length=122, blank=True, null=True)
    volunteer = models.CharField(max_length=122, blank=True, null=True)
    amount = models.DecimalField(decimal_places = 4,max_digits = 10)
    reason = models.CharField(max_length=122, blank=True, null=True)
    date = models.DateTimeField()
    def __str__(self):
        return self.donor
    
class Donate_Food(models.Model):
    donor = models.CharField(max_length=122, blank=True, null=True)
    volunteer = models.CharField(max_length=122, blank=True, null=True)
    foodName =  models.CharField(max_length=122, blank=True, null=True)
    quantity =  models.CharField(max_length=122, blank=True, null=True)
    date = models.DateTimeField()
    def __str__(self):
        return self.donor
    