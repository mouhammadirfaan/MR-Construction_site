from urllib import request
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


# Create your views here.
def Index(request):
    return render(request, 'constructiion/index.html')
   
def About(request):
    return render(request, 'constructiion/about.html')

def Projdcts(request):
    return render(request, 'constructiion/projdcts.html')

def Contect(request):
    return render(request, 'constructiion/contect.html')