from django.urls import path
from . import views

app_name = "front"

urlpatterns = [
    # path('create_user/', views.create_user, name="create_user"),
    # path('create_superuser/', views.create_superuser, name="create_superuser"),
    # path('change_password/', views.change_password, name="change_password"),
    # path('login_in/', views.login_in, name="login_in"),
    # # path('whether/', views.whether_superuser, name="whether"),
    # path('one_to_one/', views.one_attend_view, name="one_to_one"),
    # path('my_login_in/', views.my_login_in, name="my_login_in"),
    path('abstract_user/', views.abstract_user, name="abstract_user"),
    path('abstract_login/', views.abstract_login, name="abstract_login"),
    path('login/', views.my_login, name="login"),
    path('logout/', views.my_logout, name="logout"),
    path('profile/', views.profile, name="profile"),
    path('add_permission/', views.add_permission, name="add_permission"),
    path('operate_permission/', views.operate_permission, name="operate_permission"),
    path('write/', views.write, name="write"),
]