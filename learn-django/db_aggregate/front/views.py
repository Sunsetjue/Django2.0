from django.shortcuts import render
from django.http import HttpResponse
from .models import Book,Author,BookOrder,Publisher
from django.db.models import Avg,Count,Max,Min,Sum,F,Q,Prefetch
from django.db import connection

# Create your views here.
def front_one(request):
    '''求图书价格的平均值'''
    average = Book.objects.aggregate(Avg("price"))
    print(average)
    # 返回一个字典 默认键值为price__avg

    print(connection.queries)
    # 原生SQL语言

    return HttpResponse("success")

def front_two(request):
    '''求图书的售卖价格'''
    averages = Book.objects.annotate(avg=Avg("bookorder__price"))
    print(averages)
    for average in averages:
        print(average.name + str(average.avg))
    # 返回一个QuerySet对象

    print(connection.queries)

    return HttpResponse("success")

def front_three(request):
    '''获取图书的数量'''
    sum = Book.objects.aggregate(book_sum=Count("id"))
    print(sum)

    # 获取作者的邮箱
    email = Author.objects.aggregate(email_sum=Count("email", distinct=True))
    # distinct 表示不把重复的算进去
    print(email)

    # 获取图书卖的数量
    siles = Book.objects.annotate(sile_sum=Count("bookorder__book_id"))
    for sile in siles:
        print(sile.name+str(sile.sile_sum))

    return HttpResponse("success")

def front_four(request):
    '''获取作者年龄的最大值和最小值'''
    age = Author.objects.aggregate(max=Max("age"), min=Min("age"))
    print(age)
    name1 = Author.objects.get(age__exact=46)
    name2 = Author.objects.get(age__exact=28)
    print("最小年龄的作者是{} 最大年龄的作者是{}".format(name1.name, name2.name))

    # 获取售卖价格的最大值的及书名和最低价格的价格及其书名
    books = Book.objects.annotate(book_max=Max("bookorder__price"),book_min=Min("bookorder__price"))
    print(books)
    for book in books:
        print(book)
        print(book.name+str(book.book_max)+str(book.book_min))

    return HttpResponse("success")

def front_five(request):
    '''sum求总和'''
    # 图书页数总和
    pages = Book.objects.aggregate(sum=Sum("pages"))
    print(pages)

    # 各个图书价格总和
    prices = Book.objects.annotate(price_sum1=Sum("bookorder__price"))
    for price in prices:
        print(price.name+str(price.price_sum1))

    # 查页数980到1005的图书的价格的总额
    prices2 = Book.objects.filter(pages__range=(980,1005)).aggregate(price_sum2=Sum("price"))
    print(prices2)

    # 查页数800到1010的图书的售卖价格
    prices3 = Book.objects.filter(pages__range=(980,1010)).annotate(price_sum3=Sum("bookorder__price"))
    for price0 in prices3:
        print(price0.name+str(price0.price_sum3))

    # QuerySet也具有aggregate 和 annotate 属性
    return HttpResponse("success")

def front_six(request):
    '''F表达式 让所有图书的价格增加10圆的方便写法'''
    Book.objects.update(price=F("price")+10)

    # Q表达式，用来查询与或非
    # 查找页数大于980并且价格小于等于108的
    books1 = Book.objects.filter(Q(pages__gt=980)&Q(price__lte=108))
    for book1 in books1:
        print("这些书有{}，价格是{}，页数是{}".format(book1.name,book1.price,book1.pages))

    print('\n')

    # 查找页数大于等于1000或者价格小于108的
    books2 = Book.objects.filter(Q(pages__gte=1000)|Q(price__lt=108))
    for book2 in books2:
        print("这些书有{}，价格是{}，页数是{}".format(book2.name,book2.price,book2.pages))

    print('\n')

    # 查找价格小于200但名字没有记的书
    books3 = Book.objects.filter(Q(price__lt=200)&~Q(name__contains="记"))
    for book3 in books3:
        print("这些书有{}，价格是{}，页数是{}".format(book3.name, book3.price, book3.pages))

    return HttpResponse("success")

def front_seven(request):
    books1 = Book.objects.filter(id__gte=2).filter(~Q(id=3))
    print(books1)
    books2 = Book.objects.filter(id__gte=2).exclude(id=3) # exclude 表示不包括
    print(books2)

    books3 = Book.objects.annotate(author_names=F("author__name"))
    for book in books3:
        print("{}/{}".format(book.name,book.author_names))

    return HttpResponse("success")

def front_eight(request):
    '''order_by 按照指定的顺序由小到大进行排序 时间越靠近现在越大'''
    orderes1 = Book.objects.order_by("-rating","price") # 前面加负号表示从大到小进行排序 也就是倒序 可以有多个排序
    for order1 in orderes1:
        print("{}/{}/评分{}/价格{}".format(order1.id,order1.name,order1.rating,order1.price))

    orderes2 = Book.objects.annotate(num=Count("bookorder__id")).order_by("-num")
    for order2 in orderes2:
        print("{}/{}/售卖数量{}".format(order2.id,order2.name,order2.num))

    return HttpResponse("success")

def front_ninth(request):
    '''values用来指定在提取数据出来，需要提取哪些字段。默认情况下会把表中所有的字段全部都提取出来
    可以使用 values来进行指定，并且使用了values方法后，提取出的 QuerySet中的数据类型不是模型，
    而是在 values方法中指定的字段和值形成的字典'''
    books = Book.objects.values("name", "price", author_name=F("author__name"), num=Count("bookorder__id"))
    # values 里面也可以使用聚合函数
    # 将author__name改名为author_name使用F方法
    # books仍是一个QuerySet对象
    for book in books:
        print(book)
    # 返回的是一个个的字典

    '''values_list 与values不同的是形成的是元组而不是字典'''
    publishers1 = Publisher.objects.values_list()
    for publisher1 in publishers1:
        print(publisher1)
    publishers2 = Publisher.objects.values_list("name", flat=True)
    # 当元组内只有一个值的时候，使用flat=True将元组转换为字符串
    for publisher2 in publishers2:
        print(publisher2)
    return HttpResponse("success")

def front_ten(request):
    '''减少SQL查询语句的方法'''
    authors = Book.objects.prefetch_related("author")
    for author in authors:
        print(author.author.name)
    print("*"*20)

    prefetch = Prefetch("bookorder_set", queryset=BookOrder.objects.filter(price__lte=90))
    # 为了在下面不再使用新的产生QuerySet语句 于是在上面使用Prefetch 模块
    books = Book.objects.prefetch_related(prefetch)
    for book in books:
        print(book.name)
        orders = book.bookorder_set.all() # 这里不能使用会产生新的QuerySet的语句，不然并不能减少查询语句
        for order in orders:
            print(order.id)
    # print(connection.queries)

    return HttpResponse("success")

def front_eleven(request):
    '''create 方法创建一个对象 '''
    '''publisher = Publisher.objects.create(name="人民邮电出版社")'''

    # get_or_create 根据某个条件进行查找，如果找到了那么就返回这条数据，如果没有查找到，那么就创建一个
    # 所查的数据因为使用了get 语句，所以如果数据有重复或者多个，那么会报错
    # get 到一个数据会报False, create 一个数据会报True
    find1 = Publisher.objects.get_or_create(name="人民邮电出版社")
    print(find1)
    find2 = Publisher.objects.get_or_create(name="电子工业出版社")
    print(find2)
    publishers = Publisher.objects.all()
    for publisher1 in publishers:
        print(publisher1.name)

    # bulk_create 也是创建新的数据，不过这个一次性可以创建多个数据
    # 使用列表的形式 需要在列表里添加模型的路径
    Publisher.objects.bulk_create([Publisher(name="外研社"),Publisher(name="南京大学出版社")])

    return HttpResponse("success")

def front_twelve(request):
    '''count 查询数据的个数和出现次数'''
    books = Book.objects.all()
    print(len(books))
    # print(connection.queries)

    num = Book.objects.count()
    print(num)
    # print(connection.queries)

    # exists 判断某数据是否在模型中返回布尔值
    result = Publisher.objects.filter(name="人民邮电出版社").exists()
    print(result)

    return HttpResponse("success")

def front_thirteen(request):
    '''distinct 去掉重复的数据'''
    books1 = Book.objects.filter(bookorder__price__gte=80).distinct()
    for book in books1:
        print(book.name)

    print('\n')

    # 如果有别的需要提取的重复字段，那么distinct也没有作用
    books2 = Book.objects.annotate(order_price=F("bookorder__price")).filter(bookorder__price__gte=80).distinct()
    for book in books2:
        print(book.name)

    return HttpResponse("success")