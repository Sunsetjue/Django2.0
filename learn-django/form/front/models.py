from django.db import models

# Create your models here.
class Registered(models.Model):
    name = models.CharField(max_length=4)
    telephone = models.CharField(max_length=11)