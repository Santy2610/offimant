from django.db import models


# Create your models here.
class mantplan(models.Model):
    codigo=models.CharField(max_length=5)
    area=models.CharField(max_length=150)
    tarea=models.TextField()
    eneroP=models.CharField(max_length=2, default="No")
    febreroP=models.CharField(max_length=2, default="No")
    marzoP=models.CharField(max_length=2, default="No")
    abrilP=models.CharField(max_length=2, default="No")
    mayoP=models.CharField(max_length=2, default="No")
    junioP=models.CharField(max_length=2, default="No")
    julioP=models.CharField(max_length=2, default="No")
    agostoP=models.CharField(max_length=2, default="No")
    septiembreP=models.CharField(max_length=2, default="No")
    octubreP=models.CharField(max_length=2, default="No")
    noviembreP=models.CharField(max_length=2, default="No")
    diciembreP=models.CharField(max_length=2, default="No")
    eneroR=models.CharField(max_length=2)
    febreroR=models.CharField(max_length=2)
    marzoR=models.CharField(max_length=2)
    abrilR=models.CharField(max_length=2)
    mayoR=models.CharField(max_length=2)
    junioR=models.CharField(max_length=2)
    julioR=models.CharField(max_length=2)
    agostoR=models.CharField(max_length=2)
    septiembreR=models.CharField(max_length=2)
    octubreR=models.CharField(max_length=2)
    noviembreR=models.CharField(max_length=2)
    diciembreR=models.CharField(max_length=2)




    
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

    


