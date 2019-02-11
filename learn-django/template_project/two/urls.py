from django.urls import path
from . import views

app_name = "two"
urlpatterns = [
    path('company/', views.company, name="company"),
    path('school/', views.school, name="school"),
    path('index/', views.index_index, name="index_index"),
    path('', views.index, name="index"),
]