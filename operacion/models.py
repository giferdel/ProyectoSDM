

from django.db import models
from django.utils import timezone

class VtvEstado(models.Model):
    estado = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.estado}"
    class Meta:
        verbose_name_plural = "VTV estado"


class Vtv(models.Model):
    vencimiento = models.DateField()
    turno = models.BooleanField()
    estado = models.ForeignKey(VtvEstado, on_delete=models.RESTRICT)

    def __str__(self):
        return f"{self.estado}"

    class Meta:
        verbose_name_plural = "VTV"








class Seguro(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.nombre}"
    
class Coberturas(models.Model):
    tipo = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.tipo}"
    class Meta:
        verbose_name_plural = "Coberturas"
        
class Poliza(models.Model):
    empresa = models.ForeignKey(Seguro, on_delete=models.RESTRICT)
    cobertura = models.ForeignKey(Coberturas, on_delete=models.RESTRICT)
    franquicia = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.empresa} {self.cobertura}"

    
    
class Cliente(models.Model):
    razon_social = models.CharField(max_length=50)
    dni = models.PositiveBigIntegerField(unique=True)
    cuil = models.PositiveBigIntegerField(unique=True)
    cuit = models.PositiveBigIntegerField(unique=True)
    direccion = models.CharField(max_length=50)
    telefono = models.PositiveIntegerField(default=0)
    email = models.CharField(max_length=50)
    visible = models.BooleanField(default=True)  # Campo de visibilidad

    def __str__(self):
        return f"{self.razon_social}"
    
    class Meta:
        verbose_name_plural = "Cliente empresa"

  
class Flota(models.Model):
    descripcion = models.CharField(max_length=50)
    cliente = models.ForeignKey(Cliente, on_delete=models.RESTRICT)
    disponible = models.BooleanField(default=True)


    def __str__(self):
        return f"{self.descripcion}"
# Create your models here.
    class Meta:
        verbose_name_plural = "Flotas"

class Automovil(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    anio = models.PositiveIntegerField()
    color = models.CharField(max_length=30)
    kilometraje = models.PositiveIntegerField()
    numero_chasis = models.CharField(max_length=30, unique=True)
    numero_motor = models.CharField(max_length=30, unique=True)
    patente = models.CharField(max_length=10, unique=True)
    vtv = models.ForeignKey(Vtv, on_delete=models.RESTRICT)
    visibilidad = models.BooleanField(default=True)  # Campo de visibilidad para ocultar automóviles eliminados
    flota = models.ForeignKey(Flota, on_delete=models.RESTRICT, blank=True, null=True)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.anio})"

# Create your models here.
    class Meta:
        verbose_name_plural = "Automóviles"

class Turno_VTV(models.Model):
    auto = models.ForeignKey(Automovil, related_name='turnos', on_delete=models.CASCADE)
    fecha_turno = models.DateTimeField()
    lugar_verificacion = models.CharField(max_length=255)
    estado = models.CharField(
        max_length=50, 
        choices=[
            ('pendiente', 'Pendiente'),
            ('completado', 'Completado'),
            ('cancelado', 'Cancelado')
        ], 
        default='pendiente'
    )
    comentarios = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Turno para {self.auto.patente} en {self.fecha_turno}'
