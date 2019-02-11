from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, "3.html")

def index_index(request):
    return HttpResponse("首页中的首页")

def books(request):
    return HttpResponse("图书首页")

def books_detail(request,book_name):
    text = "目前最火的书籍名称是: <{}>".format(book_name)
    return HttpResponse(text)

def movies(request):
    return HttpResponse("电影首页")

def cities(request):
    return HttpResponse("同城首页")

def login(request):
    vl = request.GET.get('next')
    text = "得到的密码是{}".format(vl)
    return HttpResponse(text)