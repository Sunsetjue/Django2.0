from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "files"

urlpatterns = [
    path('one/', views.One.as_view(), name="one"),
    path('two/', views.Two.as_view(), name='two'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)