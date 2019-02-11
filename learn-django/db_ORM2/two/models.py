from django.db import models

# Create your models here.
class Front(models.Model):
    username = models.CharField(max_length=100)
    def __str__(self):
        return self.username

class Message(models.Model):
    gender = models.CharField(max_length=3)
    age = models.IntegerField()
    message = models.OneToOneField('Front', on_delete=models.CASCADE, null=True, related_name='sun')
    # 与Front类构建一对一的关系 related_name 表示使用指定的关键字来查找
    def __str__(self):
        return "年龄是{} 性别是{} ".format(self.age,self.gender)