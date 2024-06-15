import random
from django.shortcuts import render, redirect
from ordenes.models import orden
from producciones.models import producciones
from vales.models import vale, materialv
from codificadores.models import centrocosto
from mantenimiento.models import mantplan
from django.db.models import Sum, Count, F
from django.core.paginator import Paginator
from datetime import date



def barracont():
      mes=date.today()
      rest=mes.month
      if rest == 1:
            tareas=mantplan.objects.all().order_by('area').annotate(conteo=Count('area')).filter(eneroP="X")
      elif rest == 2:       
            tareas=mantplan.objects.all().filter(febreroP="X")
      elif rest == 3:       
            tareas=mantplan.objects.all().filter(marzoP="X")
      elif rest == 4:       
            tareas=mantplan.objects.all().filter(abrilP="X")
      elif rest == 5:       
            tareas=mantplan.objects.all().filter(mayoP="X")
      elif rest == 6:       
            tareas=mantplan.objects.all().filter(junioP="X").order_by('codigo').annotate(last=F('junioR'))
      elif rest == 7:       
            tareas=mantplan.objects.all().filter(julioP="X")                     
      elif rest == 8:       
            tareas=mantplan.objects.all().filter(agostoP="X")                     
      elif rest == 9:       
            tareas=mantplan.objects.all().filter(septiembreP="X")                                 
      elif rest == 10:       
            tareas=mantplan.objects.all().filter(octubreP="X")                                 
      elif rest == 11:       
            tareas=mantplan.objects.all().filter(noviembreP="X")                                             
      else:       
            tareas=mantplan.objects.all().filter(diciembreP="X")
            
      return tareas

def tareaM():
      listaM=orden.objects.filter(culminada="No")
      return listaM



def principal(request):
     listcentro=centrocosto.objects.all().order_by('descripcion')
     listorden=orden.objects.all().order_by('-codigo')[0:7]
     listvale=vale.objects.values('costo').order_by('costo').annotate(cant=Count('costo'))
     listprod=producciones.objects.values('descripcion','unidad').order_by('descripcion').annotate(prosu=Sum('cantidad'))
     listordp=orden.objects.values('area').order_by('area').annotate(cant=Count('codigo'))
     datosPT=[]
     for item in listprod:
            a = random.randint(0,255)
            b = random.randint(0,255)
            c = random.randint(0,255)
            color='rgba'+ '(%s' % a +', %s' % b +', %s' % c + ', 0.7)'
            datosPT.append({
              'descripcion':item['descripcion'],
              'prosu':item['prosu'],
              'color':color    
            })
      
     datosOT=[]
     for item in listordp:
            a = random.randint(0,255)
            b = random.randint(0,255)
            c = random.randint(0,255)
            color='rgba'+ '(%s' % a +', %s' % b +', %s' % c + ', 0.7)'  
            datosOT.append({
              'area':item['area'],
              'cant':item['cant'],
              'color':color
            })


     return render(request,"index.html", {"listord":listorden, "listpro":listprod, "listv":listvale, "listcentrosw":listcentro, "datosPT":datosPT, "datosOT":datosOT, "contadorSW":barracont(), "ordenmSW":tareaM()})


