from django.urls import path

from .views import barra_navegacion, menu_automoviles, listado_clientes, home
from .views import alta_automovil, eliminar_automovil,editar_automovil,detalle_automovil
from .views import agregar_cliente,eliminar_cliente,editar_cliente
from .views import listado_clientes_empresa,agregar_empresa,eliminar_empresa,editar_empresa

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

    path('empresas/', listado_clientes_empresa, name='cliente_empresa'),
    path('empresas/agregar/', agregar_empresa, name='agregar_empresa'),
    path('empresas/eliminar/<int:pk>/', eliminar_empresa, name='eliminar_empresa'),
    path('empresas/editar/<int:pk>/', editar_empresa, name='editar_empresa'),

]
