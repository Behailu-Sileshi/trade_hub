from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

# Custom User Manager
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


# Custom User model
class User(AbstractUser):
    objects = UserManager()  # Attach custom manager to handle user creation
    ADMIN = 0
    VENDOR = 1
    CUSTOMER = 2

    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (VENDOR, 'Vendor'),
        (CUSTOMER, 'Customer'),
    )

    username = None  # We don't need the username anymore
    email = models.EmailField(unique=True)  # Use email as the unique identifier
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, default=CUSTOMER)

    USERNAME_FIELD = 'email'  # Set email as the login field
    REQUIRED_FIELDS = []  # We don't need username or other fields for superuser creation


    def __str__(self):
        return self.email

