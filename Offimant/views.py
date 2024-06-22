import random
from django.shortcuts import render, redirect
from ordenes.models import orden
from producciones.models import producciones
from vales.models import vale, materialv
from codificadores.models import centrocosto
from mantenimiento.models import mantplan
from tiempoperdido.models import tiempo
from django.db.models import Sum, Count, F
from django.core.paginator import Paginator
from datetime import date


def barracont():
    mes = date.today()
    rest = mes.month
    if rest == 1:
        tareas = mantplan.objects.all().filter(eneroP="X").order_by(
            'codigo').annotate(last=F('eneroR'))
    elif rest == 2:
        tareas = mantplan.objects.all().filter(febreroP="X").order_by(
            'codigo').annotate(last=F('febreroR'))
    elif rest == 3:
        tareas = mantplan.objects.all().filter(marzoP="X").order_by(
            'codigo').annotate(last=F('marzoR'))
    elif rest == 4:
        tareas = mantplan.objects.all().filter(abrilP="X").order_by(
            'codigo').annotate(last=F('abrilR'))
    elif rest == 5:
        tareas = mantplan.objects.all().filter(
            mayoP="X").order_by('codigo').annotate(last=F('mayoR'))
    elif rest == 6:
        tareas = mantplan.objects.all().filter(junioP="X").order_by(
            'codigo').annotate(last=F('junioR'))
    elif rest == 7:
        tareas = mantplan.objects.all().filter(julioP="X").order_by(
            'codigo').annotate(last=F('julioR'))
    elif rest == 8:
        tareas = mantplan.objects.all().filter(agostoP="X").order_by(
            'codigo').annotate(last=F('agostoR'))
    elif rest == 9:
        tareas = mantplan.objects.all().filter(septiembreP="X").order_by(
            'codigo').annotate(last=F('septiembreR'))
    elif rest == 10:
        tareas = mantplan.objects.all().filter(octubreP="X").order_by(
            'codigo').annotate(last=F('octubreR'))
    elif rest == 11:
        tareas = mantplan.objects.all().filter(noviembreP="X").order_by(
            'codigo').annotate(last=F('noviembreR'))
    else:
        tareas = mantplan.objects.all().filter(diciembreP="X").order_by(
            'codigo').annotate(last=F('diciembreR'))

    return tareas


def tareaM():
    listaM = orden.objects.filter(culminada="No")
    return listaM


def tiempoP():
    totalT = tiempo.objects.values('area').order_by(
        'area').annotate(sumT=Sum('dias'))
    return totalT


def principal(request):
    listcentro = centrocosto.objects.all().order_by('descripcion')
    listorden = orden.objects.all().order_by('-codigo')[0:7]
    listvale = vale.objects.values('costo').order_by(
        'costo').annotate(cant=Count('costo'))
    listprod = producciones.objects.values('descripcion', 'unidad').order_by(
        'descripcion').annotate(prosu=Sum('cantidad'))
    listordp = orden.objects.values('area').order_by(
        'area').annotate(cant=Count('codigo'))
    datosPT = []
    for item in listprod:
        a = random.randint(0, 255)
        b = random.randint(0, 255)
        c = random.randint(0, 255)
        color = 'rgba' + '(%s' % a + ', %s' % b + ', %s' % c + ', 0.7)'
        datosPT.append({
            'descripcion': item['descripcion'],
            'prosu': item['prosu'],
            'color': color
        })

    datosOT = []
    for item in listordp:
        a = random.randint(0, 255)
        b = random.randint(0, 255)
        c = random.randint(0, 255)
        color = 'rgba' + '(%s' % a + ', %s' % b + ', %s' % c + ', 0.7)'
        datosOT.append({
            'area': item['area'],
            'cant': item['cant'],
            'color': color
        })

    return render(request, "index.html", {"listord": listorden, "listpro": listprod, "listv": listvale, "listcentrosw": listcentro, "datosPT": datosPT, "datosOT": datosOT, "contadorSW": barracont(), "ordenmSW": tareaM(), 'tiempopSW': tiempoP()})
