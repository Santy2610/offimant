from django.shortcuts import render, redirect
from producciones.models import producciones, materiales
from django.core.paginator import Paginator
from producciones.formulario import formulariopro

# Create your views here.
def indexprod(request, vista, dato):
    page=request.GET.get('page',1)
    prolist=producciones.objects.all()
    paginador=Paginator(prolist, 10)
    prolist=paginador.page(page)
    if vista == 'index':
      formprod=formulariopro()
    else:
      prolubica=producciones.objects.get(pk=dato)
      formprod=formulariopro(initial={'codigo':prolubica.codigo, 'unidad':prolubica.unidad, 'descripcion':prolubica.descripcion, 'cantidad':prolubica.cantidad})
    return render(request, "listaprod.html",{"form":formprod, "prosw":prolist, "vistasw":vista, "listpsw":prolist, "paginador":paginador, "dato":dato})


def codprodadd(request):
      codigo=request.GET["codigo"]
      descripcion=request.GET["descripcion"]
      unidad=request.GET["unidad"]
      cantidad=request.GET["cantidad"]
      prolist=producciones.objects.create(codigo=codigo, descripcion=descripcion, unidad=unidad, cantidad=cantidad)
      return redirect(indexprod, vista='index', dato=0)


def codprodupdate(request, dato, page):
      codigo=request.GET["codigo"]
      descripcion=request.GET["descripcion"]
      unidad=request.GET["unidad"]
      cantidad=request.GET["cantidad"]
      prolist=producciones.objects.get(pk=dato)
      prolist.codigo=codigo
      prolist.descripcion=descripcion
      prolist.unidad=unidad
      prolist.cantidad=cantidad
      prolist.save()
      return redirect("/indexprod/index/0/?page=%s" %page)

def codproddel(request, dato, page):
      prolist=producciones.objects.get(pk=dato)
      prolist.delete()
      return redirect("/indexprod/index/0/?page=%s" %page)
   