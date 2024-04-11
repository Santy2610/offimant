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
   lismant=mantplan.objects.get(pk=dato)
   lismant.codigo=codigo
   lismant.area=area
   lismant.tarea=tarea
   lismant.eneroP=enero
   lismant.febreroP=febrero
   lismant.marzoP=marzo
   lismant.abrilP=abril
   lismant.mayoP=mayo
   lismant.junioP=junio
   lismant.julioP=julio
   lismant.agostoP=agosto
   lismant.septiembreP=septiembre
   lismant.octubreP=octubre
   lismant.noviembreP=noviembre
   lismant.diciembreP=diciembre
   lismant.save()
   return redirect("/listmant?page=%s" %page)


def mantdel(request, dato):
    lisman=mantplan.objects.get(pk=dato)
    lisman.delete()
    return redirect(listmant)

def estadomant(request, dato, page):
    list=mantplan.objects.get(pk=dato)
    tareaf=list.tarea
    format=formmant(initial={ 'codigof':list.codigo, 'areaf':list.area,'enerorf':list.eneroR, 'febrerorf':list.febreroR,'marzorf':list.marzoR,'abrilrf':list.abrilR,'mayorf':list.mayoR,
                              'juniorf':list.junioR,'juliorf':list.julioR,'agostorf':list.agostoR,'septiembrerf':list.septiembreR,'octubrerf':list.octubreR,
                              'noviembrerf':list.noviembreR,'diciembrerf':list.diciembreR })   
    return render(request, "estadomant.html",{"form":format,"listsw":list,"dato":dato, "pagesw":page, "tareasw":tareaf})

def estadomantupdate(request, dato, page):
   lismant=mantplan.objects.get(pk=dato)
   enero=request.GET["enerorf"]
   febrero=request.GET["febrerorf"]
   marzo=request.GET["marzorf"]
   abril=request.GET["abrilrf"]
   mayo=request.GET["mayorf"]
   junio=request.GET["juniorf"]
   julio=request.GET["juliorf"]
   agosto=request.GET["agostorf"]
   septiembre=request.GET["septiembrerf"]
   octubre=request.GET["octubrerf"]
   noviembre=request.GET["noviembrerf"]
   diciembre=request.GET["diciembrerf"]
   lismant.eneroR=enero
   lismant.febreroR=febrero
   lismant.marzoR=marzo
   lismant.abrilR=abril
   lismant.mayoR=mayo
   lismant.junioR=junio
   lismant.julioR=julio
   lismant.agostoR=agosto
   lismant.septiembreR=septiembre
   lismant.octubreR=octubre
   lismant.noviembreR=noviembre
   lismant.diciembreR=diciembre
   lismant.save()
   return redirect("/listmant?page=%s" %page)

