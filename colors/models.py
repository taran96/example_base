from django.db import models
#from users.models import User
#from users.models import User
# Create your models here.
class Color(models.Model):
    name = models.CharField(max_length=8)
    #user = models.ForeignKey(User, related_name='color', on_delete=models.CASCADE)