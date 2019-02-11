from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    pages = models.IntegerField()

    class Meta:
        db_table = "article"