from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from datetime import datetime
# Create your views here.
def first(request):
    title = render_to_string("1.html") # 找到模板，然后将模板编译后渲染成Python的字符串格式
    return HttpResponse(title)

def second(request):
    vl = {'one':{'first':1,'hahahaha':'hohohohho'},'two':['second',2],'three':('third',3),'age':22} # 变量必须为字典格式
    return render(request, '2.html', context=vl)

def third(request):
    vl = {
        "value1":[1,2,3,4,5],
        "value2":['6','7',8],
        "today":datetime.now(),
        "value3":34.555,
        "value4":['a','b','c'],
        "value5":"<h1>哇哈哈哈哈哈</h1>",
        "value6":"江宝龙是个沙雕啊",
        "value7":"<p>江宝龙是个沙雕啊</p>"
    }
    return render(request, '4.html', context=vl)

def fourth(request):
    vl = {"value":"刘洋",
          "def_time":datetime(year=2018,month=12,day=3,hour=17,minute=0,second=0)
          }
    return render(request, "5.html", context=vl)