from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE,related_name='bin')
    # 获取一个APP下的外键 相当于建立一对多的关系 使用related_name来表示查找关键字
    username = models.ForeignKey('two.Front', on_delete=models.CASCADE, null=True) # 获取另一个APP下的外键
    def __str__(self):
        return self.title

class Tags(models.Model):
    name = models.CharField(max_length=50)
    tag = models.ManyToManyField('Article')
    def __str__(self):
        return self.name
    # 建立多对多的关系