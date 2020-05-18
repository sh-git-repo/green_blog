from django.urls import path
from .views import HomePageView, AboutPageView, DetailPageView

urlpatterns = [
        path('', HomePageView.as_view(), name='blog-home'),
        path('about/', AboutPageView.as_view(), name='blog-about'),
        path('msg/<int:pk>/', DetailPageView.as_view(), name='blog-detail')
]
