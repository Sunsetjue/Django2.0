from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)
    time = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Category'