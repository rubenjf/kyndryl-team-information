from django.db import models
from django.utils import timezone

from django.contrib import messages
from django_summernote.fields import SummernoteTextFormField, SummernoteTextField  
from django.conf import settings
from django.contrib.auth import get_user_model
User = get_user_model()






UPLOAD_CHOICES= [
    ('Active', 'Active'),
    ('Archieve', 'Archieve'),
    ]

ADDRESS_TYPE_CHOICES = [
    ('Present', 'Present Address'),
    ('Home', 'Home'),
    ('Work', 'Work'),
    ('Permanent', 'Permanent Address'),
    ('Other', 'Other'),

]



class Event(models.Model):
    name = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    description = models.TextField()
    upload_date = models.DateTimeField(default=timezone.now)
    upload_choices = models.CharField("Upload Type",max_length=20,choices=UPLOAD_CHOICES, default='Active') 
    upload_image = models.ImageField(upload_to='images', default='images/anc-logo.png')
    document = models.FileField(upload_to ='documents')  # file will be saved to MEDIA_ROOT / uploads / 2015 / 01 / 30 
    current_url = models.CharField(max_length = 250, null = True, blank = True) 
   
    def __str__(self):
        return f'{self.name +",  "+ self.location}'
    class Meta:
        ordering = ['-upload_date'] 
        

class Categories(models.Model):
    name = models.CharField(max_length=250)
    url = models.CharField(max_length=25, default='personal')
   
    def __str__(self):
        return f'{self.name}'
  

# class Product(models.Model):

#     def __str__(self):
#         return f'{self.name}'
#     class Meta:
         
class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address_type=models.CharField(max_length=10, choices=ADDRESS_TYPE_CHOICES)
    address = models.TextField("Address",blank=True)

    def __str__(self):
        return f' {self.user.username} , {self.address_type}  Address'

# class Article(models.Model):
#     author = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#     )