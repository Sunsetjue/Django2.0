from django.db import models

# Create your models here.
class Book(models.Model):
    id = models.AutoField(primary_key=True) # 表示ID是随着自增长的，后面的primary_key是指它是Book的一个自定义主键
    name = models.CharField(max_length=40, null=False)# null=False 表示字符串不能为空
    author = models.CharField(max_length=20, null=False)
    price = models.FloatField(null=False)

    def __str__(self):
        return "book:{},price:{}".format(self.name,self.price)