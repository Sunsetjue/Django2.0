from django.db import models

# Create your models here.
class Time(models.Model):
    remove = models.BooleanField() # 填写一个布尔值，False为0 True为1 不能为空，若需要为空则使用NullBooleanField
    create_time = models.DateTimeField(auto_now_add=True) # 填写一个时间
    # create_time = models.DateTimeField(auto_now_add=True)
    # auto_now_add会在第一次保存数据的时候自动获取当前的时间
    # auto_now会在每次使用save方法的时候将当前的时间进行更新,可以随时修改时间
    telephone = models.CharField(unique=True, null=True, max_length=12)
    def __str__(self):
        return "time:{} tel:{}".format(self.create_time, self.telephone)
    class Meta:
        db_table = 'sunset' # 修改表的名称
        ordering = ['-create_time', 'id'] # 加上一个减号来作为反转 先按照反转的时间排序再用id排序