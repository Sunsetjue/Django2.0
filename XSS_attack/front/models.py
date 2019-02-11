from django.db import models

# Create your models here.
class Commit(models.Model):
    commit = models.TextField()