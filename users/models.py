import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    birthday = models.DateField()
    password = models.CharField(max_length=255)

    username = None
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []