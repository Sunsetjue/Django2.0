from django.shortcuts import render
from django.views.generic import View,TemplateView
from django.http import HttpResponse

# Create your views here.

# get 方法请求类视图
class BookList(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("book list")

# 分别定义get 方法和post 方法
class Book(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'book.html')
    def post(self, request, *args, **kwargs):
        name = request.POST.get("title")
        author = request.POST.get("author")
        return HttpResponse("书名是{} 作者是{}".format(name,author))

# 在类视图里添加参数
class BookDetail(View):
    def get(self, request, book_id, **kwargs):
        msg = "图书id是{}".format(book_id)
        return HttpResponse(msg)

    # 如果使用post 求情 可以定义一个在没有post 请求时候的一个函数
    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponse("请使用get请求")

# 使用TemplateView 渲染模板传递参数的时候
class About(TemplateView):
    template_name = "About1.html"

    def get_context_data(self, **kwargs):
        context = {"name":"sunbin"}
        return context