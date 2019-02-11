from django.db import models
# from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core import validators
from django.contrib.auth.models import AbstractUser,BaseUserManager

# Create your models here.
'''
# 设置Proxy模型来扩展用户模型
class SuperUser(User):
    class Meta:
        proxy = True

    @classmethod
    def superuser(cls):
        return cls.objects.filter(is_superuser=True)
'''

'''
# 一对一外键来扩展用户模型

class UserExtension(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="extension")
    telephone = models.CharField(max_length=11)

@receiver(post_save, sender=User)
def user_extension(sender, instance, created, **kwargs):
    if created:
        UserExtension.objects.create(user=instance)
    else:
        instance.extension.save()
'''

# 继承自AbstractBaseUser模型 修改源代码中的字段 让默认的username改为别的字段或者是添加一些新的字段
# 修改objects中的添加用户个超级用户的属性
class UserManager(BaseUserManager):
    def _create_user(self, telephone, username, password, **kwargs):
        if not telephone:
            raise ValueError("The given telephone must be set !")
        if not password:
            raise ValueError("The given password must be set !")
        user = self.model(telephone=telephone, username=username, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, telephone, username, password, **kwargs):
        kwargs["is_superuser"] = False
        return self._create_user(telephone=telephone, username=username, password=password, **kwargs)

    def create_superuser(self, telephone, username, password, **kwargs):
        kwargs["is_superuser"] = True
        return self._create_user(telephone=telephone, username=username, password=password, **kwargs)

class User(AbstractUser):
    telephone = models.CharField(max_length=11, unique=True)

    objects = UserManager()

    # 修改默认的唯一标识字段
    USERNAME_FIELD = "telephone"

    # 运行之前应该保证没有表映射在数据库中过

class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

# 通过在模型中添加用户的权限
    class Meta:
        permissions = (
            ('view_article','可以添加权限'),
        )