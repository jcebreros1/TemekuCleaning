from django import forms

# Create your views here.

class ContactForm(forms.Form):
    contact_name = forms.EmailField(required=True)
    phone = forms.CharField(required=True)
    time_preference = forms.CharField(widget=forms.Textarea, required=True)



