from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
     path('', views.Index, name='index'),
    # path('about', views.About, name='about'),
    # path('prijects', views.Projdcts, name='projects'),
    # path('contact', views.Contect, name='contect'), 
]
