from django.db import models

# Create your models here.
class tiempo(models.Model):
    area=models.CharField(max_length=50)
    equipo=models.CharField(max_length=150)
    fechaI=models.DateField()
    fechaF=models.DateField()
    causa=models.CharField(max_length=150)
    observacion=models.TextField()
    dias=models.CharField(max_length=10)