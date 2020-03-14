from django.contrib.gis.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from core.ModelManagers import UserManage


class User(AbstractBaseUser, PermissionsMixin):
    """ Custom user model that supports using email instead of username """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManage()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

class AbstractPatient(models.Model):
    BLOOD_GROUPS = [
        (0, 'A+'), (1, 'A-'), (2, 'B+'),(3, 'B-'),
        (4, 'O+'),(5, 'O-'),(6, 'AB+'),(7, 'AB-'),(8, 'UNKNOWN'),
    ]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nid_or_passport = models.CharField(max_length=20)   
    profession = models.CharField(max_length=100,null=True, blank=True)
    blood_group = models.IntegerField(choices=BLOOD_GROUPS, default=8)


class Patient(AbstractPatient):
    """Patient model to store patine recored"""
    
    
    came_from = models.CharField(max_length=100)
    
    location = models.PointField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)

    hospital_name = models.CharField(max_length=150)
    bed_no = models.CharField(max_length=100, null=True, blank=True)
    admitted_on = models.DateTimeField(null=True, blank=True)
    released_on = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} - {self.last_name}'

class Followup(AbstractPatient):
    """Patinent relatives or closed ones followups"""
    Patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} - {self.last_name}'