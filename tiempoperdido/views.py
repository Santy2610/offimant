from django.shortcuts import render,redirect
from tiempoperdido.models import tiempo
from django.core.paginator import Paginator
from tiempoperdido.formulario import tiempoF
from datetime import datetime
from django.db.models import Sum, Count
import random
from Offimant.views import barracont, tareaM 

# Create your views here.

def listadotiempo(request):
    page=request.GET.get('page',1)
    listT=tiempo.objects.all().order_by('fechaI')
    paginador=Paginator(listT, 8)
    listT=paginador.page(page)
    Grafth=tiempo.objects.values('area').order_by('area').annotate(canti=Sum('dias'))
    total=0
    for item in Grafth:
           total=total+item['canti']       
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



    return render(request, "listadotiempo.html",{"listFor":listF, "listTsw":listT,"datosTP":datosTP, "paginador":paginador, "listpsw":listT, "Grafthsw":Grafth, "totalSW":total, "contadorSW":barracont(), "ordenmSW":tareaM()})

def tiempoadd(request):
    area=request.GET["areaf"]
    equipo=request.GET["equiposf"]
    fechaI=request.GET["fechaIf"]
    fechaF=request.GET["fechaFf"]
    fechaI=datetime.strptime(fechaI, '%Y-%m-%d').date()
    fechaF=datetime.strptime(fechaF, '%Y-%m-%d').date()
    time=((fechaI-fechaF)*24)*-1
    time=time.days
    causa=request.GET["causaf"]
    observacion=request.GET["observacionf"]
    listT=tiempo.objects.create(area=area, equipo=equipo, fechaI=fechaI, fechaF=fechaF, causa=causa, observacion=observacion, dias=time)
    listT.save()
    return redirect(listadotiempo)

def tiempoupdate(request, dato):
    area=request.GET["areaf"]
    equipo=request.GET["equiposf"]
    fechaI=request.GET["fechaIf"]
    fechaF=request.GET["fechaFf"]
    fechaI=datetime.strptime(fechaI, '%Y-%m-%d').date()
    fechaF=datetime.strptime(fechaF, '%Y-%m-%d').date()
    time=((fechaI-fechaF)*24)*-1
    time=str(time.days)
    causa=request.GET["causaf"]
    observacion=request.GET["observacionf"]
    listT=tiempo.objects.get(pk=dato)
    listT.area=area
    listT.equipo=equipo
    listT.fechaI=fechaI
    listT.fechaF=fechaF
    listT.causa=causa
    listT.observacion=observacion
    listT.dias=time
    listT.save()
    return redirect(listadotiempo)

def tiempodel(request, dato, page):
    listT=tiempo.objects.get(pk=dato)
    listT.delete()
    return redirect(listadotiempo) 

def imptiemp(request):
    listT=tiempo.objects.all().order_by('fechaI')
    Grafth=tiempo.objects.values('area').order_by('area').annotate(canti=Sum('dias'))
    total=0
    for item in Grafth:
           total=total+item['canti']    
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



    return render(request, "implistadotiempo.html",{"listTsw":listT,"datosTP":datosTP, "Grafthsw":Grafth, "totalSW":total}) 
