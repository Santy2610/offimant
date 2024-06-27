from django.shortcuts import render, redirect
from Offimant.views import barracont, tareaM, tiempoP
from ordenes.models import orden
from producciones.models import producciones
from tiempoperdido.models import tiempo
from vales.models import vale, materialv

# Create your views here.


def config(request):
    ordenes = orden.objects.all()
    ordenFI = orden.objects.all().order_by('fechaRep')[0:1]
    ordenFF = orden.objects.all().order_by('-fechaRep')[0:1]
    prod = producciones.objects.all()
    prodFI = producciones.objects.all().order_by('fechaf')[0:1]
    prodFF = producciones.objects.all().order_by('-fechaf')[0:1]
    tiem = tiempo.objects.all()
    tiemFI = tiempo.objects.all().order_by('fechaI')[0:1]
    tiemFF = tiempo.objects.all().order_by('-fechaI')[0:1]
    valet = vale.objects.all()
    valeFI = vale.objects.all().order_by('fecha')[0:1]
    valeFF = vale.objects.all().order_by('-fecha')[0:1]
    return render(request, "indexsys.html", {"prodFISW": prodFI, "prodFFSW": prodFF, "prodSW": prod, "ordenFISW": ordenFI, "ordenFFSW": ordenFF, "ordenesSW": ordenes, "contadorSW": barracont(), "ordenmSW": tareaM(), 'tiempopSW': tiempoP(),
                                             "tiemSW": tiem, "tiemFISW": tiemFI, "tiemFFSW": tiemFF, "valetSW": valet, "valeFISW": valeFI, "valeFFSW": valeFF})


def proddel(request):
    producciones.objects.all().delete()
    return redirect(config)


def ordendel(request):
    orden.objects.all().delete()
    return redirect(config)


def tiemdel(request):
    tiempo.objects.all().delete()
    return redirect(config)


def valedel(request):
    vale.objects.all().delete()
    materialv.objects.all().delete()
    return redirect(config)
