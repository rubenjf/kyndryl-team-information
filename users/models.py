from django.db import models
#from django.contrib.auth.models import User
from accounts.models import User
from django.core.files.storage import default_storage as storage
import os
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile, TemporaryUploadedFile
from django.dispatch import receiver #add this
from django.db.models.signals import post_save #add this
from PIL import Image
import phonenumbers
from phonenumber_field.modelfields import PhoneNumberField


#ref: https://www.devhandbook.com/django/user-profile/

TITLE_CHOICES = [
    ('choose','Choose'),
    ('Mr.', 'Mr.'),
    ('Mrs.', 'Mrs.'),
    ('Ms.', 'Ms.'),
    ('Dr.', 'Dr.'),
    ('Prof.', 'Prof.'),
    ('__', 'Other.'),
]

USER_TYPE_CHOICES = [
    ('Permanent', 'Permanent'),
    ('Contractor', 'Contractor'),
]






class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=6, choices=TITLE_CHOICES, default='choose')
    job_title =  models.CharField("Job Title",max_length=40, blank=True, default='')
    user_type = models.CharField("Employment Type",max_length=10, choices=USER_TYPE_CHOICES , default='Permanent')
    summary = models.TextField("Summary", blank=True)
    other_names = models.CharField("Other Names",max_length=200, blank=True, default='')
    nick_name = models.CharField("Nick Names", max_length=200, blank=True, default='')
    image = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics/')
    phone1 =   models.CharField("Work Phone",max_length=20,blank=True)
    phone2 =   models.CharField("Personal Phone",max_length=20,blank=True)
    birth_date = models.DateField("Date of Birth",blank=True, null=True)
    email2 = models.EmailField("Company Email",null=True, blank=True)
    location = models.CharField("Current Location",max_length=25, blank=True, default='')
    skills_have = models.TextField("Skills I Have",blank=True)
    skills_like2_have = models.TextField("Skills I Would Like To Have", blank=True)
    timezone = models.CharField("Time Zone",max_length=25, blank=True, default='')
    zip_post_code = models.CharField("Zip/Post Code",max_length=25, blank=True, default='')

    
    def __str__(self):
        return f' {self.user.username} ,  Profile'
    

    @receiver(post_save, sender=User) #add this
    def create_user_profile(sender, instance, created, **kwargs):
       if created:
          Profile.objects.create(user=instance)

    @receiver(post_save, sender=User) #add this
    def save_user_profile(sender, instance, **kwargs):
       instance.profile.save()
    #    img = Image.open(instance.image.path) # Open image
    #    # resize image  
    #    if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size) # Resize image
    #         img.save(self.image.path) # Save it again and override the larger image
        
        
