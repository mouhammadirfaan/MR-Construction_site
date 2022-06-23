from dataclasses import field
import imp
from pyexpat import model
from django.forms import ModelForm
from . models import ContactForm

class Contect(ModelForm):
    class meta:
        model = ContactForm
        field = '__all__'