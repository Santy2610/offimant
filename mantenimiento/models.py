from django.db import models

# Create your models here.
class mantplan(models.Model):
    codigo=models.CharField(max_length=5)
    area=models.CharField(max_length=150)
    tarea=models.TextField()
    eneroP=models.BooleanField()
    febreroP=models.BooleanField()
    marzoP=models.BooleanField()
    abrilP=models.BooleanField()
    mayoP=models.BooleanField()
    junioP=models.BooleanField()
    julioP=models.BooleanField()
    agostoP=models.BooleanField()
    septiembreP=models.BooleanField()
    octubreP=models.BooleanField()
    noviembreP=models.BooleanField()
    diciembreP=models.BooleanField()
    eneroR=models.BooleanField()
    febreroR=models.BooleanField()
    marzoR=models.BooleanField()
    abrilR=models.BooleanField()
    mayoR=models.BooleanField()
    junioR=models.BooleanField()
    julioR=models.BooleanField()
    agostoR=models.BooleanField()
    septiembreR=models.BooleanField()
    octubreR=models.BooleanField()
    noviembreR=models.BooleanField()
    diciembreR=models.BooleanField()




    
    #febreroP=models.CharField(max_length=1)
    #marzoP=models.CharField(max_length=1)
    #abrilP=models.CharField(max_length=1)
    #mayoP=models.CharField(max_length=1)
    #junioP=models.CharField(max_length=1)
    #julioP=models.CharField(max_length=1)
    #agostoP=models.CharField(max_length=1)
    #septiembreP=models.CharField(max_length=1)
    #octubreP=models.CharField(max_length=1)
    #noviembreP=models.CharField(max_length=1)
    #diciembreP=models.CharField(max_length=1)

    


