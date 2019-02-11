from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
# Create your views here.
def index(request):
    name = request.GET.get("username")
    if name:
        return HttpResponse("cms登陆成功，你的名字是{}".format(name))
    else:
        get_name = request.resolver_match.namespace
        return redirect(reverse("{}:logon".format(get_name)))
        # 跳转页面 前面加上app_name的名称加冒号
        # 实例命名空间的用法，可能多个URL映射一个同一个APP，因此需要使用实例命名空间

def login(request):
    return HttpResponse("cms登陆界面")