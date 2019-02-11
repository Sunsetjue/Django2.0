from django.shortcuts import render
from django.db import connection

def data(request):
    cursor = connection.cursor()

    # 向数据库力添加数据
    cursor.execute("insert into book(id,name,author) value(null,'龙族','江南')")
    # 查找数据
    cursor.execute("select * from book")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    return render(request, "data.html")