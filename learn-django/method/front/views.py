from django.shortcuts import render,redirect,reverse
from .models import Article
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse,JsonResponse,StreamingHttpResponse
import json
import csv
from django.template import loader

# Create your views here.
@require_http_methods(['GET']) # 使用装饰器 表示只能使用 get 请求
def front_one(request):
    articles = Article.objects.all()
    return render(request, "one.html", context={"articles":articles})

@require_http_methods(["POST","GET"])
def front_two(request):
    if request.method == "GET":
        # 当为get请求时 返回添加文章的页面
        return render(request, "two.html")
    else:
        title = request.POST.get("title")
        content = request.POST.get("content")
        pages = request.POST.get("pages")
        Article.objects.create(title=title, content=content, pages=pages)
        return HttpResponse("success")

def index(request):
    name = request.GET.get("name")
    if name:
        return HttpResponse("index")
    else:
        return redirect(reverse("front:signup"))

def signup(request):
    print(request.path) # 获取服务器的路径 不包括域名和参数
    print(request.get_full_path()) # 获取服务器的路径 包括参数
    print(request.get_raw_uri()) # 获取路径 包括所有
    for k,v in request.META.items():
        print("{}:{}".format(k,v))
    return HttpResponse("signup")

def front_three(request):
    response = HttpResponse(content_type="text/plain;charset=utf-8")
    response.content = "<h1>孙彬</h1>" # 返回的内容 默认格式是text/html（默认的，html文件）
    response.write("songyue")
    return response

def front_four(request):
    '''
    person = {
       "name": 'sunbin',
        "age": '21',
        'gender': 'man'
    }
    '''
    # 第一种方式 用 HttpResponse
    '''
    person_json = json.dumps(person)
    response = HttpResponse(person_json, content_type='application/json')
    return response
    '''
    # 第二种方式 用 JsonHttpResponse
    '''return JsonResponse(person)'''

    # 当JsonResponse 传入非字典的参数时 使用safe=False
    persons = [
        {"name": "sunbin", "age": 21, "gender": 'man'},
        {"name": 'songyue', "age": 18, "gender": 'woman'}
    ]
    return JsonResponse(persons, safe=False)

# 生成 csv 文件
def front_five(request):
    response = HttpResponse(content_type="text/csv")
    # 给 csv 文件取名字
    response['Content-Disposition'] = "attachment; filename='sunbin.csv'"
    writer = csv.writer(response)
    # 写入csv 文件 使用列表
    writer.writerow(["name", "age"])
    writer.writerow(["sunbin", 21])
    return response

def front_six(request):
    # 将 cvs 定义成模板
    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = "attachment; filename='download.csv'"
    contents = [
        ["name", "age"],
        ["sunbin", 21]
        ]
    template = loader.get_template('download.txt')
    response.content = template.render({"rows": contents})
    return response

def front_seven(request):
    '''生成大型的 csv 文件'''
    response = StreamingHttpResponse(content_type="text/csv")
    response['Content-Disposition'] = "attachment; filename='large_file.csv'"
    rows = ("{} : {} \t".format(i, i**2) for i in range(10000)) # 必须返回一个生成器 可迭代的对象
    response.streaming_content = rows
    '''
    这个类没有属性content，相反是streaming_content。
    这个类的streaming_content必须是一个可以迭代的对象。
    
    StreamingHttpResponse会启动一个进程来和客户端保持长连接，
    所以会很消耗资源。所以如果不是特殊要求，尽量少用这种方法。
    '''
    return response

