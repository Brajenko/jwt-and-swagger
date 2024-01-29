import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True
    
    def create_superuser(self, email, password):
        user: User = self.model(
            email=self.normalize_email(email),
            birthday="2000-01-01",
            first_name="admin",
            last_name="admin",
        )
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.active = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    birthday = models.DateField()
    password = models.CharField(max_length=255)

    username = None
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    objects = UserManager()