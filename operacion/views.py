from .models import Automovil, Cliente,VtvEstado,Turno_VTV,Flota
from django.shortcuts import render, redirect,get_object_or_404
from .forms import AutomovilForm
from django.contrib.auth import login, authenticate
from .forms import CustomLoginForm, ClienteForm, TurnoVTVForm, FlotaForm


from django.db.models import Q



def home(request):
    
    return render(request, 'index.html')

def barra_navegacion(request):
    opciones_menu = ['Automoviles', 'Clientes', 'VTV', 'Seguros','Patentes','Mantenimiento']
    return render(request, 'bnav.html', {'opciones_menu': opciones_menu})


####################################################################################################################################

def menu_automoviles(request):
    estado_vtv = request.GET.get('estado_vtv', None)  # Obtén el estado de la VTV desde los parámetros GET
    autos = Automovil.objects.filter(visibilidad=True)

    if estado_vtv:  # Aplica el filtro si se especifica un estado
        autos = autos.filter(vtv__estado__estado=estado_vtv)

    # Obtener todos los estados posibles para mostrarlos como opciones en el filtro
    estados_vtv = VtvEstado.objects.all()

    return render(request, 'automovil/automoviles.html', {
        'autos': autos,
        'estados_vtv': estados_vtv,
        'estado_seleccionado': estado_vtv,
    })



def menu_clientes(request):

    cliente = {'nombre': Cliente.nombre,
            'apellido':Cliente.apellido,
            'dni':Cliente.dni,
            'cuil':Cliente.cuil,
            'direccion':Cliente.direccion,
            'tel':Cliente.telefono,
            'email':Cliente.email}
    
    return render(request, 'clientes/clientes_list.html', cliente)
    
def alta_automovil(request):
    if request.method == 'POST':
        form = AutomovilForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo objeto Automovil
            return redirect('listado_automoviles')  #
    else:
        form = AutomovilForm()
        form.fields.pop("flota")

    return render(request, 'automovil/alta_automovil.html', {'form': form})


def eliminar_automovil(request, auto_id):
    auto = get_object_or_404(Automovil, id=auto_id)
    auto.visibilidad = False  # Cambia visibilidad a False
    auto.save()  # Guarda el cambio en la base de datos
    return redirect('listado_automoviles')  # Redirige a la lista después


def editar_automovil(request, auto_id):
    auto = get_object_or_404(Automovil, id=auto_id)

    if request.method == 'POST':
        form = AutomovilForm(request.POST, instance=auto)
        if form.is_valid():
            form.save()
            return redirect('listado_automoviles')  # Redirige a la lista después de guardar
    else:
        form = AutomovilForm(instance=auto)

    return render(request, 'automovil/editar_automovil.html', {'form': form, 'auto': auto})


def detalle_automovil(request, pk):
    auto = get_object_or_404(Automovil, pk=pk)
    return render(request, 'automovil/detalle_automovil.html', {'auto': auto})

#############################################################################################################################################
# FLOTA
#############################################################################################################################################

def listado_flota(request):
    
    # Obtener todos los estados posibles para mostrarlos como opciones en el filtro
    flota = Flota.objects.all()

    return render(request, 'flota/listado_flota.html', {'flota': flota})

def alta_flota(request):
    if request.method == 'POST':
        form = FlotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listado_flota')  # Redirige a una lista de turnos o la página que consideres apropiada
    else:
        form = FlotaForm()
    return render(request, 'flota/alta_flota.html', {'form': form})


def eliminar_flota(request, pk):
    flota = get_object_or_404(Flota, pk=pk)
    flota.delete()
    return redirect('listado_flota')  # Redirige a la lista después de cancelar uno

#############################################################################################################################################
# LOGIN
#############################################################################################################################################



def login_view(request):
    if request.method == "POST":
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirige a la vista principal después del login
    else:
        form = CustomLoginForm()
    return render(request, 'registration/login.html', {'form': form})



##################################################################################################################################
# CLIENTES
##################################################################################################################################


def listado_clientes(request):

    clientes = Cliente.objects.filter(visible=True)
    return render(request, 'clientes/clientes_list.html', {'clientes': clientes})


def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listado_clientes')  # Redirige al listado de clientes
    else:
        form = ClienteForm()
    return render(request, 'clientes/agregar_cliente.html', {'form': form})



def eliminar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    cliente.visible = False  # Oculta el cliente
    cliente.save()
    return redirect('listado_clientes')  # Redirige al listado de clientes



def editar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('listado_clientes')  # Redirigir al listado después de guardar
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'clientes/editar_cliente.html', {'form': form})


######################################################################################################################
def listado_turno_vtv(request):
    # Lógica para registrar turnos
    turnos_vtv = Turno_VTV.objects.filter(estado='pendiente')
    return render(request, 'vtv/listado_turno_vtv.html', {'turnos_vtv': turnos_vtv})
    

def alta_turno_vtv(request):
    if request.method == 'POST':
        form = TurnoVTVForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listado_turno_vtv')  # Redirige a una lista de turnos o la página que consideres apropiada
    else:
        form = TurnoVTVForm()
    return render(request, 'vtv/alta_turno.html', {'form': form})

def eliminar_turno_vtv(request, pk):
    turno = get_object_or_404(Turno_VTV, pk=pk)
    
    if request.method == 'POST':
        turno.estado = 'cancelado'
        turno.save()
        return redirect('listado_turno_vtv')  # Redirige a la lista de turnos después de cancelar uno


def editar_turno_vtv(request, pk):
    turno = get_object_or_404(Turno_VTV, pk=pk)

    if request.method == 'POST':
        form = TurnoVTVForm(request.POST, instance=turno)
        if form.is_valid():
            form.save()
            return redirect('listado_turno_vtv')  # Redirige a la lista de turnos después de editar uno
    else:
        form = TurnoVTVForm(instance=turno)
    
    return render(request, 'vtv/editar_turno.html', {'form': form, 'turno': turno})


def asociar_automovil(request, pk):
    if request.method == 'POST':
        flota = get_object_or_404(Flota, pk=pk)
        automovil_id = request.POST.get('automovil_id')
        automovil = get_object_or_404(Automovil, id=automovil_id)
        automovil.flota = flota
        automovil.save()

        flota.disponible = True
        flota.save()


        return redirect('editar_flota', pk=pk)

def editar_flota(request, pk):
    flota = get_object_or_404(Flota, pk=pk)
    automoviles_asociados = Automovil.objects.filter(flota=flota)
    automoviles_restantes = Automovil.objects.exclude(flota=flota)

    if request.method == 'POST':
        form = FlotaForm(request.POST, instance=flota)
        if form.is_valid():
            form.save()
            return redirect('listado_flota')  # Redirigir al listado después de guardar
    else:
        form = FlotaForm(instance=flota)
    return render(request, 'flota/editar_flota.html', {
        'form': form,
        'flota': flota,
        'automoviles_asociados': automoviles_asociados,
        'automoviles_restantes': automoviles_restantes,
})


def eliminar_asociacion(request, pk, auto_id):
    flota = get_object_or_404(Flota, pk=pk)
    automovil = get_object_or_404(Automovil, id=auto_id)
    
    # Desasociar el automóvil de la flota
    if automovil.flota == flota:
        automovil.flota = None
        automovil.save()

    # Verificar si quedan automóviles asociados a la flota
    if not Automovil.objects.filter(flota=flota).exists():
        flota.disponible = True
        flota.save()

    return redirect('editar_flota', pk=pk)