from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index,name = 'rate-index'),
    path('about/', views.about,name = 'rate-about'),
] + static(settings.MEDIA_URL, documet_root = settings.MEDIA_ROOT)