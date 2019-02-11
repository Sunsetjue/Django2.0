from django.shortcuts import render
from django.http import HttpResponse
from .models import Article,Category
from datetime import datetime
from django.utils.timezone import make_aware

# Create your views here.
# exact 使用精确的 = 查找
def front_one(request):
    article1 = Article.objects.filter(id__exact=1)
    print(article1)
    article2 = Article.objects.get(id=1)
    print(article2)
    # id=1 和 id__exact=1 的用法和效果相同
    print(type(article1)) # 返回的是<class 'django.db.models.query.QuerySet'> 这个是QuerySet属性
    print(type(article2)) # 返回的是<class 'front.models.Article'> 这个是普通的ORM模型
    # get方式和filter方式获取的对象属性是不一样的

    article3 = Article.objects.filter(content__exact="bbb")
    # 查找不区分大小写
    print(article3)
    article4 = Article.objects.filter(content="bbb")
    print(article4)

    article5 = Article.objects.filter(id__exact=None)
    print(article5.query) # 查看SQL的原生代码
    print(article5)
    # 使用exact的时候如果对象输入为None，则sql会自动将其转化为查找NULL 例如这里面就是  id = NULL
    return HttpResponse("success")

# contains 对大小写敏感 查找某个字段内是否包括某段数据
def front_two(request):
    article = Article.objects.filter(content__contains='b')
    print(article)
    print(article.query)

# icontains 对大小写不敏感 也是查找某个字段内是否包括某段数据
    articles = Article.objects.filter(content__icontains='b')
    print(articles)
    print(articles.query)

# 在SQL的原生语句中 对大小写敏感的是 LIKE BINARY     对大小写不敏感的是 LIKE
    return HttpResponse("success")

# 提取那些给定的field的值是否在给定的容器中
def front_three(request):
    # 当有查找不到的时候就不在进行查找，比如id=5的并没有，那么就不再打印出来
    articles = Article.objects.filter(id__in=[1,2,3,4,5])
    print(articles)

    # 查询关联表的信息 这是是反转查询 直接使用models的小写而不是使用models_set
    categories = Category.objects.filter(article__id__in=[1,3])
    print(categories)
    articles1 = Article.objects.filter(category__id__in=[1])
    print(articles1)

    # 当容器为一个QuerySet对象时
    articles2 = Article.objects.filter(title__contains="Python")
    categories1 = Category.objects.filter(article__in=articles2)
    print(categories1)

    return HttpResponse("success")

# gt 查找大于某个值  gte 查找大于等于某个值  lt 查找小于某个值  lte 查找小于等于某个值
def front_four(request):
    articles1 = Article.objects.filter(id__gt=2)
    print(articles1)

    articles2 = Article.objects.filter(id__gte=2)
    print(articles2)

    articles3 = Article.objects.filter(id__lt=2)
    print(articles3)

    articles4 = Article.objects.filter(id__lte=2)
    print(articles4)

    return HttpResponse("success")

# startswith 对大小写敏感 查找以给定值开头的的某段数据 istartwith 则对大小写不敏感
# endswith 对大小写敏感 查找以给定值结束的某段数据 iendswith 则对大小写不敏感
def front_five(request):
    articles1 = Article.objects.filter(title__startswith="python")
    print(articles1)

    articles2 = Article.objects.filter(title__istartswith="python")
    print(articles2)

    articles3 = Article.objects.filter(title__endswith="c")
    print(articles3)

    articles4 = Article.objects.filter(title__iendswith='c')
    print(articles4)

    return HttpResponse("success")

# range 判断某个field的值是否在给定的区间中
def front_six(request):
    # make_aware 在django中讲naive时间变成aware时间
    start_time = make_aware(datetime(year=2018, month=12, day=14, hour=17, minute=0, second=0))
    end_time = make_aware(datetime(year=2018, month=12, day=14, hour=18, minute=0, second=0))
    articles = Article.objects.filter(time__range=(start_time,end_time))
    print(articles)

    # 针对某些date或者datetime类型的字段。可以指定date的范围
    articles2 = Article.objects.filter(time__date=(datetime(year=2018, month=12, day=14, hour=17, minute=29)))
    print(articles2)

    return HttpResponse("success")

# isnull 根据值是否为空进行查找
def front_seven(request):
    articles = Article.objects.filter(time__isnull=True)
    print(articles)

    # regex 用正则进行查找 对大小写敏感
    articles2 = Article.objects.filter(title__regex=r'^Python')
    print(articles2)

    # iregex 用正则进行查找 对大小写不敏感
    articles3 = Article.objects.filter(title__iregex=r'^python')
    print(articles3)

    return HttpResponse("success")