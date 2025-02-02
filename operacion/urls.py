from django.urls import path
from django.contrib.auth import views as auth_views


from .views import barra_navegacion, menu_automoviles, home
from .views import alta_automovil, eliminar_automovil,editar_automovil,detalle_automovil
from .views import listado_clientes,agregar_cliente,eliminar_cliente,editar_cliente
from .views import listado_turno_vtv,alta_turno_vtv,eliminar_turno_vtv,editar_turno_vtv
from .views import login_view
from .views import listado_flota, alta_flota,eliminar_flota,editar_flota,asociar_automovil,eliminar_asociacion
from .views import listado_titular,agregar_titular,eliminar_titular,editar_titular
from .views import listado_aseguradoras,agregar_aseguradoras,eliminar_aseguradoras,editar_aseguradoras
from .views import listado_poliza,agregar_poliza,eliminar_poliza,editar_poliza
from .views import listado_servicios,agregar_servicios,eliminar_servicios,editar_servicios
from .views import listado_mantenimiento,agregar_mantenimiento,eliminar_mantenimiento,editar_mantenimiento







urlpatterns = [
    path('home/', home,name='home'),
    path('menu/', barra_navegacion, name='bnav'),
    path('automoviles/', menu_automoviles,name='listado_automoviles'),
    path('automoviles/alta/', alta_automovil, name='alta_automovil'),
    path('automoviles/eliminar/<int:auto_id>/', eliminar_automovil, name='eliminar_automovil'),
    path('automoviles/editar/<int:auto_id>/', editar_automovil, name='editar_automovil'),
    # path('automoviles/detalle/<int:pk>/', detalle_automovil, name='detalle_automovil'),
    path('automoviles/detalle/<int:pk>/', detalle_automovil, name='detalle_automovil'),

    
    path('clientes/', listado_clientes, name='listado_clientes'),
    path('clientes/agregar/', agregar_cliente, name='agregar_cliente'),
    path('clientes/eliminar/<int:pk>/', eliminar_cliente, name='eliminar_cliente'),
    path('clientes/editar/<int:pk>/', editar_cliente, name='editar_cliente'),

    path('titular/', listado_titular, name='titular_listado'),
    path('titular/agregar/', agregar_titular, name='agregar_titular'),
    path('titular/eliminar/<int:pk>/', eliminar_titular, name='eliminar_titular'),
    path('titular/editar/<int:pk>/', editar_titular, name='editar_titular'),

    path('listado_turno_vtv/', listado_turno_vtv, name='listado_turno_vtv'),
    path('listado_turno_vtv/agregar/', alta_turno_vtv, name='agregar_turno_vtv'),
    path('listado_turno_vtv/eliminar/<int:pk>/', eliminar_turno_vtv, name='eliminar_turno'),
    path('editar_turno/<int:pk>/', editar_turno_vtv, name='editar_turno'),
    path('automovil/<int:auto_id>/', detalle_automovil, name='detalle_automovil'),

    path('login/', login_view, name='login'),

    path('flota/', listado_flota, name='listado_flota'),
    path('flota/agregar/', alta_flota, name='agregar_flota'),
    path('flota/eliminar/<int:pk>/', eliminar_flota, name='eliminar_flota'),
    path('flota/<int:pk>/', editar_flota, name='editar_flota'),
    path('flota/<int:pk>/asociar_automovil/', asociar_automovil, name='asociar_automovil'),
    path('flota/<int:pk>/eliminar_asociacion/<int:auto_id>/', eliminar_asociacion, name='eliminar_asociacion'),


    path('seguros/aseguradoras', listado_aseguradoras, name='aseguradoras_listado'),
    path('seguros/aseguradoras/agregar/', agregar_aseguradoras, name='agregar_aseguradoras'),
    path('seguros/aseguradoras/eliminar/<int:pk>/', eliminar_aseguradoras, name='eliminar_aseguradoras'),
    path('seguros/aseguradoras/editar/<int:pk>/', editar_aseguradoras, name='editar_aseguradoras'),



    path('seguros/poliza', listado_poliza, name='listado_poliza'),
    path('seguros/poliza/agregar/', agregar_poliza, name='agregar_poliza'),
    path('seguros/poliza/eliminar/<int:pk>/', eliminar_poliza, name='eliminar_poliza'),
    path('seguros/poliza/editar/<int:pk>/', editar_poliza, name='editar_poliza'),


    path('servicios/', listado_servicios, name='listado_servicios'),
    path('servicios/agregar/', agregar_servicios, name='agregar_servicios'),
    path('servicios/eliminar/<int:pk>/', eliminar_servicios, name='eliminar_servicios'),
    path('servicios/editar/<int:pk>/', editar_servicios, name='editar_servicios'),




    path('mantenimiento/', listado_mantenimiento, name='listado_mantenimiento'),
    path('mantenimiento/agregar/', agregar_mantenimiento, name='agregar_mantenimiento'),
    path('mantenimiento/eliminar/<int:pk>/', eliminar_mantenimiento, name='eliminar_mantenimiento'),
    path('mantenimiento/editar/<int:pk>/', editar_mantenimiento, name='editar_mantenimiento'),


    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),


]
