from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Automovil

class AutomovilForm(forms.ModelForm):
    class Meta:
        model = Automovil
        fields = '__all__'  # Incluye todos los campos del modelo
        widgets = {
            'anio': forms.NumberInput(attrs={'min': 1900, 'max': 2100}),
            'kilometraje': forms.NumberInput(attrs={'min': 0}),
            'patente': forms.TextInput(attrs={'placeholder': 'ABC123'}),
        }




class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}))
