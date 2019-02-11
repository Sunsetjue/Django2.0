from django.urls import path
from .models import Article
from . import views

app_name = "front"

urlpatterns = [
    path('one/', views.one),
    path('create/', views.create, name="create"),
    path('list/', views.List.as_view(), name="list"),
    path('login_in/', views.LoginIn.as_view(), name='login_in'),
    path('login_up/', views.LoginUp.as_view(), name='login_up'),

]