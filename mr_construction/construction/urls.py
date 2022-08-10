# from django.contrib import admin
from django.urls import path
from django.contrib.auth import views
from construction import views

# from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.Index, name='index'),
    path('index/', views.Index, name='index'),
    path('about/', views.About, name='about'),
    path('projects/', views.Projects, name='projects'),
    path('contact/', views.Contect_view, name='contact_view'), 
]
# urlpatterns += staticfiles_urlpatterns()