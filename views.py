from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings as conf_settings
from django.core.files.storage import FileSystemStorage
from .forms import EventForm
from .models import Event, Address
from .filters import EventFilter
from django.urls import reverse_lazy
from django.contrib.auth.mixins import  UserPassesTestMixin
import os
from django.http import FileResponse
import mimetypes
from users.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .forms import AddressForm,  AddressUpdateForm
from users.models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from accounts.models import User
from .models import Address







from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

NUM_ROWS = conf_settings.PAGINATION_ROWS
# Create your views here.

def index(request):
    u=request.user
    a=Address.objects.filter(user=u,address_type="Present").first().address
    
    context = {
        'perm_addr': a,
        'title': 'Index',
    }

    return render(request, 'kyndril/index.html', context )
    
def home(request):

    return render(request, 'upload/edit_list.html', {'title': 'Home'})

def login(request):
    return render(request, 'users/login.html', {'title': 'Login'})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
           
            form.save()
            users_without_profile = User.objects.filter(profile__isnull=True)
            for user in users_without_profile:
                Profile.objects.create(user=user)

            username = form.cleaned_data.get('username')
            messages.success(request, f'{username}, Your account has been created! You are now able to log in')
            return redirect('user_login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
    
def address(request):
    initial_data = {
        "user" : request.user
        
    }
    if request.method == 'POST':
        form = AddressForm(request.POST)
       
        
        if form.is_valid():
            form.save()
            data=form.cleaned_data
            
            messages.success(request, f'{request.user.username}, Your address has been created!')
            return redirect('index')
        else: 
            messages.error(request, f'{request.user.username}, Your address could not be created!')   
            return redirect('index') 
    else:
        form = AddressForm(initial=initial_data)
        add_list = Address.objects.filter(user=request.user)
        context = {'form':form,'add_list':add_list}

    
    return render(request,'kyndril/address.html',context)


def profile_list(request):
    user_list = User.objects.all()
    context={'users':user_list}
    return render(request, 'kyndril/profile_list.html', context)

def getProfile(request,id):
    obj= get_object_or_404(User, id=id)
    context= {'user':obj}
    return render(request,'kyndril/get_profile.html' , context)


def delete(request, id):
    u = request.user
    Address.objects.filter(user=u,id=id).delete()

    return redirect('address')

def update(request, id):
    obj= get_object_or_404(Address, id=id)
    form = AddressForm(request.POST or None, instance= obj)
    context= {'form': form}

    u = request.user
    add_list=Address.objects.filter(user=u)
    
    if form.is_valid():
        obj= form.save(commit= False)
        obj.save()
        messages.success(request, "You successfully updated the address")
        context = {'form':form,'add_list':add_list}
        return render(request,'kyndril/index.html',context)

    else:
        context= {'form': form,
                'error': 'The form was not updated successfully. Please enter correct data'}
        return render(request,'kyndril/update_address.html' , context)







    
    
    
    


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
            print("Your form save  has a problem") 


    else:
        u=request.user
        address=Address.objects.filter(user=u,address_type="Present").first().address

        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)   
       


    context = {
        'u_form': u_form,
        'p_form': p_form,
     
    }

    return render(request, 'kyndril/user_profile.html', context)

     


def personal(request):
    #https://www.devhandbook.com/django/user-profile/

    return render(request, 'kyndril/index.html')


def eventlist(request):
   
    context={}
    post_list=Event.objects.all()
    
    filtered_posts = EventFilter(request.GET, queryset=post_list)
    context['filter'] = filtered_posts

    #page=1 by default
    urlmeta=request.META['QUERY_STRING']
    if urlmeta=='':
        urlmeta='?page=1'

    # CURRENT_URL=urlmeta


#    urlmeta=request.META['QUERY_STRING']
    if urlmeta=='':
        urlmeta='?name=&location=&prayed=&upload_choices=&upload_date='

    CURRENT_URL=urlmeta

    filtered_posts.qs.update(current_url=urlmeta)

    #used for pagination



    paginated_rs = Paginator(filtered_posts.qs, NUM_ROWS)
    page_number = int(request.GET.get('page', '1'))
    page_obj = paginated_rs.get_page(page_number)
    context['page_obj']= page_obj
    
    

    request.session['CURRENT_URL']=CURRENT_URL

    return render(
        request, 
        'upload/edit_list.html', 
        {'context': context},
    )

class EventUpdateView(UserPassesTestMixin, UpdateView):
    model = Event
    
    def get_success_url(self):
        root_url = reverse_lazy('home') 

        # if self.object.current_url == None:
        #     self.object.current_url=''
            

        # myurl=root_url+"?"+self.object.current_url
        messages.success(self.request, "Record has been updated")
        return root_url
    

    
    fields = ['name','location','upload_choices','description','upload_image','document']

    def __init__(self, *args, **kwargs):                    
        super(EventUpdateView, self).__init__(*args, **kwargs)   
        instance = getattr(self, 'instance', None)
            
    def form_valid(self, form):
        
        return super().form_valid(form)

    def test_func(self):
        quiz = self.get_object()
        return True   

  

def eventupdate(request, pk=None): 
    # dictionary for initial data with  
    # field names as keys 
    context ={} 
  
    # fetch the object related to passed id 
    if pk:
        obj = get_object_or_404(Event, id = pk) 
  
    # pass the object as instance in form 
    form = EventForm(request.POST or None, instance = obj) 
  
    # save the data from the form and 
    # redirect to detail_view 
    if form.is_valid(): 
        form.save() 
        return HttpResponseRedirect("/home") 
  
    # add form dictionary to context 
    context["form"] = form 
  
    return render(request, "upload/edit.html", context) 


def eventdelete(request, pk=None): 
    # dictionary for initial data with  
    # field names as keys 
     instance = Event.objects.get(id=pk)
     instance.delete()
     return HttpResponseRedirect("/home") 
  


      
    

def eventdetail(request, pk=None):
    context ={} 
    context["data"] = Event.objects.get(id = pk)
    return render(request, "upload/detail.html", context) 

def download_detail(request, pk=None):
    context ={} 
    context["data"] = Event.objects.get(id = pk)
    return render(request, "upload/download_detail.html", context) 





def download_doc(request, pk=None):
    obj = Event.objects.get(id = pk)
    file_path = obj.document.path
    #file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            mime_type, _ = mimetypes.guess_type(file_path)
            
            response = HttpResponse(fh, content_type=mime_type)
            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
            return response
    raise Http404

def download_img(request, pk=None):
    obj = Event.objects.get(id = pk)
    file_path = obj.upload_image.path
    #file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            mime_type, _ = mimetypes.guess_type(file_path)
            
            response = HttpResponse(fh, content_type=mime_type)
            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
            return response
    raise Http404

 