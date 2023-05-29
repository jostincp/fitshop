from django.contrib.auth.models import User
from django.db import models

class Ejemplo(models.Model):
    name = models.CharField(max_length=50, default='')
    description = models.CharField(max_length=200, default='')
    number = models.IntegerField(default=0)
#