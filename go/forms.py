from django.forms import ModelForm
from .models import *
from django import forms
from django.utils.translation import gettext as _
       
class TravelForm(ModelForm):
    class Meta:
        model = Travels
        fields = "__all__"
 
class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['start_date', 'end_date', 'client_name', 'contact_email']
        labels = { 'client_name': _('Your Name'),
                  'start_date': _('Start Date'),
                  'end_date': _('End Date'),
                  'contact_email': _('Your Email'),
                  }

