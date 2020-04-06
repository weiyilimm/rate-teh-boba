from django.urls import path
from . import views
from .views import (
    CafeListView,
    CafeDetailView,
    CafeCreateView,
    CafeUpdateView,
    CafeDeleteView
)


urlpatterns = [
    path('', CafeListView.as_view(), name='rate-home'),
    path('cafe/<int:pk>/', CafeDetailView.as_view(), name='cafe-detail'),
    path('cafe/new/', CafeCreateView.as_view(), name='cafe-create'),
    path('cafe/<int:pk>/update/', CafeUpdateView.as_view(), name='cafe-update'),
    path('cafe/<int:pk>/delete/', CafeDeleteView.as_view(), name='cafe-delete'),
    path('about/', views.about,name = 'rate-about')

]
