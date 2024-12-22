from .models import Automovil, ClienteParticular
from django.shortcuts import render, redirect,get_object_or_404
from .forms import AutomovilForm


def home(request):
    
    return render(request, 'index.html')

def barra_navegacion(request):

    opciones_menu = ['Automoviles', 'Clientes', 'VTV', 'Seguros','Patentes','Mantenimiento']
    return render(request, 'bnav.html', {'opciones_menu': opciones_menu})

def menu_automoviles(request):
    # Obtén todos los automóviles desde la base de datos
#    autos = Automovil.objects.all()
    autos = Automovil.objects.filter(visibilidad=True)  # Filtra los autos visibles


    # Crea una lista de diccionarios con los datos de los automóviles
    autos_data = [
        {
            'id': auto.id,
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
    
   



def alta_automovil(request):
    if request.method == 'POST':
        form = AutomovilForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo objeto Automovil
            return redirect('listado_automoviles')  #
    else:
        form = AutomovilForm()

    return render(request, 'alta_automovil.html', {'form': form})




def eliminar_automovil(request, auto_id):
    auto = get_object_or_404(Automovil, id=auto_id)
    auto.visibilidad = False  # Cambia visibilidad a False
    auto.save()  # Guarda el cambio en la base de datos
    return redirect('listado_automoviles')  # Redirige a la lista después