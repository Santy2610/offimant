from django.shortcuts import render, redirect
from producciones.models import producciones, materiales
from vales.models import vale
from django.core.paginator import Paginator
from producciones.formulario import formulariopro,formulariomate

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
      formprod=formulariopro(initial={'codigo':prolubica.codigo, 'unidad':prolubica.unidad, 'descripcion':prolubica.descripcion, 'cantidad':prolubica.cantidad, 'fechafab':prolubica.fechaf})
    return render(request, "listaprod.html",{"form":formprod, "prosw":prolist, "vistasw":vista, "listpsw":prolist, "paginador":paginador, "dato":dato})

def codprodadd(request):
      codigo=request.GET["codigo"]
      descripcion=request.GET["descripcion"]
      unidad=request.GET["unidad"]
      cantidad=request.GET["cantidad"]
      fechaf=request.GET["fechafab"]
      prolist=producciones.objects.create(codigo=codigo, descripcion=descripcion, unidad=unidad, cantidad=cantidad, fechaf=fechaf)
      return redirect(indexprod, vista='index', dato=0)

def codprodupdate(request, dato, page):
      codigo=request.GET["codigo"]
      descripcion=request.GET["descripcion"]
      unidad=request.GET["unidad"]
      cantidad=request.GET["cantidad"]
      fechaf=request.GET["fechafab"]
      prolist=producciones.objects.get(pk=dato)
      prolist.codigo=codigo
      prolist.descripcion=descripcion
      prolist.unidad=unidad
      prolist.cantidad=cantidad
      prolist.fechaf=fechaf
      prolist.save()
      return redirect("/indexprod/index/0/?page=%s" %page)

def codproddel(request, dato, page):
      prolist=producciones.objects.get(pk=dato)
      prolist.delete()
      return redirect("/indexprod/index/0/?page=%s" %page)

def indexmate(request, dato, pagina):
      prodlist=producciones.objects.get(pk=dato)
      page=request.GET.get('page',1)
      matelist=materiales.objects.filter(idprod=prodlist).order_by('novale')
      paginador=Paginator(matelist, 10)
      matelist=paginador.page(page)
      matebot=materiales.objects.filter(idprod=prodlist).order_by('novale')
      formate=formulariomate()
      return render(request,"listavale.html",{"form":formate, "prodsw":prodlist, "matesw":matelist, "pagesw":pagina, "datosw":dato, "matebot":matebot, "paginador":paginador,"listpsw":matelist})

def codmateadd(request, dato, pagina):
    codigo=request.GET["Novale"] 
    valer=vale.objects.get(codigo=codigo)
    valelist=materiales.objects.create(novale=valer.codigo, almacen=valer.almacen, costo=valer.costo, entregado=valer.entregado, fecha=valer.fecha)
    valelist.save()
    return redirect(indexmate, dato, pagina)
   