from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.utils.timezone import make_aware

# Create your views here.
def one(request):
    response = HttpResponse("one")
    date = datetime(year=2019, month=1 ,day=3, hour=16, minute=50, second=0)
    # 这里需要设置清醒的时间 不然并不是中国这边的时区
    date = make_aware(date)
    response.set_cookie(key="username", value="sunbin", max_age=60, expires=date, path="/cookie1/three/")
    # max_age 的单位是秒 表示从现在在开始多少秒后这个cookie 过期
    # 在同时设置max_age 和expires 的时候 只执行expires 实际中只需要使用一个max_age
    # path 设置路径 只有在那个里面的路径才能够访问 默认为根路径
    # domain：针对哪个域名有效 默认是针对主域名下都有效 如果只要针对某个子域名才有效 那么可以设置这个属性
    # secure：是否是安全的，如果设置为True，那么只能在https协议下才可用。
    # httponly：默认是False。如果为True，那么在客户端不能通过JavaScript进行操作。
    return response

def two(request):
    response = request.COOKIES.get("username")
    return HttpResponse(response)

def three(request):
    response = request.COOKIES.get("username")
    return HttpResponse(response)

def delete(request):
    '''删除cookie'''
    response = HttpResponse("delete")
    response.delete_cookie("username")
    # 寻找到指定的key 来进行删除 将其key 变为空
    return response

def session(request):
    request.session["username"] = "sunbin"
    return HttpResponse("success")

def four(request):
    '''
    get：用来从session中获取指定值
    pop：从session中删除一个值
    keys：从session中获取所有的键
    items：从session中获取所有的值
    clear：清除当前这个用户的session数据
    flush：删除session并且删除在浏览器中存储的session_id 一般在注销的时候用得比较多
    set_expiry(value)：设置过期时间
    整形：代表秒数，表示多少秒后过期
    0：代表只要浏览器关闭，session就会过期
    None：会使用全局的session配置 在settings.py中可以设置SESSION_COOKIE_AGE来配置全局的过期时间
    默认是1209600秒，也就是2周的时间。
    clear_expired：清除过期的session
    Django并不会清除过期的session 需要定期手动的清理
    或者是在终端 使用命令行python manage.py clearsessions 来清除过期的session
    '''
    '''
    username = request.session.get("username")
    print(username)
    
    pop_name = request.session.pop("username")
    # 从session 中移除一个值
    print(pop_name)
    '''
    keys = request.session.keys()
    print(keys)
    values = request.session.values()
    print(values)

    # request.session.clear()
    # 清除session 里的数据 数据库中还有session_key

    # request.session.flush()
    # 注销数据 session_key 也一同清除

    request.session.set_expiry(0)
    # 设置过期时间 单位为秒 为0的时候是当服务器关闭的时候就过期 为None的时候是使用默认的两周
    return HttpResponse("success")