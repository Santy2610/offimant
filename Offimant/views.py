from django.shortcuts import render, redirect
from ordenes.models import orden
from producciones.models import producciones
from vales.models import vale, materialv
from django.db.models import Sum, Count
from django.core.paginator import Paginator

def principal(request):
      listorden=orden.objects.all().order_by('-codigo')[0:5]
      listvale=vale.objects.values('costo').order_by('costo').annotate(cant=Count('costo'))
      listprod=producciones.objects.values('descripcion','unidad').order_by('descripcion').annotate(prosu=Sum('cantidad'))
      return render(request,"index.html", {"listord":listorden, "listpro":listprod, "listv":listvale})

def consolmat(request):
      page=request.GET.get('page',1)
      listma=materialv.objects.values('material','unidad').order_by('material').annotate(tot=Sum('cantidad'), sal=Count('material'))
      paginador=Paginator(listma, 13)
      listma=paginador.page(page)
      return render(request, "materialconsol.html", {"listmasw":listma, "paginador":paginador,"listpsw":listma})