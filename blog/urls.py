from django.urls import path
from . import views
from .views import HomePageView, DetailPageView, ReadPageView

urlpatterns = [
    path('',HomePageView.as_view(), name='home'),
    path('read/',ReadPageView.as_view(), name='read'),
    path('post/<int:pk>/',DetailPageView.as_view(), name='detail'),
    path('post/new/', views.postNew, name='postNew'),
    path('post/<int:pk>/edit/', views.postEdit, name='postEdit'),
    path('post/<pk>/remove/', views.postDelete, name='postDelete'),
]