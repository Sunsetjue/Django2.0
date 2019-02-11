from django.urls import path
from . import views

app_name = "front"

urlpatterns = [
    path('', views.index, name="index"),
    path('sign_in/', views.SignIn.as_view(), name="sign_in"),
    path('sign_up/', views.SignUp.as_view(), name="sign_up"),
    path('transform/', views.Transform.as_view(), name="transform"),
    path('logout/', views.logout, name='logout'),
    path('extra_money/', views.ExtraMoney.as_view(), name="extra_money"),
]