from django.urls import path
from . import views

app_name = "one"
urlpatterns = [
    path('', views.index),
    path('index_index/', views.index_index),
    path('books/', views.books, name="book"),
    path('books/detail/<book_name>', views.books_detail, name='detail'),
    path('movies/', views.movies, name="movie"),
    path('cities/', views.cities, name="city"),
    path('login/', views.login, name="login"),
]