from django import forms
#from django.contrib.auth.models import User
#from accounts.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from flatpickr import DatePickerInput
from django.forms import ModelForm, Textarea
from django.contrib.auth import get_user_model

User = get_user_model()




class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email','first_name','last_name']



class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['title' , 'job_title', 'summary','image' , 'user_type' , 'other_names' , 'nick_name' , 'phone1' , 'phone2' , 
                  'birth_date' ,  'email2' , 'location' , 'skills_have' , 'skills_like2_have' , 'timezone' , 'zip_post_code' ]
        widgets = {
            'birth_date': DatePickerInput(),
            'summary': Textarea(attrs={'cols': 125, 'rows': 4}),
            'skills_have': Textarea(attrs={'rows': 3}),
            'skills_like2_have': Textarea(attrs={'rows': 3}),
            
        }          



