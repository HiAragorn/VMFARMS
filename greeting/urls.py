"""
Author: Tresor Omari
this is the greeting url.
when someone types the website/hello, this is where the website will take them
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage, name='main'),
    path('hello/', views.hello, name='hello'),
    ]
