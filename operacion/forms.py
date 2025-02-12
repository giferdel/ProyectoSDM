from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Automovil, Cliente , Servicio
from .models import Turno_VTV
from .models import Flota,Titular,Aseguradora,PolizaSeguro,HistorialMantenimiento



class AutomovilForm(forms.ModelForm):
    class Meta:
        model = Automovil
        fields = '__all__'  # Incluye todos los campos del modelo
        exclude=['visibilidad']
        widgets = {

            'anio': forms.NumberInput(attrs={'min': 1900, 'max': 2100}),
            'kilometraje': forms.NumberInput(attrs={'min': 0}),
            'patente': forms.TextInput(attrs={'placeholder': 'ABC123'}),

        }
    anio = forms.CharField(label='Año')

class FlotaForm(forms.ModelForm):
    class Meta:
        model = Flota
        fields = '__all__'  # Incluye todos los campos del modelo
        exclude=['visibilidad']
    
class TitularForm(forms.ModelForm):
    class Meta:
        model = Titular
        fields = '__all__'  # Incluye todos los campos del modelo
 
    


    
class AseguradoraForm(forms.ModelForm):
    class Meta:
        model = Aseguradora
        fields = '__all__'  # Incluye todos los campos del modelo
 


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}))



class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'  # Incluye todos los campos del modelo
        exclude = ['visible']  # Sustituye con el nombre del campo que deseas ocultar

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'dni': forms.NumberInput(attrs={'class': 'form-control'}),
            'cuil': forms.NumberInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }




class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'  # Incluye todos los campos del modelo
        exclude = ['visible']  # Sustituye con el nombre del campo que deseas ocultar

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'cuit': forms.NumberInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }



class TurnoVTVForm(forms.ModelForm):
    class Meta:
        model = Turno_VTV
        fields = ['auto', 'fecha_turno', 'lugar_verificacion', 'comentarios']
        widgets = {
            'fecha_turno': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }



class PolizaForm(forms.ModelForm):
    class Meta:
        model = PolizaSeguro
        fields = '__all__'  # Incluye todos los campos del modelo

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = '__all__'  # Incluye todos los campos del modelo


class MantenimientoForm(forms.ModelForm):
    class Meta:
        model = HistorialMantenimiento
        fields = '__all__'  # Incluye todos los campos del modelo
        widgets = {
            'fecha_inicio_mantenimiento': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'}
            ),


            'fecha_fin_mantenimiento': forms.DateInput(
                attrs={'type': 'date'}
            ),
        }

    