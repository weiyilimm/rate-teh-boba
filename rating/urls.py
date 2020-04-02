from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name = 'rate-index'),
    path('about/', views.about,name = 'rate-about'),
]
