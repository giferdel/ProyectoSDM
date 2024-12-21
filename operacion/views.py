from django.shortcuts import render
#from django.http import HttpResponse
#from django.template import Template , Context
from .models import Automovil, ClienteParticular

def home(request):
    
    return render(request, 'index.html')

def barra_navegacion(request):

    opciones_menu = ['Automoviles', 'Clientes', 'VTV', 'Seguros','Patentes','Mantenimiento']
    return render(request, 'bnav.html', {'opciones_menu': opciones_menu})

def menu_automoviles(request):

    auto = {'marca': Automovil.marca,
            'modelo':Automovil.modelo,
            'anio':Automovil.anio,
            'color':Automovil.color,
            'km':Automovil.kilometraje,
            'ncha':Automovil.numero_chasis,
            'nmot':Automovil.numero_motor,
            'pat':Automovil.patente,
            'vtv':Automovil.vtv}
    return render(request, 'automoviles.html', auto)



def menu_clientes(request):

    cliente = {'nombre': ClienteParticular.nombre,
            'apellido':ClienteParticular.apellido,
            'dni':ClienteParticular.dni,
            'cuil':ClienteParticular.cuil,
            'direccion':ClienteParticular.direccion,
            'tel':ClienteParticular.telefono,
            'email':ClienteParticular.email}
    
    return render(request, 'clientes.html', cliente)
    
   


#def mi_vista(request):
#    contexto = {
#        'mensaje': 'Este es un mensaje desde la vista.',
#        'cantidad': '18'
#    }
#    return render(request, 'index.html', contexto)