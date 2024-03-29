from django.db import models


# Create your models here.
class ContactForm(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.EmailField(max_length=50)
    text_area = models.TextField(max_length=100)

    def __str__(self):
        return self.email_address


