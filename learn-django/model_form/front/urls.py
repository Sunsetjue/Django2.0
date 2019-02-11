from django.urls import path
from . import views

app_name = "front"

urlpatterns = [
    path('one/', views.one, name='one'),
    path('two/', views.two, name='two'),
]