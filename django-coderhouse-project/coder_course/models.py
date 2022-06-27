from django.db import models
from django.contrib.auth.models import User

class Insumos(models.Model):
    insumo = models.CharField(max_length=40)
    unidad = models.CharField(max_length=40)
    precio =models.IntegerField()
    fecha = models.DateField()
    proveedor = models.CharField(max_length=40)
    familia = models.CharField(max_length=40)

class Tareas(models.Model):
    codigo = models.CharField(max_length=40)
    rubro = models.CharField(max_length=40)
    tarea = models.CharField(max_length=40)
    unidad = models.CharField(max_length=40)
    costo = models.IntegerField()
    fecha = models.DateField()
    especificacion = models.CharField(max_length=40)


class Rubros(models.Model):
    codigo = models.CharField(max_length=40)
    nombre = models.CharField(max_length=40)
    
class Familias(models.Model):
    codigo = models.CharField(max_length=40)
    nombre = models.CharField(max_length=40)
    

    def __str__(self):
        return f'Codigo:{self.codigo} - Nombre:{self.nombre}'

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    avatares = models.ImageField(upload_to='avatares', null=True, blank=True)