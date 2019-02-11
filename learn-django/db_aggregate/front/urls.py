from django.urls import path
from . import views

app_name ="front"

urlpatterns = [
    path('one/', views.front_one, name='one'),
    path('two/', views.front_two, name='two'),
    path('three/', views.front_three, name='three'),
    path('four/', views.front_four, name='four'),
    path('five/', views.front_five, name='five'),
    path('six/', views.front_six, name='six'),
    path('seven/',views.front_seven, name='seven'),
    path('eight/', views.front_eight, name='eight'),
    path('ninth/', views.front_ninth, name='ninth'),
    path('ten/', views.front_ten, name='ten'),
    path('eleven/', views.front_eleven, name='eleven'),
    path('twelve/', views.front_twelve, name='twelve'),
    path('thirteen/', views.front_thirteen, name='thirteen'),
]