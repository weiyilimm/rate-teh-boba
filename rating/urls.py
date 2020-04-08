from django.urls import path
from . import views
from .views import (
    ListCafe,
    DetailCafe,
    RegisterCafe,
    UpdateCafe,
    DeleteCafe,
    WriteFeedback
)


urlpatterns = [
    path('', views.ListCafe, name='rate-home'),
    path('cafe/<slug:cafe_slug>/', views.DetailCafe, name="cafe-detail"),
    path('new/', views.RegisterCafe, name='cafe-create'),
    path('cafe/<slug:cafe_slug>/update/', views.UpdateCafe, name='cafe-update'),
    path('cafe/<slug:cafe_slug>/delete/', views.DeleteCafe, name='cafe-delete'),
    path('cafe/<slug:cafe_slug>/feedback/',
         views.WriteFeedback, name='feedback-create'),
    path('about/', views.about, name='rate-about'),
    path('contact/', views.contact, name='rate-contact'),
    path('terms/', views.terms, name='rate-terms'),
    path('privacy/', views.privacy, name='rate-privacy'),
    path('faq/', views.faq, name='rate-faq'),
    path('search/', views.search, name='search'),
]
