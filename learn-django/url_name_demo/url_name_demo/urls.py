"""url_name_demo URL Configuration

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
from django.urls import path,include,re_path,converters,register_converter
from django.http import HttpResponse

# 自定义的path路径转换器
class CateConverter():
    regex = r'\w+|(\w+\+\w+)+'

    def to_python(self, value):
        r = value.split("+")
        return r

    def to_url(self, value):
        b = "+".join(value)
        return b

register_converter(CateConverter,"cate")

def book(request, lei):
    text = "选择的图书是{}".format(lei)
    return HttpResponse(text)

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include('front.urls')),
    path(r'cms1/', include('cms.urls', namespace='cms1')), # 分层的URL namespace代表实例命名空间
    path(r'cms2/',include('cms.urls', namespace='cms2')), # namespace用来区分当不同的URL映射同一个app
    # re_path(r'(?P<lei>\w+|(\w+\+\w+)+)/', book), # re_path URL填写正则表达式
    path(r'one/<cate:lei>', book),
]
