from django.shortcuts import render,redirect,reverse
from .models import Commit
from django.views.decorators.http import require_http_methods
import bleach # 用来清理包含html格式字符串的库 指定哪些标签需要保留，哪些标签是需要过滤掉的。
                # 也可以指定标签上哪些属性是可以保留，哪些属性是不需要的
from bleach.sanitizer import ALLOWED_TAGS,ALLOWED_ATTRIBUTES
# Create your views here.
def index(request):
    dict = {
        "commits": Commit.objects.all()
    }
    return render(request, "index.html", context=dict)

@require_http_methods(["POST"])
def add_commit(request):
    msg = request.POST.get("commit")
    # 添加允许的标签img ALLOWDED_TAGS 是一个列表
    ALLOWED_TAGS = bleach.ALLOWED_TAGS + ['img']
    # 添加允许标签的属性img ALLWODED_ATTRIBUTES 是一个字典
    ALLOWED_ATTRIBUTES = {**bleach.ALLOWED_ATTRIBUTES, 'img': ['src','alt']}
    ALLOWED_ATTRIBUTES['a'] = ['href', 'title', 'target']
    # 在这里进行过滤标签
    cleaned_data = bleach.clean(msg, tags=ALLOWED_TAGS, attributes=ALLOWED_ATTRIBUTES)
    Commit.objects.create(commit=cleaned_data)

    # Commit.objects.create(commit=msg)
    return redirect(reverse("index"))