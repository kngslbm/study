from django import forms
from . models import Sale


class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = '__all__'
        exclude = ['user']
