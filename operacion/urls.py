from django.urls import path

from .views import barra_navegacion, menu_automoviles, home
from .views import alta_automovil, eliminar_automovil,editar_automovil,detalle_automovil
from .views import listado_clientes,agregar_cliente,eliminar_cliente,editar_cliente
from .views import listado_turno_vtv,alta_turno_vtv,eliminar_turno_vtv,editar_turno_vtv
from .views import login_view
from .views import listado_flota, alta_flota,eliminar_flota,editar_flota,asociar_automovil,eliminar_asociacion
from .views import listado_titular,agregar_titular,eliminar_titular,editar_titular



urlpatterns = [
    path('home/', home,name='home'),
    path('menu/', barra_navegacion, name='bnav'),
    path('automoviles/', menu_automoviles,name='listado_automoviles'),
    path('automoviles/alta/', alta_automovil, name='alta_automovil'),
    path('automoviles/eliminar/<int:auto_id>/', eliminar_automovil, name='eliminar_automovil'),
    path('automoviles/editar/<int:auto_id>/', editar_automovil, name='editar_automovil'),
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

    path('login/', login_view, name='login'),

    path('flota/', listado_flota, name='listado_flota'),
    path('flota/agregar/', alta_flota, name='agregar_flota'),
    path('flota/eliminar/<int:pk>/', eliminar_flota, name='eliminar_flota'),
    path('flota/<int:pk>/', editar_flota, name='editar_flota'),
    path('flota/<int:pk>/asociar_automovil/', asociar_automovil, name='asociar_automovil'),
    path('flota/<int:pk>/eliminar_asociacion/<int:auto_id>/', eliminar_asociacion, name='eliminar_asociacion'),






]
