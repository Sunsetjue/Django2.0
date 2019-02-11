from django.shortcuts import render,redirect,reverse
from django.db import connection

# Create your views here.
def get_cursor():
    return connection.cursor()

def index(request):
    cursor = get_cursor()
    cursor.execute("select * from books")
    books = cursor.fetchall()
    return render(request, "base.html", context={"books":books})

def add_book(request):
    if request.method == "GET":
        return render(request, "add_book.html")
    if request.method == "POST":
        name = request.POST.get("name")
        author = request.POST.get("author")
        cursor = get_cursor()
        cursor.execute("insert into books(id,name,author) value(null,'%s','%s')" % (name,author))
        return redirect(reverse("index"))

def book_detail(request, book_id):
    cursor = get_cursor()
    cursor.execute("select id,name,author from books where id=%s" % book_id)
    book = cursor.fetchone()
    return render(request, "book_detail.html", context={"book":book})

def delete_book(request):
    cursor = get_cursor()
    if request.method == "POST":
        id_name = request.POST.get("id_name")
        cursor.execute("delete from books where id=%s" % id_name)
        return redirect(reverse("index"))
    else:
        raise Exception("报错了")