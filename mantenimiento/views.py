from django.shortcuts import render, redirect
from mantenimiento.models import mantplan
from mantenimiento.formulario import formmant

# Create your views here.

def listmant(request):
    listm=mantplan.objects.all().order_by("area")
    return render(request,"listadomant.html", {"mantsw":listm})

def adicionarmant(request, vista, dato):
    if vista == "index":  
     format=formmant()
    else:
     list=mantplan.objects.get(pk=dato)
     format=formmant(initial={'codigof':list.codigo, 'areaf':list.area, 'tareaf':list.tarea, 'enerof':list.eneroP, 'febrerof':list.febreroP,
                              'marzof':list.marzoP,'abrilf':list.abrilP,'mayof':list.mayoP, 'juniof':list.junioP,
                               'juliof':list.julioP,'agostof':list.agostoP,'septiembref':list.septiembreP,'octubref':list.octubreP,
                                'noviembref':list.noviembreP,'diciembref':list.diciembreP })   
    return render(request, "adicionarmant.html",{"form":format, 'vistasw':vista})

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
   listmant=mantplan.objects.create(codigo=codigo, area=area, tarea=tarea, eneroP=enero, febreroP=febrero, marzoP=marzo, abrilP=abril,
                                    mayoP=mayo, junioP=junio, julioP=julio, agostoP=agosto, septiembreP=septiembre, octubreP=octubre, noviembreP=noviembre,
                                    diciembreP=diciembre)
   listmant.save()
   return redirect(listmant)