from django.urls import path
from . import views

app_name = "homework"

urlpatterns = [
    path('one/', views.homework_one, name='one'),
    path('two/', views.homework_two, name='two'),
    path('three/', views.home_three, name='three'),
    path('four/', views.homework_four, name='four'),
    path('five/', views.homework_five, name='five'),
    path('six/', views.homework_six, name='six'),
    path('seven/', views.homework_seven, name='seven'),
]