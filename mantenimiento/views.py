from django.shortcuts import render, redirect
from mantenimiento.models import mantplan
from mantenimiento.formulario import formmant
from django.core.paginator import Paginator

# Create your views here.

def listmant(request):
    page=request.GET.get('page',1)
    listm=mantplan.objects.all().order_by("id")
    paginador=Paginator(listm, 8)
    listm=paginador.page(page)
    
    return render(request,"listadomant.html", {"mantsw":listm, "paginador":paginador,"listpsw":listm})

def adicionarmant(request, vista, dato, page):
    if vista == "index":  
     format=formmant()
     return render(request, "adicionarmant.html",{"form":format, "vistasw":vista, "dato":dato, "pagesw":page})
    else:
     list=mantplan.objects.get(pk=dato)
     rtarea=list.tarea
     format=formmant(initial={'codigof':list.codigo, 'areaf':list.area, 'enerof':list.eneroP, 'febrerof':list.febreroP,
                              'marzof':list.marzoP,'abrilf':list.abrilP,'mayof':list.mayoP, 'juniof':list.junioP,
                               'juliof':list.julioP,'agostof':list.agostoP,'septiembref':list.septiembreP,'octubref':list.octubreP,
                                'noviembref':list.noviembreP,'diciembref':list.diciembreP })   
     
    return render(request, "adicionarmant.html",{"form":format, "vistasw":vista, "dato":dato, "pagesw":page, "tareasw":rtarea})

def mantadd(request):
   codigo=request.GET["codigof"]
   area=request.GET["areaf"]
   tarea=request.GET["tareaf"]
   enero=request.GET["enerof"]
   febrero=request.GET["febrerof"]
   marzo=request.GET["marzof"]
   abril=request.GET["abrilf"]
   mayo=request.GET["mayof"]
   junio=request.GET["juniof"]
   julio=request.GET["juliof"]
   agosto=request.GET["agostof"]
   septiembre=request.GET["septiembref"]
   octubre=request.GET["octubref"]
   noviembre=request.GET["noviembref"]
   diciembre=request.GET["diciembref"]
   lisma=mantplan.objects.create(codigo=codigo, area=area, tarea=tarea, eneroP=enero, febreroP=febrero, marzoP=marzo, abrilP=abril,
                                    mayoP=mayo, junioP=junio, julioP=julio, agostoP=agosto, septiembreP=septiembre, octubreP=octubre, noviembreP=noviembre,
                                    diciembreP=diciembre)
   lisma.save()
   return redirect(listmant)

def mantupdate(request, dato, page):
   codigo=request.GET["codigof"]
   area=request.GET["areaf"]
   tarea=request.GET["tareaf"]
   enero=request.GET["enerof"]
   febrero=request.GET["febrerof"]
   marzo=request.GET["marzof"]
   abril=request.GET["abrilf"]
   mayo=request.GET["mayof"]
   junio=request.GET["juniof"]
   julio=request.GET["juliof"]
   agosto=request.GET["agostof"]
   septiembre=request.GET["septiembref"]
   octubre=request.GET["octubref"]
   noviembre=request.GET["noviembref"]
   diciembre=request.GET["diciembref"]
   listmant=mantplan.objects.get(pk=dato)
   listmant.codigo=codigo
   listmant.area=area
   listmant.tarea=tarea
   listmant.eneroP=enero
   listmant.febreroP=febrero
   listmant.marzoP=marzo
   listmant.abrilP=abril
   listmant.mayoP=mayo
   listmant.junioP=junio
   listmant.julioP=julio
   listmant.agostoP=agosto
   listmant.septiembreP=septiembre
   listmant.octubreP=octubre
   listmant.noviembreP=noviembre
   listmant.diciembreP=diciembre
   listmant.save()
   return redirect("/listmant?page=%s" %page)


def mantdel(request, dato):
    lisman=mantplan.objects.get(pk=dato)
    lisman.delete()
    return redirect(listmant)