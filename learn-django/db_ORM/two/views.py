from django.shortcuts import render
from django.http import HttpResponse
from django.utils.timezone import now,localtime #这里的now时间是UTC时间不是东八区的时间
from .models import Time

# Create your views here.
def two1(request):
    create_time = Time(remove=False, create_time=now())
    create_time.save()
    time = Time.objects.get(id=2) # 获取数据
    ctime = time.create_time # 获取数据中的create_time
    print(ctime)
    print(localtime(ctime))
    # return HttpResponse("success")
    return render(request, "two1.html", context={'ctime':ctime})

def two2(request):
    tel = Time(remove=True,telephone="3666332553")
    tel.save()
    times = Time.objects.all()
    for time in times:
        print(time)
    return HttpResponse("success")
