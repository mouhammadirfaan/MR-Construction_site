from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.Index, name='index'),
    path('index/', views.Index, name='index'),
    path('about/', views.About, name='about'),
    path('projects/', views.Projects, name='projects'),
    path('contact/', views.Contect, name='contact'), 
]
urlpatterns += staticfiles_urlpatterns()