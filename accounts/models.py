from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    password1 = models.CharField(max_length=128)
    password2 = models.CharField(max_length=128)


    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email