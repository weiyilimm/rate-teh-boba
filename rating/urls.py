from django.urls import path
from . import views
from .views import (
    CafeListView,
    CafeDetailView,
    CafeCreateView,
    CafeUpdateView,
    CafeDeleteView,
    FeedbackCreateView,
    SearchCafeListView
)


urlpatterns = [
    path('', CafeListView.as_view(), name='rate-home'),
    path('cafe/<str:city>', SearchCafeListView.as_view(), name='search-city'),
    path('cafe/<int:pk>/', CafeDetailView.as_view(), name='cafe-detail'),
    path('cafe/new/', CafeCreateView.as_view(), name='cafe-create'),
    path('cafe/<int:pk>/update/', CafeUpdateView.as_view(), name='cafe-update'),
    path('cafe/<int:pk>/delete/', CafeDeleteView.as_view(), name='cafe-delete'),
    path('cafe/<int:pk>/feedback/', FeedbackCreateView.as_view(), name='feedback-create'),
    path('about/', views.about,name = 'rate-about'),
    path('contact/', views.contact,name = 'rate-contact'),
    path('terms/', views.terms,name = 'rate-terms'),
    path('privacy/', views.privacy,name = 'rate-privacy'),
     path('faq/', views.faq, name = 'rate-faq')
]
