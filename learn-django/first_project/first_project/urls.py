"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,converters,include
from django.http import HttpResponse

def index(request):
    return HttpResponse('first_project')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path(r'song/', include('song.urls')),# url分层模块化
    # # 传递参数
    # # 在URL里面添加变量
    # path(r'song/sun/<sun_loc>/<loc_id>/', vi.sun), # 可以使用转换器来限制输入的URL的格式 比如<int:sun_loc>表示输入的必须是整数格式
    # # 第二种，查询字符串
    # path(r'song/bin/', vi.bin),
]
