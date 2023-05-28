from django.db import models

# Crea tus modelos aquí.
class Ejemplo(models.Model):
    name = models.CharField(max_length=50,default='')
    description = models.CharField(max_length=200,default='')
    number = models.IntegerField(default=0)