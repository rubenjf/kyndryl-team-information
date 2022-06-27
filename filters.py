
from django_filters.widgets import RangeWidget
import django_filters
import django_filters.widgets
from .models import Event


class EventFilter(django_filters.FilterSet):
    _CHOICES = {
    ('Active', 'Active'),
    ('Archieve', 'Archieve')

    }
    upload_date = django_filters.DateFromToRangeFilter(label='Search For  Events  Between Date Range',widget=RangeWidget(attrs={'type': 'date'}))
    upload_choices = django_filters.ChoiceFilter(label='Status',field_name='upload_choices',choices=_CHOICES,initial='Active')
    
    class Meta:
        model = Event
        fields = ['name','location','upload_choices','upload_date']



