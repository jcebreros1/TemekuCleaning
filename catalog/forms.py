from django import forms

# Create your views here.

class ContactForm(forms.Form):
    """View function for home page of site."""
    contact_name = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    time_preference = forms.CharField(required=True)
    
 




