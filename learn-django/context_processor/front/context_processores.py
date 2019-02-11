from .models import Username
from .form import SignInView

# 设置上下文处理器 用来显示一些在标签中不变的静态页面
def front_username(request):
    user_id = request.session.get("user_id")
    context = {}
    if user_id:
        try:
            username = Username.objects.get(id=user_id)
            context["front_username"] = username
        except:
            pass
    return context