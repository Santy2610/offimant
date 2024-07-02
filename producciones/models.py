from datetime import date
from django.db import models


class producciones(models.Model):
    codigo = models.CharField(max_length=10)
    lote = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=100)
    unidad = models.CharField(max_length=5)
    cantidad = models.FloatField()
    fechaf = models.DateField()


class materiales(models.Model):
    idprod = models.ForeignKey(
        producciones, on_delete=models.CASCADE, null=False, blank=False)
    novale = models.CharField(max_length=5)
    almacen = models.CharField(max_length=50)
    costo = models.CharField(max_length=50)
    entregado = models.CharField(max_length=100)
    fecha = models.DateField()
