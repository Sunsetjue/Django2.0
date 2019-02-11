from django.shortcuts import render
from django.http import HttpResponse
from .models import Category,Article,Tags
from two.models import Front,Message
# Create your views here.
def index(request):
    article = Article(title='111', content='hahahahahahaha')
    category = Category(name='hot article')
    category.save()
    article.category = category
    article.save()
    article = Article.objects.first()
    print(article.category.name)
    return HttpResponse("success")

def delete_view(request):
    category = Category.objects.get(id=1) # 连级操作 如果对应的外键被删除了，那么这条数据也会被删除
    category.delete()
    return HttpResponse("success")

def one_to_many_view(request):
    article = Article(title='222',content='hohhohohohoh') # 插入数据
    category = Category.objects.first()
    author = Front.objects.first()
    article.category = category
    article.username = author
    article.save() # 并保存一对多的数据
    return HttpResponse("success")

def get_view(request):
    category = Category.objects.first()
    authors = category.bin.all()
    # 查找一对多的数据, 通过非定义的一来访问定义的多方，使用模型里的关键字
    # 如果没有定义关键字 那么使用定义方的小写加下划线加set 例如：article_set
    for author in authors:
        print(author)
    author2 = category.bin.get(id=3)
    return HttpResponse(author2)

# 通过多的一方来查找一的一方，使用非定义方的小写
def get_view2(request):
    article = Article.objects.get(id=2)
    cate = article.category
    return HttpResponse(cate)


# 定义一个一对一的数据并保存在数据库里
def one_to_one_view(request):
    msg = Message(gender="男",age=14)
    msg.message = Front.objects.first()
    msg.save()
    return HttpResponse("success")

# 查找定义的一对一的数据
def get_one_to_one_view(request):
    author = Front.objects.get(id=1)
    msg = author.sun
    return HttpResponse(msg)
    # 通过非定义的一方的来访问定义的另一方，使用在模型里使用的关键字

# 通过定义方来访问非定义方，使用非定义方的小写
def get_one_to_one_view2(request):
    msg = Message.objects.first()
    author = msg.message
    return HttpResponse(author)

# 向Tags里添加数据并与Article建立多对多的连接
def many_to_many_view(request):
    tag1 = Tags(name="社会")
    tag1.save()
    tag1.tag.add(Article.objects.get(id=2))
    tag1.tag.add(Article.objects.get(id=3))

    tag2 = Tags(name='经济')
    tag2.save()
    tag2.tag.add(Article.objects.get(id=2))
    tag2.tag.add(Article.objects.get(id=3))
    return HttpResponse('success')

# 查找数据 由定义方查找非定义方
def get_many_to_many_view(request):
    msg = Tags.objects.get(id=6)
    arts = msg.tag.all()
    print(arts)
    return HttpResponse("success")

# 由非定义方查找定义方
def get_mant_to_many_view2(request):
    article = Article.objects.first()
    tags = article.tags_set.all()
    print(tags)
    tag2 = article.tags_set.first()
    return HttpResponse(tag2)

