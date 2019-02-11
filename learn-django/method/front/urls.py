from django.urls import path
from . import views

app_name = 'front'

urlpatterns = [
    path('one/', views.front_one, name='one'),
    path('two/', views.front_two, name='two'),
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('three/', views.front_three, name='three'),
    path('four/', views.front_four, name='four'),
    path('five/', views.front_five, name='five'),
    path('six/', views.front_six, name='six'),
    path('seven/', views.front_seven, name='seven'),
]