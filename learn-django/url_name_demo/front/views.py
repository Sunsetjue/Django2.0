
from django.shortcuts import redirect,reverse
from django.http import HttpResponse

def index(request):
    name = request.GET.get("username")
    if name:
        return HttpResponse("登陆成功，你的名字是{}".format(name))
    else:
        return redirect(reverse("front:logon"))
        # 跳转页面 前面加上app_name的名称加冒号

def login(request):
    return HttpResponse("front登陆界面")