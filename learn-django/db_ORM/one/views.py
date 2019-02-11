from django.shortcuts import render
from .models import Book
from django.http import HttpResponse
# Create your views here.
def index(request):
    # book1 = Book(id=1, name='Dragon Raja', author='Jangnan', price=40)
    # book1.save()
    return HttpResponse("插入图书")

def insert(request):
    book2 = Book(id=2, name='追风筝的人', author='xxx', price=30)
    book2.save()
    return HttpResponse("图书插入成功！")

def select1(request):
    book = Book.objects.get(id=2)
    print(book)
    return HttpResponse("图书查找成功")

def select2(request):
    book = Book.objects.filter(name="Dragon Raja")
    print(book)
    return HttpResponse("图书添加成功")

def delete(request):
    book = Book.objects.get(id=2)
    book.delete()
    return HttpResponse("图书删除成功")

def change(request):
    book = Book.objects.get(id=1)
    book.price = 100000
    book.save()
    return HttpResponse("图书修改成功")