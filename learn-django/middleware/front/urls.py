from django.urls import path
from . import views

app_name = "front"

urlpatterns = [
    path('', views.index, name="index"),
    path('python/', views.python, name="python"),
    path('sign_in/', views.Sign_in.as_view(), name="sign_in")
]