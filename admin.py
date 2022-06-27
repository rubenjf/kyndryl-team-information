from django.contrib import admin
from .models import Event,Categories
from .models import Address
from django_summernote.admin import SummernoteModelAdmin
from accounts.models import User
# Register your models here.
from .forms import AddressForm

class EventAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)

admin.site.register(Event,EventAdmin)
admin.site.register(Categories)
admin.site.register(Address)
admin.site.register(User)