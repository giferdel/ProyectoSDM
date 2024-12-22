from django.urls import path
#from .views import mi_vista
from .views import barra_navegacion, menu_automoviles, menu_clientes, home
from .views import alta_automovil, eliminar_automovil,editar_automovil



urlpatterns = [
    path('home/', home),
    path('menu/', barra_navegacion),
    path('automoviles/', menu_automoviles,name='listado_automoviles'),
    path('automoviles/alta/', alta_automovil, name='alta_automovil'),
    path('automoviles/eliminar/<int:auto_id>/', eliminar_automovil, name='eliminar_automovil'),
    path('automoviles/editar/<int:auto_id>/', editar_automovil, name='editar_automovil'),
    path('clientes/', menu_clientes)
]