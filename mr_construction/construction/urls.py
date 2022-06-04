from django.contrib import admin
from django.urls import path
from . import views

urlspatren=[
    path('', views.Index, name='index'),
    path('', views.About, name='about'),
    path('', views.Projdcts, name='projects'),
    path('', views.Contect, name='contect'),

]