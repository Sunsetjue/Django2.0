from django.shortcuts import render,reverse,redirect
from django.http import HttpResponse
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
# from .models import SuperUser
from .models import User,Article
from .form import UserForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Permission,ContentType

# Create your views here.
'''
# 快速创建一个用户
def create_user(request):
    User.objects.create_user(username="sunbin01", password="sunbin01", email="sunbin01@qq.com")
    return HttpResponse("success")

# 快速创建一个超级用户
def create_superuser(request):
    User.objects.create_superuser(username="sunbin02", email="sunbin02@qq.com", password="sunbin02")
    return HttpResponse("success")

# 用命令行创建就是python manage.py createsuperuser (我创建的密码是tel18340680889 修改后密码是sunbin03)

# 修改用户的密码
def change_password(request):
    get_user = User.objects.get(username="sunbin03")
    get_user.set_password("sunbin03") # 记得保存
    get_user.save()
    return HttpResponse("success")

# 登陆
def login_in(request):
    user = authenticate(username="sunbin03", password="sunbin03")
    # 如果登陆失败 则会返回一个None值
    if user:
        print("登陆成功！")
    else:
        print("登陆失败！")
    return HttpResponse("success")
'''

'''
# 检测是否是超级用户 使用Proxy
def whether_superuser(request):
    users = SuperUser.superuser()
    for user in users:
        print(user.username)
    return HttpResponse("success")
'''

'''
# 自己定义一个authenticate 的登陆函数
def own_authenticate(telephone, password):
    user = User.objects.filter(extension__telephone=telephone).first()
    if user:
        # password = User.objects.filter(password=password).first()
        is_right = user.check_password(password)
        if is_right:
            return user
        else:
            return None
    else:
        return None

# 使用一对一的外键来添加一个字段telephone
def one_attend_view(request):
    user = User.objects.create_user(username="sunbin04", email="sunbin04@qq.com", password="sunbin04")
    user.extension.telephone = '15504975049'
    user.save()
    return HttpResponse("success")

# 使用完一对一的外键添加后 用自己定义的验证方法来登陆用户
def my_login_in(request):
    password = request.GET.get("password")
    telephone = request.GET.get("telephone")
    user = own_authenticate(telephone, password)
    if user:
        print("login in success!")
    else:
        print("login in failed!")
    return HttpResponse("success")
'''

# 重写继承后创建用户 必须的字段重写为电话号码
def abstract_user(request):
    telephone = '15972743041'
    username = "sunbin01"
    password = "sunbin01"
    user = User.objects.create_user(telephone=telephone, username=username, password=password)
    print(user.username)
    return HttpResponse("success")

# 重写继承后登陆用户 改变了username 的属性以及必须要的字段改为电话号码
def abstract_login(request):
    user = authenticate(username="15972743041", password="sunbin01")
    # 如果登陆失败 则会返回一个None值
    if user:
        print("登陆成功！")
    else:
        print("登陆失败！")
    return HttpResponse("success")

# 登陆
def my_login(request):
    if request.method == "GET":
        return render(request, "my_login.html")
    else:
        form = UserForm(request.POST)
        if form.is_valid():
            telephone = form.cleaned_data.get("telephone")
            password = form.cleaned_data.get("password")
            user = authenticate(username=telephone, password=password)
            if user and user.is_active: # 判断用户是否是活跃也就是说没有加入黑名单
                login(request, user)
                remember = form.cleaned_data.get("remember")
                if remember:
                    request.session.set_expiry(None)
                else:
                    request.session.set_expiry(0)
                next_exist = request.GET.get("next")
                if next_exist:
                    return redirect(reverse("front:profile"))
                else:
                    return HttpResponse("login success!")
            else:
                print("login failed!")
                return redirect(reverse("front:login"))
        else:
            print(form.errors.get_json_data())
            return HttpResponse("Wrong!")

# 退出登陆
def my_logout(request):
    logout(request)
    return HttpResponse("logout success!")

# 登陆限制
@login_required(login_url='/login/')
def profile(request):
    return HttpResponse("只有登陆了才能看的到的界面")

# 通过代码来添加用户的权限
def add_permission(request):
    permission_object = ContentType.objects.get_for_model(Article)
    Permission.objects.create(content_type=permission_object, codename="code_article", name="通过代码添加权限")
    return HttpResponse("success")

# 操作用户的权限
def operate_permission(request):
    permission_object = ContentType.objects.get_for_model(Article)
    # 找到有关文章的权限
    article_permissions = Permission.objects.filter(content_type=permission_object)
    for article_permission in article_permissions:
        print(article_permission)
    # 操作权限本身是给用户数据的权限来进行操作
    user = User.objects.get(id=1)

    # 直接给定一个权限的列表
    # user.user_permissions.set(article_permissions)
    # 清除权限
    # user.user_permissions.clear()
    # 一个个添加权限
    # user.user_permissions.add(article_permissions[2])
    # user.user_permissions.add(*article_permissions)
    # 一个个删除权限
    # user.user_permissions.remove(*article_permissions)
    # 判断是否拥有某个权限
    if user.has_perm('front.code_article'):
        print("has this permission")
    else:
        print("no this permission")
    get_all_permissions = user.get_all_permissions()
    # 获取当前所有的权限
    for get_all_permission in get_all_permissions:
        print(get_all_permission)
    return HttpResponse("success")

# 控制登陆后是否有权限访问页面
@permission_required('front.add_article', login_url='/login/', raise_exception=True)
def write(request):
    return HttpResponse("wa ha ha ha ha ha ha !")