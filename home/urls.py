"""boutique_ado URL Configuration
This is the root urls and we don't need include and 
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home')
]