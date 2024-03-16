from django.shortcuts import render, redirect
from codificadores.admin import equiposAdmin
from codificadores.formulario import formularioalmacen, formularioareas, formulariocausas, formulariocosto, formulariounidadm, formularioequipos, formulariocausas,formulariotrab
from codificadores.models import areas, centrocosto, trabajadores, unidadm, almacen, equipos, causas
from django.core.paginator import Paginator

# Create your views here.

# unidades

def codunidad(request, vista, dato):
      page=request.GET.get('page',1)
      unidlist=unidadm.objects.all().order_by('descripcion')
      paginador=Paginator(unidlist, 10)
      unidlist=paginador.page(page)
      if vista == 'index':
       formUnidad=formulariounidadm()
      else:
       unidg=unidadm.objects.get(pk=dato)
       formUnidad=formulariounidadm(initial={'Unidad':unidg.unid, 'Descripcion':unidg.descripcion})
      return render(request,"unidadindex.html",{"form":formUnidad, "unisw":unidlist, "vistasw":vista, "dato":dato, "paginador":paginador,"listpsw":unidlist})
    

def codunidadadd(request):
      unid=request.GET["Unidad"]
      descripcion=request.GET["Descripcion"]
      unilist=unidadm.objects.create(unid=unid, descripcion=descripcion)
      return redirect(codunidad, vista='index', dato=0)

def codunidadupdate(request, dato, page):
    unidad=request.GET["Unidad"]
    descripcion=request.GET["Descripcion"]
    unidg=unidadm.objects.get(pk=dato)
    unidg.unid=unidad
    unidg.descripcion=descripcion
    unidg.save()
    return redirect("/codunidad/index/0/?page=%s" %page) 


def codunidaddel(request, dato, page):
      unilist=unidadm.objects.get(pk=dato)
      unilist.delete()
      return redirect("/codunidad/index/0/?page=%s" %page)

# fin unidades


# almacenes

def codalmacen(request, vista, dato):
      page=request.GET.get('page',1)
      Almalist=almacen.objects.all().order_by('codigo')
      paginador=Paginator(Almalist, 10)
      Almalist=paginador.page(page)
      if vista == 'index':
       formAlmacen=formularioalmacen()
      else:
       almaceng=almacen.objects.get(pk=dato)
       formAlmacen=formularioalmacen(initial={'Codigo':almaceng.codigo, 'Descripcion':almaceng.descripcion})
      return render(request,"almacenesindex.html",{"form":formAlmacen, "Almasw":Almalist, "vistasw":vista, "dato":dato , "paginador":paginador,"listpsw":Almalist})    

def codalmacenadd(request):
      codigo=request.GET["Codigo"]
      descripcion=request.GET["Descripcion"]
      almalist=almacen.objects.create(codigo=codigo, descripcion=descripcion)
      return redirect(codalmacen, vista='index',dato=0)

def codalmacenupdate(request, dato,page):
    codigo=request.GET["Codigo"]
    descripcion=request.GET["Descripcion"]
    almacendg=almacen.objects.get(pk=dato)
    almacendg.codigo=codigo
    almacendg.descripcion=descripcion
    almacendg.save()
    return redirect("/codalmacen/index/0/?page=%s" %page) 

def codalmacendel(request, dato, page):
     Almalist=almacen.objects.get(pk=dato)
     Almalist.delete()
     return redirect("/codalmacen/index/0/?page=%s" %page)


# fin almacenes
      
# centro de costos

def codcosto(request, vista, dato):
      page=request.GET.get('page',1)
      costolist=centrocosto.objects.all().order_by('codigo')
      paginador=Paginator(costolist, 10)
      costolist=paginador.page(page)
      if vista == 'index':
       formcosto=formulariocosto()
      else:
       costong=centrocosto.objects.get(pk=dato)
       formcosto=formulariocosto(initial={'Codigo':costong.codigo, 'Descripcion':costong.descripcion, 'Produccion':costong.prod})
      return render(request,"costoindex.html",{"form":formcosto, "costosw":costolist, "vistasw":vista, "dato":dato, "paginador":paginador,"listpsw":costolist})

def codcostoadd(request):
      codigo=request.GET["Codigo"]
      descripcion=request.GET["Descripcion"]
      prod=request.GET["Produccion"]
      costolist=centrocosto.objects.create(codigo=codigo, descripcion=descripcion, prod=prod)
      return redirect(codcosto, vista='index', dato=0)

def codcostoupdate(request, dato, page):
    codigo=request.GET["Codigo"]
    descripcion=request.GET["Descripcion"]
    prod=request.GET["Produccion"]
    costodg=centrocosto.objects.get(pk=dato)
    costodg.codigo=codigo
    costodg.descripcion=descripcion
    costodg.prod=prod
    costodg.save()
    return redirect("/codcosto/index/0/?page=%s" %page)    

def codcostodel(request, dato, page):
     costolist=centrocosto.objects.get(pk=dato)
     costolist.delete()
     return redirect("/codcosto/index/0/?page=%s" %page)

# fin de centro de costo

# Areas

def codareas(request, vista, dato):
      page=request.GET.get('page',1)
      areaslist=areas.objects.all().order_by('codigo')
      paginador=Paginator(areaslist, 10)
      areaslist=paginador.page(page)
      if vista == 'index':
       formareas=formularioareas()
      else:
       areasdg=areas.objects.get(pk=dato)
       formareas=formularioareas(initial={'Codigo':areasdg.codigo, 'Descripcion':areasdg.descripcion})
      return render(request,"areasindex.html", {"form":formareas, "areassw":areaslist, "dato":dato, "vistasw":vista, "paginador":paginador,"listpsw":areaslist})
      
def codareasadd(request):
      codigo=request.GET["Codigo"]
      descripcion=request.GET["Descripcion"]
      areaslist=areas.objects.create(codigo=codigo, descripcion=descripcion)
      return redirect(codareas, vista='index', dato=0)

def codareasupdate(request, dato, page):
    codigo=request.GET["Codigo"]
    descripcion=request.GET["Descripcion"]
    areasdg=areas.objects.get(pk=dato)
    areasdg.codigo=codigo
    areasdg.descripcion=descripcion
    areasdg.save()
    return redirect("/codareas/index/0/?page=%s" %page)
   

def codareasdel(request, dato, page):
     areaslist=areas.objects.get(pk=dato)
     areaslist.delete()
     return redirect("/codareas/index/0/?page=%s" %page)



# fin areas

# Equipos

def codequipos(request, dato):
      areaslist=areas.objects.get(pk=dato)
      page=request.GET.get('page',1)
      equiposlist=equipos.objects.filter(masterArea=areaslist).order_by('codigo')
      paginador=Paginator(equiposlist, 10)
      equiposlist=paginador.page(page)
      equiposbot=equipos.objects.filter(masterArea=areaslist).order_by('codigo')
      formequipos=formularioequipos()
      return render(request,"equiposindex.html",{"form":formequipos, "areassw":areaslist, "equipossw":equiposlist, "equiposbot":equiposbot, "paginador":paginador,"listpsw":equiposlist})

def codequiposadd(request, dato):
      codigo=request.GET["Codigo"]
      descripcion=request.GET["Descripcion"]
      arealist=areas.objects.get(pk=dato)
      equiposlist=equipos.objects.create(masterArea=arealist, codigo=codigo, descripcion=descripcion)
      return redirect(codequipos,dato)

def codequiposedit(request, dato, area):
     areaslist=areas.objects.get(pk=area)
     page=request.GET.get('page',1)
     equiposlist=equipos.objects.filter(masterArea=areaslist).order_by('codigo')
     paginador=Paginator(equiposlist, 10)
     equiposbot=equipos.objects.filter(masterArea=areaslist).order_by('codigo')
     equiposlist=paginador.page(page)
     equiposdg=equipos.objects.get(pk=dato)
     formequipos=formularioequipos(initial={'Codigo':equiposdg.codigo, 'Descripcion':equiposdg.descripcion})
     return render(request,"equiposedit.html", {"form":formequipos, "equipossw":equiposlist, "equiposbot":equiposbot, "areassw":areaslist, "area":area, "dato":dato, "paginador":paginador,"listpsw":equiposlist})


def codequiposupdate(request, dato, area, page):
    codigo=request.GET["Codigo"]
    descripcion=request.GET["Descripcion"]
    equiposdg=equipos.objects.get(pk=dato)
    equiposdg.codigo=codigo
    equiposdg.descripcion=descripcion
    equiposdg.save()
    return redirect("/codequipos/"+area+"/?page=%s" %page) 

def codequiposdel(request, dato, area, page):
     equiposlist=equipos.objects.get(pk=dato)
     equiposlist.delete()
     return redirect("/codequipos/"+area+"/?page=%s" %page) 

# fin Equipos

# Causas

def codcausas(request, vista, dato):
      page=request.GET.get('page',1)
      causalist=causas.objects.all().order_by('codigo')
      paginador=Paginator(causalist, 10)
      causalist=paginador.page(page)
      if vista == 'index':
       formcausas=formulariocausas()
      else:
       causasdg=causas.objects.get(pk=dato)
       formcausas=formulariocausas(initial={'Codigo':causasdg.codigo, 'Descripcion':causasdg.descripcion})
      return render(request,"causasindex.html",{"form":formcausas, "causassw":causalist, "vistasw":vista, "dato":dato, "paginador":paginador,"listpsw":causalist })   

def codcausasadd(request):
      codigo=request.GET["Codigo"]
      descripcion=request.GET["Descripcion"]
      causaslist=causas.objects.create(codigo=codigo, descripcion=descripcion)
      return redirect(codcausas, vista='index', dato=0)

def codcausasupdate(request, dato, page):
    codigo=request.GET["Codigo"]
    descripcion=request.GET["Descripcion"]
    causasdg=causas.objects.get(pk=dato)
    causasdg.codigo=codigo
    causasdg.descripcion=descripcion
    causasdg.save()
    return redirect("/codcausas/index/0/?page=%s" %page) 

def codcausasdel(request, dato, page):
     causaslist=causas.objects.get(pk=dato)
     causaslist.delete()
     return redirect("/codcausas/index/0/?page=%s" %page) 



# Fin Causas

# Inicio trabajadores

def codtraba(request, vista, dato):
      page=request.GET.get('page',1)
      trablist=trabajadores.objects.all().order_by('codigo')
      paginador=Paginator(trablist, 10)
      trablist=paginador.page(page)
      if vista == 'index':
       formtrab=formulariotrab()
      else:
       trabdg=trabajadores.objects.get(pk=dato)
       formtrab=formulariotrab(initial={'codigo':trabdg.codigo, 'nombre':trabdg.nombre, 'Solic':trabdg.solic, 'Person':trabdg.person})
      return render(request,"trabajadoresindex.html",{"form":formtrab, "trabsw":trablist, "vistasw":vista, "dato":dato, "paginador":paginador,"listpsw":trablist})
    

def codtrabaadd(request):
      codigo=request.GET["codigo"]
      nombre=request.GET["nombre"]
      solic=request.GET["Solic"]
      person=request.GET["Person"]
      trablist=trabajadores.objects.create(codigo=codigo, nombre=nombre, solic=solic, person=person)
      return redirect(codtraba, vista='index', dato=0)

def codtrabaupdate(request, dato, page):
    codigo=request.GET["codigo"]
    nombre=request.GET["nombre"]
    solic=request.GET["Solic"]
    person=request.GET["Person"]
    trabdg=trabajadores.objects.get(pk=dato)
    trabdg.codigo=codigo
    trabdg.nombre=nombre
    trabdg.solic=solic
    trabdg.person=person
    trabdg.save()
    return redirect("/codtraba/index/0/?page=%s" %page) 


def codtrabadel(request, dato, page):
      trablist=trabajadores.objects.get(pk=dato)
      trablist.delete()
      return redirect("/codtraba/index/0/?page=%s" %page)



# Fin trabajadores




def codparada(request):
      return render(request,"paradasindex.html")