from django.shortcuts import render, redirect
from vales.models import vale, materialv
from vales.formulario import formulariovales, formulariomaterial
from django.core.paginator import Paginator
from django.db.models import Sum, Count
from codificadores.models import centrocosto


# Create your views here.

# vista de los vales

def codvales(request, vista, dato):
    listcentro=centrocosto.objects.all().order_by('descripcion')
    page = request.GET.get('page', 1)
    valeslist = vale.objects.all().order_by('codigo')
    paginador = Paginator(valeslist, 10)
    valeslist = paginador.page(page)
    if vista == 'index':
        formavales = formulariovales()
        materialeslist = materialv.objects.all()
        return render(request, "valesindex.html",
                      {"form": formavales, "valessw": valeslist, "materialessw": materialeslist, "vistasw": vista,
                       "paginador": paginador, "listpsw": valeslist, "listcentrosw":listcentro})
    else:
        valesdg = vale.objects.get(pk=dato)
        formvales = formulariovales(
            initial={'Codigo': valesdg.codigo, 'Almacen': valesdg.almacen, 'Costo': valesdg.costo,
                     'Entregado': valesdg.entregado, 'Fecha': valesdg.fecha})
        return render(request, "valesindex.html",
                      {"form": formvales, "valessw": valeslist, "dato": dato, "vistasw": vista, "paginador": paginador,
                       "listpsw": valeslist})


def codvalesadd(request):
    codigo = request.GET["Codigo"]
    almacen = request.GET["Almacen"]
    costo = request.GET["Costo"]
    entregado = request.GET["Entregado"]
    fecha = request.GET["Fecha"]
    valeslist = vale.objects.create(codigo=codigo, almacen=almacen, costo=costo, entregado=entregado, fecha=fecha)
    return redirect(codvales, vista='index', dato=0)


def codvalesupdate(request, dato, page):
    codigo = request.GET["Codigo"]
    almacen = request.GET["Almacen"]
    costo = request.GET["Costo"]
    entregado = request.GET["Entregado"]
    fecha = request.GET["Fecha"]
    valedg = vale.objects.get(pk=dato)
    valedg.codigo = codigo
    valedg.almacen = almacen
    valedg.costo = costo
    valedg.entregado = entregado
    valedg.fecha = fecha
    valedg.save()
    return redirect("/codvales/index/0/?page=%s" % page)


def codvalesdel(request, dato, page):
    valeslist = vale.objects.get(pk=dato)
    valeslist.delete()
    return redirect("/codvales/index/0/?page=%s" % page)


# termina Vales

# comienza materiales

def codmaterial(request, dato, pagina):
    valeslist = vale.objects.get(pk=dato)
    page = request.GET.get('page', 1)
    materiallist = materialv.objects.filter(valeID=valeslist).order_by('id')
    paginador = Paginator(materiallist, 8)
    materiallist = paginador.page(page)
    materialbot = materialv.objects.filter(valeID=valeslist).order_by('id')
    formmaterial = formulariomaterial()
    consol=materialv.objects.values('material','unidad').order_by('material').annotate(tot=Sum('cantidad'), sal=Count('material'))
    return render(request, "materialindex.html",
                  {"form": formmaterial, "valessw": valeslist, "materialsw": materiallist, "materialbot": materialbot,
                   "paginador": paginador, "listpsw": materiallist, "pagesw": pagina, "consolsw":consol})


def codmaterialorden(request, dato, page, retro):
    resort = vale.objects.get(codigo=dato)
    materiallist = materialv.objects.filter(valeID=resort).order_by('id')
    return render(request, "materialview.html", {"valessw": resort, "materialsw": materiallist, "pagesw": page, "retrosw":retro})


def codmaterialadd(request, dato, pagina):
    material = request.GET["Material"]
    unidad = request.GET["Unidad"]
    cantidad = request.GET["Cantidad"]
    valeslist = vale.objects.get(pk=dato)
    materialeslist = materialv.objects.create(valeID=valeslist, material=material, unidad=unidad, cantidad=cantidad)
    return redirect(codmaterial, dato, pagina)


def codmaterialdel(request, dato, vale, pagina):
    materiallist = materialv.objects.get(pk=dato)
    materiallist.delete()
    return redirect(codmaterial, vale, pagina)

def consolmat(request):
      page=request.GET.get('page',1)
      listma=materialv.objects.values('material','unidad').order_by('material').annotate(tot=Sum('cantidad'), sal=Count('material'))
      paginador=Paginator(listma, 13)
      listma=paginador.page(page)
      return render(request, "materialconsol.html", {"listmasw":listma, "paginador":paginador,"listpsw":listma})

def consolspe(request, dato):
      page=request.GET.get('page',1)
      listma=materialv.objects.filter(valeID__costo__contains=dato).values('material','unidad').order_by('material').annotate(tot=Sum('cantidad'), sal=Count('material'))
      paginador=Paginator(listma, 13)
      listma=paginador.page(page)
      return render(request, "materialconsol.html", {"listmasw":listma, "paginador":paginador,"listpsw":listma})