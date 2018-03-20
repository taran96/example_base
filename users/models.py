from django.db import models
from django.contrib.auth.models import AbstractUser
from colors.models import Color


class User(AbstractUser):
    pass  # Get rid of this when you add the missing field
