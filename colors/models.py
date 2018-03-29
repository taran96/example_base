from django.db import models


class Color(models.Model):
    title = models.CharField(max_length=20, unique=True)
