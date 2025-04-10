from enum import unique
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    ADMIN = 0
    VENDOR = 1
    CUSTOMER = 2
    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (VENDOR, 'Vendor'),
        (CUSTOMER, 'Customer'),
    )
    username = None
    email = models.EmailField(unique=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, default=CUSTOMER)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.email
