from django.urls import path
from . import views

app_name = "one"

urlpatterns = [
    path('', views.index, name="index"),
    path('delete/', views.delete_view, name="delete"),
    path('one_to_many/', views.one_to_many_view, name="one_to_many"),
    path('get/', views.get_view, name='get'),
    path('get2/', views.get_view2, name='get2'),
    path('one_to_one/', views.one_to_one_view, name='one_to_one'),
    path('get_one_to_one/', views.get_one_to_one_view, name='get_one_to_one'),
    path('get_one_to_one2/', views.get_one_to_one_view2, name='get_one_to_one2'),
    path('many_to_many/', views.many_to_many_view, name='many_to_many'),
    path('get_many_to_many/', views.get_many_to_many_view, name='get_many_to_many'),
    path('get_many_to_many2/', views.get_mant_to_many_view2, name='many_to_many2'),
]