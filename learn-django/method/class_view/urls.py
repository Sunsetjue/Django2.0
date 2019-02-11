from django.urls import path
from . import views

app_name = 'class_view'

urlpatterns = [
    path('book_list/', views.BookList.as_view(), name="book_list"),
    path('book/', views.Book.as_view(), name='book'),
    path('book_detail/<book_id>/', views.BookDetail.as_view(), name='detail'),
    path('about1/', views.About.as_view(), name='about1'),
]