from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name = 'rate-home'),
    path('about/', views.about,name = 'rate-about')
]
