from django.shortcuts import render,redirect
from tiempoperdido.models import tiempo
from django.core.paginator import Paginator
from tiempoperdido.formulario import tiempoF

# Create your views here.

def listadotiempo(request):
    page=request.GET.get('page',1)
    listT=tiempo.objects.all().order_by('fechaI')
    paginador=Paginator(listT, 10)
    listT=paginador.page(page)
    listF=tiempoF()
    return render(request, "listadotiempo.html",{"listFor":listF, "listTsw":listT})

def tiempoadd(request):
    area=request.GET["areaf"]
    equipo=request.GET["equiposf"]
    fechaI=request.GET["fechaIf"]
    fechaF=request.GET["fechaFf"]
    causa=request.GET["causaf"]
    observacion=request.GET["observacionf"]
    listT=tiempo.objects.create(area=area, equipo=equipo, fechaI=fechaI, fechaF=fechaF, causa=causa, observacion=observacion)
    listT.save()
    return redirect(listadotiempo)


def tiempodel(request, dato):
    listT=tiempo.objects.get(pk=dato)
    listT.delete()
    return redirect(listadotiempo) 
