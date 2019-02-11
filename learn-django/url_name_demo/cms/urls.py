from . import views
from django.shortcuts import redirect,reverse
from django.urls import path

# 指定应用命名空间
app_name = 'cms'

urlpatterns = [
    path(r'', views.index, name="index"),
    path(r'login', views.login, name="logon"),
]