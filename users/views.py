from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile
#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from accounts.models import User
import requests 

#https://www.devhandbook.com/django/user-profile/


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
          
            form.save()
            
            users_without_profile = get_user_model().objects.filter(profile__isnull=True)
            print("$$$$",users_without_profile)
            for user in users_without_profile:
                Profile.objects.create(user=user)
            return redirect('user_login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('index')
        else:    
            messages.success(request, f'Your form save  has a problem!')  
 

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
       



    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    
    return render(request, 'upload/company.html', context)

  



