from django import forms
from .models import product
from django.contrib.auth.models import User


class productForm(forms.ModelForm):
    class  Meta:
        model=product
        fields='__all__'

        
        
        
