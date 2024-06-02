from django.shortcuts import render,redirect
from tiempoperdido.models import tiempo
from django.core.paginator import Paginator
from tiempoperdido.formulario import tiempoF
from datetime import datetime
from django.db.models import Sum, Count
import random

# Create your views here.

def listadotiempo(request):
    page=request.GET.get('page',1)
    listT=tiempo.objects.all().order_by('fechaI')
    paginador=Paginator(listT, 10)
    listT=paginador.page(page)
    Grafth=tiempo.objects.values('area').order_by('area').annotate(canti=Sum('dias'))
    listF=tiempoF()
    datosTP=[]
    for item in Grafth:
            a = random.randint(0,255)
            b = random.randint(0,255)
            c = random.randint(0,255)
            color='rgba'+ '(%s' % a +', %s' % b +', %s' % c + ', 0.7)'
            datosTP.append({
              'area':item['area'],
              'canti':item['canti'],
              'color':color    
            })



    return render(request, "listadotiempo.html",{"listFor":listF, "listTsw":listT,"datosTP":datosTP})

def tiempoadd(request):
    area=request.GET["areaf"]
    equipo=request.GET["equiposf"]
    fechaI=request.GET["fechaIf"]
    fechaF=request.GET["fechaFf"]
    fechaI=datetime.strptime(fechaI, '%Y-%m-%d').date()
    fechaF=datetime.strptime(fechaF, '%Y-%m-%d').date()
    time=(fechaI-fechaF)*-1
    time=time.days
    causa=request.GET["causaf"]
    observacion=request.GET["observacionf"]
    listT=tiempo.objects.create(area=area, equipo=equipo, fechaI=fechaI, fechaF=fechaF, causa=causa, observacion=observacion, dias=time)
    listT.save()
    return redirect(listadotiempo)


def tiempodel(request, dato):
    listT=tiempo.objects.get(pk=dato)
    listT.delete()
    return redirect(listadotiempo) 
