from django.forms import ModelForm
from django import forms
from django.contrib.admin import widgets

from locations.models import Station

class StationPoliceForm(forms.Form):
    """
        A form used to register a Police Station and add extra information 
        (profile) of that police.
    """
    username = forms.CharField(max_length=50)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    police_code = forms.CharField(max_length=255, help_text="A police ID number")
    
    station = forms.ModelChoiceField(Station)
    phone_number = forms.CharField(max_length=13, null=True, blank=True)
    email = forms.EmailField()
    
class ChangePasswordForm(forms.Form):
    """
        A form to change user password.
    """
    current_password = forms.PasswordField()
    new_password = forms.PasswordField()
    verify_new_password = forms.PasswordField()
    