from django.db import models
from django.contrib.auth.models import AbstractUser

from colors.models import Color


class User(AbstractUser):
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True)
