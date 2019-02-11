from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=15)
    content = models.TextField()
    on_load = models.FileField(upload_to="%Y/%m/%d")

    '''
    我们也可以指定MEDIA_ROOT，就不需要在FielField中指定upload_to，
    他会自动的将文件上传到MEDIA_ROOT的目录下
    
    如果我们同时指定MEDIA_ROOT和upload_to，
    那么会将文件上传到MEDIA_ROOT下的upload_to文件夹中如果我们同时指定MEDIA_ROOT和upload_to，
    那么会将文件上传到MEDIA_ROOT下的upload_to文件夹中
    '''