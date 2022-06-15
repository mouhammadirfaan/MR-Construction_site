from tkinter import Widget
from django.db import models

# Create your models here.
class ContactForm(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email_address = models.EmailField(max_length=200)
    tex_area = models.TextField(max_length=2000)


