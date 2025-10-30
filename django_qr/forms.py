from django import forms
from . import views

class QRCodeForm(forms.Form):
    resturant_name = forms.CharField(
        max_length=50,
        label='Resturant Name',
        widget=forms.TextInput(attrs={'placeholder': 'Enter Resturant Name', 'class': 'form-control'}
        ))
    url = forms.URLField(
        max_length=200,
        label='Resturant URL',
        widget=forms.URLInput(attrs={'placeholder': 'Enter Resturant URL', 'class': 'form-control'}))
