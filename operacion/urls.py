from django.urls import path
#from .views import mi_vista
from .views import barra_navegacion, menu_automoviles, menu_clientes, home

urlpatterns = [
    path('home/', home),
    path('menu/', barra_navegacion),
    path('automoviles/', menu_automoviles),
    path('clientes/', menu_clientes)
]