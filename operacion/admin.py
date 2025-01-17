from django.contrib import admin
from .models import Automovil,Seguro, Vtv, Coberturas, Poliza, VtvEstado



class SeguroAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'telefono')

class CoberturasAdmin(admin.ModelAdmin):
    pass
    
class PolizaAdmin(admin.ModelAdmin):
    list_display = ('empresa', 'cobertura', 'franquicia')



class AutomovilAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'kilometraje', 'numero_chasis', 'numero_motor', 'patente','vtv')
    search_fields = ('marca', 'modelo', 'numero_chasis', 'numero_motor')
    list_filter = ('marca', 'anio', 'color')
    actions = ['vtv']


    def vtv(self, request, queryset):
        pass
    vtv.short_description = "Actualizar Datos de VTV"



class VtvAdmin(admin.ModelAdmin):
    list_display = ('vencimiento','estado','turno')
    search_fields = ('vencimiento', 'estado')
    list_filter = ('vencimiento', 'estado')
   

class VtvEstadoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Automovil, AutomovilAdmin)
admin.site.register(Poliza, PolizaAdmin)
admin.site.register(Coberturas, CoberturasAdmin)
admin.site.register(Seguro, SeguroAdmin)
admin.site.register(Vtv,VtvAdmin)
admin.site.register(VtvEstado,VtvEstadoAdmin)

# Register your models here.
