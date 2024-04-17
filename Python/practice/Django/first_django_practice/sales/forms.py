from django import forms
from . models import Sale, User


class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = '__all__'
        exclude = ['user']


class UserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
