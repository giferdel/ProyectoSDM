"""
URL configuration for arrendadora project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static

def redirect_to_home(request):
    return redirect('home')  # Cambia 'inicio' por el nombre de tu URL de destino


urlpatterns = [
    path('', redirect_to_home),  # Redirige la raíz a otra página
    path('admin/', admin.site.urls),
    path('operacion/', include('operacion.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    

admin.site.site_header = "SDM administración"
admin.site.site_title = "SOLUCIONES DE MOVILIDAD SA"
admin.site.index_title = "Bienvenido al panel de administración de SDM"