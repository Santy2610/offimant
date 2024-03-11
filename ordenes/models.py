from django.db import models

# Create your models here.
class orden(models.Model):
    codigo=models.CharField(max_length=10)
    departamento=models.CharField(max_length=100)
    area=models.CharField(max_length=50)
    equipo=models.CharField(max_length=150)
    idequipo=models.CharField(max_length=20, null=True)
    fechaRep=models.DateField()
    motivosolic=models.CharField(max_length=50, null=True)
    falla=models.TextField()
    solicitante=models.CharField(max_length=100)
    Afectacion=models.CharField(max_length=2)
    prioridad=models.CharField(max_length=50)
    Resumen=models.TextField()
    Reparado=models.CharField(max_length=150)
    fechaEje=models.DateField()
    Destino=models.CharField(max_length=100)
    valecodigo=models.CharField(max_length=5, null=True)
    culminada=models.CharField(max_length=2)
