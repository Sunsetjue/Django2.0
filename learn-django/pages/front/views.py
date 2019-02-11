from django.shortcuts import render,redirect,reverse
from .models import Article
from django.http import HttpResponse
from django.views.generic import ListView,View
from django.utils.decorators import method_decorator

# Create your views here.
def one(request):
    return render(request, 'one.html')

def create(request):
    articles = []
    for i in range(100,1000):
        article = Article(title="书名：%d"%i, content="内容：%d"%i**2)
        articles.append(article)
    Article.objects.bulk_create(articles)
    return HttpResponse("success")

class List(ListView):
    model = Article
    template_name = 'list2.html'
    context_object_name = 'articles'
    paginate_by = 10
    ordering = 'time'
    page_kwarg = 'p' # 定义第几页的数据的参数名称
    
    def get_context_data(self, **kwargs):
        msg = super(List, self).get_context_data(**kwargs)
        # msg返回的是一个字典 有paginator 和 page_obj两个比较重要的参数
        '''print(msg)
        paginator = msg.get('paginator')
        print(paginator.count) # 打印总共有多少条数据
        print(paginator.num_pages) # 打印总共有多少页

        page_obj = msg.get('page_obj')
        print(page_obj.has_next()) # 是否还有下一页
        print(page_obj.has_previous()) # 是否还有上一页 返回布尔值
        print(page_obj.next_page_number()) # 返回下一页的页码 没有了就报错
        print(page_obj.previous_page_number()) # 返回上一页的页码 没有就报错
        print(page_obj.number) # 返回当前页的页码
        '''
        paginator = msg.get("paginator")
        page_obj = msg.get("page_obj")
        around = self.get_around_context(paginator, page_obj)
        msg.update(around)
        return msg
    '''
    def get_queryset(self):
        # 定义可以获取的数据的数量也就是对数据进行限制，重写一个函数将不需要的数据过滤掉
        return Article.objects.filter(id__lte=20)
    '''
    def get_around_context(self, paginator, page_obj, around=2):
        present = page_obj.number
        end = paginator.num_pages
        left_omit = True
        right_omit = True

        if present <= 2 + around:
            left_ranges = range(1, present+1)
            left_omit = False
        else:
            left_ranges = range(present-around, present+1)

        if present >= end - around - 1:
            right_ranges = range(present+1, end+1)
            right_omit = False
        else:
            right_ranges = range(present+1, present+around+1)

        result = {
            "left_ranges": left_ranges,
            "right_ranges":right_ranges,
            "present": present,
            "end": end,
            "left_omit": left_omit,
            "right_omit": right_omit
        }
        return result

def logging(func):
    def wrapper(request, *args, **kwargs):
        username = request.GET.get("username")
        if username:
            return func(request, *args, **kwargs)
        else:
            return redirect(reverse("front:login_up"))
    return wrapper

# 类装饰器
@method_decorator(logging, name='dispatch')
class LoginIn(View):
    def get(self, request):
        return HttpResponse("你已经进来了")

class LoginUp(View):
    def get(self, request):
        return HttpResponse("请登陆")
