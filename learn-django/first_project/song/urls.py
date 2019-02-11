from django.urls import path,include
from . import views as vi

urlpatterns = [
    path(r'', vi.yue),
    # 传递参数
    # 在URL里面添加变量
    path(r'sun/<sun_loc>/<loc_id>/', vi.sun), # 可以使用转换器来限制输入的URL的格式 比如<int:sun_loc>表示输入的必须是整数格式
    # 第二种，查询字符串
    path(r'bin/', vi.bin),
    path(r'sb/', vi.sb),
    path(r'login/', vi.login, name="login"), # 可以给URL改名
]