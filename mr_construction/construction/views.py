from urllib import request
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpRequest

from construction.models import ContactForm 


# Create your views here.
def Index(request):
    return render(request, 'construction/index.html')
   
def About(request):
    return render(request, 'construction/about.html')

def Projects(request):
    return render(request, 'construction/projects.html')

def Contect_view(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'construction/success.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'construction/contact.html')
    
    #     if request.method == "POST":
    #     firtname = request.POST['first_name']
    #     lastname = request.POST['last_name']
    #     email = request.POST['email_address']
    #     message = request.POST['text_area'] 

    #     form_variable = ContactForm(first_name=firtname, last_nam=lastname, email_address=email, text_area=message)
    # return render(request, 'construction/contact.html')

    # if request.method == "POST":
    #     form = ContactForm(request.POST)
    #     if form.is_valid():
    #         firtname = form.cleaned_data['first_name']
    #         lastname = form.cleaned_deta['last_name']
    #         email = form.cleaned_deta['email_address']
    #         message = form.cleaned_deta['text_area']
    # else:
    #     form = ContactForm()
    # return render(request, 'construction/contact.html', {"form":form})