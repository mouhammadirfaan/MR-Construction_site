from django import forms
from construction.models import ContactForm

class Contact(forms.ModelForm):
    class meta:
        model = ContactForm
        fields = '__all__'