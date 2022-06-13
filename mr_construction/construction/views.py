from urllib import request
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


# Create your views here.
def Index(request):
    return render(request, 'construction/index.html')
   
def About(request):
    return render(request, 'construction/about.html')

def Projects(request):
    return render(request, 'construction/projects.html')

def Contect(request):
    return render(request, 'construction/contact.html')