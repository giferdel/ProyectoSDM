from django.contrib import admin
from .models import  Coberturas, VtvEstado



class CoberturasAdmin(admin.ModelAdmin):
    pass
    
class VtvEstadoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Coberturas, CoberturasAdmin)

admin.site.register(VtvEstado,VtvEstadoAdmin)

# Register your models here.
