from urllib import request
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

from construction.models import ContactForm 


# Create your views here.
def Index(request):
    return render(request, 'construction/index.html')
   
def About(request):
    return render(request, 'construction/about.html')

def Projects(request):
    return render(request, 'construction/projects.html')

def Contect(request):

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            firtname = form.cleaned_data['firsr_name']
            lastname = form.cleaned_deta['firsr_name']
            email = form.cleaned_deta['email_address']
            message = form.cleaned_deta['text']






    return render(request, 'construction/contact.html')