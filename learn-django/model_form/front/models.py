from django.db import models
from django.core import validators

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=15)
    pages = models.IntegerField()
    price = models.FloatField(validators=[validators.MaxValueValidator(limit_value=1000)])
    # 价格最大为1000

class Username(models.Model):
    name = models.CharField(max_length=4)
    password = models.IntegerField()
    telephone = models.IntegerField(validators=[validators.RegexValidator(r'1[345678]\d{9}')])