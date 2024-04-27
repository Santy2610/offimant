from django.shortcuts import render, redirect
from ordenes.models import orden
from producciones.models import producciones
from vales.models import vale, materialv
from codificadores.models import centrocosto
from django.db.models import Sum, Count
from django.core.paginator import Paginator

def principal(request):
      listcentro=centrocosto.objects.all().order_by('descripcion')
      listorden=orden.objects.all().order_by('-codigo')[0:5]
      listvale=vale.objects.values('costo').order_by('costo').annotate(cant=Count('costo'))
      listprod=producciones.objects.values('descripcion','unidad').order_by('descripcion').annotate(prosu=Sum('cantidad'))
      return render(request,"index.html", {"listord":listorden, "listpro":listprod, "listv":listvale, "listcentrosw":listcentro})

