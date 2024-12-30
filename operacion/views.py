from .models import Automovil, ClienteParticular, ClienteEmpresa
from django.shortcuts import render, redirect,get_object_or_404
from .forms import AutomovilForm
from django.contrib.auth import login, authenticate
from .forms import CustomLoginForm, ClienteForm, ClienteEmpForm


def home(request):
    
    return render(request, 'index.html')

def barra_navegacion(request):
    opciones_menu = ['Automoviles', 'Clientes', 'VTV', 'Seguros','Patentes','Mantenimiento']
    return render(request, 'bnav.html', {'opciones_menu': opciones_menu})

def menu_automoviles(request):
    autos = Automovil.objects.filter(visibilidad=True)  # Filtra los autos visibles
    return render(request, 'automovil/automoviles.html', {'autos': autos})


def menu_clientes(request):

    cliente = {'nombre': ClienteParticular.nombre,
            'apellido':ClienteParticular.apellido,
            'dni':ClienteParticular.dni,
            'cuil':ClienteParticular.cuil,
            'direccion':ClienteParticular.direccion,
            'tel':ClienteParticular.telefono,
            'email':ClienteParticular.email}
    
    return render(request, 'clientes/clientes_list.html', cliente)
    
   



def alta_automovil(request):
    if request.method == 'POST':
        form = AutomovilForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo objeto Automovil
            return redirect('listado_automoviles')  #
    else:
        form = AutomovilForm()

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

    clientes = ClienteParticular.objects.filter(visible=True)
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
    cliente = get_object_or_404(ClienteParticular, pk=pk)
    cliente.visible = False  # Oculta el cliente
    cliente.save()
    return redirect('listado_clientes')  # Redirige al listado de clientes



def editar_cliente(request, pk):
    cliente = get_object_or_404(ClienteParticular, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('listado_clientes')  # Redirigir al listado después de guardar
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'clientes/editar_cliente.html', {'form': form})

##################################################################################################################################
# CLIENTES EMPRESA
##################################################################################################################################


def listado_clientes_empresa(request):

    clientes_empresa = ClienteEmpresa.objects.filter(visible=True)
    return render(request, 'empresa/clientes_empresa.html', {'clientes_empresa': clientes_empresa})

def agregar_empresa(request):
    if request.method == 'POST':
        form = ClienteEmpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cliente_empresa')  # Redirige al listado de clientes
    else:
        form = ClienteEmpForm()
    return render(request, 'empresa/agregar_cliente_empresa.html', {'form': form})



def eliminar_empresa(request, pk):
    cliente = get_object_or_404(ClienteEmpresa, pk=pk)
    cliente.visible = False  # Oculta el cliente
    cliente.save()
    return redirect('cliente_empresa')  # Redirige al listado de clientes



def editar_empresa(request, pk):
    cliente = get_object_or_404(ClienteEmpresa, pk=pk)
    if request.method == 'POST':
        form = ClienteEmpForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('cliente_empresa')  # Redirigir al listado después de guardar
    else:
        form = ClienteEmpForm(instance=cliente)
    return render(request, 'empresa/editar_cliente_empresa.html', {'form': form})




######################################################################################################################
