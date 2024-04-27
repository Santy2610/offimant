from django.db import models

# Create your models here.
class vale(models.Model):
  codigo=models.CharField(max_length=5)
  almacen=models.CharField(max_length=50)
  costo=models.CharField(max_length=50)
  entregado=models.CharField(max_length=100)
  fecha=models.DateField()

class materialv(models.Model):
  valeID=models.ForeignKey(vale, on_delete=models.CASCADE, null=False, blank=False)
  material=models.CharField(max_length=150)
  unidad=models.CharField(max_length=4)
  cantidad=models.FloatField()
    