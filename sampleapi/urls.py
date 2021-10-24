from django.urls import path
from sampleapi import views

urlpatterns = [
    path('articles/', views.ArticlesListView.as_view()),
    path('articles/<int:pk>', views.ArticlesDetailView.as_view()),
]