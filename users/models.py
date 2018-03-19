from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass  # Get rid of this when you add the missing field
