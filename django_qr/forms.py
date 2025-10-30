from django import forms
from . import views

class QRCodeForm(forms.Form):
        name = forms.CharField(
        max_length=50,
        label='Name',
        widget=forms.TextInput(attrs={'placeholder': 'Enter Name', 'class': 'form-control'}
        ))
        url = forms.URLField(
        max_length=200,
        label='Resturant URL',
        widget=forms.URLInput(attrs={'placeholder': 'Enter  URL', 'class': 'form-control'}))
