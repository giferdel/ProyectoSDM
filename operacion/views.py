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
    # Obtén todos los automóviles desde la base de datos
    autos = Automovil.objects.all()

    # Crea una lista de diccionarios con los datos de los automóviles
    autos_data = [
        {
            'marca': auto.marca,
            'modelo': auto.modelo,
            'anio': auto.anio,
            'color': auto.color,
            'km': auto.kilometraje,
            'ncha': auto.numero_chasis,
            'nmot': auto.numero_motor,
            'pat': auto.patente,
            'vtv': auto.vtv,
        }
        for auto in autos
    ]

    # Pasar los datos al contexto
    return render(request, 'automoviles.html', {'autos': autos_data})


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