
from django.urls import path
from . import views
# Create your views here.
# 创建应用命名空间
app_name = "front"

urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'login/', views.login, name='logon'), # 给URL命名
]