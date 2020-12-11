from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    dob = models.DateField(null=True, blank=True, verbose_name='Дата рождение')
    city = models.CharField(max_length=100, null=True, blank=True, verbose_name='Город')
    phone = models.CharField(max_length=12, null=True, blank=True, verbose_name='Номер телефона')


