from django import forms
from django.forms import ModelForm, Textarea
from django import forms
from .models import Event

from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django_summernote.fields import SummernoteTextFormField, SummernoteTextField 
from .models import Address



class EventForm(ModelForm):
    required_css_class = 'required'
   
    description = forms.CharField(widget=SummernoteWidget())
    class Meta:
        model = Event
   
        fields  = ['name','location','description','upload_choices','upload_image','document']
        labels = {
            
        }
        widgets = {
            
            'description' : SummernoteWidget(),

        }

class EventForm2(forms.Form):
    content = forms.CharField(widget=SummernoteInplaceWidget())


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'
        widgets = {
            'address': Textarea(attrs={'rows': 4}),
        }          

class AddressUpdateForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'
        widgets = {
            'address': Textarea(attrs={'rows': 1}),
        }   
