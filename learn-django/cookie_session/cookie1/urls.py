from django.urls import path
from . import views

app_name = "cookie_and_session"

urlpatterns = [
    path('one/', views.one),
    path('two/', views.two),
    path('three/', views.three),
    path('delete/', views.delete),
    path('session/', views.session),
    path('four/', views.four)
]