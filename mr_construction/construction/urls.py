from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.Index, name='index'),
    path('index/', views.Index, name='index'),
    path('about/', views.About, name='about'),
    path('prijects/', views.Projdcts, name='projects'),
    path('contact/', views.Contect, name='contect'), 
]
urlpatterns += staticfiles_urlpatterns()