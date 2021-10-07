from django.urls import path
from sampleapi import views

urlpatterns = [
    path('users/', views.usersApi)
]