from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "front"

urlpatterns = [
    path('', views.index, name="index"),
    path('sign_in/', views.SignIn.as_view(), name='sign_in'),
    path('sign_up/', views.SignUp.as_view(), name="sign_up"),
    path('python/', views.python, name='python'),
    path('django/', views.django, name='django'),
    path('photo/', views.CutPhoto.as_view(), name='photo'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)