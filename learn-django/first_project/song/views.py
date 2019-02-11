from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect,reverse
# Create your views here.
def yue(request):
    return HttpResponse("hohohohoh")

def sun(request, sun_loc, loc_id):
    # 加入参数
    text = "提取的地址是 {}, 门牌号是 {}".format(sun_loc, loc_id)
    return HttpResponse(text)

def bin(request):
    bin_id = request.GET.get("id") # 在URL里使用 ?id= 即可使用
    text1 = "所输入的id是{}".format(bin_id)
    return HttpResponse(text1)

def sb(request):
    name = request.GET.get("username")
    if name:
        word = "你输入的名字是{}".format(name)
        return HttpResponse(word)
    else:
        # song_name = request.resolver_match.namespace
        return redirect(reverse("login")) # 跳转到指定的URL里面去

def login(request):
    return HttpResponse("please login")

