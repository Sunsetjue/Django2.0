from django.db import models
from django.core import validators

# Create your models here.
class Username(models.Model):
    username = models.CharField(max_length=20)
    telephone = models.IntegerField(validators=[validators.RegexValidator(r'1[345678]\d{9}')])
    password = models.IntegerField()
    money = models.IntegerField()