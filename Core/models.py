from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    balance = models.DecimalField(decimal_places=2, max_digits=8, default=0)
    image = models.ImageField(upload_to='images/')
    # Don't forget to install Pillow

