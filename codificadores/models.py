from django.db import models

class unidadm(models.Model):
     descripcion=models.CharField(max_length=50)
     unid=models.CharField(max_length=4)

class almacen(models.Model):
     descripcion=models.CharField(max_length=50)
     codigo=models.CharField(max_length=20)

class centrocosto(models.Model):
     descripcion=models.CharField(max_length=50)
     codigo=models.CharField(max_length=20)

class areas(models.Model):
     codigo=models.CharField(max_length=1)
     descripcion=models.CharField(max_length=150)

class equipos(models.Model):
     masterArea=models.ForeignKey(areas, on_delete=models.CASCADE, null=False, blank=False)
     codigo=models.CharField(max_length=15)
     descripcion=models.CharField(max_length=150)

class causas(models.Model):
     codigo=models.CharField(max_length=2)
     descripcion=models.CharField(max_length=150)

class trabajadores(models.Model):
     codigo=models.CharField(max_length=5)
     nombre=models.CharField(max_length=150)


