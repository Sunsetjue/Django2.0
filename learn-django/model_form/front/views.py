from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from .modelform import BookForm,Registered
# Create your views here.

@require_http_methods(["POST"])
def one(request):
    form = BookForm(request.POST)
    if form.is_valid():
        title = form.cleaned_data.get("title")
        pages = form.cleaned_data.get("pages")
        price = form.cleaned_data.get("pirce")
        print("书名：{} 页数：{} 价格：{}".format(title,pages,price))
        return HttpResponse("success")
    else:
        print(form.errors.get_json_data())
        return HttpResponse("fail")

@require_http_methods(["POST"])
def two(request):
    form = Registered(request.POST)
    if form.is_valid():
        user = form.save(commit=False)
        user.password = form.cleaned_data.get("pwd1")
        user.save()
        return HttpResponse("success")
    else:
        print(form.errors.get_json_data())
        return HttpResponse("fail")