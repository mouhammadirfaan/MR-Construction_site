import re
from tkinter import Widget
from django.db import models

# Create your models here.
class ContactForm(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email_address = models.EmailField(max_length=200)
    text_area = models.TextField(max_length=2000)

    def __str__(self):
        return self.email_address


